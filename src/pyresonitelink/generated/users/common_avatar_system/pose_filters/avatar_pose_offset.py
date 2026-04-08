"""Generated component: AvatarPoseOffset."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_pose_filter import IAvatarPoseFilter
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarPoseOffset(GeneratedComponent, IAvatarPoseFilter, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseOffset.

    Category: Users/Common Avatar System/Pose Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseOffset"

    def __init__(self, position_offset: primitives.Float3 | None = None, rotation_offset: primitives.FloatQ | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_offset: Initial value for PositionOffset.
            rotation_offset: Initial value for RotationOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_offset is not None:
            self.position_offset = position_offset
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset

    @property
    def position_offset(self) -> primitives.Float3 | None:
        """The PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_offset.setter
    def position_offset(self, value: primitives.Float3) -> None:
        """Set the PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOffset", fields.FieldFloat3(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.FloatQ | None:
        """The RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_offset.setter
    def rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOffset", fields.FieldFloatQ(value=value)
            )

