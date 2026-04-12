"""Generated component: AssetOptimizationBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetOptimizationBlock(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AssetOptimizationBlock component is used to prevent the asset optimization tasks in the game from slots tagged by this component.
Currently according to decompiled code as of 13/10/2024, asset optimization block just prevents materials on the same slot that are the same value wise from being merged.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetOptimizationBlock"

    pass

