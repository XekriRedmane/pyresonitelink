"""Generated type: IEnumerable."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IEnumerable(Generic[T]):
    """Interface: IEnumerable<>."""

    RESONITE_TYPE: str = "IEnumerable<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

