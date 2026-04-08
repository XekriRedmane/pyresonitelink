"""Generated component: AsyncRangeLoopInt."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class AsyncRangeLoopInt(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Async Range Loop Int node is the async analogue to the Range Loop Int node. It is used to perform looping operations by allowing one to define a range of values and step size for iterations to follow. It is a more flexible version of the Async For node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.AsyncRangeLoopInt"

    def __init__(self, start: str | INodeValueOutput[primitives.Int] | None = None, end: str | INodeValueOutput[primitives.Int] | None = None, step_size: str | INodeValueOutput[primitives.Int] | None = None, loop_start: str | INodeOperation | None = None, loop_iteration: str | INodeOperation | None = None, loop_end: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start: Initial value for Start.
            end: Initial value for End.
            step_size: Initial value for StepSize.
            loop_start: Initial value for LoopStart.
            loop_iteration: Initial value for LoopIteration.
            loop_end: Initial value for LoopEnd.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if step_size is not None:
            self.step_size = step_size
        if loop_start is not None:
            self.loop_start = loop_start
        if loop_iteration is not None:
            self.loop_iteration = loop_iteration
        if loop_end is not None:
            self.loop_end = loop_end

    @property
    def start(self) -> str | None:
        """Target ID of the Start reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Start")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @start.setter
    def start(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Start reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Start")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Start",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def end(self) -> str | None:
        """Target ID of the End reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("End")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @end.setter
    def end(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the End reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("End")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "End",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def step_size(self) -> str | None:
        """Target ID of the StepSize reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("StepSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @step_size.setter
    def step_size(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the StepSize reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("StepSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "StepSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
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
    def current(self) -> members.EmptyElement | None:
        """The Current member."""
        member = self.get_member("Current")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @current.setter
    def current(self, value: members.EmptyElement) -> None:
        """Set the Current member."""
        self.set_member("Current", value)

