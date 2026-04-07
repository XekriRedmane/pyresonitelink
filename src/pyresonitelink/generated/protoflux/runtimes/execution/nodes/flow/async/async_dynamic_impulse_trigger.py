"""Generated component: AsyncDynamicImpulseTrigger."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AsyncDynamicImpulseTrigger(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTrigger.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Actions.AsyncDynamicImpulseTrigger"

    def __init__(self, next: str | INodeOperation | None = None, tag: str | INodeObjectOutput[str] | None = None, target_hierarchy: str | INodeObjectOutput[Slot] | None = None, exclude_disabled: str | INodeValueOutput[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            tag: Initial value for Tag.
            target_hierarchy: Initial value for TargetHierarchy.
            exclude_disabled: Initial value for ExcludeDisabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if tag is not None:
            self.tag = tag
        if target_hierarchy is not None:
            self.target_hierarchy = target_hierarchy
        if exclude_disabled is not None:
            self.exclude_disabled = exclude_disabled

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def tag(self) -> str | None:
        """Target ID of the Tag reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Tag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tag.setter
    def tag(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Tag reference by target ID or INodeObjectOutput[str] instance."""
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
    def target_hierarchy(self) -> str | None:
        """Target ID of the TargetHierarchy reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("TargetHierarchy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_hierarchy.setter
    def target_hierarchy(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the TargetHierarchy reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("TargetHierarchy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetHierarchy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def exclude_disabled(self) -> str | None:
        """Target ID of the ExcludeDisabled reference (targets INodeValueOutput[bool])."""
        member = self.get_member("ExcludeDisabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exclude_disabled.setter
    def exclude_disabled(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the ExcludeDisabled reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ExcludeDisabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ExcludeDisabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def triggered_count(self) -> members.EmptyElement | None:
        """The TriggeredCount member."""
        member = self.get_member("TriggeredCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @triggered_count.setter
    def triggered_count(self, value: members.EmptyElement) -> None:
        """Set the TriggeredCount member."""
        self.set_member("TriggeredCount", value)

