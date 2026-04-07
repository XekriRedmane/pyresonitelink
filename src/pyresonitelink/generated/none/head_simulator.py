"""Generated component: HeadSimulator."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HeadSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HeadSimulator.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HeadSimulator"

    pass

