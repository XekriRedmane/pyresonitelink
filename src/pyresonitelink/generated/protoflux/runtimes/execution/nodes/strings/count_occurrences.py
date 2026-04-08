"""Generated component: CountOccurrences."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class CountOccurrences(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.CountOccurrences.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.CountOccurrences"

    def __init__(self, str_: str | INodeObjectOutput[primitives.String] | None = None, search: str | INodeObjectOutput[primitives.String] | None = None, comparison_mode: str | INodeValueOutput[StringComparison] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            search: Initial value for Search.
            comparison_mode: Initial value for ComparisonMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_
        if search is not None:
            self.search = search
        if comparison_mode is not None:
            self.comparison_mode = comparison_mode

    @property
    def str_(self) -> str | None:
        """Target ID of the Str reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @str_.setter
    def str_(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Str reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Str",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def search(self) -> str | None:
        """Target ID of the Search reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Search")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search.setter
    def search(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Search reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Search")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Search",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def comparison_mode(self) -> str | None:
        """Target ID of the ComparisonMode reference (targets INodeValueOutput[StringComparison])."""
        member = self.get_member("ComparisonMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @comparison_mode.setter
    def comparison_mode(self, target: str | INodeValueOutput[StringComparison] | None) -> None:
        """Set the ComparisonMode reference by target ID or INodeValueOutput[StringComparison] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ComparisonMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ComparisonMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<StringComparison>'),
            )

