"""Generated component: UserLoginStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserLoginStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UserLoginStatus component gets the current login status of the local user.

    Category: Cloud/Indicators

    Attach to a Component to instantly get info on the local user's login
    status.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserLoginStatus"

    def __init__(self, is_logged_in: primitives.Bool | None = None, logged_user_id: primitives.String | None = None, logged_username: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
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
    def is_logged_in(self) -> primitives.Bool | None:
        """Whether the local user is logged in."""
        member = self.get_member("IsLoggedIn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_logged_in.setter
    def is_logged_in(self, value: primitives.Bool) -> None:
        """Set the IsLoggedIn field value."""
        member = self.get_member("IsLoggedIn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLoggedIn", fields.FieldBool(value=value)
            )

    @property
    def logged_user_id(self) -> primitives.String | None:
        """The userID of the local user if they are logged in."""
        member = self.get_member("LoggedUserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @logged_user_id.setter
    def logged_user_id(self, value: primitives.String) -> None:
        """Set the LoggedUserId field value."""
        member = self.get_member("LoggedUserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoggedUserId", fields.FieldString(value=value)
            )

    @property
    def logged_username(self) -> primitives.String | None:
        """The username of the local user if they are logged in."""
        member = self.get_member("LoggedUsername")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @logged_username.setter
    def logged_username(self, value: primitives.String) -> None:
        """Set the LoggedUsername field value."""
        member = self.get_member("LoggedUsername")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoggedUsername", fields.FieldString(value=value)
            )

