"""Generated type: IReadOnlyCollection."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.ienumerable import IEnumerable

T = TypeVar('T')


class IReadOnlyCollection(IEnumerable, Generic[T]):
    """Interface: IReadOnlyCollection<>."""

    RESONITE_TYPE: str = "IReadOnlyCollection<>"

