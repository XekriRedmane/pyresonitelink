"""Generated component: ValuePlusMinus."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValuePlusMinus(GenericComponent[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators

    Parameterize with a value type::

        ValuePlusMinus[np.float32]
        ValuePlusMinus[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValuePlusMinus<>"

    def __init__(self, value: str | INodeValueOutput[T] | None = None, offset: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            offset: Initial value for Offset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value
        if offset is not None:
            self.offset = offset

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
    def offset(self) -> str | None:
        """Target ID of the Offset reference (targets INodeValueOutput[T])."""
        member = self.get_member("Offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset.setter
    def offset(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Offset reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def plus(self) -> members.EmptyElement | None:
        """The Plus member."""
        member = self.get_member("Plus")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @plus.setter
    def plus(self, value: members.EmptyElement) -> None:
        """Set the Plus member."""
        self.set_member("Plus", value)

    @property
    def minus(self) -> members.EmptyElement | None:
        """The Minus member."""
        member = self.get_member("Minus")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @minus.setter
    def minus(self, value: members.EmptyElement) -> None:
        """Set the Minus member."""
        self.set_member("Minus", value)

