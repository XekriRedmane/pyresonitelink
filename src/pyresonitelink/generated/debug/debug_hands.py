"""Generated component: DebugHands."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugHands(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugHands component shows the vector axes and finger axes for a particular hand on a particular user.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugHands"

    def __init__(self, user: str | User | None = None, chirality: Chirality | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            chirality: Initial value for Chirality.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if chirality is not None:
            self.chirality = chirality

    @property
    def user(self) -> str | None:
        """The user to make the debug for."""
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
    def chirality(self) -> Chirality | None:
        """The hand to make the debug visual for."""
        member = self.get_member("Chirality")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @chirality.setter
    def chirality(self, value: Chirality | str) -> None:
        """Set Chirality. The hand to make the debug visual for."""
        member = self.get_member("Chirality")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Chirality",
                members.FieldEnum(value=str(value)),
            )

