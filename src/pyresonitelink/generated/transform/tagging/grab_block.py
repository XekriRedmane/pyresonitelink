"""Generated component: GrabBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_block import IGrabBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabBlock(GeneratedComponent, IGrabBlock, IWorldEventReceiver):
    """Used to prevent grabbing a Slot from a certain Collider or set of colliders. Place between a collider and a Grabbable component and the slot will no longer be able to be grabbed via that collider.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabBlock"

    pass

