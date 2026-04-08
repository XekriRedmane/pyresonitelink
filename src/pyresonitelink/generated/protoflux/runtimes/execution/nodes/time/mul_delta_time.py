"""Generated component: MulDeltaTime."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MulDeltaTime(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.MulDeltaTime<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Time

    Parameterize with a value type::

        MulDeltaTime[primitives.Float]
        MulDeltaTime[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.MulDeltaTime<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Operators.MulDeltaTime<>"

    def __init__(self, a: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            a: Initial value for A.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if a is not None:
            self.a = a

    @property
    def a(self) -> str | None:
        """Target ID of the A reference (targets INodeValueOutput[T])."""
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a.setter
    def a(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the A reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("A")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

