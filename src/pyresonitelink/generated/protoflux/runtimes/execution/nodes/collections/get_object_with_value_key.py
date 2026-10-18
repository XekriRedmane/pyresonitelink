"""Generated component: GetObjectWithValueKey."""

from typing import Any

TDictionary = Any
TKey = Any
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


class GetObjectWithValueKey(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.GetObjectWithValueKey<,,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.GetObjectWithValueKey<,,>"

    def __init__(self, dictionary: str | INodeObjectOutput[TDictionary] | None = None, key: str | INodeValueOutput[TKey] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dictionary: Initial value for Dictionary.
            key: Initial value for Key.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dictionary is not None:
            self.dictionary = dictionary
        if key is not None:
            self.key = key

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

