"""Generated component: TeleportSurface."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TeleportSurface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Teleport Surface component is a component that is used to mark surfaces on slots tagged with this component in a world as specific spots the user can teleport to via the Teleport Locomotion Mode regardless of the CharacterCollider field on a slot's collider.

    Category: Transform/Tagging

    Attach this component to the same slot as a collider to mark that
    collider as a spot a user can specifically teleport to.

    **Related Components**: * Teleport Passthrough
* Teleport Block
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TeleportSurface"

    pass

