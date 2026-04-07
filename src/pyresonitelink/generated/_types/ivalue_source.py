"""Generated type: IValueSource."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IValueSource(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.IValueSource<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

