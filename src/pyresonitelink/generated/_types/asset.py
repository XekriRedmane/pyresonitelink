"""Generated type: Asset."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iasset import IAsset
from pyresonitelink.generated._types.iengine_asset_variant_descriptor import IEngineAssetVariantDescriptor

V = TypeVar('V')


class Asset(IAsset, Generic[V]):
    """Abstract class: [FrooxEngine]FrooxEngine.Asset<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.Asset<>"

