"""ResoniteLink client.

We don't expect concurrent requests; request() blocks until the response is received.

I strongly suggest using the async versions of the functions.
"""

import asyncio
import dataclasses as dc
import json
import uuid
from collections.abc import Sequence

import numpy as np
import websockets

from .data import codec
from .data import fields
from .data import members
from .data import messages
from .data import primitives
from .data import responses
from .data import workers


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
        assert isinstance(
            response, response_type
        ), f"Expected response Response, got {type(response)}"
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

    async def add_slot(
        self,
        *,
        parent: members.Reference | None = None,
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
    ) -> responses.NewEntityId:
        """Create a new slot.

        Each field parameter accepts either the Field wrapper or a raw
        value.  For example, ``name="Hello"`` is equivalent to
        ``name=fields.FieldString(value="Hello")``.  Vector parameters
        (``position``, ``scale``) also accept a 3-element sequence or
        numpy array, and ``rotation`` accepts a 4-element sequence or
        array.

        Args:
            parent: Reference to the parent slot.
            name: Slot name (``str`` or ``FieldString``).
            position: World position (``Float3``, 3-sequence, or
                ``FieldFloat3``).
            rotation: World rotation (``FloatQ``, 4-sequence, or
                ``FieldFloatQ``).
            scale: World scale (``Float3``, 3-sequence, or
                ``FieldFloat3``).
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
            Response with ``entityId`` of the new slot.
        """
        slot = workers.Slot(
            id=id,
            parent=parent,
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
        return await self.send_message(
            messages.AddSlot(data=slot),
            responses.NewEntityId, debug,
        )

    async def add_slot_to_root(
        self,
        *,
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
    ) -> responses.NewEntityId:
        """Create a new slot under the root slot.

        Convenience wrapper around :meth:`add_slot` with the parent set
        to the root slot.  See :meth:`add_slot` for parameter details.

        Args:
            name: Slot name (``str`` or ``FieldString``).
            position: World position (``Float3``, 3-sequence, or
                ``FieldFloat3``).
            rotation: World rotation (``FloatQ``, 4-sequence, or
                ``FieldFloatQ``).
            scale: World scale (``Float3``, 3-sequence, or
                ``FieldFloat3``).
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
            Response with ``entityId`` of the new slot.
        """
        return await self.add_slot(
            parent=members.Reference(targetId=workers.Slot.ROOT_SLOT_ID),
            name=name,
            position=position,
            rotation=rotation,
            scale=scale,
            isActive=isActive,
            isPersistent=isPersistent,
            tag=tag,
            orderOffset=orderOffset,
            components=components,
            children=children,
            id=id,
            debug=debug,
        )

    async def update_slot(
        self,
        data: workers.Slot,
        debug: bool = False,
    ) -> responses.Response:
        """Update an existing slot.

        Args:
            data: Slot data with ``id`` set to the target slot.
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.UpdateSlot(data=data),
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
        references: dict[str, str],
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
            references: Mapping of member name to target ID.
            debug: Print request/response JSON.
        """
        get_resp = await self.get_component(
            componentId=componentId, debug=debug,
        )
        assert get_resp.data is not None
        update_members: dict[str, members.Member] = {}
        for name, target_id in references.items():
            existing = get_resp.data.members.get(name)
            assert existing is not None, (
                f"Member {name!r} not found on component {componentId}"
            )
            update_members[name] = members.Reference(
                id=existing.id, targetId=target_id,
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

        Args:
            categoryPath: Category path (e.g. ``"/Data"``).
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

    # =========================================================================
    # Session operations
    # =========================================================================

    async def request_session_data(
        self,
        debug: bool = False,
    ) -> responses.Response:
        """Request session data for the current ResoniteLink session.

        Args:
            debug: Print request/response JSON.
        """
        return await self.send_message(
            messages.RequestSessionData(),
            responses.Response, debug,
        )
