"""Generated component: ContinuouslyChangingValueRelay."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContinuouslyChangingValueRelay(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Utility

    Parameterize with a value type::

        ContinuouslyChangingValueRelay[primitives.Float]
        ContinuouslyChangingValueRelay[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.ContinuouslyChangingValueRelay<>"

    def __init__(self, input_: str | INodeValueOutput[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            input_: Initial value for Input.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if input_ is not None:
            self.input_ = input_

    @property
    def input_(self) -> str | None:
        """Target ID of the Input reference (targets INodeValueOutput[T])."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the Input reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

