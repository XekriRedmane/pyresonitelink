"""Generated component: AsyncFor."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AsyncFor(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncFor.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncFor"

    def __init__(self, count: str | INodeValueOutput[np.int32] | None = None, reverse: str | INodeValueOutput[bool] | None = None, loop_start: str | INodeOperation | None = None, loop_iteration: str | INodeOperation | None = None, loop_end: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            count: Initial value for Count.
            reverse: Initial value for Reverse.
            loop_start: Initial value for LoopStart.
            loop_iteration: Initial value for LoopIteration.
            loop_end: Initial value for LoopEnd.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if count is not None:
            self.count = count
        if reverse is not None:
            self.reverse = reverse
        if loop_start is not None:
            self.loop_start = loop_start
        if loop_iteration is not None:
            self.loop_iteration = loop_iteration
        if loop_end is not None:
            self.loop_end = loop_end

    @property
    def count(self) -> str | None:
        """Target ID of the Count reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("Count")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @count.setter
    def count(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the Count reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Count")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Count",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def reverse(self) -> str | None:
        """Target ID of the Reverse reference (targets INodeValueOutput[bool])."""
        member = self.get_member("Reverse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reverse.setter
    def reverse(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the Reverse reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Reverse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reverse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def loop_start(self) -> str | None:
        """Target ID of the LoopStart reference (targets INodeOperation)."""
        member = self.get_member("LoopStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_start.setter
    def loop_start(self, target: str | INodeOperation | None) -> None:
        """Set the LoopStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("LoopStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def loop_iteration(self) -> str | None:
        """Target ID of the LoopIteration reference (targets INodeOperation)."""
        member = self.get_member("LoopIteration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_iteration.setter
    def loop_iteration(self, target: str | INodeOperation | None) -> None:
        """Set the LoopIteration reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("LoopIteration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopIteration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def loop_end(self) -> str | None:
        """Target ID of the LoopEnd reference (targets INodeOperation)."""
        member = self.get_member("LoopEnd")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_end.setter
    def loop_end(self, target: str | INodeOperation | None) -> None:
        """Set the LoopEnd reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("LoopEnd")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopEnd",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def iteration(self) -> members.EmptyElement | None:
        """The Iteration member."""
        member = self.get_member("Iteration")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @iteration.setter
    def iteration(self, value: members.EmptyElement) -> None:
        """Set the Iteration member."""
        self.set_member("Iteration", value)

