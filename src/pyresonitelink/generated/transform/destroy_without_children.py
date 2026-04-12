"""Generated component: DestroyWithoutChildren."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyWithoutChildren(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DestroyWithoutChildren component is used to make a slot self-destruct when it has no children.

    Category: Transform
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyWithoutChildren"

    pass

