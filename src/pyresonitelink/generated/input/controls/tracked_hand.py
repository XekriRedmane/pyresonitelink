"""Generated component: TrackedHand."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrackedHand(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TrackedHand component controls the grabbing and updating of a hand including camera based hand tracking of a user.

    Category: Input/Controls
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackedHand"

    def __init__(self, user: str | User | None = None, hand_chirality: Chirality | str | None = None, grabber: str | Grabber | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            hand_chirality: Initial value for HandChirality.
            grabber: Initial value for _grabber.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if hand_chirality is not None:
            self.hand_chirality = hand_chirality
        if grabber is not None:
            self.grabber = grabber

    @property
    def user(self) -> str | None:
        """The user this tracked hand belongs to."""
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
    def hand_chirality(self) -> Chirality | None:
        """The hand side this tracked hand corresponds to."""
        member = self.get_member("HandChirality")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @hand_chirality.setter
    def hand_chirality(self, value: Chirality | str) -> None:
        """Set HandChirality. The hand side this tracked hand corresponds to."""
        member = self.get_member("HandChirality")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HandChirality",
                members.FieldEnum(value=str(value)),
            )

    @property
    def grabber(self) -> str | None:
        """The grabber component this hand is controlling."""
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

