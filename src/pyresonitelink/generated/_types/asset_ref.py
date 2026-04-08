"""Generated type: AssetRef."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.iasset_ref import IAssetRef
from pyresonitelink.generated._types.iasset import IAsset

A = TypeVar('A')


class AssetRef(SyncRef, IAssetRef, Generic[A]):
    """Class: [FrooxEngine]FrooxEngine.AssetRef<>."""

