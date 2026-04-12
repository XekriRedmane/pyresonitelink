"""Generated component: DebugTrackingAligner."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugTrackingAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugTrackingAligner calls the align tracking for all users in the world every 0.5 seconds if they have a slot called "Bases" with bases "Base 0" and "Base 1" under them.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugTrackingAligner"

    pass

