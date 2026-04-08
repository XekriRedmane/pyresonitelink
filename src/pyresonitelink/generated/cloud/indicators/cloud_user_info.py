"""Generated component: CloudUserInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CloudUserInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CloudUserInfo.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloudUserInfo"

    def __init__(self, user_id: primitives.String | None = None, is_loaded: primitives.Bool | None = None, username: primitives.String | None = None, registration_date: str | None = None, original_registration_date: str | None = None, icon_url: str | None = None, is_contact: primitives.Bool | None = None, loaded_user_id: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_id: Initial value for UserId.
            is_loaded: Initial value for IsLoaded.
            username: Initial value for Username.
            registration_date: Initial value for RegistrationDate.
            original_registration_date: Initial value for OriginalRegistrationDate.
            icon_url: Initial value for IconURL.
            is_contact: Initial value for IsContact.
            loaded_user_id: Initial value for _loadedUserId.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_id is not None:
            self.user_id = user_id
        if is_loaded is not None:
            self.is_loaded = is_loaded
        if username is not None:
            self.username = username
        if registration_date is not None:
            self.registration_date = registration_date
        if original_registration_date is not None:
            self.original_registration_date = original_registration_date
        if icon_url is not None:
            self.icon_url = icon_url
        if is_contact is not None:
            self.is_contact = is_contact
        if loaded_user_id is not None:
            self.loaded_user_id = loaded_user_id

    @property
    def user_id(self) -> primitives.String | None:
        """The UserId field value."""
        member = self.get_member("UserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_id.setter
    def user_id(self, value: primitives.String) -> None:
        """Set the UserId field value."""
        member = self.get_member("UserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserId", fields.FieldString(value=value)
            )

    @property
    def is_loaded(self) -> primitives.Bool | None:
        """The IsLoaded field value."""
        member = self.get_member("IsLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_loaded.setter
    def is_loaded(self, value: primitives.Bool) -> None:
        """Set the IsLoaded field value."""
        member = self.get_member("IsLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLoaded", fields.FieldBool(value=value)
            )

    @property
    def username(self) -> primitives.String | None:
        """The Username field value."""
        member = self.get_member("Username")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @username.setter
    def username(self, value: primitives.String) -> None:
        """Set the Username field value."""
        member = self.get_member("Username")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Username", fields.FieldString(value=value)
            )

    @property
    def registration_date(self) -> str | None:
        """The RegistrationDate field value."""
        member = self.get_member("RegistrationDate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @registration_date.setter
    def registration_date(self, value: str) -> None:
        """Set the RegistrationDate field value."""
        member = self.get_member("RegistrationDate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RegistrationDate", fields.FieldDateTime(value=value)
            )

    @property
    def original_registration_date(self) -> str | None:
        """The OriginalRegistrationDate field value."""
        member = self.get_member("OriginalRegistrationDate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_registration_date.setter
    def original_registration_date(self, value: str) -> None:
        """Set the OriginalRegistrationDate field value."""
        member = self.get_member("OriginalRegistrationDate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OriginalRegistrationDate", fields.FieldDateTime(value=value)
            )

    @property
    def icon_url(self) -> str | None:
        """The IconURL field value."""
        member = self.get_member("IconURL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @icon_url.setter
    def icon_url(self, value: str) -> None:
        """Set the IconURL field value."""
        member = self.get_member("IconURL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IconURL", fields.FieldUri(value=value)
            )

    @property
    def is_contact(self) -> primitives.Bool | None:
        """The IsContact field value."""
        member = self.get_member("IsContact")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_contact.setter
    def is_contact(self, value: primitives.Bool) -> None:
        """Set the IsContact field value."""
        member = self.get_member("IsContact")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsContact", fields.FieldBool(value=value)
            )

    @property
    def loaded_user_id(self) -> primitives.String | None:
        """The _loadedUserId field value."""
        member = self.get_member("_loadedUserId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @loaded_user_id.setter
    def loaded_user_id(self, value: primitives.String) -> None:
        """Set the _loadedUserId field value."""
        member = self.get_member("_loadedUserId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_loadedUserId", fields.FieldString(value=value)
            )

