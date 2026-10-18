"""Generated type: SyncDelegate."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_field import SyncField
from pyresonitelink.generated._types.isync_delegate import ISyncDelegate
from pyresonitelink.generated._types.delegate import Delegate

T = TypeVar('T')


class SyncDelegate(SyncField, ISyncDelegate, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncDelegate<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncDelegate<>"

