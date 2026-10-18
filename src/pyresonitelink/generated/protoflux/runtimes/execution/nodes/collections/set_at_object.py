"""Generated component: SetAtObject."""

from typing import Any

TCollection = Any
TValue = Any
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetAtObject(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.SetAtObject<,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.SetAtObject<,>"

    def __init__(self, on_set: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, element: str | INodeObjectOutput[TValue] | None = None, index_: str | INodeValueOutput[primitives.Int] | None = None, collection: str | INodeObjectOutput[TCollection] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_set: Initial value for OnSet.
            on_fail: Initial value for OnFail.
            element: Initial value for Element.
            index_: Initial value for Index.
            collection: Initial value for Collection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_set is not None:
            self.on_set = on_set
        if on_fail is not None:
            self.on_fail = on_fail
        if element is not None:
            self.element = element
        if index_ is not None:
            self.index_ = index_
        if collection is not None:
            self.collection = collection

    @property
    def on_set(self) -> str | None:
        """Target ID of the OnSet reference (targets INodeOperation)."""
        member = self.get_member("OnSet")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_set.setter
    def on_set(self, target: str | INodeOperation | None) -> None:
        """Set the OnSet reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnSet")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSet",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_fail(self) -> str | None:
        """Target ID of the OnFail reference (targets INodeOperation)."""
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
    def element(self) -> str | None:
        """Target ID of the Element reference (targets INodeObjectOutput[TValue])."""
        member = self.get_member("Element")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @element.setter
    def element(self, target: str | INodeObjectOutput[TValue] | None) -> None:
        """Set the Element reference by target ID or INodeObjectOutput[TValue] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Element")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Element",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<TValue>'),
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

