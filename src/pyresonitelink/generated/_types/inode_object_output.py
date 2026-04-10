"""Generated type: INodeObjectOutput."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.inode_output import INodeOutput

T = TypeVar('T')


class INodeObjectOutput(INodeOutput, Generic[T]):
    """Interface: [FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<>"

