"""Generated type: SyncAssetList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_element_list import SyncElementList
from pyresonitelink.generated._types.iread_only_list import IReadOnlyList
from pyresonitelink.generated._types.ilist import IList
from pyresonitelink.generated._types.iasset import IAsset

T = TypeVar('T')


class SyncAssetList(SyncElementList, IReadOnlyList, IList, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncAssetList<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncAssetList<>"

