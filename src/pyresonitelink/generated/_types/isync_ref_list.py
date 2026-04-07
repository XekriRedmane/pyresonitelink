"""Generated type: ISyncRefList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.ilinkable import ILinkable
from pyresonitelink.generated._types.iworld_element import IWorldElement

T = TypeVar('T')


class ISyncRefList(ILinkable, Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ISyncRefList<>."""

