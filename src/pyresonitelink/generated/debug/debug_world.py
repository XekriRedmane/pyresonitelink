"""Generated component: DebugWorld."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugWorld(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugWorld component renders out a block of text that displays information about the current world the component is in.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugWorld"

    pass

