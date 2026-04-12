"""Generated component: DestroyBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idestroy_block import IDestroyBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyBlock(GeneratedComponent, IDestroyBlock, IWorldEventReceiver):
    """The Destroy Block component blocks destroying a Slot tagged by this component via the Context Menu. Does not block destroying via Scene Inspector or ProtoFlux.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyBlock"

    pass

