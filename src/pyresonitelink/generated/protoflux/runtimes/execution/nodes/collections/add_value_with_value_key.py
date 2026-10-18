"""Generated component: AddValueWithValueKey."""

from typing import Any

TDictionary = Any
TKey = Any
TValue = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AddValueWithValueKey(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.AddValueWithValueKey<,,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.AddValueWithValueKey<,,>"

    def __init__(self, dictionary: str | INodeObjectOutput[TDictionary] | None = None, key: str | INodeValueOutput[TKey] | None = None, value: str | INodeValueOutput[TValue] | None = None, on_added: str | INodeOperation | None = None, on_already_exists: str | INodeOperation | None = None, on_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dictionary: Initial value for Dictionary.
            key: Initial value for Key.
            value: Initial value for Value.
            on_added: Initial value for OnAdded.
            on_already_exists: Initial value for OnAlreadyExists.
            on_fail: Initial value for OnFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dictionary is not None:
            self.dictionary = dictionary
        if key is not None:
            self.key = key
        if value is not None:
            self.value = value
        if on_added is not None:
            self.on_added = on_added
        if on_already_exists is not None:
            self.on_already_exists = on_already_exists
        if on_fail is not None:
            self.on_fail = on_fail

    @property
    def dictionary(self) -> str | None:
        """Target ID of the Dictionary reference (targets INodeObjectOutput[TDictionary])."""
        member = self.get_member("Dictionary")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dictionary.setter
    def dictionary(self, target: str | INodeObjectOutput[TDictionary] | None) -> None:
        """Set the Dictionary reference by target ID or INodeObjectOutput[TDictionary] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Dictionary")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dictionary",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<TDictionary>'),
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
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[TValue])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[TValue] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[TValue] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<TValue>'),
            )

    @property
    def on_added(self) -> str | None:
        """Target ID of the OnAdded reference (targets INodeOperation)."""
        member = self.get_member("OnAdded")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_added.setter
    def on_added(self, target: str | INodeOperation | None) -> None:
        """Set the OnAdded reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnAdded")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnAdded",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_already_exists(self) -> str | None:
        """Target ID of the OnAlreadyExists reference (targets INodeOperation)."""
        member = self.get_member("OnAlreadyExists")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_already_exists.setter
    def on_already_exists(self, target: str | INodeOperation | None) -> None:
        """Set the OnAlreadyExists reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnAlreadyExists")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnAlreadyExists",
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

