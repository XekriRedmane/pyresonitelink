"""Generated component: UserInfo."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserInfo component handles keeping certain bits of data about a player spawned physically in the world. It's stored under the user root slot.

    Category: Users

    Used internally.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserInfo"

    @property
    def controllers(self) -> members.SyncList | None:
        """The slots of the controllers this user is using."""
        member = self.get_member("Controllers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @controllers.setter
    def controllers(self, value: members.SyncList) -> None:
        """Set Controllers. The slots of the controllers this user is using."""
        self.set_member("Controllers", value)

    @property
    def hands(self) -> members.SyncList | None:
        """The slots of the hands this user."""
        member = self.get_member("Hands")
        if isinstance(member, members.SyncList):
            return member
        return None

    @hands.setter
    def hands(self, value: members.SyncList) -> None:
        """Set Hands. The slots of the hands this user."""
        self.set_member("Hands", value)

