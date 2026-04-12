"""Generated component: DuplicateBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iduplicate_block import IDuplicateBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DuplicateBlock(GeneratedComponent, IDuplicateBlock, IWorldEventReceiver):
    """The Duplicate Block component blocks duplication of a Grabbable slot tagged with this component by using the Context menu, but not via the Scene Inspector or ProtoFlux.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DuplicateBlock"

    pass

