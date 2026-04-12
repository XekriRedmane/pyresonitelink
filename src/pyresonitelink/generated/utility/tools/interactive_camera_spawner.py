"""Generated component: InteractiveCameraSpawner."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraSpawner(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The InteractiveCameraSpawner can receive Button Events, including ones from a button on the same slot. When receiving a pressed event, this component will spawn an InteractiveCamera in the currently focused world.

    Category: Utility/Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraSpawner"

    pass

