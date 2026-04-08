"""Generated component: AvatarPoseSmoothLerp."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_pose_filter import IAvatarPoseFilter
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarPoseSmoothLerp(GeneratedComponent, IAvatarPoseFilter, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseSmoothLerp.

    Category: Users/Common Avatar System/Pose Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseSmoothLerp"

    def __init__(self, position_smooth_speed: np.float32 | None = None, rotation_smooth_speed: np.float32 | None = None, smooth_simulated_poses: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_smooth_speed: Initial value for PositionSmoothSpeed.
            rotation_smooth_speed: Initial value for RotationSmoothSpeed.
            smooth_simulated_poses: Initial value for SmoothSimulatedPoses.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_smooth_speed is not None:
            self.position_smooth_speed = position_smooth_speed
        if rotation_smooth_speed is not None:
            self.rotation_smooth_speed = rotation_smooth_speed
        if smooth_simulated_poses is not None:
            self.smooth_simulated_poses = smooth_simulated_poses

    @property
    def position_smooth_speed(self) -> np.float32 | None:
        """The PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_smooth_speed.setter
    def position_smooth_speed(self, value: np.float32) -> None:
        """Set the PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def rotation_smooth_speed(self) -> np.float32 | None:
        """The RotationSmoothSpeed field value."""
        member = self.get_member("RotationSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_smooth_speed.setter
    def rotation_smooth_speed(self, value: np.float32) -> None:
        """Set the RotationSmoothSpeed field value."""
        member = self.get_member("RotationSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def smooth_simulated_poses(self) -> bool | None:
        """The SmoothSimulatedPoses field value."""
        member = self.get_member("SmoothSimulatedPoses")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_simulated_poses.setter
    def smooth_simulated_poses(self, value: bool) -> None:
        """Set the SmoothSimulatedPoses field value."""
        member = self.get_member("SmoothSimulatedPoses")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothSimulatedPoses", fields.FieldBool(value=value)
            )

