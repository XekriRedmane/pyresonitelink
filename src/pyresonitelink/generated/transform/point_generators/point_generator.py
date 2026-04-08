"""Generated component: PointGenerator."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointGenerator(GeneratedComponent, IPointGenerator, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PointGenerator.

    Category: Transform/Point Generators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointGenerator"

    pass

