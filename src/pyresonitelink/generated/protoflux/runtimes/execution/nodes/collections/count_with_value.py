"""Generated component: CountWithValue."""

from typing import Any

TCollection = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CountWithValue(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Count node takes in a Collection and returns the number of elements (list/array) or number of KeyValuePairs (dictionary).

Since lists and arrays are zero indexed in Resonite, the last element in the list/array is at count minus 1.

Known compatible types: any collection.

Known incompatible types: none.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.Count<,>"

    def __init__(self, collection: str | INodeObjectOutput[TCollection] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            collection: Initial value for Collection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if collection is not None:
            self.collection = collection

    @property
    def collection(self) -> str | None:
        """The collection to count from."""
        member = self.get_member("Collection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collection.setter
    def collection(self, target: str | INodeObjectOutput[TCollection] | None) -> None:
        """Set the Collection reference by target ID or INodeObjectOutput[TCollection] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Collection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Collection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<TCollection>'),
            )

