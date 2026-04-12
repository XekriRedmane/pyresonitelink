"""Generated component: TeleportBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TeleportBlock(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Teleport Block component is a component that is used to Tag colliders like platforms and walls as a place where a user cannot teleport to via the Teleport Locomotion Mode.

    Category: Transform/Tagging

    **Behavior**: When a user using teleport mode tries to teleport onto or through a collider with this component, it will make the path turn red and deny them from teleporting to the selected point.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TeleportBlock"

    pass

