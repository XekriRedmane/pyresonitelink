"""ResoniteLink client.

We don't expect concurrent requests; request() blocks until the response is received.

I strongly suggest using the async versions of the functions.
"""

import asyncio
import dataclasses as dc
import json
import random
import uuid
from collections.abc import Mapping, Sequence
from typing import TYPE_CHECKING, Any

import numpy as np
import websockets

from .data import codec
from .data import fields
from .data import members
from .data import mesh
from .data import messages
from .data import primitives
from .data import responses
from .data import transforms
from .data import workers

if TYPE_CHECKING:
    # The methods that use these import them at call time, so importing the
    # client doesn't import the generated component packages.
    from .components.assets import StaticAudioClip
    from .generated.assets.utility.asset_multiplexer import AssetMultiplexer


MAX_RESPONSE_SIZE: int = 64 * 1024 * 1024
DEFAULT_TIMEOUT: float = 10

# Type aliases for parameters that accept both Field wrappers and raw values.
Float3Like = (
    fields.FieldFloat3 | primitives.Float3 | Sequence[float] | np.ndarray
)
FloatQLike = (
    fields.FieldFloatQ | primitives.FloatQ | Sequence[float] | np.ndarray
)


def _coerce_scalar_field[F](
    value: object,
    field_cls: type[F],
    np_type: type | None = None,
) -> F:
    """Coerce a raw scalar into a field wrapper.

    If *value* is already an instance of *field_cls* it is returned
    unchanged.  Otherwise a new *field_cls* is constructed with
    ``value=`` set to the raw value, optionally cast through *np_type*
    first (e.g. ``np.int64``).

    Works for any scalar field type:
    ``FieldString``/``str``, ``FieldBool``/``bool``,
    ``FieldLong``/``int``, ``FieldFloat``/``float``, etc.

    Args:
        value: The raw value or an existing field wrapper.
        field_cls: The target field class.
        np_type: Optional numpy type to cast through before wrapping.
    """
    if isinstance(value, field_cls):
        return value
    raw = np_type(value) if np_type is not None else value  # type: ignore[call-arg]
    return field_cls(value=raw)  # type: ignore[call-arg]


def _coerce_composite_field[F](
    value: object,
    field_cls: type[F],
    primitive_cls: type,
) -> F:
    """Coerce a raw value into a composite (multi-component) field wrapper.

    Accepts three forms of input:

    1. **Field wrapper** (e.g. ``FieldFloat3``) — returned unchanged.
    2. **Primitive dataclass** (e.g. ``Float3``) — wrapped in the field.
    3. **Sequence / ndarray** — components are unpacked positionally
       into the primitive constructor using its dataclass field names,
       then wrapped.

    Works for any ``(FieldXxx, PrimitiveXxx)`` pair including 2D, 3D,
    and 4D vectors (``Int2``, ``Float3``, ``Double4``, …), quaternions
    (``FloatQ``, ``DoubleQ``), colours (``Color``, ``Color32``), and
    matrices (``Float2x2``, ``Double4x4``, …).

    Args:
        value: The raw value or an existing field wrapper.
        field_cls: The target field class (e.g. ``FieldFloat3``).
        primitive_cls: The primitive dataclass (e.g. ``Float3``).
    """
    if isinstance(value, field_cls):
        return value
    if isinstance(value, primitive_cls):
        return field_cls(value=value)  # type: ignore[call-arg]
    # Sequence or ndarray — unpack by dataclass field order.
    names = [f.name for f in dc.fields(primitive_cls)]  # type: ignore[arg-type]
    kwargs = {name: value[i] for i, name in enumerate(names)}  # type: ignore[index]
    return field_cls(value=primitive_cls(**kwargs))  # type: ignore[call-arg]


# The engine runs components in ascending UpdateOrder (a SortedDictionary
# of buckets in UpdateManager), so the largest int runs last.
_PROBE_UPDATE_ORDER = np.int32(np.iinfo(np.int32).max)
# Seconds between reads of a global transform probe. Each read already takes
# about 8 ms, and an engine update at 60 FPS takes about 17 ms.
_PROBE_POLL_INTERVAL = 0.005
# The magnitude bound of each component of a probe's sentinel values.
_SENTINEL_RANGE = 1e4

# The slot fields that UpdateSlot can change, each of which is a member with
# an ID.
_SLOT_MEMBER_FIELDS = (
    "parent", "position", "rotation", "scale", "isActive", "isPersistent",
    "name", "tag", "orderOffset",
)


def _random_float3() -> primitives.Float3:
    """Returns a Float3 with each component uniform in +/-_SENTINEL_RANGE."""
    return primitives.Float3(
        *(random.uniform(-_SENTINEL_RANGE, _SENTINEL_RANGE) for _ in range(3))
    )


def _transform_of(data: workers.Slot, slot_id: str) -> transforms.Transform:
    """Returns a slot's transform relative to its parent.

    Args:
        data: The slot's data, as returned by GetSlot.
        slot_id: The slot's ID, for the error message.

    Raises:
        RuntimeError: The data lacks part of the transform.
    """
    position = data.position.value if data.position else None
    rotation = data.rotation.value if data.rotation else None
    scale = data.scale.value if data.scale else None
    if position is None or rotation is None or scale is None:
        raise RuntimeError(f"Slot {slot_id} has no transform data.")
    return transforms.Transform(position, rotation, scale)


def _batch_slot_data(
    batch: responses.BatchResponse, count: int,
) -> list[workers.Slot]:
    """Returns the slot data from a batch of GetSlot operations.

    Args:
        batch: The response to a batch of only GetSlot operations.
        count: The number of operations in the batch.

    Raises:
        RuntimeError: An operation failed, or the batch has the wrong
            number of responses.
    """
    results = batch.responses or []
    if len(results) != count:
        raise RuntimeError(
            f"Expected {count} responses in the batch, got {len(results)}."
        )
    slots = []
    for response in results:
        if not isinstance(response, responses.SlotData) or response.data is None:
            raise RuntimeError(f"Failed to get slot: {response.errorInfo}")
        slots.append(response.data)
    return slots


class Client:
    """ResoniteLink client."""

    _websocket: websockets.ClientConnection | None
    _loop: asyncio.AbstractEventLoop | None

    def __init__(self) -> None:
        self._websocket = None
        self._loop = None

    async def connect(
        self, port: int, host: str = "localhost", max_size: int = MAX_RESPONSE_SIZE
    ) -> None:
        """Connects to the ResoniteLink server.

        Args:
            port: Port number for the connection.
            host: Host address.
            max_size: Maximum size of incoming messages in bytes. Default is 64MB.
        """
        if self._websocket is not None:
            return

        uri = f"ws://{host}:{port}"
        self._websocket = await websockets.connect(uri, max_size=max_size)

        # Hacky fix for first request fails.
        try:
            await self.get_slot(slot="Root", depth=0)
        except websockets.exceptions.ConnectionClosedError:
            self._websocket = await websockets.connect(uri, max_size=max_size)
            await self.get_slot(slot="Root", depth=0)

    def sync_connect(
        self,
        port: int,
        host: str = "localhost",
        timeout: float = DEFAULT_TIMEOUT,
        max_size: int = MAX_RESPONSE_SIZE,
    ) -> None:
        """Connects to the ResoniteLink server synchronously."""
        self._loop = asyncio.new_event_loop()
        self._loop.run_until_complete(
            asyncio.wait_for(self.connect(port, host, max_size), timeout=timeout)
        )

    async def request_json(
        self, message: messages.Message, debug: bool = False
    ) -> dict[str, codec.JsonValue]:
        """Sends a message to the ResoniteLink server and returns the JSON response."""
        if self._websocket is None:
            raise RuntimeError("Client is not connected")

        if message.messageId is None:
            message.messageId = str(uuid.uuid4())

        # The server rejects a payload whose size doesn't match the message,
        # and the error is easier to act on before anything is sent.
        if isinstance(message, messages.BinaryPayloadMessage):
            expected = message.expected_payload_size()
            actual = len(message.payload) if message.payload is not None else 0
            if expected is not None and actual != expected:
                raise ValueError(
                    f"{type(message).__name__} needs a {expected}-byte payload, "
                    f"but has {actual} bytes"
                )

        encoded_data = codec.encode(message)
        json_data = json.dumps(encoded_data, ensure_ascii=False)
        if debug:
            print("=================================")
            print(f"Request: {json_data}")

        await self._websocket.send(json_data.encode("utf-8"), text=True)

        # If the message has a binary payload, send it after the json data.
        if (
            isinstance(message, messages.BinaryPayloadMessage)
            and message.payload is not None
        ):
            await self._websocket.send(message.payload, text=False)

        # There doesn't seem to be binary payload responses yet.
        response_data = await self._websocket.recv()
        json_response = json.loads(response_data)
        if debug:
            print(f"Response: {json_response}")
            print()
        return json_response

    async def request(
        self, message: messages.Message, debug: bool = False
    ) -> responses.Response:
        """Sends a message to the ResoniteLink server and returns the response."""
        json_response = await self.request_json(message, debug)
        response = codec.decode_response(json_response)
        return response

    async def close(self) -> None:
        """Closes the connection to the ResoniteLink server."""
        if self._websocket is not None:
            await self._websocket.close()
            self._websocket = None

    def sync_close(self) -> None:
        """Closes the connection to the ResoniteLink server synchronously."""
        if self._loop is None:
            return
        self._loop.run_until_complete(self.close())
        self._loop.close()

    async def send_message[T](
        self, request: messages.Message, response_type: type[T], debug: bool = False
    ) -> T:
        """Sends a message to the ResoniteLink server and waits for the response."""
        response = await self.request(request, debug)
        if not isinstance(response, response_type):
            # The server returned an error response instead of the
            # expected type.  Extract the error info if available.
            error_info = getattr(response, "errorInfo", None)
            if error_info:
                raise RuntimeError(
                    f"Server error: {error_info}"
                )
            raise RuntimeError(
                f"Expected {response_type.__name__}, "
                f"got {type(response).__name__}: {response}"
            )
        return response

    def sync_send_message[T](
        self,
        request: messages.Message,
        response_type: type[T],
        debug: bool = False,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> T:
        """Sends a message to the ResoniteLink server and waits for the response."""
        if self._loop is None:
            raise RuntimeError("Client is not connected")
        return self._loop.run_until_complete(
            asyncio.wait_for(
                self.send_message(request, response_type, debug), timeout=timeout
            )
        )

    # =========================================================================
    # Slot operations
    # =========================================================================

    async def get_slot(
        self,
        slot: str | workers.Slot,
        depth: int = 0,
        includeComponentData: bool = False,
        debug: bool = False,
    ) -> responses.SlotData:
        """Fetch slot data.

        Args:
            slot: The slot to fetch — either a slot ID string, or a
                ``Slot`` instance (whose ``id`` is used).  Use
                ``"Root"`` for the root slot.
            depth: Hierarchy depth (0=self, 1=children, -1=all).
            includeComponentData: Whether to include full component data.
            debug: Print request/response JSON.
        """
        slot_id = slot.id if isinstance(slot, workers.Slot) else slot
        assert slot_id is not None, "Slot has no ID"
        return await self.send_message(
            messages.GetSlot(
                slotId=slot_id, depth=depth,
                includeComponentData=includeComponentData,
            ),
            responses.SlotData, debug,
        )

    async def get_slot_data(
        self,
        slotId: str,
        debug: bool = False,
    ) -> responses.SlotData:
        """Fetch slot data by ID.

        Args:
            slotId: ID of the slot.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetSlot(slotId=slotId),
            responses.SlotData, debug,
        )

    async def add_slot(
        self,
        *,
        parent: str | workers.Slot | None = None,
        name: fields.FieldString | str | None = None,
        position: Float3Like | None = None,
        rotation: FloatQLike | None = None,
        scale: Float3Like | None = None,
        isActive: fields.FieldBool | bool | None = None,
        isPersistent: fields.FieldBool | bool | None = None,
        tag: fields.FieldString | str | None = None,
        orderOffset: fields.FieldLong | int | None = None,
        components: list[workers.Component] | None = None,
        children: list[workers.Slot] | None = None,
        id: str | None = None,
        debug: bool = False,
    ) -> workers.Slot:
        """Create a new slot.

        Each field parameter accepts either the Field wrapper or a raw
        value.  For example, ``name="Hello"`` is equivalent to
        ``name=fields.FieldString(value="Hello")``.  Vector parameters
        (``position``, ``scale``) also accept a 3-element sequence or
        numpy array, and ``rotation`` accepts a 4-element sequence or
        array.

        Args:
            parent: The parent slot — a slot ID string, a ``Slot``
                instance, or None for the root slot (default).
            name: Slot name (``str`` or ``FieldString``).
            position: Position relative to the parent (``Float3``,
                3-sequence, or ``FieldFloat3``).
            rotation: Rotation relative to the parent (``FloatQ``,
                4-sequence, or ``FieldFloatQ``).
            scale: Scale relative to the parent (``Float3``, 3-sequence,
                or ``FieldFloat3``).
            isActive: Whether the slot is active (``bool`` or
                ``FieldBool``).
            isPersistent: Whether the slot persists across sessions
                (``bool`` or ``FieldBool``).
            tag: Slot tag string (``str`` or ``FieldString``).
            orderOffset: Order offset among siblings (``int`` or
                ``FieldLong``).
            components: Components to attach.
            children: Child slots.
            id: Optional client-assigned ID.
            debug: Print request/response JSON.

        Returns:
            The created Slot.

        Raises:
            RuntimeError: If the server rejects the request.
        """
        parent_ref: members.Reference
        if parent is None:
            parent_ref = members.Reference(
                targetId=workers.Slot.ROOT_SLOT_ID,
            )
        elif isinstance(parent, workers.Slot):
            parent_ref = members.Reference(targetId=parent.id)
        else:
            parent_ref = members.Reference(targetId=parent)

        slot = workers.Slot(
            id=id,
            parent=parent_ref,
            name=(
                _coerce_scalar_field(name, fields.FieldString)
                if name is not None else None
            ),
            position=(
                _coerce_composite_field(
                    position, fields.FieldFloat3, primitives.Float3,
                )
                if position is not None else None
            ),
            rotation=(
                _coerce_composite_field(
                    rotation, fields.FieldFloatQ, primitives.FloatQ,
                )
                if rotation is not None else None
            ),
            scale=(
                _coerce_composite_field(
                    scale, fields.FieldFloat3, primitives.Float3,
                )
                if scale is not None else None
            ),
            isActive=(
                _coerce_scalar_field(isActive, fields.FieldBool)
                if isActive is not None else None
            ),
            isPersistent=(
                _coerce_scalar_field(isPersistent, fields.FieldBool)
                if isPersistent is not None else None
            ),
            tag=(
                _coerce_scalar_field(tag, fields.FieldString)
                if tag is not None else None
            ),
            orderOffset=(
                _coerce_scalar_field(
                    orderOffset, fields.FieldLong, np.int64,
                )
                if orderOffset is not None else None
            ),
            components=components if components is not None else [],
            children=children if children is not None else [],
        )
        resp = await self.send_message(
            messages.AddSlot(data=slot),
            responses.NewEntityId, debug,
        )
        if resp.entityId is None:
            raise RuntimeError(
                f"Failed to create slot: {resp.errorInfo}"
            )
        return workers.Slot(id=resp.entityId)

    async def get_global_transform(
        self,
        slot: str | workers.Slot,
        timeout: float = DEFAULT_TIMEOUT,
        debug: bool = False,
    ) -> transforms.Transform:
        """Returns a slot's position, rotation, and scale in world space.

        The transforms of a slot and of each of its ancestors can change in
        every engine update, so composing local transforms that were read
        in separate requests would mix values from different updates.
        Instead, this adds a temporary probe slot under Root with a
        CopyGlobalTransform and a CopyGlobalScale component whose source is
        the slot. In each engine update the two components set the probe's
        transform relative to Root to the slot's. The probe's position and
        scale start at random values, and the probe is read until the
        drives have replaced both.

        The components have the largest UpdateOrder, so they copy the
        transform after every other component's common update. The result
        is the slot's transform at that point in one engine update. Changes
        made later in the same update, such as by IK, aren't included.

        This takes about 60 ms at 60 FPS, regardless of how deeply the slot
        is nested.

        Args:
            slot: The slot, either a slot ID string or a ``Slot``
                instance (whose ``id`` is used).
            timeout: Seconds to wait for the drives to run.
            debug: Print request/response JSON.

        Returns:
            The slot's transform relative to the world, which includes
            Root's own transform.

        Raises:
            RuntimeError: If the server rejects a request, such as when
                the slot doesn't exist.
            TimeoutError: If the drives haven't run within the timeout.
        """
        slot_id = slot.id if isinstance(slot, workers.Slot) else slot
        assert slot_id is not None, "Slot has no ID"
        root = workers.Slot.ROOT_SLOT_ID
        if slot_id == root:
            # Root has no parent, so its local transform is its global one.
            # A probe would give the wrong scale, because CopyGlobalScale
            # treats Root as its own parent.
            return _transform_of(
                await self._get_slot_data(root, debug), root,
            )

        probe_id = str(uuid.uuid4())
        # Any value could be a real transform, so the sentinels are drawn
        # anew for each call. The chance that a driven value equals one
        # exactly is about 2**-96. They're far from the float32 limits and
        # from values a world is likely to use, such as float.MaxValue.
        position_sentinel = _random_float3()
        scale_sentinel = _random_float3()
        probe = workers.Slot(
            id=probe_id,
            parent=members.Reference(targetId=root),
            name=fields.FieldString(value="Global transform probe"),
            position=fields.FieldFloat3(value=position_sentinel),
            scale=fields.FieldFloat3(value=scale_sentinel),
            isPersistent=fields.FieldBool(value=False),
        )
        # Both components drive the fields of the slot they're attached to,
        # without being told which.
        probe_components = [
            workers.Component(
                id=str(uuid.uuid4()),
                componentType="[FrooxEngine]FrooxEngine.CopyGlobalTransform",
                members={
                    "Source": members.Reference(targetId=slot_id),
                    "UpdateOrder": fields.FieldInt(value=_PROBE_UPDATE_ORDER),
                },
            ),
            workers.Component(
                id=str(uuid.uuid4()),
                componentType="[FrooxEngine]FrooxEngine.CopyGlobalScale",
                members={
                    "Source": members.Reference(targetId=slot_id),
                    "NonUniform": fields.FieldBool(value=True),
                    "UpdateOrder": fields.FieldInt(value=_PROBE_UPDATE_ORDER),
                },
            ),
        ]
        try:
            # AddSlot fails when given components, so they're added separately in the
            # same batch. The GetSlot reports a missing slot.
            created = await self.data_model_operation_batch(
                [
                    messages.GetSlot(slotId=slot_id),
                    messages.AddSlot(data=probe),
                    *(messages.AddComponent(containerSlotId=probe_id, data=c)
                      for c in probe_components),
                ],
                debug,
            )
            for response in created.responses or []:
                if not response.success:
                    raise RuntimeError(
                        f"Failed to probe slot {slot_id}: {response.errorInfo}"
                    )

            deadline = asyncio.get_running_loop().time() + timeout
            while True:
                # Root is read in the same engine update as the probe.
                polled = await self.data_model_operation_batch(
                    [messages.GetSlot(slotId=probe_id),
                     messages.GetSlot(slotId=root)],
                    debug,
                )
                probe_data, root_data = _batch_slot_data(polled, 2)
                if (
                    probe_data.position is not None
                    and probe_data.position.value != position_sentinel
                    and probe_data.scale is not None
                    and probe_data.scale.value != scale_sentinel
                ):
                    return transforms.compose(
                        _transform_of(root_data, root),
                        _transform_of(probe_data, probe_id),
                    )
                if asyncio.get_running_loop().time() > deadline:
                    raise TimeoutError(
                        f"The probe of slot {slot_id} wasn't driven within "
                        f"{timeout} s."
                    )
                await asyncio.sleep(_PROBE_POLL_INTERVAL)
        finally:
            await self.remove_slot(probe_id, debug)

    async def _get_slot_data(self, slot_id: str, debug: bool) -> workers.Slot:
        """Returns a slot's data.

        Raises:
            RuntimeError: If the server rejects the request.
        """
        resp = await self.get_slot(slot_id, debug=debug)
        if resp.data is None:
            raise RuntimeError(f"Failed to get slot {slot_id}: {resp.errorInfo}")
        return resp.data

    async def update_slot(
        self,
        data: workers.Slot,
        debug: bool = False,
    ) -> responses.Response:
        """Updates an existing slot.

        Only the fields that are set in data are changed. The server
        associates the member ID in an update with the slot's field
        (ResoniteLinkTranslator.WriteMemberData), and it fails on a second ID
        for a field that already has one, with "One of the dictionaries
        already contains one of the elements". A field gets an ID when it's
        read or written with one, and a field constructed in Python has a
        fresh random ID. The server skips the association for an empty ID,
        so this sends every field with an empty ID. data itself isn't
        modified.

        Args:
            data: Slot data with ``id`` set to the target slot.
            debug: Print request/response JSON.

        Returns:
            The response, whose ``success`` is True if the update was
            applied.
        """
        anonymous = {
            name: dc.replace(member, id="")
            for name in _SLOT_MEMBER_FIELDS
            if (member := getattr(data, name)) is not None
        }
        return await self.send_message(
            messages.UpdateSlot(data=dc.replace(data, **anonymous)),
            responses.Response, debug,
        )

    async def remove_slot(
        self,
        slot: str | workers.Slot,
        debug: bool = False,
    ) -> responses.Response:
        """Remove a slot.

        Args:
            slot: The slot to remove — either a slot ID string, or a
                ``Slot`` instance (whose ``id`` is used).
            debug: Print request/response JSON.
        """
        slot_id = slot.id if isinstance(slot, workers.Slot) else slot
        assert slot_id is not None, "Slot has no ID"
        return await self.send_message(
            messages.RemoveSlot(slotId=slot_id),
            responses.Response, debug,
        )

    # =========================================================================
    # Component operations
    # =========================================================================

    async def get_component(
        self,
        componentId: str,
        debug: bool = False,
    ) -> responses.ComponentData:
        """Fetch component data.

        Args:
            componentId: ID of the component.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetComponent(componentId=componentId),
            responses.ComponentData, debug,
        )

    async def add_component(
        self,
        containerSlotId: str | workers.Slot,
        *,
        data: workers.Component | None = None,
        componentType: str | None = None,
        references: dict[str, str] | None = None,
        debug: bool = False,
    ) -> responses.NewEntityId:
        """Add a component to a slot.

        Can be called in two ways:

        1. **With ``data``** — pass a full ``Component`` object::

               await client.add_component(
                   containerSlotId=slot_id,
                   data=workers.Component(componentType="..."),
               )

        2. **With ``componentType`` (and optional ``references``)** —
           the ``Component`` is built automatically.  Each entry in
           *references* maps a member name to a target ID, which the
           server applies when creating the component::

               await client.add_component(
                   containerSlotId=slot_id,
                   componentType="[ProtoFluxBindings]...ValueDisplay<float>",
                   references={"Input": node_id, "_value": field_id},
               )

        Args:
            containerSlotId: ID of the slot to add the component to.
            data: A pre-built Component. Mutually exclusive with
                *componentType*.
            componentType: Fully-qualified Resonite component type. A
                ``Component`` is created from this and *references*.
            references: Mapping of member name to target ID for
                reference members to wire at creation time.
            debug: Print request/response JSON.

        Returns:
            Response with ``entityId`` of the new component.
        """
        if isinstance(containerSlotId, workers.Slot):
            assert containerSlotId.id is not None, "Slot has no ID"
            containerSlotId = containerSlotId.id
        if data is None:
            if componentType is None:
                raise ValueError(
                    "Either 'data' or 'componentType' must be provided"
                )
            component_members: dict[str, members.Member] = {}
            if references:
                for name, target_id in references.items():
                    component_members[name] = members.Reference(
                        targetId=target_id,
                    )
            data = workers.Component(
                componentType=componentType,
                members=component_members,
            )
        return await self.send_message(
            messages.AddComponent(
                containerSlotId=containerSlotId, data=data,
            ),
            responses.NewEntityId, debug,
        )

    async def update_references(
        self,
        componentId: str,
        references: Mapping[str, str | members.Reference],
        debug: bool = False,
    ) -> responses.Response:
        """Wire reference members on an existing component.

        Fetches the component to learn server-assigned member IDs, then
        sends an update setting each named reference to the given
        target ID.  This avoids the manual ``get_component`` /
        ``update_component`` dance::

            await client.update_references(
                componentId=comp_id,
                references={"Input": node_id, "_value": field_id},
            )

        Args:
            componentId: ID of the component to update.
            references: Mapping of member name to target ID or Reference.
            debug: Print request/response JSON.
        """
        get_resp = await self.get_component(
            componentId=componentId, debug=debug,
        )
        assert get_resp.data is not None
        update_members: dict[str, members.Member] = {}
        for name, ref_val in references.items():
            existing = get_resp.data.members.get(name)
            if isinstance(ref_val, members.Reference):
                new_ref = ref_val
                if existing is not None:
                    new_ref.id = existing.id
                update_members[name] = new_ref
            else:
                target_id = ref_val
                if existing is not None:
                    update_members[name] = members.Reference(
                        id=existing.id, targetId=target_id,
                    )
                else:
                    # Member not on the component data (e.g. proxy members
                    # like _value on ValueFieldDrive). Send with a fresh ID
                    # and let the server resolve it.
                    update_members[name] = members.Reference(
                        targetId=target_id,
                    )
        return await self.update_component(
            data=workers.Component(
                id=componentId,
                componentType=get_resp.data.componentType,
                members=update_members,
            ),
            debug=debug,
        )

    async def update_component(
        self,
        data: workers.Component,
        debug: bool = False,
    ) -> responses.Response:
        """Update an existing component.

        Args:
            data: Component data with ``id`` set. Only include members
                that should be updated; each member must have its ``id``
                from a prior ``get_component`` call.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.UpdateComponent(data=data),
            responses.Response, debug,
        )

    async def remove_component(
        self,
        componentId: str,
        debug: bool = False,
    ) -> responses.Response:
        """Remove a component.

        Args:
            componentId: ID of the component to remove.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.RemoveComponent(componentId=componentId),
            responses.Response, debug,
        )

    # =========================================================================
    # Reflection operations
    # =========================================================================

    async def get_component_type_list(
        self,
        categoryPath: str | None = None,
        debug: bool = False,
    ) -> responses.ComponentTypeList:
        """List component types in a category.

        The doc comment on GetComponentTypeList.CategoryPath, in
        ResoniteLink/Models/Messages/Reflection/GetComponentDefinitionList.cs
        of the ResoniteLink repository, says that ``"*"`` lists every
        component. As of Resonite 2026.9.18.82 it returns an empty list, so
        listing everything means walking the subcategories.

        Args:
            categoryPath: Category path (e.g. ``"/Data"``). None or ``"/"``
                is the root category.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetComponentTypeList(categoryPath=categoryPath),
            responses.ComponentTypeList, debug,
        )

    async def get_component_definition(
        self,
        componentType: str,
        flattened: bool = True,
        debug: bool = False,
    ) -> responses.ComponentDefinitionData:
        """Get a component's type definition.

        Args:
            componentType: Fully qualified component type name.
            flattened: Include inherited members.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetComponentDefinition(
                componentType=componentType, flattened=flattened,
            ),
            responses.ComponentDefinitionData, debug,
        )

    async def get_type_definition(
        self,
        type: str,  # pylint: disable=redefined-builtin
        debug: bool = False,
    ) -> responses.TypeDefinitionData:
        """Get any type's definition, including interfaces and enums.

        GetTypeDefinition fails for component types. Use
        get_component_definition for those.

        Args:
            type: Fully qualified type name, e.g.
                ``"[FrooxEngine]FrooxEngine.IAssetProvider<>"``.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetTypeDefinition(type=type),
            responses.TypeDefinitionData, debug,
        )

    async def get_generic_type_definition(
        self,
        genericInstanceType: str,
        debug: bool = False,
    ) -> responses.TypeDefinitionData:
        """Get the generic definition of a constructed generic type.

        For ``ValueField<float>`` this returns the definition of
        ``ValueField<>``.

        Args:
            genericInstanceType: The constructed generic type.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetGenericTypeDefinition(
                genericInstanceType=genericInstanceType,
            ),
            responses.TypeDefinitionData, debug,
        )

    async def get_enum_definition(
        self,
        type: str,  # pylint: disable=redefined-builtin
        debug: bool = False,
    ) -> responses.EnumDefinitionData:
        """Get an enum's values and backing type.

        Many enums live outside FrooxEngine. ColorProfile, for one, is
        ``"[Renderite.Shared]Renderite.Shared.ColorProfile"``. As of
        Resonite 2026.9.18.82, a name that doesn't resolve fails with a
        NullReferenceException message where "not a valid type" is meant.

        Args:
            type: Fully qualified enum type name.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetEnumDefinition(type=type),
            responses.EnumDefinitionData, debug,
        )

    async def get_sync_object_definition(
        self,
        syncObjectType: str,
        flattened: bool = True,
        debug: bool = False,
    ) -> responses.SyncObjectDefinitionData:
        """Get a sync object type's definition, such as UserRef's.

        Slot and Component are workers, not sync objects, so this fails
        for them.

        Args:
            syncObjectType: Fully qualified sync object type name.
            flattened: Include inherited members.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.GetSyncObjectDefinition(
                syncObjectType=syncObjectType, flattened=flattened,
            ),
            responses.SyncObjectDefinitionData, debug,
        )

    # =========================================================================
    # Sync methods and batches
    # =========================================================================

    async def call_sync_method(
        self,
        target: str | workers.Worker | Any,
        methodName: str,
        arguments: dict[str, object] | None = None,
        debug: bool = False,
    ) -> responses.MethodResult:
        """Call a sync method on a component or sync member.

        Generated components also have a wrapper for each of their sync
        methods.

        As of Resonite 2026.9.18.82, a method whose definition has
        ``isAsync`` set fails with "Type not supported: Task`1" after the
        server has started it, so its effect still happens. That covers
        nearly every asset processing method, such as
        StaticMesh.RecalculateNormals.

        Args:
            target: The target's ID, or an object with an ``id``, such as a
                component.
            methodName: The method's name, as in the definition's methods.
            arguments: Parameter names mapped to values. A primitive is
                passed as its field class, such as
                ``fields.FieldInt(value=2)``. A component or slot is passed
                as itself and becomes a reference.
            debug: Print request/response JSON.

        Returns:
            The result, whose ``result`` holds the returned value.
        """
        target_id = target if isinstance(target, str) else target.id
        assert target_id is not None, "Target has no ID"
        return await self.send_message(
            messages.CallSyncMethod(
                targetID=target_id, methodName=methodName,
                arguments=members.tag_method_arguments(arguments),
            ),
            responses.MethodResult, debug,
        )

    async def call_static_sync_method(
        self,
        targetType: str,
        methodName: str,
        arguments: dict[str, object] | None = None,
        debug: bool = False,
    ) -> responses.MethodResult:
        """Call a static sync method on a type.

        As of Resonite 2026.9.18.82, most static sync methods, such as
        MeterTool.FilterUsers, fail with "Type must derive from Delegate",
        and the server returns a plain Response, which raises
        RuntimeError here. AvatarCreator's static methods are the
        exception.

        Args:
            targetType: Fully qualified type name.
            methodName: The method's name, as in the definition's methods.
            arguments: Parameter names mapped to values, as for
                call_sync_method.
            debug: Print request/response JSON.

        Returns:
            The result, whose ``result`` holds the returned value.
        """
        return await self.send_message(
            messages.CallStaticSyncMethod(
                targetType=targetType, methodName=methodName,
                arguments=members.tag_method_arguments(arguments),
            ),
            responses.MethodResult, debug,
        )

    # Messages that derive from DataModelOperation in ResoniteLink, which
    # are the only ones a batch can hold.
    _BATCHABLE: tuple[type, ...] = (
        messages.GetSlot, messages.AddSlot, messages.UpdateSlot,
        messages.RemoveSlot, messages.GetComponent, messages.AddComponent,
        messages.UpdateComponent, messages.RemoveComponent,
        messages.CallSyncMethod, messages.CallStaticSyncMethod,
    )

    async def data_model_operation_batch(
        self,
        operations: Sequence[messages.Message],
        debug: bool = False,
    ) -> responses.BatchResponse:
        """Apply several data model operations in one engine update.

        The server processes the operations in order with no engine update
        in between, so nothing else in the world sees or changes the
        objects halfway through. Each operation gets its own response, in
        order, and the batch's own success only says that it was
        processed.

        Args:
            operations: Slot and component operations and sync method
                calls, such as messages.AddSlot or messages.UpdateComponent.
            debug: Print request/response JSON.

        Returns:
            The batch response, whose ``responses`` hold one response per
            operation.

        Raises:
            TypeError: An operation isn't a data model operation, such as
                a reflection or import message.
        """
        for operation in operations:
            if not isinstance(operation, self._BATCHABLE):
                raise TypeError(
                    f"{type(operation).__name__} can't be batched. Only slot "
                    f"and component operations and sync method calls can."
                )
            # The server echoes each operation's ID as its response's
            # sourceMessageId, which is None for an operation without one.
            if operation.messageId is None:
                operation.messageId = str(uuid.uuid4())
        return await self.send_message(
            messages.DataModelOperationBatch(operations=list(operations)),
            responses.BatchResponse, debug,
        )

    # =========================================================================
    # Asset import operations
    # =========================================================================

    async def import_texture_2d_file(
        self,
        filePath: str,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a texture from a file.

        Args:
            filePath: Path to the texture file on the local file system.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportTexture2DFile(filePath=filePath),
            responses.AssetData, debug,
        )

    async def import_audio_clip_file(
        self,
        filePath: str,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import an audio clip from a file.

        Supported formats: WAV, OGG, FLAC.

        Args:
            filePath: Path to the audio file on the local file system.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportAudioClipFile(filePath=filePath),
            responses.AssetData, debug,
        )

    async def import_audio_clip_raw_data(
        self,
        samples: np.ndarray,
        sampleRate: int,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import an audio clip from PCM samples.

        Args:
            samples: The samples, from -1 to 1, shaped (sample count,) for
                mono or (sample count, channel count).
            sampleRate: The sample rate in Hz.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportAudioClipRawData.from_samples(samples, sampleRate),
            responses.AssetData, debug,
        )

    async def import_texture_2d_raw_data(
        self,
        pixels: np.ndarray,
        colorProfile: str = "sRGB",
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a texture from RGBA pixels.

        Args:
            pixels: The image, shaped (height, width, 4), as uint8. Row 0
                of the array is y = 0.
            colorProfile: The color profile of the data, e.g. "sRGB" or
                "Linear".
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportTexture2DRawData.from_pixels(pixels, colorProfile),
            responses.AssetData, debug,
        )

    async def import_texture_2d_raw_data_hdr(
        self,
        pixels: np.ndarray,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a texture from floating point RGBA pixels, allowing HDR values.

        Args:
            pixels: The image, shaped (height, width, 4), as float32.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportTexture2DRawDataHDR.from_pixels(pixels),
            responses.AssetData, debug,
        )

    async def import_cubemap_files(
        self,
        positiveX: str,
        positiveY: str,
        positiveZ: str,
        negativeX: str,
        negativeY: str,
        negativeZ: str,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a cubemap from six face images.

        Args:
            positiveX: Path to the +X face image, and so on for the others.
            positiveY: Path to the +Y face image.
            positiveZ: Path to the +Z face image.
            negativeX: Path to the -X face image.
            negativeY: Path to the -Y face image.
            negativeZ: Path to the -Z face image.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportCubemapFiles(
                filePathPositiveX=positiveX, filePathPositiveY=positiveY,
                filePathPositiveZ=positiveZ, filePathNegativeX=negativeX,
                filePathNegativeY=negativeY, filePathNegativeZ=negativeZ,
            ),
            responses.AssetData, debug,
        )

    async def import_cubemap_file_with_regions(
        self,
        filePath: str,
        positiveX: primitives.Rect,
        positiveY: primitives.Rect,
        positiveZ: primitives.Rect,
        negativeX: primitives.Rect,
        negativeY: primitives.Rect,
        negativeZ: primitives.Rect,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a cubemap from one image that holds all six faces.

        As of Resonite 2026.9.18.82, this always fails with "The supplied
        Bitmap2D's don't all have mipmaps", because of a server bug. Use
        import_cubemap_files or import_cubemap_raw_data instead.

        Args:
            filePath: Path to the image.
            positiveX: The +X face's region of the image, in coordinates
                from 0 to 1, and so on for the others.
            positiveY: The +Y face's region.
            positiveZ: The +Z face's region.
            negativeX: The -X face's region.
            negativeY: The -Y face's region.
            negativeZ: The -Z face's region.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportCubemapFileWithRegions(
                filePath=filePath,
                positiveXregion=positiveX, positiveYregion=positiveY,
                positiveZregion=positiveZ, negativeXregion=negativeX,
                negativeYregion=negativeY, negativeZregion=negativeZ,
            ),
            responses.AssetData, debug,
        )

    async def import_cubemap_raw_data(
        self,
        levels: Sequence[np.ndarray],
        colorProfile: str = "sRGB",
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a cubemap from RGBA faces.

        Args:
            levels: The mip levels, each shaped (6, size, size, 4) as uint8,
                with the faces in the order +X, +Y, +Z, -X, -Y, -Z. One
                level means no mip maps. More than one must be the whole
                chain down to 1x1.
            colorProfile: The color profile of the data.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportCubemapRawData.from_levels(levels, colorProfile),
            responses.AssetData, debug,
        )

    async def import_cubemap_raw_data_hdr(
        self,
        levels: Sequence[np.ndarray],
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a cubemap from floating point RGBA faces, allowing HDR values.

        Args:
            levels: The mip levels, as for import_cubemap_raw_data, but as
                float32.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportCubemapRawDataHDR.from_levels(levels),
            responses.AssetData, debug,
        )

    async def import_mesh_json(
        self,
        vertices: Sequence[mesh.Vertex],
        submeshes: Sequence[
            mesh.PointSubmesh | mesh.TriangleSubmesh | mesh.TriangleSubmeshFlat
        ],
        bones: Sequence[mesh.Bone] | None = None,
        blendshapes: Sequence[mesh.BlendShape] | None = None,
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a mesh described in JSON. Convenient for small meshes.

        As of Resonite 2026.9.18.82, the server rejects any vertex with UV
        coordinates, with "UV channel 0 is already configured with 0
        dimensions". import_mesh_raw_data handles UVs.

        Args:
            vertices: The vertices.
            submeshes: The submeshes, which index into the vertices.
            bones: The bones, for a skinned mesh.
            blendshapes: The blendshapes.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.ImportMeshJSON(
                vertices=list(vertices), submeshes=list(submeshes),
                bones=list(bones) if bones else None,
                blendshapes=list(blendshapes) if blendshapes else None,
            ),
            responses.AssetData, debug,
        )

    async def import_mesh_raw_data(
        self,
        positions: np.ndarray,
        submeshes: Sequence[mesh.RawTriangles | mesh.RawPoints],
        *,
        normals: np.ndarray | None = None,
        tangents: np.ndarray | None = None,
        colors: np.ndarray | None = None,
        uvs: Sequence[np.ndarray] = (),
        bone_indices: np.ndarray | None = None,
        bone_weights: np.ndarray | None = None,
        bones: Sequence[mesh.Bone] | None = None,
        blendshapes: Sequence[mesh.RawBlendShape] = (),
        debug: bool = False,
    ) -> responses.AssetData:
        """Import a mesh given as numpy arrays, for meshes of any size.

        The arguments are those of messages.ImportMeshRawData.from_arrays.
        """
        return await self.send_message(
            messages.ImportMeshRawData.from_arrays(
                positions, submeshes, normals=normals, tangents=tangents,
                colors=colors, uvs=uvs, bone_indices=bone_indices,
                bone_weights=bone_weights, bones=bones,
                blendshapes=blendshapes,
            ),
            responses.AssetData, debug,
        )

    async def find_slot(
        self,
        parent: str | workers.Slot,
        *,
        name: str | None = None,
        tag: str | None = None,
        depth: int = -1,
        match_substring: bool = False,
        ignore_case: bool = False,
        debug: bool = False,
    ) -> workers.Slot | None:
        """Find a child slot by name or tag using ProtoFlux search nodes.

        Creates temporary ProtoFlux nodes (FindChildByName or
        FindChildByTag) on a temporary slot, lets the engine evaluate
        the search, reads the result, and cleans up.  This is much
        faster than fetching the entire slot hierarchy for deep searches.

        Args:
            parent: The slot to search under (string ID or Slot instance).
            name: The slot name to search for.
            tag: The slot tag to search for.
            depth: Maximum search depth (-1 for unlimited).
            match_substring: If True, match substrings of the name.
            ignore_case: If True, ignore case when matching.
            debug: Print request/response JSON.

        Returns:
            The found Slot, or None if not found.

        Raises:
            ValueError: If neither name nor tag is specified.
        """
        from pyresonitelink.data import primitives
        from pyresonitelink.protoflux.core import (
            RefObjectInput,
            ValueInput,
            ValueObjectInput,
        )
        from pyresonitelink.protoflux.flow import Update
        from pyresonitelink.protoflux.variables.dynamic import (
            WriteDynamicObjectVariable,
        )
        from pyresonitelink.components.data.dynamic import (
            DynamicReferenceVariable,
            DynamicVariableSpace,
        )

        if name is None and tag is None:
            raise ValueError("Either name or tag must be specified.")

        parent_id = parent.id if isinstance(parent, workers.Slot) else parent

        # Create a temporary slot for the search nodes
        tmp = await self.add_slot(
            name="__find_slot_tmp__", debug=debug,
        )

        try:
            # Dynamic variable to hold the result
            dyn_space = DynamicVariableSpace()
            await dyn_space.add_to_slot(self, tmp, debug=debug)
            result_var = DynamicReferenceVariable[workers.Slot](
                variable_name="result",
            )
            await result_var.add_to_slot(self, tmp, debug=debug)

            # Parent slot reference (for FindChild)
            parent_ref = RefObjectInput[workers.Slot](target=parent_id)
            await parent_ref.add_to_slot(self, tmp, debug=debug)

            # Tmp slot reference (for WriteDynamicObjectVariable target)
            tmp_ref = RefObjectInput[workers.Slot](target=tmp)
            await tmp_ref.add_to_slot(self, tmp, debug=debug)

            # Depth input
            depth_input = ValueInput[primitives.Int](primitives.Int(depth))
            await depth_input.add_to_slot(self, tmp, debug=debug)

            # Create the appropriate find node
            if name is not None:
                from pyresonitelink.protoflux.slots.searching import (
                    FindChildByName,
                )

                name_input = ValueObjectInput[primitives.String](value=name)
                await name_input.add_to_slot(self, tmp, debug=debug)

                match_substring_id: str | None = None
                if match_substring:
                    ms_input = ValueInput[primitives.Bool](
                        primitives.Bool(True),
                    )
                    await ms_input.add_to_slot(self, tmp, debug=debug)
                    match_substring_id = ms_input.id
                ignore_case_id: str | None = None
                if ignore_case:
                    ic_input = ValueInput[primitives.Bool](
                        primitives.Bool(True),
                    )
                    await ic_input.add_to_slot(self, tmp, debug=debug)
                    ignore_case_id = ic_input.id

                find = FindChildByName(
                    instance=parent_ref.id,
                    name=name_input.id,
                    search_depth=depth_input.id,
                    match_substring=match_substring_id,
                    ignore_case=ignore_case_id,
                )
                await find.add_to_slot(self, tmp, debug=debug)
            else:
                from pyresonitelink.protoflux.slots.searching import (
                    FindChildByTag,
                )

                assert tag is not None
                tag_input = ValueObjectInput[primitives.String](value=tag)
                await tag_input.add_to_slot(self, tmp, debug=debug)

                find = FindChildByTag(
                    instance=parent_ref.id,
                    tag=tag_input.id,
                    search_depth=depth_input.id,
                )
                await find.add_to_slot(self, tmp, debug=debug)

            # Write the find result to the dynamic variable
            path_input = ValueObjectInput[primitives.String](value="result")
            await path_input.add_to_slot(self, tmp, debug=debug)

            WriteSlot = WriteDynamicObjectVariable[workers.Slot]
            write = WriteSlot()
            await write.add_to_slot(self, tmp, debug=debug)
            await self.update_references(
                componentId=write.id,  # type: ignore[arg-type]
                references={
                    "Target": tmp_ref.id,  # type: ignore[arg-type]
                    "Path": path_input.id,  # type: ignore[arg-type]
                    "Value": find.id,  # type: ignore[arg-type]
                },
                debug=debug,
            )

            # Update fires the write once
            update = Update(on_update=write.id)  # type: ignore[arg-type]
            await update.add_to_slot(self, tmp, debug=debug)

            # Wait for engine evaluation
            await asyncio.sleep(0.5)

            # Read the result
            await result_var.refresh(self, debug=debug)
            found_id = result_var.reference
            if found_id is None:
                return None
            return workers.Slot(id=found_id)
        finally:
            # Clean up the temporary slot
            await self.remove_slot(slot=tmp, debug=debug)

    async def create_audio_clip(
        self,
        slot: str | workers.Slot,
        filePath: str,
        debug: bool = False,
    ) -> "StaticAudioClip":
        """Import an audio file and create a StaticAudioClip on a slot.

        This is a convenience method that combines ``import_audio_clip_file``
        and ``StaticAudioClip`` creation. The import is content-addressed
        and idempotent — importing the same file twice returns the same
        URL without duplication.

        Args:
            slot: The slot to add the StaticAudioClip to.
            filePath: Path to the audio file (WAV, OGG, FLAC).
            debug: Print request/response JSON.

        Returns:
            A ``StaticAudioClip`` component added to the slot, with its
            URL set to the imported asset.
        """
        import os

        from pyresonitelink.components.assets import StaticAudioClip

        asset = await self.import_audio_clip_file(
            filePath=os.path.abspath(filePath), debug=debug,
        )
        clip = StaticAudioClip(url=asset.assetURL)
        await clip.add_to_slot(self, slot, debug=debug)
        return clip

    async def create_audio_multiplexer(
        self,
        slot: str | workers.Slot,
        filePaths: list[str],
        debug: bool = False,
    ) -> "AssetMultiplexer":
        """Import multiple audio files and create an AssetMultiplexer.

        Creates a ``StaticAudioClip`` for each file, then an
        ``AssetMultiplexer<AudioClip>`` with all clips in its Assets
        list.  The multiplexer's ``Index`` field selects which clip
        is active.

        Audio imports are content-addressed and idempotent — the same
        file always produces the same URL without duplication.  Safe to
        call repeatedly.

        Usage::

            mux = await resolink.create_audio_multiplexer(slot, [
                "sounds/notification.wav",
                "sounds/ptink.wav",
                "sounds/tikatak.wav",
            ])

            # Use in Dergflux — bind the loop index to the multiplexer
            with g.For(3) as f:
                with f.OnIterate() as i:
                    g.Bind(i, mux, "Index")
                    with g.PlayOneShotAndWait(clip=mux) as r:
                        ...

        Args:
            slot: The slot to add all components to.
            filePaths: Paths to audio files (WAV, OGG, FLAC).
            debug: Print request/response JSON.

        Returns:
            An ``AssetMultiplexer<AudioClip>`` component with all clips
            loaded in its Assets list.
        """
        from pyresonitelink.generated.assets.utility.asset_multiplexer import AssetMultiplexer
        from pyresonitelink.generated._types.audio_clip import AudioClip
        from pyresonitelink.data import members as mem

        # Import each file and create StaticAudioClip components
        clips = []
        for path in filePaths:
            clip = await self.create_audio_clip(slot, path, debug=debug)
            clips.append(clip)

        # Create the multiplexer
        AudioClipMux = AssetMultiplexer[AudioClip]
        mux = AudioClipMux()
        await mux.add_to_slot(self, slot, debug=debug)

        # Populate the Assets SyncList
        assets_list = mux.get_member("Assets")
        assets_id = (
            assets_list.id
            if isinstance(assets_list, mem.SyncList)
            else assets_list.get("id")
            if isinstance(assets_list, dict)
            else None
        )
        new_list = mem.SyncList(
            elements=[
                mem.Reference(targetId=clip.id) for clip in clips
            ],
        )
        if assets_id is not None:
            new_list.id = assets_id
        mux.set_member("Assets", new_list)
        await mux.update(self, debug=debug)

        return mux

    # =========================================================================
    # Session operations
    # =========================================================================

    async def request_session_data(
        self,
        debug: bool = False,
    ) -> responses.SessionData:
        """Request session data for the current ResoniteLink session.

        Args:
            debug: Print request/response JSON.

        Returns:
            The Resonite and ResoniteLink versions, and the session's
            uniqueSessionId.
        """
        return await self.send_message(
            messages.RequestSessionData(),
            responses.SessionData, debug,
        )
