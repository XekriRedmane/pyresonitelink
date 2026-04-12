"""Generated component: PointGenerator."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ipoint_generator import IPointGenerator
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PointGenerator(GeneratedComponent, IPointGenerator, IWorldEventReceiver):
    """Generates points only at a single point which is the position of the slot this component is on.

    Category: Transform/Point Generators

    Used in a Common Spawn Area to define in what kind of spawn area shape
    users should initially spawn into. In this case, it spawns them at the
    exact location of the component's slot.

    **Related Components**: * CommonSpawnArea
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PointGenerator"

    pass

