"""Generated component: DelayValue."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_update_receiver import IExecutionUpdateReceiver
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DelayValue(GenericComponent[T], IExecutionUpdateReceiver[T], IMappableNode, IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Delay Value node takes in the amount of seconds and the value, then outputs the value at a later time equal to the provided seconds.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility

    Parameterize with a value type::

        DelayValue[primitives.Float]
        DelayValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Utility.DelayValue<>"

    def __init__(self, delay_seconds: str | INodeValueOutput[primitives.Float] | None = None, value: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            delay_seconds: Initial value for DelaySeconds.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if delay_seconds is not None:
            self.delay_seconds = delay_seconds
        if value is not None:
            self.value = value

    @property
    def delay_seconds(self) -> str | None:
        """Target ID of the DelaySeconds reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("DelaySeconds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delay_seconds.setter
    def delay_seconds(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the DelaySeconds reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DelaySeconds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DelaySeconds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def value(self) -> str | None:
        """Target ID of the Value reference (targets INodeValueOutput[T])."""
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @value.setter
    def value(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Value reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Value")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Value",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
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

