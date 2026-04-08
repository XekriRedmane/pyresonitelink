"""Generated component: AvatarObjectScale."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarObjectScale(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectScale.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectScale"

    def __init__(self, user_space_scale: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_space_scale: Initial value for UserSpaceScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_space_scale is not None:
            self.user_space_scale = user_space_scale

    @property
    def user_space_scale(self) -> primitives.Float3 | None:
        """The UserSpaceScale field value."""
        member = self.get_member("UserSpaceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_space_scale.setter
    def user_space_scale(self, value: primitives.Float3) -> None:
        """Set the UserSpaceScale field value."""
        member = self.get_member("UserSpaceScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserSpaceScale", fields.FieldFloat3(value=value)
            )

