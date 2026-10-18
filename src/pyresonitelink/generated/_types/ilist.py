"""Generated type: IList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.icollection import ICollection

T = TypeVar('T')


class IList(ICollection, Generic[T]):
    """Interface: IList<>."""

    RESONITE_TYPE: str = "IList<>"

