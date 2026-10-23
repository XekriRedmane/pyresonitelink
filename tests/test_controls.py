"""Unit tests for pyresonitelink.utils.controls, against a fake client."""

from typing import Any

import pytest

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.utils import controls
from pyresonitelink.utils import wiring
from tests.test_wiring import PROXY_TYPE, FakeClient

Z = primitives.Float3(0, 0, 1)


@pytest.fixture(autouse=True)
def no_delays(monkeypatch: pytest.MonkeyPatch) -> None:
    """Removes the pauses, which the fake doesn't need."""
    monkeypatch.setattr(wiring, "WIRE_DELAY", 0)
    monkeypatch.setattr(wiring, "_PROXY_POLL_INTERVAL", 0)


def _of_type(fake: FakeClient, suffix: str) -> list[workers.Component]:
    """Returns the added components whose type ends with suffix."""
    return [c for c in fake.components.values() if (c.componentType or "").endswith(suffix)]


def _value(component: workers.Component, name: str) -> Any:
    """Returns the value of one of a component's field members."""
    member = component.members[name]
    assert hasattr(member, "value"), f"{name} isn't a field"
    return getattr(member, "value")


class TestAddCrank:
    async def test_adds_a_free_joint_and_a_limited_knob(self) -> None:
        fake = FakeClient()
        grip = await controls.add_crank(
            fake, "crank", axis=Z, target_id="count", per_turn=10.0,  # type: ignore[arg-type]
            minimum=0.0, maximum=99.99,
        )
        (joint,) = _of_type(fake, "FrooxEngine.Joint")
        assert joint.id == grip.id and fake.slot_of[joint.id or ""] == "crank"
        assert _value(joint, "Axis") == Z
        assert _value(joint, "MaxSwing") == 0
        # MathX.LimitTwist leaves the twist free only at 180 or more.
        assert _value(joint, "MaxTwist") >= 180
        (knob,) = _of_type(fake, "KnobControl")
        assert fake.slot_of[knob.id or ""] == "crank"
        target = knob.members["Target"]
        assert isinstance(target, members.Reference) and target.targetId == "count"
        assert _value(knob, "RotationAxis") == Z
        assert _value(knob, "_lastAxis") == Z
        assert _value(knob, "Rate") == pytest.approx(10.0)
        assert _value(knob, "Min") == pytest.approx(0.0)
        assert _value(knob, "Max") == pytest.approx(99.99)

    async def test_no_limits_keeps_the_defaults(self) -> None:
        fake = FakeClient()
        await controls.add_crank(fake, "crank", axis=Z, target_id="count", per_turn=1.0)  # type: ignore[arg-type]
        (knob,) = _of_type(fake, "KnobControl")
        assert "Min" not in knob.members and "Max" not in knob.members


class TestTrackAngle:
    async def test_counts_degrees_in_the_axis_angle_sense(self) -> None:
        fake = FakeClient()
        knob = await controls.track_angle(fake, "crank", axis=Z, target_id="angle")  # type: ignore[arg-type]
        (stored,) = _of_type(fake, "KnobControl")
        assert stored.id == knob.id
        # KnobControl adds -angle * Rate / 360.
        assert _value(stored, "Rate") == pytest.approx(-360.0)
        assert "Min" not in stored.members and "Max" not in stored.members
        target = stored.members["Target"]
        assert isinstance(target, members.Reference) and target.targetId == "angle"


class TestDriveGrabbed:
    async def test_drives_the_field_from_the_grab_state(self) -> None:
        fake = FakeClient()
        await controls.drive_grabbed(fake, "graph", "joint-id", "held")  # type: ignore[arg-type]
        (reference,) = _of_type(fake, f"RefObjectInput<{controls.GRABBABLE_TYPE}>")
        (grabbed,) = _of_type(fake, "IsGrabbableGrabbed")
        (drive,) = _of_type(fake, "ValueFieldDrive<bool>")
        (proxy,) = [c for c in fake.components.values() if c.componentType == PROXY_TYPE]
        wired = {component_id: targets for component_id, targets in fake.wired}
        assert wired[reference.id or ""]["Target"].targetId == "joint-id"
        assert wired[grabbed.id or ""]["Grabbable"].targetId == reference.id
        assert wired[drive.id or ""]["Value"].targetId == grabbed.id
        assert wired[proxy.id or ""]["Drive"].targetId == "held"
        assert {fake.slot_of[c.id or ""] for c in (reference, grabbed, drive)} == {"graph"}
