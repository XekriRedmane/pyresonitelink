"""Generated type: DynamicAssetProvider."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.asset_provider import AssetProvider
from pyresonitelink.generated._types.asset import Asset

A = TypeVar('A')


class DynamicAssetProvider(AssetProvider, Generic[A]):
    """Abstract class: [FrooxEngine]FrooxEngine.DynamicAssetProvider<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.DynamicAssetProvider<>"

