"""Generated type: SharedMaterialBase."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.dynamic_renderer_asset import DynamicRendererAsset

A = TypeVar('A')


class SharedMaterialBase(DynamicRendererAsset, Generic[A]):
    """Abstract class: [FrooxEngine]FrooxEngine.SharedMaterialBase<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SharedMaterialBase<>"

