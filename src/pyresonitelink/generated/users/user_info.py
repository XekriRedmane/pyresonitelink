"""Generated component: UserInfo."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserInfo.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInfo"

    @property
    def controllers(self) -> members.SyncList | None:
        """The Controllers member."""
        member = self.get_member("Controllers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @controllers.setter
    def controllers(self, value: members.SyncList) -> None:
        """Set the Controllers member."""
        self.set_member("Controllers", value)

    @property
    def hands(self) -> members.SyncList | None:
        """The Hands member."""
        member = self.get_member("Hands")
        if isinstance(member, members.SyncList):
            return member
        return None

    @hands.setter
    def hands(self, value: members.SyncList) -> None:
        """Set the Hands member."""
        self.set_member("Hands", value)

