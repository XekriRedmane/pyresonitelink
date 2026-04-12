"""Generated component: TeleportPassthrough."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TeleportPassthrough(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Teleport Passthrough component makes a collider on the same slot tagged with this component act as if the collider doesn't exist to the teleport selector when teleporting via the Teleport Locomotion Mode.

    Category: Transform/Tagging

    Attach to a slot with a collider, to enable teleporting through a wall
    via the Teleport Locomotion Mode.

    **Related Components**: * Teleport Surface
* Teleport Block
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TeleportPassthrough"

    pass

