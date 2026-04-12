"""Generated component: SimpleVirtualKeyboard."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimpleVirtualKeyboard(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SimpleVirtualKeyboard component makes a simple keyboard UI that can be used.

    Category: Userspace/Virtual Keyboard

    On apply this component populates a VirtualKeyboard as well as a basic
    UIX layout.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimpleVirtualKeyboard"

    pass

