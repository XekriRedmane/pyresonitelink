"""Generated component: DefaultUserScale."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DefaultUserScale(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """This component sets the default scale of the avatar it is attached to, which also affects the scale of the user wearing said avatar.

    Category: Users/Common Avatar System

    **Behavior**: The default scale determines what scale the avatar spawns at, as well as what scale it returns to when using the Reset Scale option in the context menu.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.DefaultUserScale"

    def __init__(self, set_on_equip: primitives.Bool | None = None, default_scale: primitives.Float | None = None, active_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            set_on_equip: Initial value for SetOnEquip.
            default_scale: Initial value for DefaultScale.
            active_user: Initial value for _activeUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if set_on_equip is not None:
            self.set_on_equip = set_on_equip
        if default_scale is not None:
            self.default_scale = default_scale
        if active_user is not None:
            self.active_user = active_user

    @property
    def set_on_equip(self) -> primitives.Bool | None:
        """TBD"""
        member = self.get_member("SetOnEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_on_equip.setter
    def set_on_equip(self, value: primitives.Bool) -> None:
        """Set the SetOnEquip field value."""
        member = self.get_member("SetOnEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetOnEquip", fields.FieldBool(value=value)
            )

    @property
    def default_scale(self) -> primitives.Float | None:
        """The default scale (normal value is 1)"""
        member = self.get_member("DefaultScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_scale.setter
    def default_scale(self, value: primitives.Float) -> None:
        """Set the DefaultScale field value."""
        member = self.get_member("DefaultScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultScale", fields.FieldFloat(value=value)
            )

    @property
    def active_user(self) -> str | None:
        """Internal"""
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_user.setter
    def active_user(self, target: str | User | None) -> None:
        """Set the _activeUser reference by target ID or User instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

