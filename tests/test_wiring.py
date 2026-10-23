"""Unit tests for pyresonitelink.utils.wiring, against a fake client."""

from collections.abc import Mapping
from typing import Any

import pytest

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import workers
from pyresonitelink.protoflux import core
from pyresonitelink.protoflux import operators
from pyresonitelink.utils import wiring

FLOAT_OUTPUT = "[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>"
FLOAT_FIELD = "[FrooxEngine]FrooxEngine.IField<float>"
PROXY_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.CoreNodes.FieldDriveBase<float>+Proxy"


class FakeClient:
    """Stores components and records reference updates.

    A component's data, as get_component returns it, has the members it
    was added with, plus a member for each entry of reported, which
    stands in for the members and targetTypes that the server reports.
    For each added field drive, the fake adds a Proxy beside it once
    get_slot has been called proxy_after times.

    Attributes:
        components (dict[str, workers.Component]): The components, by ID.
        slot_of (dict[str, str]): The slot ID of each component.
        wired (list[tuple[str, Mapping[str, Any]]]): The component ID and
            references of each update_references call.
        get_slot_calls (int): How many times get_slot was called.
    """

    def __init__(
        self,
        reported: Mapping[str, members.Member] | None = None,
        proxy_after: int = 0,
        wire_success: bool = True,
    ) -> None:
        self.reported = dict(reported or {})
        self.proxy_after = proxy_after
        self.wire_success = wire_success
        self.components: dict[str, workers.Component] = {}
        self.slot_of: dict[str, str] = {}
        self.wired: list[tuple[str, Mapping[str, Any]]] = []
        self.get_slot_calls = 0
        self._pending_proxies: list[tuple[str, str]] = []

    def _store(self, slot_id: str, component: workers.Component) -> str:
        component.id = f"comp-{len(self.components) + 1}"
        self.components[component.id] = component
        self.slot_of[component.id] = slot_id
        return component.id

    async def add_component(
        self, containerSlotId: str, data: workers.Component, debug: bool = False,
    ) -> responses.NewEntityId:
        """Stores the component, with the reported members added."""
        component = workers.Component(
            componentType=data.componentType, members={**data.members, **self.reported},
        )
        component_id = self._store(containerSlotId, component)
        if "FieldDrive" in (data.componentType or ""):
            self._pending_proxies.append((containerSlotId, component_id))
        return responses.NewEntityId(success=True, entityId=component_id)

    async def get_component(
        self, componentId: str, debug: bool = False,
    ) -> responses.ComponentData:
        """Returns the stored component."""
        return responses.ComponentData(success=True, data=self.components[componentId])

    async def get_slot(
        self, slot: str | workers.Slot, includeComponentData: bool = False,
    ) -> responses.SlotData:
        """Returns the components on a slot, adding pending Proxies when due."""
        self.get_slot_calls += 1
        if self.get_slot_calls > self.proxy_after:
            for slot_id, drive_id in self._pending_proxies:
                self._store(slot_id, workers.Component(
                    componentType=PROXY_TYPE,
                    members={
                        "Node": members.Reference(targetId=drive_id),
                        "Drive": members.Reference(targetType=FLOAT_FIELD),
                    },
                ))
            self._pending_proxies = []
        slot_id = slot if isinstance(slot, str) else slot.id
        return responses.SlotData(success=True, data=workers.Slot(
            id=slot_id,
            components=[c for i, c in self.components.items() if self.slot_of[i] == slot_id],
        ))

    async def update_references(
        self, componentId: str, references: Mapping[str, Any], debug: bool = False,
    ) -> responses.Response:
        """Records the references."""
        self.wired.append((componentId, references))
        return responses.Response(
            success=self.wire_success, errorInfo=None if self.wire_success else "refused",
        )


@pytest.fixture(autouse=True)
def no_delays(monkeypatch: pytest.MonkeyPatch) -> None:
    """Removes the pauses, which the fake doesn't need."""
    monkeypatch.setattr(wiring, "WIRE_DELAY", 0)
    monkeypatch.setattr(wiring, "_PROXY_POLL_INTERVAL", 0)


def _reference(targets: Mapping[str, Any], name: str) -> members.Reference:
    """Returns one of the references sent in an update_references call."""
    reference = targets[name]
    assert isinstance(reference, members.Reference)
    return reference


class TestAddNode:
    async def test_wires_with_the_reported_target_types(self) -> None:
        fake = FakeClient(reported={
            "A": members.Reference(targetType=FLOAT_OUTPUT),
            "B": members.Reference(targetType=FLOAT_OUTPUT),
        })
        a = core.ValueInput[primitives.Float](primitives.Float(1))
        await wiring.add_node(fake, "slot", a)  # type: ignore[arg-type]
        add = operators.ValueAdd[primitives.Float]()
        await wiring.add_node(fake, "slot", add, {"A": a, "B": "some-id"})  # type: ignore[arg-type]
        assert add.id is not None and fake.slot_of[add.id] == "slot"
        ((component_id, targets),) = fake.wired
        assert component_id == add.id
        assert _reference(targets, "A").targetId == a.id
        assert _reference(targets, "B").targetId == "some-id"
        assert _reference(targets, "A").targetType == FLOAT_OUTPUT
        assert _reference(targets, "B").targetType == FLOAT_OUTPUT

    async def test_member_without_a_target_type(self) -> None:
        fake = FakeClient()
        add = operators.ValueAdd[primitives.Float]()
        await wiring.add_node(fake, "slot", add, {"A": "some-id"})  # type: ignore[arg-type]
        ((_, targets),) = fake.wired
        assert _reference(targets, "A").targetType == wiring._DEFAULT_TARGET_TYPE

    async def test_no_references_sends_no_update(self) -> None:
        fake = FakeClient()
        await wiring.add_node(fake, "slot", operators.ValueAdd[primitives.Float]())  # type: ignore[arg-type]
        assert fake.wired == []

    async def test_refused(self) -> None:
        fake = FakeClient(wire_success=False)
        with pytest.raises(RuntimeError, match="refused"):
            await wiring.add_node(
                fake, "slot", operators.ValueAdd[primitives.Float](), {"A": "x"},  # type: ignore[arg-type]
            )


class TestDriveField:
    async def test_sets_drive_on_the_proxy(self) -> None:
        fake = FakeClient(proxy_after=3)
        drive = core.ValueFieldDrive[primitives.Float]()
        await wiring.add_node(fake, "slot", drive)  # type: ignore[arg-type]
        await wiring.drive_field(fake, "slot", drive, "field-id")  # type: ignore[arg-type]
        (proxy,) = [c for c in fake.components.values() if c.componentType == PROXY_TYPE]
        ((component_id, targets),) = fake.wired
        assert component_id == proxy.id
        drive_reference = _reference(targets, "Drive")
        assert drive_reference.targetId == "field-id"
        assert drive_reference.targetType == FLOAT_FIELD
        assert fake.get_slot_calls == 4

    async def test_picks_the_proxy_of_the_given_drive(self) -> None:
        fake = FakeClient()
        first = core.ValueFieldDrive[primitives.Float]()
        await wiring.add_node(fake, "slot", first)  # type: ignore[arg-type]
        second = core.ValueFieldDrive[primitives.Float]()
        await wiring.add_node(fake, "slot", second)  # type: ignore[arg-type]
        assert second.id is not None
        proxy = await wiring.find_drive_proxy(fake, "slot", second.id)  # type: ignore[arg-type]
        node = proxy.members["Node"]
        assert isinstance(node, members.Reference) and node.targetId == second.id

    async def test_no_proxy(self) -> None:
        fake = FakeClient(proxy_after=1000)
        drive = core.ValueFieldDrive[primitives.Float]()
        await wiring.add_node(fake, "slot", drive)  # type: ignore[arg-type]
        with pytest.raises(RuntimeError, match="No Proxy"):
            await wiring.drive_field(fake, "slot", drive, "field-id")  # type: ignore[arg-type]
        assert fake.wired == []


class TestDriveFrom:
    async def test_wires_the_value_then_the_proxy(self) -> None:
        fake = FakeClient()
        source = core.ValueInput[primitives.Float](primitives.Float(1))
        await wiring.add_node(fake, "slot", source)  # type: ignore[arg-type]
        drive = await wiring.drive_from(fake, "slot", source, "field-id", primitives.Float)  # type: ignore[arg-type]
        assert drive.COMPONENT_TYPE.endswith("ValueFieldDrive<float>")
        assert drive.id is not None and fake.slot_of[drive.id] == "slot"
        (value_wiring, drive_wiring) = fake.wired
        assert value_wiring[0] == drive.id
        assert _reference(value_wiring[1], "Value").targetId == source.id
        proxy = fake.components[drive_wiring[0]]
        assert proxy.componentType == PROXY_TYPE
        assert _reference(drive_wiring[1], "Drive").targetId == "field-id"


GRABBABLE = "[FrooxEngine]FrooxEngine.IGrabbable"
GRABBABLE_TARGET = f"[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<{GRABBABLE}>"


class TestAddReferenceInput:
    async def test_adds_and_targets_with_the_reported_type(self) -> None:
        fake = FakeClient(reported={"Target": members.Reference(targetType=GRABBABLE)})
        node_id = await wiring.add_reference_input(fake, "slot", "joint-id", GRABBABLE)  # type: ignore[arg-type]
        node = fake.components[node_id]
        assert node.componentType == (
            "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes"
            f".RefObjectInput<{GRABBABLE}>"
        )
        assert fake.slot_of[node_id] == "slot"
        ((component_id, targets),) = fake.wired
        assert component_id == node_id
        target = _reference(targets, "Target")
        assert target.targetId == "joint-id"
        assert target.targetType == GRABBABLE

    async def test_takes_a_component(self) -> None:
        fake = FakeClient()
        source = core.ValueInput[primitives.Float](primitives.Float(1))
        await wiring.add_node(fake, "slot", source)  # type: ignore[arg-type]
        await wiring.add_reference_input(fake, "slot", source, GRABBABLE)  # type: ignore[arg-type]
        ((_, targets),) = fake.wired
        assert _reference(targets, "Target").targetId == source.id

    async def test_refused(self) -> None:
        fake = FakeClient(wire_success=False)
        with pytest.raises(RuntimeError, match="refused"):
            await wiring.add_reference_input(fake, "slot", "joint-id", GRABBABLE)  # type: ignore[arg-type]
