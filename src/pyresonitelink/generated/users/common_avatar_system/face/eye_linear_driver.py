"""Generated component: EyeLinearDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.eye_manager import EyeManager
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeLinearDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.EyeLinearDriver.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.EyeLinearDriver"

    def __init__(self, eye_manager: str | EyeManager | None = None, projection_plane_size: primitives.Float2 | None = None, projection_point_distance: np.float32 | None = None, position_offset_center: primitives.Float2 | None = None, position_offset_range: primitives.Float2 | None = None, minimum_target_point_distance: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            eye_manager: Initial value for EyeManager.
            projection_plane_size: Initial value for ProjectionPlaneSize.
            projection_point_distance: Initial value for ProjectionPointDistance.
            position_offset_center: Initial value for PositionOffsetCenter.
            position_offset_range: Initial value for PositionOffsetRange.
            minimum_target_point_distance: Initial value for MinimumTargetPointDistance.
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

    @property
    def eye_manager(self) -> str | None:
        """Target ID of the EyeManager reference (targets EyeManager)."""
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
        """The ProjectionPlaneSize field value."""
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
    def projection_point_distance(self) -> np.float32 | None:
        """The ProjectionPointDistance field value."""
        member = self.get_member("ProjectionPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @projection_point_distance.setter
    def projection_point_distance(self, value: np.float32) -> None:
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
        """The PositionOffsetCenter field value."""
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
        """The PositionOffsetRange field value."""
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
    def minimum_target_point_distance(self) -> np.float32 | None:
        """The MinimumTargetPointDistance field value."""
        member = self.get_member("MinimumTargetPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_target_point_distance.setter
    def minimum_target_point_distance(self, value: np.float32) -> None:
        """Set the MinimumTargetPointDistance field value."""
        member = self.get_member("MinimumTargetPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumTargetPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def position_clamp_mode(self) -> members.FieldEnum | None:
        """The PositionClampMode member."""
        member = self.get_member("PositionClampMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @position_clamp_mode.setter
    def position_clamp_mode(self, value: members.FieldEnum) -> None:
        """Set the PositionClampMode member."""
        self.set_member("PositionClampMode", value)

    @property
    def left_close_subtract_limits(self) -> members.SyncList | None:
        """The LeftCloseSubtractLimits member."""
        member = self.get_member("LeftCloseSubtractLimits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @left_close_subtract_limits.setter
    def left_close_subtract_limits(self, value: members.SyncList) -> None:
        """Set the LeftCloseSubtractLimits member."""
        self.set_member("LeftCloseSubtractLimits", value)

    @property
    def right_close_subtract_limits(self) -> members.SyncList | None:
        """The RightCloseSubtractLimits member."""
        member = self.get_member("RightCloseSubtractLimits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @right_close_subtract_limits.setter
    def right_close_subtract_limits(self, value: members.SyncList) -> None:
        """Set the RightCloseSubtractLimits member."""
        self.set_member("RightCloseSubtractLimits", value)

    @property
    def combined_close_subtract_limits(self) -> members.SyncList | None:
        """The CombinedCloseSubtractLimits member."""
        member = self.get_member("CombinedCloseSubtractLimits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @combined_close_subtract_limits.setter
    def combined_close_subtract_limits(self, value: members.SyncList) -> None:
        """Set the CombinedCloseSubtractLimits member."""
        self.set_member("CombinedCloseSubtractLimits", value)

    @property
    def eyes(self) -> members.SyncList | None:
        """The Eyes member."""
        member = self.get_member("Eyes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @eyes.setter
    def eyes(self, value: members.SyncList) -> None:
        """Set the Eyes member."""
        self.set_member("Eyes", value)

