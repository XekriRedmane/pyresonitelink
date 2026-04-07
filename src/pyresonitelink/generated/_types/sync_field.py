"""Generated type: SyncField."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.conflicting_sync_element import ConflictingSyncElement
from pyresonitelink.generated._types.ifield import IField

T = TypeVar('T')


class SyncField(ConflictingSyncElement, IField, Generic[T]):
    """Abstract class: [FrooxEngine]FrooxEngine.SyncField<>."""

