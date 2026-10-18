"""Generated type: SyncFieldList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_element_list import SyncElementList
from pyresonitelink.generated._types.iread_only_list import IReadOnlyList
from pyresonitelink.generated._types.ilist import IList

T = TypeVar('T')


class SyncFieldList(SyncElementList, IReadOnlyList, IList, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncFieldList<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncFieldList<>"

