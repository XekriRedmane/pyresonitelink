"""Offline tests of the client's slot methods, against a scripted server."""

# pylint: disable=missing-function-docstring,missing-class-docstring

from collections.abc import Callable
from typing import Any

import pytest

from pyresonitelink import client
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import messages
from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import transforms
from pyresonitelink.data import workers


class ScriptedClient(client.Client):
    """A client whose server is a function from each message to its response.

    Every message sent is recorded in ``sent``.
    """

    def __init__(
        self, server: Callable[[messages.Message], responses.Response],
    ) -> None:
        super().__init__()
        self.server = server
        self.sent: list[messages.Message] = []

    async def send_message[T](
        self, request: messages.Message, response_type: type[T], debug: bool = False,
    ) -> T:
        self.sent.append(request)
        response = self.server(request)
        assert isinstance(response, response_type), response
        return response


def _slot(
    slot_id: str,
    position: tuple[float, float, float] = (0, 0, 0),
    rotation: tuple[float, float, float, float] = (0, 0, 0, 1),
    scale: tuple[float, float, float] = (1, 1, 1),
) -> workers.Slot:
    """Returns slot data with the given local transform."""
    return workers.Slot(
        id=slot_id,
        position=fields.FieldFloat3(value=primitives.Float3(*position)),
        rotation=fields.FieldFloatQ(value=primitives.FloatQ(*rotation)),
        scale=fields.FieldFloat3(value=primitives.Float3(*scale)),
    )


def _ok() -> responses.Response:
    return responses.Response(success=True)


class FakeProbeServer:
    """Serves a global transform probe whose drives run on a given poll.

    Args:
        root: Root's data.
        driven: The probe's data once its drives have run.
        polls_before_driven: The number of polls that see the sentinels.
        slot_exists: Whether the probed slot exists.
    """

    def __init__(
        self,
        root: workers.Slot,
        driven: workers.Slot,
        polls_before_driven: int = 1,
        slot_exists: bool = True,
    ) -> None:
        self.root = root
        self.driven = driven
        self.polls_before_driven = polls_before_driven
        self.slot_exists = slot_exists
        self.probe: workers.Slot | None = None
        self.polls = 0
        self.removed: list[str] = []

    def get_slot(self, slot_id: str) -> responses.Response:
        if slot_id == workers.Slot.ROOT_SLOT_ID:
            return responses.SlotData(success=True, data=self.root)
        if self.probe is not None and slot_id == self.probe.id:
            self.polls += 1
            if self.polls <= self.polls_before_driven:
                return responses.SlotData(success=True, data=self.probe)
            return responses.SlotData(success=True, data=self.driven)
        if self.slot_exists:
            return responses.SlotData(success=True, data=_slot(slot_id))
        return responses.Response(errorInfo=f"Slot {slot_id} not found")

    def __call__(self, message: messages.Message) -> responses.Response:
        if isinstance(message, messages.DataModelOperationBatch):
            return responses.BatchResponse(
                success=True, responses=[self(m) for m in message.operations],
            )
        if isinstance(message, messages.AddSlot):
            self.probe = message.data
            return responses.NewEntityId(success=True, entityId=message.data.id)
        if isinstance(message, messages.AddComponent):
            return _ok()
        if isinstance(message, messages.GetSlot):
            return self.get_slot(message.slotId)
        if isinstance(message, messages.RemoveSlot):
            self.removed.append(message.slotId)
            return _ok()
        raise AssertionError(f"Unexpected message {message}")


def _assert_transform(actual: transforms.Transform, expected: transforms.Transform) -> None:
    assert actual.position == expected.position
    assert actual.rotation == expected.rotation
    assert actual.scale == expected.scale


class TestGetGlobalTransform:

    async def test_composes_root_and_driven_probe(self) -> None:
        root = _slot("Root", position=(0, 10, 0))
        driven = _slot("probe", (1, 2, 3), (0, 0.6, 0, 0.8), (2, 2, 2))
        server = FakeProbeServer(root, driven, polls_before_driven=2)
        resolink = ScriptedClient(server)

        result = await resolink.get_global_transform("target")

        _assert_transform(result, transforms.compose(
            client._transform_of(root, "Root"),
            client._transform_of(driven, "probe"),
        ))
        assert server.polls == 3
        assert server.probe is not None
        assert server.removed == [server.probe.id]

    async def test_probe_copies_the_slot_last(self) -> None:
        server = FakeProbeServer(_slot("Root"), _slot("probe", (1, 2, 3)))
        resolink = ScriptedClient(server)

        await resolink.get_global_transform("target")

        created = resolink.sent[0]
        assert isinstance(created, messages.DataModelOperationBatch)
        components = [
            m.data for m in created.operations
            if isinstance(m, messages.AddComponent)
        ]
        assert [c.componentType for c in components] == [
            "[FrooxEngine]FrooxEngine.CopyGlobalTransform",
            "[FrooxEngine]FrooxEngine.CopyGlobalScale",
        ]
        for component in components:
            source = component.members["Source"]
            assert isinstance(source, members.Reference)
            assert source.targetId == "target"
            order = component.members["UpdateOrder"]
            assert isinstance(order, fields.FieldInt)
            assert order.value == 2**31 - 1

    async def test_sentinels_differ_between_calls(self) -> None:
        probes = []
        for _ in range(2):
            server = FakeProbeServer(_slot("Root"), _slot("probe", (1, 2, 3)))
            await ScriptedClient(server).get_global_transform("target")
            probes.append(server.probe)
        assert probes[0] is not None and probes[1] is not None
        assert probes[0].position != probes[1].position
        assert probes[0].scale != probes[1].scale

    async def test_missing_slot(self) -> None:
        server = FakeProbeServer(_slot("Root"), _slot("probe"), slot_exists=False)
        with pytest.raises(RuntimeError, match="not found"):
            await ScriptedClient(server).get_global_transform("missing")
        assert server.probe is not None
        assert server.removed == [server.probe.id]

    async def test_timeout(self) -> None:
        server = FakeProbeServer(
            _slot("Root"), _slot("probe"), polls_before_driven=10**9,
        )
        with pytest.raises(TimeoutError):
            await ScriptedClient(server).get_global_transform("target", timeout=0.05)
        assert server.probe is not None
        assert server.removed == [server.probe.id]

    async def test_root_is_read_directly(self) -> None:
        root = _slot("Root", position=(0, 10, 0), scale=(3, 3, 3))
        server = FakeProbeServer(root, _slot("probe"))
        resolink = ScriptedClient(server)

        result = await resolink.get_global_transform(workers.Slot.ROOT_SLOT_ID)

        _assert_transform(result, client._transform_of(root, "Root"))
        assert server.probe is None


class TestUpdateSlot:

    async def test_sends_empty_member_ids(self) -> None:
        sent: list[workers.Slot] = []

        def server(message: messages.Message) -> responses.Response:
            assert isinstance(message, messages.UpdateSlot)
            sent.append(message.data)
            return _ok()

        update = workers.Slot(
            id="target",
            parent=members.Reference(targetId="Root"),
            position=fields.FieldFloat3(value=primitives.Float3(1, 2, 3)),
            name=fields.FieldString(value="New"),
        )
        fresh_ids: dict[str, Any] = {
            "parent": update.parent.id if update.parent else None,
            "position": update.position.id if update.position else None,
            "name": update.name.id if update.name else None,
        }

        response = await ScriptedClient(server).update_slot(update)

        assert response.success
        [data] = sent
        assert data.id == "target"
        assert data.parent is not None and data.parent.id == ""
        assert data.parent.targetId == "Root"
        assert data.position is not None and data.position.id == ""
        assert data.position.value == primitives.Float3(1, 2, 3)
        assert data.name is not None and data.name.id == ""
        assert data.name.value == "New"
        # Fields that weren't set stay unset, and the argument is unchanged.
        assert data.rotation is None
        assert update.parent is not None and update.position is not None
        assert update.name is not None
        assert update.parent.id == fresh_ids["parent"]
        assert update.position.id == fresh_ids["position"]
        assert update.name.id == fresh_ids["name"]
