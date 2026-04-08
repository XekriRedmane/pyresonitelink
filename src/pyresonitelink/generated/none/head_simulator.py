"""Generated component: HeadSimulator."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HeadSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The HeadSimulator used to control the movement of the user's head.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HeadSimulator"

    pass

