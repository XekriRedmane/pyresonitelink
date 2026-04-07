"""Generated type: SyncRef."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_field import SyncField
from pyresonitelink.generated._types.isync_ref import ISyncRef
from pyresonitelink.generated._types.iworld_element import IWorldElement

T = TypeVar('T')


class SyncRef(SyncField, ISyncRef, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncRef<>."""

