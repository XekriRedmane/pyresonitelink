"""Generated type: ISyncRef."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iworld_element import IWorldElement

T = TypeVar('T')


class ISyncRef(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ISyncRef<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None


