"""Generated type: IExecutionUpdateReceiver."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.iproto_flux_node import IProtoFluxNode

C = TypeVar('C')


class IExecutionUpdateReceiver(IProtoFluxNode, Generic[C]):
    """Interface: [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IExecutionUpdateReceiver<>."""

    RESONITE_TYPE: str = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.IExecutionUpdateReceiver<>"

