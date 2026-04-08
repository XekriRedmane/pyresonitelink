"""Generated component: DynamicSubtitleProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicSubtitleProvider(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicSubtitleProvider.

    Category: Assets/Procedural Animations
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicSubtitleProvider"

    def __init__(self, high_priority_integration: bool | None = None, asset_url: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            asset_url: Initial value for AssetURL.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if asset_url is not None:
            self.asset_url = asset_url

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def asset_url(self) -> str | None:
        """The AssetURL field value."""
        member = self.get_member("AssetURL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @asset_url.setter
    def asset_url(self, value: str) -> None:
        """Set the AssetURL field value."""
        member = self.get_member("AssetURL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AssetURL", fields.FieldUri(value=value)
            )

