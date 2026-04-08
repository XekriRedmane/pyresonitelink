"""Generated component: Component."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Component(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Component"

    pass

