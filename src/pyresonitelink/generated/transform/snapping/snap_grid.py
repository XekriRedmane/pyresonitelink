"""Generated component: SnapGrid."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ipoint_snappable import IPointSnappable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SnapGrid(GeneratedComponent, IPointSnappable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SnapGrid.

    Category: Transform/Snapping
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SnapGrid"

    def __init__(self, bounds_size: primitives.Float3 | None = None, grid_size: primitives.Float3 | None = None, collider_size: str | IField[primitives.Float3] | None = None, snap_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bounds_size: Initial value for BoundsSize.
            grid_size: Initial value for GridSize.
            collider_size: Initial value for ColliderSize.
            snap_parent: Initial value for SnapParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bounds_size is not None:
            self.bounds_size = bounds_size
        if grid_size is not None:
            self.grid_size = grid_size
        if collider_size is not None:
            self.collider_size = collider_size
        if snap_parent is not None:
            self.snap_parent = snap_parent

    @property
    def bounds_size(self) -> primitives.Float3 | None:
        """The BoundsSize field value."""
        member = self.get_member("BoundsSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bounds_size.setter
    def bounds_size(self, value: primitives.Float3) -> None:
        """Set the BoundsSize field value."""
        member = self.get_member("BoundsSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoundsSize", fields.FieldFloat3(value=value)
            )

    @property
    def grid_size(self) -> primitives.Float3 | None:
        """The GridSize field value."""
        member = self.get_member("GridSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grid_size.setter
    def grid_size(self, value: primitives.Float3) -> None:
        """Set the GridSize field value."""
        member = self.get_member("GridSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GridSize", fields.FieldFloat3(value=value)
            )

    @property
    def collider_size(self) -> str | None:
        """Target ID of the ColliderSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("ColliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the ColliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ColliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
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

