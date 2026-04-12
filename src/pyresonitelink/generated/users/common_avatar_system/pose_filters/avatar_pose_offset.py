"""Generated component: AvatarPoseOffset."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_pose_filter import IAvatarPoseFilter
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarPoseOffset(GeneratedComponent, IAvatarPoseFilter, IWorldEventReceiver):
    """The Avatar Pose Offset Component is used to offset a user's limb while they use a tool tip or sit in an anchor.

    Category: Users/Common Avatar System/Pose Filters

    this can be applied in a certain order relative to other constraints in
    AvatarAnchor or in use with a tooltip. Because of this, the Component
    can be used to either make a user's hand(s) or feet positioned as an
    offset to where they originally are tracked or to apply an offset after
    another Pose component has restricted movement. This component's
    rotation can be driven in combination with using a
    AvatarPoseBoxConstraint to freeze the user's body node. this is done by
    driving ``RotationOffset`` to counteract the rotation of the user's
    hand, effectively offsetting it back to zero and stopping movement.
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
        """How much position to offset a body node by after previous pose constraints have been applied."""
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
        """How much rotation to offset a body node by after previous pose constraints have been applied."""
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

