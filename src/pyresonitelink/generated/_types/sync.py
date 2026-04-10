"""Generated type: Sync."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_field import SyncField

T = TypeVar('T')


class Sync(SyncField, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.Sync<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.Sync<>"

