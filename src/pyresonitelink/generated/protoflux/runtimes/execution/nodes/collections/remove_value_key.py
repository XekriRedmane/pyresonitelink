"""Generated component: RemoveValueKey."""

from typing import Any

TDictionary = Any
TKey = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RemoveValueKey(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.RemoveValueKey<,,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.RemoveValueKey<,,>"

    def __init__(self, on_removed: str | INodeOperation | None = None, on_does_not_exist: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, key: str | INodeValueOutput[TKey] | None = None, collection: str | INodeObjectOutput[TDictionary] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_removed: Initial value for OnRemoved.
            on_does_not_exist: Initial value for OnDoesNotExist.
            on_fail: Initial value for OnFail.
            key: Initial value for Key.
            collection: Initial value for Collection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_removed is not None:
            self.on_removed = on_removed
        if on_does_not_exist is not None:
            self.on_does_not_exist = on_does_not_exist
        if on_fail is not None:
            self.on_fail = on_fail
        if key is not None:
            self.key = key
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
    def on_does_not_exist(self) -> str | None:
        """Target ID of the OnDoesNotExist reference (targets INodeOperation)."""
        member = self.get_member("OnDoesNotExist")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_does_not_exist.setter
    def on_does_not_exist(self, target: str | INodeOperation | None) -> None:
        """Set the OnDoesNotExist reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnDoesNotExist")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDoesNotExist",
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
    def key(self) -> str | None:
        """Target ID of the Key reference (targets INodeValueOutput[TKey])."""
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @key.setter
    def key(self, target: str | INodeValueOutput[TKey] | None) -> None:
        """Set the Key reference by target ID or INodeValueOutput[TKey] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Key",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<TKey>'),
            )

    @property
    def collection(self) -> str | None:
        """Target ID of the Collection reference (targets INodeObjectOutput[TDictionary])."""
        member = self.get_member("Collection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collection.setter
    def collection(self, target: str | INodeObjectOutput[TDictionary] | None) -> None:
        """Set the Collection reference by target ID or INodeObjectOutput[TDictionary] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Collection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Collection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<TDictionary>'),
            )

