"""Generated component: ButtonActionTrigger."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonActionTrigger(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonActionTrigger.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonActionTrigger"

    pass

