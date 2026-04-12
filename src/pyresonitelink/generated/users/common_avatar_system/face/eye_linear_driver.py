"""Generated component: EyeLinearDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.clamp_mode import ClampMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.eye_manager import EyeManager
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeLinearDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The EyeLinearDriver component is used to drive the shapekeys on eyes. It can also do eye look direction shapekeys if each eye is provided a projection plane slot.

This component can also be used to drive position offsets for eyes. This can be used to make 2D texture based eyes or anime eyes work without needing to use rotation. Please see How Projection Plane Works.

    Category: Users/Common Avatar System/Face

    Can be used to drive 2D eyeballs, the shapekeys for eyeballs, and look
    shapekeys using Ray plane intersection calculations within the
    component.

    **How Projection Plane Works**: When any eye on this component is provided a slot for ``ProjectionPlanePoint``, the projection calculations are allowed to work. 

For each eye the Calculation is able to be done on, the component shoots a simulated ray from the ``ProjectionPlanePoint`` to the eye's look target through an offseted plane. The resulting hit point is modified by some of the component's values (See above fields) and then clamped between -1 to 1. Or within a circle if using ClampMode circle. The value is then modifed by some more component fields, before the result drives ``PositionOffset``. Which can drive a texture offset or the position of an eyeball slot for 2D eyes.

    **Eye Look Calculation**: Eye look calculations for an eye don't work if ``ProjectionPlanePoint`` is null for that eye.

The clamped hit point from The Projection System is first multiplied with ``LookMultiply`` and raised to ``LookPower`` before it is used for calculating ``LookLeft``, ``LookRight``, ``LookUp``, and ``LookDown``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.EyeLinearDriver"

    def __init__(self, eye_manager: str | EyeManager | None = None, projection_plane_size: primitives.Float2 | None = None, projection_point_distance: primitives.Float | None = None, position_offset_center: primitives.Float2 | None = None, position_offset_range: primitives.Float2 | None = None, minimum_target_point_distance: primitives.Float | None = None, position_clamp_mode: ClampMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            eye_manager: Initial value for EyeManager.
            projection_plane_size: Initial value for ProjectionPlaneSize.
            projection_point_distance: Initial value for ProjectionPointDistance.
            position_offset_center: Initial value for PositionOffsetCenter.
            position_offset_range: Initial value for PositionOffsetRange.
            minimum_target_point_distance: Initial value for MinimumTargetPointDistance.
            position_clamp_mode: Initial value for PositionClampMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if eye_manager is not None:
            self.eye_manager = eye_manager
        if projection_plane_size is not None:
            self.projection_plane_size = projection_plane_size
        if projection_point_distance is not None:
            self.projection_point_distance = projection_point_distance
        if position_offset_center is not None:
            self.position_offset_center = position_offset_center
        if position_offset_range is not None:
            self.position_offset_range = position_offset_range
        if minimum_target_point_distance is not None:
            self.minimum_target_point_distance = minimum_target_point_distance
        if position_clamp_mode is not None:
            self.position_clamp_mode = position_clamp_mode

    @property
    def eye_manager(self) -> str | None:
        """The eye manager to get the eye data from."""
        member = self.get_member("EyeManager")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eye_manager.setter
    def eye_manager(self, target: str | EyeManager | None) -> None:
        """Set the EyeManager reference by target ID or EyeManager instance."""
        target_id: str | None = target.id if isinstance(target, EyeManager) else target  # type: ignore[assignment]
        member = self.get_member("EyeManager")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EyeManager",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.EyeManager'),
            )

    @property
    def projection_plane_size(self) -> primitives.Float2 | None:
        """The scaling of the inital hit point before it is clamped. See How Projection Plane Works."""
        member = self.get_member("ProjectionPlaneSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @projection_plane_size.setter
    def projection_plane_size(self, value: primitives.Float2) -> None:
        """Set the ProjectionPlaneSize field value."""
        member = self.get_member("ProjectionPlaneSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProjectionPlaneSize", fields.FieldFloat2(value=value)
            )

    @property
    def projection_point_distance(self) -> primitives.Float | None:
        """The distance from the offseted plane to ``ProjectionPlanePoint`` on all the eyes in ``Eyes`` list. See How Projection Plane Works."""
        member = self.get_member("ProjectionPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @projection_point_distance.setter
    def projection_point_distance(self, value: primitives.Float) -> None:
        """Set the ProjectionPointDistance field value."""
        member = self.get_member("ProjectionPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProjectionPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def position_offset_center(self) -> primitives.Float2 | None:
        """How much to add to the inital plane projection hit point after clamping. See How Projection Plane Works."""
        member = self.get_member("PositionOffsetCenter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_offset_center.setter
    def position_offset_center(self, value: primitives.Float2) -> None:
        """Set the PositionOffsetCenter field value."""
        member = self.get_member("PositionOffsetCenter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOffsetCenter", fields.FieldFloat2(value=value)
            )

    @property
    def position_offset_range(self) -> primitives.Float2 | None:
        """how much to scale the inital plane projection hit after clamping. See How Projection Plane Works."""
        member = self.get_member("PositionOffsetRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_offset_range.setter
    def position_offset_range(self, value: primitives.Float2) -> None:
        """Set the PositionOffsetRange field value."""
        member = self.get_member("PositionOffsetRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOffsetRange", fields.FieldFloat2(value=value)
            )

    @property
    def minimum_target_point_distance(self) -> primitives.Float | None:
        """The minimum distance for every eye in ``Eyes`` a look target point from that eye's projection plane slot can be. Points closer than that are set to be further than this value during calculation. See How Projection Plane Works."""
        member = self.get_member("MinimumTargetPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_target_point_distance.setter
    def minimum_target_point_distance(self, value: primitives.Float) -> None:
        """Set the MinimumTargetPointDistance field value."""
        member = self.get_member("MinimumTargetPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumTargetPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def position_clamp_mode(self) -> ClampMode | None:
        """How to clamp projection plane projection range when doing projection calculations. See How Projection Plane Works."""
        member = self.get_member("PositionClampMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ClampMode(member.value)
        return None

    @position_clamp_mode.setter
    def position_clamp_mode(self, value: ClampMode | str) -> None:
        """Set PositionClampMode. How to clamp projection plane projection range when doing projection calculations. See How Projection Plane Works."""
        member = self.get_member("PositionClampMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositionClampMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def left_close_subtract_limits(self) -> members.SyncList | None:
        """The component finds the EyeCloseLimit with the maximum influence in this list. If the EyeCloseLimit with the maximum influence in ``CombinedEyeCloseSubtractLimits`` is higher, then that is used instead. Then this subtracts the result from the Left Eye close amount (essentially prying the eye open) to get the eye closed value to use with every left eye."""
        member = self.get_member("LeftCloseSubtractLimits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @left_close_subtract_limits.setter
    def left_close_subtract_limits(self, value: members.SyncList) -> None:
        """Set LeftCloseSubtractLimits. The component finds the EyeCloseLimit with the maximum influence in this list. If the EyeCloseLimit with the maximum influence in ``CombinedEyeCloseSubtractLimits`` is higher, then that is used instead. Then this subtracts the result from the Left Eye close amount (essentially prying the eye open) to get the eye closed value to use with every left eye."""
        self.set_member("LeftCloseSubtractLimits", value)

    @property
    def right_close_subtract_limits(self) -> members.SyncList | None:
        """The component finds the EyeCloseLimit with the maximum influence in this list. If the EyeCloseLimit with the maximum influence in ``CombinedEyeCloseSubtractLimits`` is higher, then that is used instead. Then this subtracts the result from the Left Eye close amount (essentially prying the eye open) to get the eye closed value to use with every right eye."""
        member = self.get_member("RightCloseSubtractLimits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @right_close_subtract_limits.setter
    def right_close_subtract_limits(self, value: members.SyncList) -> None:
        """Set RightCloseSubtractLimits. The component finds the EyeCloseLimit with the maximum influence in this list. If the EyeCloseLimit with the maximum influence in ``CombinedEyeCloseSubtractLimits`` is higher, then that is used instead. Then this subtracts the result from the Left Eye close amount (essentially prying the eye open) to get the eye closed value to use with every right eye."""
        self.set_member("RightCloseSubtractLimits", value)

    @property
    def combined_close_subtract_limits(self) -> members.SyncList | None:
        """Used with ``LeftCloseSubtractLimits`` and ``RightCloseSubtractLimits`` calculations."""
        member = self.get_member("CombinedCloseSubtractLimits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @combined_close_subtract_limits.setter
    def combined_close_subtract_limits(self, value: members.SyncList) -> None:
        """Set CombinedCloseSubtractLimits. Used with ``LeftCloseSubtractLimits`` and ``RightCloseSubtractLimits`` calculations."""
        self.set_member("CombinedCloseSubtractLimits", value)

    @property
    def eyes(self) -> members.SyncList | None:
        """The list of eyes this component is doing calculations and shapekey driving for."""
        member = self.get_member("Eyes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @eyes.setter
    def eyes(self, value: members.SyncList) -> None:
        """Set Eyes. The list of eyes this component is doing calculations and shapekey driving for."""
        self.set_member("Eyes", value)

