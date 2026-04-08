"""Generated component: ValueReciprocal."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueReciprocal(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueReciprocal<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators

    Parameterize with a value type::

        ValueReciprocal[primitives.Float]
        ValueReciprocal[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueReciprocal<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueReciprocal<>"

    def __init__(self, n: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            n: Initial value for N.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if n is not None:
            self.n = n

    @property
    def n(self) -> str | None:
        """Target ID of the N reference (targets INodeValueOutput[T])."""
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @n.setter
    def n(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the N reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("N")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "N",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

