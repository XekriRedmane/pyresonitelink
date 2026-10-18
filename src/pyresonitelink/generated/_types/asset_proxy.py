"""Generated type: AssetProxy."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.component import Component
from pyresonitelink.generated._types.ireference_source import IReferenceSource
from pyresonitelink.generated._types.iasset import IAsset

A = TypeVar('A')


class AssetProxy(Component, IReferenceSource, Generic[A]):
    """Class: [FrooxEngine]FrooxEngine.AssetProxy<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.AssetProxy<>"

