"""Generated component: LocaleStringDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.locale_resource import LocaleResource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocaleStringDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LocaleStringDriver component is used to turn a key into a translated string from a locale, and then fill its value arguments with field contents or values.

    Category: Localization

    To use the LocaleStringDriver provide it with locale resource, a string
    to be driven and the name of the locale key you want to use. A list of
    all locale keys can be found in the Yellow-Dog-Man/Locale repository.
    You can find a locale resource in the form of the StaticLocaleProvider
    component on the world Root slot. If the locale string has no template
    arguments (for example "General.OK") this is all that you need to do. If
    it does have template parameters you will need to provide them using the
    ArgumentSources and ArgumentValues dictionaries. Because Resonite does
    not support editing Dictionaries through the scene inspector, you will
    need to use the Sync Delegates that the component exposes. For example,
    if you want to format the "Dash.Exit.Header" key which in english has
    the value "Exit {appName}" you would need to provide the "appName"
    parameter using one of the dictionaries. The ArgumentValues dictionary
    will take priority over the ArgumentSources dictionary. ArgumentSources
    maps parameter names to fields which will then be read to format the
    string. To add a parameter pull out the method proxy for
    SetArgumentSource and plug "appName" into Arg0 and a reference to the
    field you want to use. In this example you might want to use the
    PlatformName field of the PlatformInfo component. ArgumentValues maps
    parameter names to values which will be directly used to format the
    string. To add a parameter pull out the method proxy for
    SetArgumentValue and plug "appName" into Arg0 and a string with the
    value you'd like into Arg1. The Format field on the LocaleStringDriver
    component can also be used to add some extra text around the translated
    string, for example putting "Click here to {0}" would produce "Click
    here to Exit Resonite" with the above example. 600px
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocaleStringDriver"

    def __init__(self, target: str | IField[primitives.String] | None = None, key: primitives.String | None = None, format_: primitives.String | None = None, locale: str | IAssetProvider[LocaleResource] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            key: Initial value for Key.
            format_: Initial value for Format.
            locale: Initial value for Locale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if key is not None:
            self.key = key
        if format_ is not None:
            self.format_ = format_
        if locale is not None:
            self.locale = locale

    @property
    def target(self) -> str | None:
        """The string field to drive with the final locale translation."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def key(self) -> primitives.String | None:
        """The locale key to get a translation with."""
        member = self.get_member("Key")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @key.setter
    def key(self, value: primitives.String) -> None:
        """Set the Key field value."""
        member = self.get_member("Key")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Key", fields.FieldString(value=value)
            )

    @property
    def format_(self) -> primitives.String | None:
        """How to format the output."""
        member = self.get_member("Format")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_.setter
    def format_(self, value: primitives.String) -> None:
        """Set the Format field value."""
        member = self.get_member("Format")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Format", fields.FieldString(value=value)
            )

    @property
    def locale(self) -> str | None:
        """The locale resource to use ``Key`` on to get the translated string for."""
        member = self.get_member("Locale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locale.setter
    def locale(self, target: str | IAssetProvider[LocaleResource] | None) -> None:
        """Set the Locale reference by target ID or IAssetProvider[LocaleResource] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Locale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Locale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.LocaleResource>'),
            )

    @property
    def argument_sources(self) -> members.SyncDictionary | None:
        """A list of argument strings in a locale translation and their fields to get the values for them from."""
        member = self.get_member("ArgumentSources")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @argument_sources.setter
    def argument_sources(self, value: members.SyncDictionary) -> None:
        """Set ArgumentSources. A list of argument strings in a locale translation and their fields to get the values for them from."""
        self.set_member("ArgumentSources", value)

    async def set_argument_source(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, field: str, debug: bool = False) -> dict:
        """Can be called to set the argument source for the locale data.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            field: The field parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetArgumentSource", {"key": key, "field": field}, debug,
        )

    async def set_argument_value(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, value: str, debug: bool = False) -> dict:
        """Can be called to set the argument value for the locale data.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            value: The value parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetArgumentValue", {"key": key, "value": value}, debug,
        )

