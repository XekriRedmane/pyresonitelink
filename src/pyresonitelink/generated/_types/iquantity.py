"""Generated type: IQuantity."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IQuantity(Generic[T]):
    """Interface: IQuantity<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

