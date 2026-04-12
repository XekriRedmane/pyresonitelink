"""Generated component: AvatarCreatorSpawner."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarCreatorSpawner(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Avatar Creator Spawner is a component that works in either userspace or real space. This component recieves button events, which means it works when on the same slot of any button. When it recieves a button press event, this component spawns a fully set up Avatar Creator in the world.

    Category: Utility/Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarCreatorSpawner"

    pass

