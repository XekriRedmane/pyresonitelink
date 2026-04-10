"""Generated type: SyncCurve."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.sync_keys import SyncKeys

T = TypeVar('T')


class SyncCurve(SyncKeys, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.SyncCurve<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.SyncCurve<>"

