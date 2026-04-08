"""Generated component: SurrogatePairToUTF32."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SurrogatePairToUTF32(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Surrogate Pair To UTF32 node returns the codepoint (UTF-32 value) generated from the two surrogate characters.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings/Characters
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.Characters.SurrogatePairToUTF32"

    def __init__(self, high_surrogate: str | INodeValueOutput[primitives.Char] | None = None, low_surrogate: str | INodeValueOutput[primitives.Char] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_surrogate: Initial value for HighSurrogate.
            low_surrogate: Initial value for LowSurrogate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_surrogate is not None:
            self.high_surrogate = high_surrogate
        if low_surrogate is not None:
            self.low_surrogate = low_surrogate

    @property
    def high_surrogate(self) -> str | None:
        """Target ID of the HighSurrogate reference (targets INodeValueOutput[primitives.Char])."""
        member = self.get_member("HighSurrogate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @high_surrogate.setter
    def high_surrogate(self, target: str | INodeValueOutput[primitives.Char] | None) -> None:
        """Set the HighSurrogate reference by target ID or INodeValueOutput[primitives.Char] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("HighSurrogate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HighSurrogate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<char>'),
            )

    @property
    def low_surrogate(self) -> str | None:
        """Target ID of the LowSurrogate reference (targets INodeValueOutput[primitives.Char])."""
        member = self.get_member("LowSurrogate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @low_surrogate.setter
    def low_surrogate(self, target: str | INodeValueOutput[primitives.Char] | None) -> None:
        """Set the LowSurrogate reference by target ID or INodeValueOutput[primitives.Char] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LowSurrogate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LowSurrogate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<char>'),
            )

