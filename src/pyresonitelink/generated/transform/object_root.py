"""Generated component: ObjectRoot."""

from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ObjectRoot(GeneratedComponent, IObjectRoot, ICustomInspector, IWorldEventReceiver):
    """The ObjectRoot component marks a slot as the root of an object, where an object is the slot itself plus all of its child slots, recursively.

    Category: Transform

    Setting a slot as the ObjectRoot helps the Scene Inspector's "up to
    object root" button find the root of the object.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ObjectRoot"

    pass

    async def remove_children_object_roots(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """will recursively delete any ObjectRoot components from this slot's children.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveChildrenObjectRoots", {}, debug,
        )

