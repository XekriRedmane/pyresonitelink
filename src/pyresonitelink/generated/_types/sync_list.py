"""Generated type: SyncList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_element_list import SyncElementList
from pyresonitelink.generated._types.isync_member import ISyncMember

T = TypeVar('T')


class SyncList(SyncElementList, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncList<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncList<>"

