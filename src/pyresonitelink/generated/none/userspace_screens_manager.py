"""Generated component: UserspaceScreensManager."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user_login_status import UserLoginStatus
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceScreensManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserspaceScreensManager component is used in the user space and handles login status and unread notifications.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceScreensManager"

    def __init__(self, login_status: str | UserLoginStatus | None = None, unread_indicator: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            login_status: Initial value for _loginStatus.
            unread_indicator: Initial value for _unreadIndicator.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if login_status is not None:
            self.login_status = login_status
        if unread_indicator is not None:
            self.unread_indicator = unread_indicator

    @property
    def login_status(self) -> str | None:
        """The current login status of the user."""
        member = self.get_member("_loginStatus")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @login_status.setter
    def login_status(self, target: str | UserLoginStatus | None) -> None:
        """Set the _loginStatus reference by target ID or UserLoginStatus instance."""
        target_id: str | None = target.id if isinstance(target, UserLoginStatus) else target  # type: ignore[assignment]
        member = self.get_member("_loginStatus")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loginStatus",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserLoginStatus'),
            )

    @property
    def unread_indicator(self) -> str | None:
        """How many unread notifications the user has, which is driven to the specified text element."""
        member = self.get_member("_unreadIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unread_indicator.setter
    def unread_indicator(self, target: str | Text | None) -> None:
        """Set the _unreadIndicator reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_unreadIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unreadIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

