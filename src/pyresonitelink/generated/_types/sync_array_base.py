"""Generated type: SyncArrayBase."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.conflicting_sync_element import ConflictingSyncElement
from pyresonitelink.generated._types.isync_array import ISyncArray
from pyresonitelink.generated._types.ienumerable import IEnumerable

T = TypeVar('T')


class SyncArrayBase(ConflictingSyncElement, ISyncArray, IEnumerable, Generic[T]):
    """Abstract class: [FrooxEngine]FrooxEngine.SyncArrayBase<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncArrayBase<>"

