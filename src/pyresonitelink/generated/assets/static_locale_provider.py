"""Generated component: StaticLocaleProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticLocaleProvider(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StaticLocaleProvider.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticLocaleProvider"

    def __init__(self, url: str | None = None, override_locale: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            override_locale: Initial value for OverrideLocale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if override_locale is not None:
            self.override_locale = override_locale

    @property
    def url(self) -> str | None:
        """The URL field value."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def override_locale(self) -> primitives.String | None:
        """The OverrideLocale field value."""
        member = self.get_member("OverrideLocale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_locale.setter
    def override_locale(self, value: primitives.String) -> None:
        """Set the OverrideLocale field value."""
        member = self.get_member("OverrideLocale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideLocale", fields.FieldString(value=value)
            )

