"""Generated component: DelayUpdatesOrTimeWithObjectSecondsDouble."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelayUpdatesOrTimeWithObjectSecondsDouble(GenericComponent[T], IAsyncNodeOperation, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithObjectSecondsDouble<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Flow/Async

    Parameterize with a value type::

        DelayUpdatesOrTimeWithObjectSecondsDouble[primitives.Float]
        DelayUpdatesOrTimeWithObjectSecondsDouble[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithObjectSecondsDouble<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Async.DelayUpdatesOrTimeWithObjectSecondsDouble<>"

    def __init__(self, next: str | INodeOperation | None = None, on_triggered: str | INodeOperation | None = None, updates: str | INodeValueOutput[primitives.Int] | None = None, value: str | INodeObjectOutput[T] | None = None, duration: str | INodeValueOutput[primitives.Double] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            on_triggered: Initial value for OnTriggered.
            updates: Initial value for Updates.
            value: Initial value for Value.
            duration: Initial value for Duration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if on_triggered is not None:
            self.on_triggered = on_triggered
        if updates is not None:
            self.updates = updates
        if value is not None:
            self.value = value
        if duration is not None:
            self.duration = duration

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
    def on_triggered(self) -> str | None:
        """Target ID of the OnTriggered reference (targets INodeOperation)."""
        member = self.get_member("OnTriggered")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_triggered.setter
    def on_triggered(self, target: str | INodeOperation | None) -> None:
        """Set the OnTriggered reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnTriggered")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnTriggered",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def updates(self) -> str | None:
        """Target ID of the Updates reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Updates")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @updates.setter
    def updates(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Updates reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Updates")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Updates",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeObjectOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeObjectOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeObjectOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<T>'),
            )

    @property
    def delayed_value(self) -> members.EmptyElement | None:
        """The DelayedValue member."""
        member = self.get_member("DelayedValue")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @delayed_value.setter
    def delayed_value(self, value: members.EmptyElement) -> None:
        """Set the DelayedValue member."""
        self.set_member("DelayedValue", value)

    @property
    def duration(self) -> str | None:
        """Target ID of the Duration reference (targets INodeValueOutput[primitives.Double])."""
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @duration.setter
    def duration(self, target: str | INodeValueOutput[primitives.Double] | None) -> None:
        """Set the Duration reference by target ID or INodeValueOutput[primitives.Double] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Duration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<double>'),
            )

