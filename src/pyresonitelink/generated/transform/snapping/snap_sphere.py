"""Generated component: SnapSphere."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapSphere(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SnapSphere.

    Category: Transform/Snapping
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapSphere"

    def __init__(self, radius: primitives.Float | None = None, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            radius: Initial value for Radius.
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if radius is not None:
            self.radius = radius
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def radius(self) -> primitives.Float | None:
        """The Radius field value."""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
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

