"""Generated component: PointerInteractionController."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointerInteractionController(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """The PointerInteractionController component is used by the game internally to handle tip touch source behavior on a user.

    Not to be used by the user, is used in internal game behavior.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointerInteractionController"

    pass

