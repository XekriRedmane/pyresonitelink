"""Generated type: ILastValueProxy."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.icomponent import IComponent

T = TypeVar('T')


class ILastValueProxy(IComponent, Generic[T]):
    """Interface: [ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.ILastValueProxy<>."""

    RESONITE_TYPE: str = "[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.Actions.ILastValueProxy<>"

