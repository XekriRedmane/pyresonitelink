"""Generated component: UnpackValueKeyValueValuePair."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.key_value_pair import KeyValuePair
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnpackValueKeyValueValuePair(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.UnpackValueKeyValueValuePair<,>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Collections
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Collections.UnpackValueKeyValueValuePair<,>"

    def __init__(self, pair: str | INodeValueOutput[KeyValuePair] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pair: Initial value for Pair.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pair is not None:
            self.pair = pair

    @property
    def pair(self) -> str | None:
        """Target ID of the Pair reference (targets INodeValueOutput[KeyValuePair])."""
        member = self.get_member("Pair")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pair.setter
    def pair(self, target: str | INodeValueOutput[KeyValuePair] | None) -> None:
        """Set the Pair reference by target ID or INodeValueOutput[KeyValuePair] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Pair")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pair",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<KeyValuePair<,>>'),
            )

    @property
    def key(self) -> members.EmptyElement | None:
        """The Key member."""
        member = self.get_member("Key")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @key.setter
    def key(self, value: members.EmptyElement) -> None:
        """Set the Key member."""
        self.set_member("Key", value)

    @property
    def value(self) -> members.EmptyElement | None:
        """The Value member."""
        member = self.get_member("Value")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @value.setter
    def value(self, value: members.EmptyElement) -> None:
        """Set the Value member."""
        self.set_member("Value", value)

