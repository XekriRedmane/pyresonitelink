"""Generated component: RemoveAt."""

from typing import Any

TCollection = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RemoveAt(GenericComponent[T], ISyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The RemoveAt node takes in a Collection and the index to remove an element from that list.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections

    Parameterize with a value type::

        RemoveAt[primitives.Float]
        RemoveAt[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.RemoveAt<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.RemoveAt<>"

    def __init__(self, on_removed: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, index_: str | INodeValueOutput[primitives.Int] | None = None, collection: str | INodeObjectOutput[TCollection] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_removed: Initial value for OnRemoved.
            on_fail: Initial value for OnFail.
            index_: Initial value for Index.
            collection: Initial value for Collection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_removed is not None:
            self.on_removed = on_removed
        if on_fail is not None:
            self.on_fail = on_fail
        if index_ is not None:
            self.index_ = index_
        if collection is not None:
            self.collection = collection

    @property
    def on_removed(self) -> str | None:
        """Target ID of the OnRemoved reference (targets INodeOperation)."""
        member = self.get_member("OnRemoved")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_removed.setter
    def on_removed(self, target: str | INodeOperation | None) -> None:
        """Set the OnRemoved reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnRemoved")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnRemoved",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_fail(self) -> str | None:
        """Fires if unable to remove the element from the list or if the index is out of bounds of the collection."""
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_fail.setter
    def on_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def index_(self) -> str | None:
        """The index or position of the element we want to remove from the list. (min: 0, max: Count of collection minus 1)"""
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

    @property
    def collection(self) -> str | None:
        """The collection to remove the element form."""
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

