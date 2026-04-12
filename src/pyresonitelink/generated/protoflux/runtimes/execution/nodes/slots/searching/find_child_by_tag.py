"""Generated component: FindChildByTag."""

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


class FindChildByTag(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Find Child By Tag node finds a child object below the instance (Slot) that matches the given Tag (String).

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots/Searching
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.FindChildByTag"

    def __init__(self, instance: str | INodeObjectOutput[Slot] | None = None, tag: str | INodeObjectOutput[primitives.String] | None = None, search_depth: str | INodeValueOutput[primitives.Int] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            tag: Initial value for Tag.
            search_depth: Initial value for SearchDepth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if tag is not None:
            self.tag = tag
        if search_depth is not None:
            self.search_depth = search_depth

    @property
    def instance(self) -> str | None:
        """The slot to scan for child slots from."""
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
    def tag(self) -> str | None:
        """The tag to look for below Instance (Slot)."""
        member = self.get_member("Tag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tag.setter
    def tag(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Tag reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Tag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def search_depth(self) -> str | None:
        """How far to search for a child with a tag that matches the given Tag (String).

Examples: 0 > Search immediate children. 1 > Search children of slot including those slot's children. -1 > Search infinitely far down (HEAVY)"""
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

