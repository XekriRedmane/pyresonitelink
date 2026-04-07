"""Generated component: IndexOfString."""

import numpy as np

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


class IndexOfString(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.IndexOfString.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Strings
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Strings.IndexOfString"

    def __init__(self, str_: str | INodeObjectOutput[str] | None = None, part: str | INodeObjectOutput[str] | None = None, start_index: str | INodeValueOutput[np.int32] | None = None, search_from_end: str | INodeValueOutput[bool] | None = None, comparison_mode: str | INodeValueOutput[StringComparison] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            str_: Initial value for Str.
            part: Initial value for Part.
            start_index: Initial value for StartIndex.
            search_from_end: Initial value for SearchFromEnd.
            comparison_mode: Initial value for ComparisonMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if str_ is not None:
            self.str_ = str_
        if part is not None:
            self.part = part
        if start_index is not None:
            self.start_index = start_index
        if search_from_end is not None:
            self.search_from_end = search_from_end
        if comparison_mode is not None:
            self.comparison_mode = comparison_mode

    @property
    def str_(self) -> str | None:
        """Target ID of the Str reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Str")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @str_.setter
    def str_(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Str reference by target ID or INodeObjectOutput[str] instance."""
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
    def part(self) -> str | None:
        """Target ID of the Part reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Part")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @part.setter
    def part(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Part reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Part")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Part",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def start_index(self) -> str | None:
        """Target ID of the StartIndex reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("StartIndex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start_index.setter
    def start_index(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the StartIndex reference by target ID or INodeValueOutput[np.int32] instance."""
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
    def search_from_end(self) -> str | None:
        """Target ID of the SearchFromEnd reference (targets INodeValueOutput[bool])."""
        member = self.get_member("SearchFromEnd")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search_from_end.setter
    def search_from_end(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the SearchFromEnd reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SearchFromEnd")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SearchFromEnd",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
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

