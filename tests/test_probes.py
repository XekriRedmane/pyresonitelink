"""Unit tests for pyresonitelink.utils.probes, against a fake client."""

from typing import Any

import pytest

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import responses
from pyresonitelink.data import workers
from pyresonitelink.utils import probes
from pyresonitelink.utils import wiring
from tests.test_wiring import PROXY_TYPE, FakeClient


# The values the fake's drives write.
DRIVEN_POSITION = primitives.Float3(1, 2, 3)
DRIVEN_ROTATION = primitives.FloatQ(0, 1, 0, 0)


class ProbeClient(FakeClient):
    """Adds slots, gives each ValueField a Value member, and imitates field drives.

    When a Proxy's Drive is set to a field, the fake writes DRIVEN_POSITION
    or DRIVEN_ROTATION to the field, as the drive would in the next engine
    update, unless drives is False.

    Attributes:
        added_slots (list[dict[str, Any]]): The arguments of each add_slot
            call.
        removed (list[str]): The IDs of the removed slots.
    """

    def __init__(self, drives: bool = True) -> None:
        super().__init__()
        self.drives = drives
        self.added_slots: list[dict[str, Any]] = []
        self.removed: list[str] = []

    async def update_references(
        self, componentId: str, references: Any, debug: bool = False,
    ) -> responses.Response:
        """Records the references, and writes a driven value to a field that a Proxy drives."""
        response = await super().update_references(componentId, references, debug)
        drive = references.get("Drive")
        if self.drives and drive is not None:
            for component in self.components.values():
                value = component.members.get("Value")
                if value is not None and value.id == drive.targetId:
                    if isinstance(value, fields.FieldFloat3):
                        component.members["Value"] = fields.FieldFloat3(id=value.id, value=DRIVEN_POSITION)
                    else:
                        component.members["Value"] = fields.FieldFloatQ(id=value.id, value=DRIVEN_ROTATION)
        return response

    async def add_slot(self, **kwargs: Any) -> workers.Slot:
        """Records the arguments and returns a slot with a new ID."""
        self.added_slots.append(kwargs)
        return workers.Slot(id=f"slot-{len(self.added_slots)}")

    async def remove_slot(self, slot: str | workers.Slot) -> responses.Response:
        """Records the removal."""
        self.removed.append(slot if isinstance(slot, str) else slot.id or "")
        return responses.Response(success=True)

    async def add_component(
        self, containerSlotId: str, data: workers.Component, debug: bool = False,
    ) -> responses.NewEntityId:
        """Stores the component, with a Value member for a ValueField."""
        added = await super().add_component(containerSlotId, data, debug)
        component = self.components[added.entityId or ""]
        if "Value" not in component.members:
            if "ValueField<float3>" in (data.componentType or ""):
                component.members["Value"] = fields.FieldFloat3(id=f"{component.id}-value")
            elif "ValueField<floatQ>" in (data.componentType or ""):
                component.members["Value"] = fields.FieldFloatQ(id=f"{component.id}-value")
        return added


@pytest.fixture(autouse=True)
def no_delays(monkeypatch: pytest.MonkeyPatch) -> None:
    """Removes the pauses, which the fake doesn't need."""
    monkeypatch.setattr(wiring, "WIRE_DELAY", 0)
    monkeypatch.setattr(wiring, "_PROXY_POLL_INTERVAL", 0)
    monkeypatch.setattr(probes, "_POLL_INTERVAL", 0)


def _of_type(fake: FakeClient, suffix: str) -> list[workers.Component]:
    """Returns the added components whose type ends with suffix."""
    return [c for c in fake.components.values() if (c.componentType or "").endswith(suffix)]


class TestViewProbe:
    async def test_drives_each_field_from_its_node(self) -> None:
        fake = ProbeClient()
        probe = await probes.ViewProbe.create(fake)  # type: ignore[arg-type]
        assert fake.added_slots == [{"parent": workers.Slot.ROOT_SLOT_ID, "name": "View Probe"}]
        wired = {component_id: targets for component_id, targets in fake.wired}
        drives = {}
        for proxy in [c for c in fake.components.values() if c.componentType == PROXY_TYPE]:
            node = proxy.members["Node"]
            drives[getattr(node, "targetId")] = wired[proxy.id or ""]["Drive"].targetId
        for node_suffix, field in (("ViewPosition", probe.position), ("ViewRotation", probe.rotation)):
            (node,) = _of_type(fake, node_suffix)
            (drive_id,) = [i for i, t in wired.items() if "Value" in t and t["Value"].targetId == node.id]
            assert drives[drive_id] == field.get_member("Value").id  # type: ignore[union-attr]
        assert {fake.slot_of[c] for c in fake.components} == {probe.slot.id}

    async def test_reads_the_driven_fields(self) -> None:
        fake = ProbeClient()
        probe = await probes.ViewProbe.create(fake, "parent", name="Probe")  # type: ignore[arg-type]
        assert fake.added_slots == [{"parent": "parent", "name": "Probe"}]
        view = await probe.read(fake)  # type: ignore[arg-type]
        assert view.position == DRIVEN_POSITION
        assert view.rotation == DRIVEN_ROTATION
        assert view.scale == primitives.Float3(1, 1, 1)
        await probe.remove(fake)  # type: ignore[arg-type]
        assert fake.removed == [probe.slot.id]

    async def test_waits_for_the_drives(self) -> None:
        fake = ProbeClient(drives=False)
        with pytest.raises(TimeoutError, match="wasn't driven"):
            await probes.ViewProbe.create(fake, timeout=0.05)  # type: ignore[arg-type]
        assert fake.removed == ["slot-1"]
