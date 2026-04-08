"""Generated component: UserLoginManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserLoginManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UserLoginManager.

    Category: Cloud
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserLoginManager"

    def __init__(self, is_logged_in: primitives.Bool | None = None, is_logging_out: primitives.Bool | None = None, current_username: primitives.String | None = None, current_user_id: primitives.String | None = None, current_account_type: primitives.String | None = None, current_account_color_override: primitives.ColorX | None = None, current_profile_icon: str | None = None, login_logout_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_logged_in: Initial value for IsLoggedIn.
            is_logging_out: Initial value for IsLoggingOut.
            current_username: Initial value for CurrentUsername.
            current_user_id: Initial value for CurrentUserId.
            current_account_type: Initial value for CurrentAccountType.
            current_account_color_override: Initial value for CurrentAccountColorOverride.
            current_profile_icon: Initial value for CurrentProfileIcon.
            login_logout_button: Initial value for LoginLogoutButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_logged_in is not None:
            self.is_logged_in = is_logged_in
        if is_logging_out is not None:
            self.is_logging_out = is_logging_out
        if current_username is not None:
            self.current_username = current_username
        if current_user_id is not None:
            self.current_user_id = current_user_id
        if current_account_type is not None:
            self.current_account_type = current_account_type
        if current_account_color_override is not None:
            self.current_account_color_override = current_account_color_override
        if current_profile_icon is not None:
            self.current_profile_icon = current_profile_icon
        if login_logout_button is not None:
            self.login_logout_button = login_logout_button

    @property
    def is_logged_in(self) -> primitives.Bool | None:
        """The IsLoggedIn field value."""
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
    def is_logging_out(self) -> primitives.Bool | None:
        """The IsLoggingOut field value."""
        member = self.get_member("IsLoggingOut")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_logging_out.setter
    def is_logging_out(self, value: primitives.Bool) -> None:
        """Set the IsLoggingOut field value."""
        member = self.get_member("IsLoggingOut")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLoggingOut", fields.FieldBool(value=value)
            )

    @property
    def current_username(self) -> primitives.String | None:
        """The CurrentUsername field value."""
        member = self.get_member("CurrentUsername")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_username.setter
    def current_username(self, value: primitives.String) -> None:
        """Set the CurrentUsername field value."""
        member = self.get_member("CurrentUsername")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentUsername", fields.FieldString(value=value)
            )

    @property
    def current_user_id(self) -> primitives.String | None:
        """The CurrentUserId field value."""
        member = self.get_member("CurrentUserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_user_id.setter
    def current_user_id(self, value: primitives.String) -> None:
        """Set the CurrentUserId field value."""
        member = self.get_member("CurrentUserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentUserId", fields.FieldString(value=value)
            )

    @property
    def current_account_type(self) -> primitives.String | None:
        """The CurrentAccountType field value."""
        member = self.get_member("CurrentAccountType")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_account_type.setter
    def current_account_type(self, value: primitives.String) -> None:
        """Set the CurrentAccountType field value."""
        member = self.get_member("CurrentAccountType")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentAccountType", fields.FieldString(value=value)
            )

    @property
    def current_account_color_override(self) -> primitives.ColorX | None:
        """The CurrentAccountColorOverride field value."""
        member = self.get_member("CurrentAccountColorOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_account_color_override.setter
    def current_account_color_override(self, value: primitives.ColorX) -> None:
        """Set the CurrentAccountColorOverride field value."""
        member = self.get_member("CurrentAccountColorOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentAccountColorOverride", fields.FieldNullableColorX(value=value)
            )

    @property
    def current_profile_icon(self) -> str | None:
        """The CurrentProfileIcon field value."""
        member = self.get_member("CurrentProfileIcon")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_profile_icon.setter
    def current_profile_icon(self, value: str) -> None:
        """Set the CurrentProfileIcon field value."""
        member = self.get_member("CurrentProfileIcon")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentProfileIcon", fields.FieldUri(value=value)
            )

    @property
    def login_logout_button(self) -> str | None:
        """Target ID of the LoginLogoutButton reference (targets Button)."""
        member = self.get_member("LoginLogoutButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @login_logout_button.setter
    def login_logout_button(self, target: str | Button | None) -> None:
        """Set the LoginLogoutButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("LoginLogoutButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoginLogoutButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    async def do_login_logout(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the DoLoginLogout sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "DoLoginLogout", {"button": button, "eventData": event_data}, debug,
        )

