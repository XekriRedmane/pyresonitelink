"""Generated component: ValueOneMinus."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueOneMinus(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Operators

    Parameterize with a value type::

        ValueOneMinus[primitives.Float]
        ValueOneMinus[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Operators.ValueOneMinus<>"

    def __init__(self, x: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            x: Initial value for X.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if x is not None:
            self.x = x

    @property
    def x(self) -> str | None:
        """Target ID of the X reference (targets INodeValueOutput[T])."""
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x.setter
    def x(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the X reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "X",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

