"""Generated type: ComponentBase."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.worker import Worker
from pyresonitelink.generated._types.icomponent_base import IComponentBase
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver

C = TypeVar('C')


class ComponentBase(Worker, IComponentBase, IWorldEventReceiver, Generic[C]):
    """Abstract class: [FrooxEngine]FrooxEngine.ComponentBase<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.ComponentBase<>"

