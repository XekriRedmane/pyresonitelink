"""Generated component: ButtonActionTrigger."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonActionTrigger(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonActionTrigger component is used for triggering C# actions (not to be confused with impulses) using the Interface IButton, such as UIX Buttons or Legacy Buttons.

This component must be on the same slot as the button in order to be bound to it.

}}

    Category: Common UI/Button Interactions

    This component allows you to trigger actions on some special components,
    such as the Random Object Spawner component, by dragging the reference
    to the target action into a trigger slot (such as ``OnPressed``).
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonActionTrigger"

    pass

