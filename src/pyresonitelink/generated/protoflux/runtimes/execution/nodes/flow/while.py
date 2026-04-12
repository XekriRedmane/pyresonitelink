"""Generated component: While."""

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


class While(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The While node is used to perform looping operations by allowing one to fire impulses continuously while a condition remains true.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow

    **Known Issues**: * As of the time of writing, there is a known issue where if the final node in the ``LoopIteration`` chain is a Write node, said node modifies a variable used for conditional evaluation, and the value to write is based off said variable, the write will be using a previously cached value. This can cause an extra loop iteration to occur, which is very annoying to debug.
** The easiest way to work around this bug is to add a "dummy" node after the write, such as an Impulse Display or, if debugging a ton of impulses and lag is undesirable, an empty Write node.
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.While"

    def __init__(self, condition: str | INodeValueOutput[primitives.Bool] | None = None, loop_start: str | ISyncNodeOperation | None = None, loop_iteration: str | ISyncNodeOperation | None = None, loop_end: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            condition: Initial value for Condition.
            loop_start: Initial value for LoopStart.
            loop_iteration: Initial value for LoopIteration.
            loop_end: Initial value for LoopEnd.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if condition is not None:
            self.condition = condition
        if loop_start is not None:
            self.loop_start = loop_start
        if loop_iteration is not None:
            self.loop_iteration = loop_iteration
        if loop_end is not None:
            self.loop_end = loop_end

    @property
    def condition(self) -> str | None:
        """Condition that the loop will check to determine if it should iterate again or not. If ``True``, it will iterate again."""
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @condition.setter
    def condition(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the Condition reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Condition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Condition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def loop_start(self) -> str | None:
        """Fires after ``*`` is pulsed and before any iterations are performed. Will be pulsed even if ``Condition`` is ``False`` at the time of the loop beginning."""
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
        """Will be pulsed for as long ``Condition`` is ``True``. Only after the context of the current loop iteration is finished will the next iteration fire."""
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
        """Fires after ``Condition`` turns ``False``, continuing the impulse chain from before."""
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

