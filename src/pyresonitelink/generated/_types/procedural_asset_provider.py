"""Generated type: ProceduralAssetProvider."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.dynamic_asset_provider import DynamicAssetProvider
from pyresonitelink.generated._types.asset import Asset

A = TypeVar('A')


class ProceduralAssetProvider(DynamicAssetProvider, Generic[A]):
    """Abstract class: [FrooxEngine]FrooxEngine.ProceduralAssetProvider<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ProceduralAssetProvider<>"

