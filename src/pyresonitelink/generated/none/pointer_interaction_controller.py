"""Generated component: PointerInteractionController."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointerInteractionController(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PointerInteractionController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointerInteractionController"

    pass

