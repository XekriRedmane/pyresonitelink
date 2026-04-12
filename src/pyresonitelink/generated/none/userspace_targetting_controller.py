"""Generated component: UserspaceTargettingController."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iview_targetting_controller import IViewTargettingController
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceTargettingController(GeneratedComponent, IViewTargettingController, IInputUpdateReceiver, IWorldEventReceiver):
    """Used as a screen controller component for userspace actions.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceTargettingController"

    pass

