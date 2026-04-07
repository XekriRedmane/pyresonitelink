"""Generated type: IProtoFluxNode."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.inode import INode

N = TypeVar('N')


class IProtoFluxNode(Generic[N]):
    """Interface: [FrooxEngine]FrooxEngine.ProtoFlux.IProtoFluxNode<>."""

    @property
    def id(self) -> str | None:
        """The element's unique ID."""
        return None


