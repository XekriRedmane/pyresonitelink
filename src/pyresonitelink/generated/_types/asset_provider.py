"""Generated type: AssetProvider."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.component import Component
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.asset import Asset

A = TypeVar('A')


class AssetProvider(Component, IAssetProvider, ICustomInspector, Generic[A]):
    """Abstract class: [FrooxEngine]FrooxEngine.AssetProvider<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.AssetProvider<>"

