"""Generated type: IValue."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IValue(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.IValue<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

