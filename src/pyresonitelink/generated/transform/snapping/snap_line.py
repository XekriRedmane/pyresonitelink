"""Generated component: SnapLine."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapLine(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SnapLine.

    Category: Transform/Snapping
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapLine"

    def __init__(self, point0: primitives.Float3 | None = None, point1: primitives.Float3 | None = None, anchor0: str | Slot | None = None, anchor1: str | Slot | None = None, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            point0: Initial value for Point0.
            point1: Initial value for Point1.
            anchor0: Initial value for Anchor0.
            anchor1: Initial value for Anchor1.
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if point0 is not None:
            self.point0 = point0
        if point1 is not None:
            self.point1 = point1
        if anchor0 is not None:
            self.anchor0 = anchor0
        if anchor1 is not None:
            self.anchor1 = anchor1
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def point0(self) -> primitives.Float3 | None:
        """The Point0 field value."""
        member = self.get_member("Point0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point0.setter
    def point0(self, value: primitives.Float3) -> None:
        """Set the Point0 field value."""
        member = self.get_member("Point0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point0", fields.FieldFloat3(value=value)
            )

    @property
    def point1(self) -> primitives.Float3 | None:
        """The Point1 field value."""
        member = self.get_member("Point1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point1.setter
    def point1(self, value: primitives.Float3) -> None:
        """Set the Point1 field value."""
        member = self.get_member("Point1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Point1", fields.FieldFloat3(value=value)
            )

    @property
    def anchor0(self) -> str | None:
        """Target ID of the Anchor0 reference (targets Slot)."""
        member = self.get_member("Anchor0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor0.setter
    def anchor0(self, target: str | Slot | None) -> None:
        """Set the Anchor0 reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Anchor0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def anchor1(self) -> str | None:
        """Target ID of the Anchor1 reference (targets Slot)."""
        member = self.get_member("Anchor1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor1.setter
    def anchor1(self, target: str | Slot | None) -> None:
        """Set the Anchor1 reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Anchor1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def snap_parent(self) -> str | None:
        """Target ID of the SnapParent reference (targets Slot)."""
        member = self.get_member("SnapParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @snap_parent.setter
    def snap_parent(self, target: str | Slot | None) -> None:
        """Set the SnapParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("SnapParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SnapParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

