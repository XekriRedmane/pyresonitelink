"""Generated component: ButtonHoverRelay."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonHoverRelay(GeneratedComponent, IButtonHoverReceiver, IWorldEventReceiver):
    """The ButtonHoverRelay component sends a signal to a button event handler (usually something internal like a Method Proxy).

    Category: Common UI/Events

    This can send a signal internally.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonHoverRelay"

    pass

