"""Generated type: IReferenceSource."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iworld_element import IWorldElement

T = TypeVar('T')


class IReferenceSource(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.IReferenceSource<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

