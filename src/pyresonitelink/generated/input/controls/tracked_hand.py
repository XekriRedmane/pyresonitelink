"""Generated component: TrackedHand."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrackedHand(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TrackedHand.

    Category: Input/Controls
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackedHand"

    def __init__(self, user: str | User | None = None, grabber: str | Grabber | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            grabber: Initial value for _grabber.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if grabber is not None:
            self.grabber = grabber

    @property
    def user(self) -> str | None:
        """Target ID of the User reference (targets User)."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | User | None) -> None:
        """Set the User reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def hand_chirality(self) -> members.FieldEnum | None:
        """The HandChirality member."""
        member = self.get_member("HandChirality")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hand_chirality.setter
    def hand_chirality(self, value: members.FieldEnum) -> None:
        """Set the HandChirality member."""
        self.set_member("HandChirality", value)

    @property
    def grabber(self) -> str | None:
        """Target ID of the _grabber reference (targets Grabber)."""
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber.setter
    def grabber(self, target: str | Grabber | None) -> None:
        """Set the _grabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

