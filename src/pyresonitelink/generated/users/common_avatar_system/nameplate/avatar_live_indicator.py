"""Generated component: AvatarLiveIndicator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarLiveIndicator(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarLiveIndicator.

    Category: Users/Common Avatar System/Nameplate
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarLiveIndicator"

    def __init__(self, is_live: bool | None = None, active_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_live: Initial value for IsLive.
            active_user: Initial value for _activeUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_live is not None:
            self.is_live = is_live
        if active_user is not None:
            self.active_user = active_user

    @property
    def is_live(self) -> bool | None:
        """The IsLive field value."""
        member = self.get_member("IsLive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_live.setter
    def is_live(self, value: bool) -> None:
        """Set the IsLive field value."""
        member = self.get_member("IsLive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLive", fields.FieldBool(value=value)
            )

    @property
    def active_user(self) -> str | None:
        """Target ID of the _activeUser reference (targets User)."""
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

