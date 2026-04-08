"""Generated component: ButtonHoverRelay."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonHoverRelay(GeneratedComponent, IButtonHoverReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonHoverRelay.

    Category: Common UI/Events
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonHoverRelay"

    pass

