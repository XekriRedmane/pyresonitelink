"""Generated type: Nullable."""

from typing import Generic, TypeVar

T = TypeVar('T')


class Nullable(Generic[T]):
    """Class: Nullable<>."""

    RESONITE_TYPE: str = "Nullable<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

