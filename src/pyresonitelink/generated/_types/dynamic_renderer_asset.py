"""Generated type: DynamicRendererAsset."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.dynamic_asset import DynamicAsset
from pyresonitelink.generated._types.irenderer_asset import IRendererAsset

A = TypeVar('A')


class DynamicRendererAsset(DynamicAsset, IRendererAsset, Generic[A]):
    """Abstract class: [FrooxEngine]FrooxEngine.DynamicRendererAsset<>."""

