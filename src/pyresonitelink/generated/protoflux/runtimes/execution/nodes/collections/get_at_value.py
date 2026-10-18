"""Generated component: GetAtValue."""

from typing import Any

TCollection = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetAtValue(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.GetAtValue<,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.GetAtValue<,>"

    def __init__(self, collection: str | INodeObjectOutput[TCollection] | None = None, index_: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            collection: Initial value for Collection.
            index_: Initial value for Index.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if collection is not None:
            self.collection = collection
        if index_ is not None:
            self.index_ = index_

    @property
    def collection(self) -> str | None:
        """Target ID of the Collection reference (targets INodeObjectOutput[TCollection])."""
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

    @property
    def index_(self) -> str | None:
        """Target ID of the Index reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Index")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @index_.setter
    def index_(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Index reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Index")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Index",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

