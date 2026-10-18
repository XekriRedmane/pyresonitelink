"""Generated type: ISyncRefList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.ilinkable import ILinkable
from pyresonitelink.generated._types.iread_only_list import IReadOnlyList
from pyresonitelink.generated._types.ilist import IList
from pyresonitelink.generated._types.iworld_element import IWorldElement

T = TypeVar('T')


class ISyncRefList(ILinkable, IReadOnlyList, IList, Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ISyncRefList<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ISyncRefList<>"

