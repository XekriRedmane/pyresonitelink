"""Generated component: LocaleSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class LocaleSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.LocaleSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocaleSettings"

    def __init__(self, primary_interface_locale_code: str | None = None, culture_locale_code: str | None = None, use_imperial_units: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            primary_interface_locale_code: Initial value for PrimaryInterfaceLocaleCode.
            culture_locale_code: Initial value for CultureLocaleCode.
            use_imperial_units: Initial value for UseImperialUnits.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if primary_interface_locale_code is not None:
            self.primary_interface_locale_code = primary_interface_locale_code
        if culture_locale_code is not None:
            self.culture_locale_code = culture_locale_code
        if use_imperial_units is not None:
            self.use_imperial_units = use_imperial_units

    @property
    def primary_interface_locale_code(self) -> str | None:
        """The PrimaryInterfaceLocaleCode field value."""
        member = self.get_member("PrimaryInterfaceLocaleCode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @primary_interface_locale_code.setter
    def primary_interface_locale_code(self, value: str) -> None:
        """Set the PrimaryInterfaceLocaleCode field value."""
        member = self.get_member("PrimaryInterfaceLocaleCode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PrimaryInterfaceLocaleCode", fields.FieldString(value=value)
            )

    @property
    def culture_locale_code(self) -> str | None:
        """The CultureLocaleCode field value."""
        member = self.get_member("CultureLocaleCode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @culture_locale_code.setter
    def culture_locale_code(self, value: str) -> None:
        """Set the CultureLocaleCode field value."""
        member = self.get_member("CultureLocaleCode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CultureLocaleCode", fields.FieldString(value=value)
            )

    @property
    def use_imperial_units(self) -> bool | None:
        """The UseImperialUnits field value."""
        member = self.get_member("UseImperialUnits")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_imperial_units.setter
    def use_imperial_units(self, value: bool) -> None:
        """Set the UseImperialUnits field value."""
        member = self.get_member("UseImperialUnits")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseImperialUnits", fields.FieldBool(value=value)
            )

    async def set_current_locale(self, resolink: protocols.ResoniteLinkClient, locale_code: str, debug: bool = False) -> dict:
        """Call the SetCurrentLocale sync method.

        Args:
            resolink: Connected ResoniteLink client.
            locale_code: The localeCode parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetCurrentLocale", {"localeCode": locale_code}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

