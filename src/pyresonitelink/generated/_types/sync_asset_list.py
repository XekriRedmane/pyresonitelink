"""Generated type: SyncAssetList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_element_list import SyncElementList
from pyresonitelink.generated._types.iasset import IAsset

T = TypeVar('T')


class SyncAssetList(SyncElementList, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncAssetList<>."""

