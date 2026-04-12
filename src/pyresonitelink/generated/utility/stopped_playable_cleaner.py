"""Generated component: StoppedPlayableCleaner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StoppedPlayableCleaner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Stopped playable cleaner is used on play one shots in order to delete or clean them once they have finished playing.

    Category: Utility

    **Behavior**: This component can stop working if the user is AFK or the slot is disabled, and can cause issues in items like boopers and overload the sound buffer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StoppedPlayableCleaner"

    def __init__(self, playable: str | IPlayable | None = None, grace_period: primitives.Float | None = None, checking_user: str | User | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playable: Initial value for Playable.
            grace_period: Initial value for GracePeriod.
            checking_user: Initial value for CheckingUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playable is not None:
            self.playable = playable
        if grace_period is not None:
            self.grace_period = grace_period
        if checking_user is not None:
            self.checking_user = checking_user

    @property
    def playable(self) -> str | None:
        """the audio player that is playing audio"""
        member = self.get_member("Playable")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playable.setter
    def playable(self, target: str | IPlayable | None) -> None:
        """Set the Playable reference by target ID or IPlayable instance."""
        target_id: str | None = target.id if isinstance(target, IPlayable) else target  # type: ignore[assignment]
        member = self.get_member("Playable")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Playable",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IPlayable'),
            )

    @property
    def grace_period(self) -> primitives.Float | None:
        """How long to wait before deleting the component after it has finished playing."""
        member = self.get_member("GracePeriod")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grace_period.setter
    def grace_period(self, value: primitives.Float) -> None:
        """Set the GracePeriod field value."""
        member = self.get_member("GracePeriod")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GracePeriod", fields.FieldFloat(value=value)
            )

    @property
    def checking_user(self) -> str | None:
        """The user that is monitoring the ``Playable`` on their machine to check when it has stopped playing"""
        member = self.get_member("CheckingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @checking_user.setter
    def checking_user(self, target: str | User | None) -> None:
        """Set the CheckingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("CheckingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheckingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

