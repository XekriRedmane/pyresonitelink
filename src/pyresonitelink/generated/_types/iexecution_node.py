"""Generated type: IExecutionNode."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iproto_flux_node import IProtoFluxNode

C = TypeVar('C')


class IExecutionNode(IProtoFluxNode, Generic[C]):
    """Interface: [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IExecutionNode<>."""

