"""Generated component: BezierCurve."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.sync_curve import SyncCurve
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BezierCurve(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BezierCurve.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BezierCurve"

    def __init__(self, coordinate_space: str | Slot | None = None, assign_curve_data: str | SyncCurve[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            coordinate_space: Initial value for CoordinateSpace.
            assign_curve_data: Initial value for AssignCurveData.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if coordinate_space is not None:
            self.coordinate_space = coordinate_space
        if assign_curve_data is not None:
            self.assign_curve_data = assign_curve_data

    @property
    def points(self) -> members.SyncList | None:
        """The Points member."""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set the Points member."""
        self.set_member("Points", value)

    @property
    def coordinate_space(self) -> str | None:
        """Target ID of the CoordinateSpace reference (targets Slot)."""
        member = self.get_member("CoordinateSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @coordinate_space.setter
    def coordinate_space(self, target: str | Slot | None) -> None:
        """Set the CoordinateSpace reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("CoordinateSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CoordinateSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def assign_curve_data(self) -> str | None:
        """Target ID of the AssignCurveData reference (targets SyncCurve[primitives.Float3])."""
        member = self.get_member("AssignCurveData")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @assign_curve_data.setter
    def assign_curve_data(self, target: str | SyncCurve[primitives.Float3] | None) -> None:
        """Set the AssignCurveData reference by target ID or SyncCurve[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, SyncCurve) else target  # type: ignore[assignment]
        member = self.get_member("AssignCurveData")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AssignCurveData",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncCurve<float3>'),
            )

