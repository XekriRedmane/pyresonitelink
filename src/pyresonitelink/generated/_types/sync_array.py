"""Generated type: SyncArray."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_array_base import SyncArrayBase
from pyresonitelink.generated._types.iread_only_list import IReadOnlyList
from pyresonitelink.generated._types.ilist import IList

T = TypeVar('T')


class SyncArray(SyncArrayBase, IReadOnlyList, IList, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncArray<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncArray<>"

