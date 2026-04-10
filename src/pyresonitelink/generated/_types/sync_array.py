"""Generated type: SyncArray."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.conflicting_sync_element import ConflictingSyncElement
from pyresonitelink.generated._types.isync_array import ISyncArray

T = TypeVar('T')


class SyncArray(ConflictingSyncElement, ISyncArray, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncArray<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncArray<>"

