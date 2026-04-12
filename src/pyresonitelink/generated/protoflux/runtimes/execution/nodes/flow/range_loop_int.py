"""Generated component: RangeLoopInt."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RangeLoopInt(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Range Loop Int node is used to perform looping operations by allowing one to define a range of values and step size for iterations to follow. It is a more flexible version of the For node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.RangeLoopInt"

    def __init__(self, start: str | INodeValueOutput[primitives.Int] | None = None, end: str | INodeValueOutput[primitives.Int] | None = None, step_size: str | INodeValueOutput[primitives.Int] | None = None, loop_start: str | ISyncNodeOperation | None = None, loop_iteration: str | ISyncNodeOperation | None = None, loop_end: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
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
        """The number for ``Current`` to start at during execution."""
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
        """The number for ``Current`` to iterate towards and compare to during execution. This input is inclusive."""
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
        """The value that is added or subtracted to ``Current`` per iteration for the current ``LoopIteration``. The loop will either add or subtract this value depending on whether ``Start`` is less than or greater than ``End``. There will be no iterations if this value is less than ``1``."""
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
        """Fires after ``*`` is pulsed and before any iterations are done. Will be pulsed even if ``StepSize < 1``."""
        member = self.get_member("LoopStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_start.setter
    def loop_start(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the LoopStart reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("LoopStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def loop_iteration(self) -> str | None:
        """Fires for each iteration of the loop. This impulse is triggered until ``Current`` exceeds ``End`` in the direction of the loop, at which point the iterations will stop."""
        member = self.get_member("LoopIteration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loop_iteration.setter
    def loop_iteration(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the LoopIteration reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("LoopIteration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoopIteration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def loop_end(self) -> str | None:
        """Fires once the loop has finished."""
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
        """This value will start at ``Start`` for the first iteration, then at each iteration, this value will either increase or decrease by ``StepSize`` depending on whether ``End`` is greater than or less than ``Start``. This value lasts for said iteration's entire context."""
        member = self.get_member("Current")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @current.setter
    def current(self, value: members.EmptyElement) -> None:
        """Set Current. This value will start at ``Start`` for the first iteration, then at each iteration, this value will either increase or decrease by ``StepSize`` depending on whether ``End`` is greater than or less than ``Start``. This value lasts for said iteration's entire context."""
        self.set_member("Current", value)

