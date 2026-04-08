"""Generated component: ReplaceFirstSubstring."""

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


class ReplaceFirstSubstring(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.ReplaceFirstSubstring.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.ReplaceFirstSubstring"

    def __init__(self, str_: str | INodeObjectOutput[primitives.String] | None = None, search_for: str | INodeObjectOutput[primitives.String] | None = None, replace_with: str | INodeObjectOutput[primitives.String] | None = None, start_index: str | INodeValueOutput[primitives.Int] | None = None, comparison_mode: str | INodeValueOutput[StringComparison] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            search_for: Initial value for SearchFor.
            replace_with: Initial value for ReplaceWith.
            start_index: Initial value for StartIndex.
            comparison_mode: Initial value for ComparisonMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_
        if search_for is not None:
            self.search_for = search_for
        if replace_with is not None:
            self.replace_with = replace_with
        if start_index is not None:
            self.start_index = start_index
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
    def search_for(self) -> str | None:
        """Target ID of the SearchFor reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("SearchFor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search_for.setter
    def search_for(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the SearchFor reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("SearchFor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SearchFor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def replace_with(self) -> str | None:
        """Target ID of the ReplaceWith reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("ReplaceWith")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @replace_with.setter
    def replace_with(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the ReplaceWith reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("ReplaceWith")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReplaceWith",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def start_index(self) -> str | None:
        """Target ID of the StartIndex reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("StartIndex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start_index.setter
    def start_index(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the StartIndex reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("StartIndex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StartIndex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
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

