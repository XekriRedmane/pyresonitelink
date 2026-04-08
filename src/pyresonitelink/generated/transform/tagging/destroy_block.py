"""Generated component: DestroyBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idestroy_block import IDestroyBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyBlock(GeneratedComponent, IDestroyBlock, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DestroyBlock.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyBlock"

    pass

