"""Generated component: TrackerController."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TrackerController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TrackerController component is an internally used component that triggers a pair of sync Delegates when a device is added to the user's list of tracked devices with position and rotation.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TrackerController"

    pass

