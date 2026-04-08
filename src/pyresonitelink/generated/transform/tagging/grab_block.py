"""Generated component: GrabBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_block import IGrabBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabBlock(GeneratedComponent, IGrabBlock, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabBlock.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabBlock"

    pass

