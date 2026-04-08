"""Generated component: UserOnlineStatusSync."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserOnlineStatusSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserOnlineStatusSync.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserOnlineStatusSync"

    @property
    def online_status(self) -> members.FieldEnum | None:
        """The OnlineStatus member."""
        member = self.get_member("OnlineStatus")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @online_status.setter
    def online_status(self, value: members.FieldEnum) -> None:
        """Set the OnlineStatus member."""
        self.set_member("OnlineStatus", value)

