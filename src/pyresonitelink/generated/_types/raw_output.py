"""Generated type: RawOutput."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.empty_sync_element import EmptySyncElement
from pyresonitelink.generated._types.ifield import IField

T = TypeVar('T')


class RawOutput(EmptySyncElement, IField, Generic[T]):
    """Class: [FrooxEngine]FrooxEngine.RawOutput<>."""

