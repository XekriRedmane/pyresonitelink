"""Generated type: SyncElementList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.conflicting_sync_element import ConflictingSyncElement
from pyresonitelink.generated._types.isync_list import ISyncList
from pyresonitelink.generated._types.isync_member import ISyncMember

T = TypeVar('T')


class SyncElementList(ConflictingSyncElement, ISyncList, Generic[T]):
    """Abstract class: [FrooxEngine]FrooxEngine.SyncElementList<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncElementList<>"

