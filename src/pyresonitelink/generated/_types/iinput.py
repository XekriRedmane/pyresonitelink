"""Generated type: IInput."""

from typing import Generic, TypeVar

T = TypeVar('T')


class IInput(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ProtoFlux.IInput<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ProtoFlux.IInput<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

