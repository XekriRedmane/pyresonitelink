"""Generated component: FullBodyCalibratorSpawner."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FullBodyCalibratorSpawner(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The FullBodyCalibratorSpawner when on the same Slot as a button, spawns a full body calibrator UI in front of the user that pressed the button.

    Category: Utility/Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FullBodyCalibratorSpawner"

    pass

