"""Generated component: ValueConditional."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueConditional(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConditional<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators

    Parameterize with a value type::

        ValueConditional[primitives.Float]
        ValueConditional[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConditional<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ValueConditional<>"

    def __init__(self, on_true: str | INodeValueOutput[T] | None = None, on_false: str | INodeValueOutput[T] | None = None, condition: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_true: Initial value for OnTrue.
            on_false: Initial value for OnFalse.
            condition: Initial value for Condition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_true is not None:
            self.on_true = on_true
        if on_false is not None:
            self.on_false = on_false
        if condition is not None:
            self.condition = condition

    @property
    def on_true(self) -> str | None:
        """Target ID of the OnTrue reference (targets INodeValueOutput[T])."""
        member = self.get_member("OnTrue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_true.setter
    def on_true(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the OnTrue reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnTrue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnTrue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def on_false(self) -> str | None:
        """Target ID of the OnFalse reference (targets INodeValueOutput[T])."""
        member = self.get_member("OnFalse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_false.setter
    def on_false(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the OnFalse reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnFalse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFalse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def condition(self) -> str | None:
        """Target ID of the Condition reference (targets INodeValueOutput[primitives.Bool])."""
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

