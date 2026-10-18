"""Generated type: IReadOnlyList."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iread_only_collection import IReadOnlyCollection

T = TypeVar('T')


class IReadOnlyList(IReadOnlyCollection, Generic[T]):
    """Interface: IReadOnlyList<>."""

    RESONITE_TYPE: str = "IReadOnlyList<>"

