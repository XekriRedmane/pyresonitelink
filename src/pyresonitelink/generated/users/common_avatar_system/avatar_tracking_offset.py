"""Generated component: AvatarTrackingOffset."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarTrackingOffset(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """AvatarTrackingOffset can be used to shift the position of your trackers (including headset and hands) by a certain amount for an avatar.
To work, the component needs to be in the avatar's hierarchy.

This component effectively works like a "Playspace Mover".

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarTrackingOffset"

    def __init__(self, offset: primitives.Float3 | None = None, user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            user: Initial value for _user.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset
        if user is not None:
            self.user = user

    @property
    def offset(self) -> primitives.Float3 | None:
        """The amount that your tracking position should be offset when in the avatar"""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def user(self) -> str | None:
        """The user to which the offset is applied. This is set automatically when equipping an avatar with this component"""
        member = self.get_member("_user")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | User | None) -> None:
        """Set the _user reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_user")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_user",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

