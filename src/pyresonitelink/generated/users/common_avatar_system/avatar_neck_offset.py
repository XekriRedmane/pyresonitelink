"""Generated component: AvatarNeckOffset."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.ineck_offset_source import INeckOffsetSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarNeckOffset(GeneratedComponent, IAvatarObjectComponent, INeckOffsetSource, IWorldEventReceiver):
    """Avatar Neck Offset is a component that allows for dynamically lengthening and shortening the neck of an avatar.

    Category: Users/Common Avatar System

    **Behavior**: The effect of this component when used updates instantly.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarNeckOffset"

    def __init__(self, priority: primitives.Int | None = None, offset: primitives.Float3 | None = None, active_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            priority: Initial value for Priority.
            offset: Initial value for Offset.
            active_user: Initial value for _activeUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if priority is not None:
            self.priority = priority
        if offset is not None:
            self.offset = offset
        if active_user is not None:
            self.active_user = active_user

    @property
    def priority(self) -> primitives.Int | None:
        """How much priority this component takes over other components that constrain or change Avatar Pose Nodes"""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """How much to offset the user's neck from it's original position in local space."""
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
    def active_user(self) -> str | None:
        """Internal. Automatically updates to active user of this component that's being affected by it."""
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_user.setter
    def active_user(self, target: str | User | None) -> None:
        """Set the _activeUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

