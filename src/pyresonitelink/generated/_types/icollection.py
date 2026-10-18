"""Generated type: ICollection."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.ienumerable import IEnumerable

T = TypeVar('T')


class ICollection(IEnumerable, Generic[T]):
    """Interface: ICollection<>."""

    RESONITE_TYPE: str = "ICollection<>"

