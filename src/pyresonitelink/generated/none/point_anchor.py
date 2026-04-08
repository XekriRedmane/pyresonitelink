"""Generated component: PointAnchor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointAnchor(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PointAnchor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointAnchor"

    def __init__(self, owner_root: str | Slot | None = None, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            owner_root: Initial value for OwnerRoot.
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if owner_root is not None:
            self.owner_root = owner_root
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def owner_root(self) -> str | None:
        """Target ID of the OwnerRoot reference (targets Slot)."""
        member = self.get_member("OwnerRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @owner_root.setter
    def owner_root(self, target: str | Slot | None) -> None:
        """Set the OwnerRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OwnerRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OwnerRoot",
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

