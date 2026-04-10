"""Generated type: ISpatialVariable."""

from typing import Generic, TypeVar

T = TypeVar('T')


class ISpatialVariable(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ISpatialVariable<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ISpatialVariable<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

