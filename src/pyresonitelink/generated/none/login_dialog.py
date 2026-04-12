"""Generated component: LoginDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.int_text_editor_parser import IntTextEditorParser
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LoginDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LoginDialog component is used in internal systems and may be replaced at any time. It is used to handle the logging in for users and the UI for such interactions.

    Not used directly by the user. Used in the dash.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LoginDialog"

    def __init__(self, register_only: primitives.Bool | None = None, interaction_enabled: primitives.Bool | None = None, swap_region: str | SlideSwapRegion | None = None, username: str | TextField | None = None, email: str | TextField | None = None, email_repeat: str | TextField | None = None, password: str | TextField | None = None, password_repeat: str | TextField | None = None, recovery_code: str | TextField | None = None, promo_code: str | TextField | None = None, birth_month: str | IntTextEditorParser | None = None, birth_day: str | IntTextEditorParser | None = None, birth_year: str | IntTextEditorParser | None = None, remember_login: str | Checkbox | None = None, policies: str | Checkbox | None = None, register_button: str | Button | None = None, login_email: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            register_only: Initial value for RegisterOnly.
            interaction_enabled: Initial value for _interactionEnabled.
            swap_region: Initial value for _swapRegion.
            username: Initial value for _username.
            email: Initial value for _email.
            email_repeat: Initial value for _emailRepeat.
            password: Initial value for _password.
            password_repeat: Initial value for _passwordRepeat.
            recovery_code: Initial value for _recoveryCode.
            promo_code: Initial value for _promoCode.
            birth_month: Initial value for _birthMonth.
            birth_day: Initial value for _birthDay.
            birth_year: Initial value for _birthYear.
            remember_login: Initial value for _rememberLogin.
            policies: Initial value for _policies.
            register_button: Initial value for _registerButton.
            login_email: Initial value for _loginEmail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if register_only is not None:
            self.register_only = register_only
        if interaction_enabled is not None:
            self.interaction_enabled = interaction_enabled
        if swap_region is not None:
            self.swap_region = swap_region
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if email_repeat is not None:
            self.email_repeat = email_repeat
        if password is not None:
            self.password = password
        if password_repeat is not None:
            self.password_repeat = password_repeat
        if recovery_code is not None:
            self.recovery_code = recovery_code
        if promo_code is not None:
            self.promo_code = promo_code
        if birth_month is not None:
            self.birth_month = birth_month
        if birth_day is not None:
            self.birth_day = birth_day
        if birth_year is not None:
            self.birth_year = birth_year
        if remember_login is not None:
            self.remember_login = remember_login
        if policies is not None:
            self.policies = policies
        if register_button is not None:
            self.register_button = register_button
        if login_email is not None:
            self.login_email = login_email

    @property
    def register_only(self) -> primitives.Bool | None:
        """Whether user should just be registered and not log in afterwards."""
        member = self.get_member("RegisterOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @register_only.setter
    def register_only(self, value: primitives.Bool) -> None:
        """Set the RegisterOnly field value."""
        member = self.get_member("RegisterOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RegisterOnly", fields.FieldBool(value=value)
            )

    @property
    def interaction_enabled(self) -> primitives.Bool | None:
        """Whether interacting with this component is enabled."""
        member = self.get_member("_interactionEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interaction_enabled.setter
    def interaction_enabled(self, value: primitives.Bool) -> None:
        """Set the _interactionEnabled field value."""
        member = self.get_member("_interactionEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_interactionEnabled", fields.FieldBool(value=value)
            )

    @property
    def swap_region(self) -> str | None:
        """Handles the slide animation as this dialogue changes pages."""
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @swap_region.setter
    def swap_region(self, target: str | SlideSwapRegion | None) -> None:
        """Set the _swapRegion reference by target ID or SlideSwapRegion instance."""
        target_id: str | None = target.id if isinstance(target, SlideSwapRegion) else target  # type: ignore[assignment]
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_swapRegion",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion'),
            )

    @property
    def username(self) -> str | None:
        """The field for entering the user's username."""
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username.setter
    def username(self, target: str | TextField | None) -> None:
        """Set the _username reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_username")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_username",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def email(self) -> str | None:
        """The field for entering the user's email address."""
        member = self.get_member("_email")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @email.setter
    def email(self, target: str | TextField | None) -> None:
        """Set the _email reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_email")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_email",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def email_repeat(self) -> str | None:
        """The field to confirm the user's email address."""
        member = self.get_member("_emailRepeat")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @email_repeat.setter
    def email_repeat(self, target: str | TextField | None) -> None:
        """Set the _emailRepeat reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_emailRepeat")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_emailRepeat",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def password(self) -> str | None:
        """The field for entering the user's password."""
        member = self.get_member("_password")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @password.setter
    def password(self, target: str | TextField | None) -> None:
        """Set the _password reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_password")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_password",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def password_repeat(self) -> str | None:
        """The field for entering the user's password again for confirmation."""
        member = self.get_member("_passwordRepeat")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @password_repeat.setter
    def password_repeat(self, target: str | TextField | None) -> None:
        """Set the _passwordRepeat reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_passwordRepeat")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_passwordRepeat",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def recovery_code(self) -> str | None:
        """The field to get a recovery code from in case of account loss."""
        member = self.get_member("_recoveryCode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @recovery_code.setter
    def recovery_code(self, target: str | TextField | None) -> None:
        """Set the _recoveryCode reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_recoveryCode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_recoveryCode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def promo_code(self) -> str | None:
        """Target ID of the _promoCode reference (targets TextField)."""
        member = self.get_member("_promoCode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @promo_code.setter
    def promo_code(self, target: str | TextField | None) -> None:
        """Set the _promoCode reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_promoCode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_promoCode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def birth_month(self) -> str | None:
        """The field to enter the user's legal birth month MM."""
        member = self.get_member("_birthMonth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @birth_month.setter
    def birth_month(self, target: str | IntTextEditorParser | None) -> None:
        """Set the _birthMonth reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_birthMonth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_birthMonth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def birth_day(self) -> str | None:
        """The field to enter the user's legal birth day DD."""
        member = self.get_member("_birthDay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @birth_day.setter
    def birth_day(self, target: str | IntTextEditorParser | None) -> None:
        """Set the _birthDay reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_birthDay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_birthDay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def birth_year(self) -> str | None:
        """The field to enter the user's legal birth year YYYY."""
        member = self.get_member("_birthYear")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @birth_year.setter
    def birth_year(self, target: str | IntTextEditorParser | None) -> None:
        """Set the _birthYear reference by target ID or IntTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, IntTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_birthYear")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_birthYear",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IntTextEditorParser'),
            )

    @property
    def remember_login(self) -> str | None:
        """Whether to keep an encrypted token on disk using modern security protocols so the user can stay remembered for 30 days since last login, token refreshing every login."""
        member = self.get_member("_rememberLogin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @remember_login.setter
    def remember_login(self, target: str | Checkbox | None) -> None:
        """Set the _rememberLogin reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_rememberLogin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rememberLogin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def policies(self) -> str | None:
        """Whether the player accepts the EULA."""
        member = self.get_member("_policies")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @policies.setter
    def policies(self, target: str | Checkbox | None) -> None:
        """Set the _policies reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_policies")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_policies",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def register_button(self) -> str | None:
        """The button for registering."""
        member = self.get_member("_registerButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @register_button.setter
    def register_button(self, target: str | Button | None) -> None:
        """Set the _registerButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_registerButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_registerButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def login_email(self) -> primitives.String | None:
        """The email used to log in."""
        member = self.get_member("_loginEmail")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @login_email.setter
    def login_email(self, value: primitives.String) -> None:
        """Set the _loginEmail field value."""
        member = self.get_member("_loginEmail")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_loginEmail", fields.FieldString(value=value)
            )

