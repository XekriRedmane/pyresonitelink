"""Generated component: ValueClamp."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueClamp(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math

    Parameterize with a value type::

        ValueClamp[primitives.Float]
        ValueClamp[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueClamp<>"

    def __init__(self, value: str | INodeValueOutput[T] | None = None, min: str | INodeValueOutput[T] | None = None, max: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            min: Initial value for Min.
            max: Initial value for Max.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max

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
    def min(self) -> str | None:
        """Target ID of the Min reference (targets INodeValueOutput[T])."""
        member = self.get_member("Min")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min.setter
    def min(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Min reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Min")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Min",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def max(self) -> str | None:
        """Target ID of the Max reference (targets INodeValueOutput[T])."""
        member = self.get_member("Max")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max.setter
    def max(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Max reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Max")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Max",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

