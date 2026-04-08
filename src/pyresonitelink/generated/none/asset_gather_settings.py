"""Generated component: AssetGatherSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AssetGatherSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.AssetGatherSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetGatherSettings"

    def __init__(self, max_concurrent_asset_transfers: np.int32 | None = None, max_concurrent_downloads: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_concurrent_asset_transfers: Initial value for MaxConcurrentAssetTransfers.
            max_concurrent_downloads: Initial value for MaxConcurrentDownloads.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_concurrent_asset_transfers is not None:
            self.max_concurrent_asset_transfers = max_concurrent_asset_transfers
        if max_concurrent_downloads is not None:
            self.max_concurrent_downloads = max_concurrent_downloads

    @property
    def max_concurrent_asset_transfers(self) -> np.int32 | None:
        """The MaxConcurrentAssetTransfers field value."""
        member = self.get_member("MaxConcurrentAssetTransfers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_concurrent_asset_transfers.setter
    def max_concurrent_asset_transfers(self, value: np.int32) -> None:
        """Set the MaxConcurrentAssetTransfers field value."""
        member = self.get_member("MaxConcurrentAssetTransfers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxConcurrentAssetTransfers", fields.FieldInt(value=value)
            )

    @property
    def max_concurrent_downloads(self) -> np.int32 | None:
        """The MaxConcurrentDownloads field value."""
        member = self.get_member("MaxConcurrentDownloads")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_concurrent_downloads.setter
    def max_concurrent_downloads(self, value: np.int32) -> None:
        """Set the MaxConcurrentDownloads field value."""
        member = self.get_member("MaxConcurrentDownloads")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxConcurrentDownloads", fields.FieldInt(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

