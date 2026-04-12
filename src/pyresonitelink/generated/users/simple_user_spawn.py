"""Generated component: SimpleUserSpawn."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimpleUserSpawn(GeneratedComponent, IComponent, IWorldEventReceiver):
    """A SimpleUserSpawn defines a simple spawn point.

    Category: Users

    A SimpleUserSpawn defines a simple spawn point. New and respawning users
    will be placed with their avatar as a child of the world's root at
    ``0,0,0``, facing the Z- direction. The position and rotation of this
    component's slot have no bearing on the user's position or rotation.

    **Related Components**: * SpawnArc
* CommonSpawnArea
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimpleUserSpawn"

    pass

