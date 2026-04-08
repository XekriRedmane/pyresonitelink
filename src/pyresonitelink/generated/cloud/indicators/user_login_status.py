"""Generated component: UserLoginStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserLoginStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserLoginStatus.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserLoginStatus"

    def __init__(self, is_logged_in: bool | None = None, logged_user_id: str | None = None, logged_username: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_logged_in: Initial value for IsLoggedIn.
            logged_user_id: Initial value for LoggedUserId.
            logged_username: Initial value for LoggedUsername.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_logged_in is not None:
            self.is_logged_in = is_logged_in
        if logged_user_id is not None:
            self.logged_user_id = logged_user_id
        if logged_username is not None:
            self.logged_username = logged_username

    @property
    def is_logged_in(self) -> bool | None:
        """The IsLoggedIn field value."""
        member = self.get_member("IsLoggedIn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_logged_in.setter
    def is_logged_in(self, value: bool) -> None:
        """Set the IsLoggedIn field value."""
        member = self.get_member("IsLoggedIn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLoggedIn", fields.FieldBool(value=value)
            )

    @property
    def logged_user_id(self) -> str | None:
        """The LoggedUserId field value."""
        member = self.get_member("LoggedUserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @logged_user_id.setter
    def logged_user_id(self, value: str) -> None:
        """Set the LoggedUserId field value."""
        member = self.get_member("LoggedUserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoggedUserId", fields.FieldString(value=value)
            )

    @property
    def logged_username(self) -> str | None:
        """The LoggedUsername field value."""
        member = self.get_member("LoggedUsername")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @logged_username.setter
    def logged_username(self, value: str) -> None:
        """Set the LoggedUsername field value."""
        member = self.get_member("LoggedUsername")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoggedUsername", fields.FieldString(value=value)
            )

