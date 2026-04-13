"""Generated component: UserOnlineStatusSync."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.online_status import OnlineStatus
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserOnlineStatusSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserOnlineStatusSync component only works in userspace. It provides the online status that your account currently has.

    Category: Cloud/Indicators

    Attach to a slot that will be in userspace (like a facet) and bring it
    into userspace in order for it to begin working.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserOnlineStatusSync"

    def __init__(self, online_status: OnlineStatus | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            online_status: Initial value for OnlineStatus.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if online_status is not None:
            self.online_status = online_status

    @property
    def online_status(self) -> OnlineStatus | None:
        """The online status of the local user."""
        member = self.get_member("OnlineStatus")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OnlineStatus(member.value)
        return None

    @online_status.setter
    def online_status(self, value: OnlineStatus | str) -> None:
        """Set OnlineStatus. The online status of the local user."""
        member = self.get_member("OnlineStatus")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnlineStatus",
                members.FieldEnum(value=str(value)),
            )

