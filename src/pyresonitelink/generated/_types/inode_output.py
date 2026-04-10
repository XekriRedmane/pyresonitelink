"""Generated type: INodeOutput."""

from typing import Generic, TypeVar

T = TypeVar('T')


class INodeOutput(Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ProtoFlux.INodeOutput<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ProtoFlux.INodeOutput<>"

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None

