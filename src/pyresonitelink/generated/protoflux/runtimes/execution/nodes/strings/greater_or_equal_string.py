"""Generated component: GreaterOrEqual_String."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.string_comparison import StringComparison
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GreaterOrEqual_String(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.GreaterOrEqual_String.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.GreaterOrEqual_String"

    def __init__(self, a: str | INodeObjectOutput[str] | None = None, b: str | INodeObjectOutput[str] | None = None, comparison_type: str | INodeValueOutput[StringComparison] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            b: Initial value for B.
            comparison_type: Initial value for ComparisonType.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a
        if b is not None:
            self.b = b
        if comparison_type is not None:
            self.comparison_type = comparison_type

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeObjectOutput[str])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the A reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def b(self) -> str | None:
        """Target ID of the B reference (targets INodeObjectOutput[str])."""
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b.setter
    def b(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the B reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("B")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def comparison_type(self) -> str | None:
        """Target ID of the ComparisonType reference (targets INodeValueOutput[StringComparison])."""
        member = self.get_member("ComparisonType")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @comparison_type.setter
    def comparison_type(self, target: str | INodeValueOutput[StringComparison] | None) -> None:
        """Set the ComparisonType reference by target ID or INodeValueOutput[StringComparison] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ComparisonType")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ComparisonType",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<StringComparison>'),
            )

