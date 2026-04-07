"""Generated type: IGlobalValueProxy."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IGlobalValueProxy(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

