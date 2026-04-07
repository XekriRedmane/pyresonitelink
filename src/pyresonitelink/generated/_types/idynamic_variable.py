"""Generated type: IDynamicVariable."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IDynamicVariable(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.IDynamicVariable<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

