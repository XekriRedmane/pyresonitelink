"""Generated component: DestroyRoot."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idestroy_root import IDestroyRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DestroyRoot(GeneratedComponent, IDestroyRoot, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DestroyRoot.

    Category: Transform/Tagging
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DestroyRoot"

    pass

