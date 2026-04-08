"""Generated component: ObjectRoot."""

from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectRoot(GeneratedComponent, IObjectRoot, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ObjectRoot.

    Category: Transform
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectRoot"

    pass

    async def remove_children_object_roots(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the RemoveChildrenObjectRoots sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveChildrenObjectRoots", {}, debug,
        )

