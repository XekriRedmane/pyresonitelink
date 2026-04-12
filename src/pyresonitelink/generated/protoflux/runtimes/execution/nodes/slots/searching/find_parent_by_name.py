"""Generated component: FindParentByName."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FindParentByName(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Finds a parent object above Instance (Slot) that matches the given arguments

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots/Searching
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.FindParentByName"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, name: str | INodeObjectOutput[primitives.String] | None = None, match_substring: str | INodeValueOutput[primitives.Bool] | None = None, ignore_case: str | INodeValueOutput[primitives.Bool] | None = None, search_depth: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            name: Initial value for Name.
            match_substring: Initial value for MatchSubstring.
            ignore_case: Initial value for IgnoreCase.
            search_depth: Initial value for SearchDepth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if name is not None:
            self.name = name
        if match_substring is not None:
            self.match_substring = match_substring
        if ignore_case is not None:
            self.ignore_case = ignore_case
        if search_depth is not None:
            self.search_depth = search_depth

    @property
    def instance(self) -> str | None:
        """The slot to scan for parent slots with."""
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @instance.setter
    def instance(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Instance reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Instance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def name(self) -> str | None:
        """The name to look for above Instance (Slot)."""
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Name reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Name",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def match_substring(self) -> str | None:
        """Whether to search for parents above Instance (Slot) that their name contains Name (String) instead of the entire name being equal."""
        member = self.get_member("MatchSubstring")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @match_substring.setter
    def match_substring(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the MatchSubstring reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MatchSubstring")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MatchSubstring",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def ignore_case(self) -> str | None:
        """Whether the capitalization should matter or not when searching for a parent above Instance (Slot)."""
        member = self.get_member("IgnoreCase")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_case.setter
    def ignore_case(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IgnoreCase reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreCase")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreCase",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def search_depth(self) -> str | None:
        """How far to search for a parent with the provided search arguments

Examples: 0 > Search immediate parent. 1 > Search parent of slot and it's next parent. -1 > Search all the way to Root (CAN BE HEAVY)"""
        member = self.get_member("SearchDepth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @search_depth.setter
    def search_depth(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the SearchDepth reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SearchDepth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SearchDepth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

