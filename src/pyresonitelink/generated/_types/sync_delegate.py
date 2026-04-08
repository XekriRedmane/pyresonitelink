"""Generated type: SyncDelegate."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_field import SyncField
from pyresonitelink.generated._types.isync_delegate import ISyncDelegate

T = TypeVar('T')


class SyncDelegate(SyncField, ISyncDelegate, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncDelegate<>."""

