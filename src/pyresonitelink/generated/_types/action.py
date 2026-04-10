"""Generated type: Action."""

from typing import Generic, TypeVar

T = TypeVar('T')


class Action(Generic[T]):
    """Class: Action<>."""

    RESONITE_TYPE: str = "Action<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

