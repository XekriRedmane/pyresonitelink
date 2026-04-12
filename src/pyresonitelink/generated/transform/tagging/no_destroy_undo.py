"""Generated component: NoDestroyUndo."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NoDestroyUndo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The NoDestroyUndo component prevents an Undo step from being created when destroying the slot that the component is attached to.

    Category: Transform/Tagging

    Attach to the root slot that will be destroyed. this will prevent the
    slot from being brought back through undoing after it is destroyed.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.NoDestroyUndo"

    pass

