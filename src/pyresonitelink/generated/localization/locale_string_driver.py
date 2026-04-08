"""Generated component: LocaleStringDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.locale_resource import LocaleResource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocaleStringDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocaleStringDriver.

    Category: Localization
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocaleStringDriver"

    def __init__(self, target: str | IField[str] | None = None, key: str | None = None, format_: str | None = None, locale: str | IAssetProvider[LocaleResource] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Target reference (targets IField[str])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[str] | None) -> None:
        """Set the Target reference by target ID or IField[str] instance."""
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
    def key(self) -> str | None:
        """The Key field value."""
        member = self.get_member("Key")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @key.setter
    def key(self, value: str) -> None:
        """Set the Key field value."""
        member = self.get_member("Key")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Key", fields.FieldString(value=value)
            )

    @property
    def format_(self) -> str | None:
        """The Format field value."""
        member = self.get_member("Format")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @format_.setter
    def format_(self, value: str) -> None:
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
        """Target ID of the Locale reference (targets IAssetProvider[LocaleResource])."""
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
        """The ArgumentSources member."""
        member = self.get_member("ArgumentSources")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @argument_sources.setter
    def argument_sources(self, value: members.SyncDictionary) -> None:
        """Set the ArgumentSources member."""
        self.set_member("ArgumentSources", value)

    async def set_argument_source(self, resolink: protocols.ResoniteLinkClient, key: str, field: str, debug: bool = False) -> dict:
        """Call the SetArgumentSource sync method.

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

    async def set_argument_value(self, resolink: protocols.ResoniteLinkClient, key: str, value: str, debug: bool = False) -> dict:
        """Call the SetArgumentValue sync method.

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

