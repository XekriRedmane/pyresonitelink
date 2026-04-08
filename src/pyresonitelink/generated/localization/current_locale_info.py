"""Generated component: CurrentLocaleInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CurrentLocaleInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CurrentLocaleInfo.

    Category: Localization
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CurrentLocaleInfo"

    def __init__(self, locale_code: str | None = None, language_code: str | None = None, native_locale_name: str | None = None, english_locale_name: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            locale_code: Initial value for LocaleCode.
            language_code: Initial value for LanguageCode.
            native_locale_name: Initial value for NativeLocaleName.
            english_locale_name: Initial value for EnglishLocaleName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if locale_code is not None:
            self.locale_code = locale_code
        if language_code is not None:
            self.language_code = language_code
        if native_locale_name is not None:
            self.native_locale_name = native_locale_name
        if english_locale_name is not None:
            self.english_locale_name = english_locale_name

    @property
    def locale_code(self) -> str | None:
        """The LocaleCode field value."""
        member = self.get_member("LocaleCode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @locale_code.setter
    def locale_code(self, value: str) -> None:
        """Set the LocaleCode field value."""
        member = self.get_member("LocaleCode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocaleCode", fields.FieldString(value=value)
            )

    @property
    def language_code(self) -> str | None:
        """The LanguageCode field value."""
        member = self.get_member("LanguageCode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @language_code.setter
    def language_code(self, value: str) -> None:
        """Set the LanguageCode field value."""
        member = self.get_member("LanguageCode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LanguageCode", fields.FieldString(value=value)
            )

    @property
    def native_locale_name(self) -> str | None:
        """The NativeLocaleName field value."""
        member = self.get_member("NativeLocaleName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @native_locale_name.setter
    def native_locale_name(self, value: str) -> None:
        """Set the NativeLocaleName field value."""
        member = self.get_member("NativeLocaleName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NativeLocaleName", fields.FieldString(value=value)
            )

    @property
    def english_locale_name(self) -> str | None:
        """The EnglishLocaleName field value."""
        member = self.get_member("EnglishLocaleName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @english_locale_name.setter
    def english_locale_name(self, value: str) -> None:
        """Set the EnglishLocaleName field value."""
        member = self.get_member("EnglishLocaleName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnglishLocaleName", fields.FieldString(value=value)
            )

