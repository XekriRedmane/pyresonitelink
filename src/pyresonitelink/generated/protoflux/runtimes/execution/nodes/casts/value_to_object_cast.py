"""Generated component: ValueToObjectCast."""

from typing import Any

I = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.icast import ICast
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueToObjectCast(GenericComponent[T], ICast, INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.ValueToObjectCast<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Casts

    Parameterize with a value type::

        ValueToObjectCast[primitives.Float]
        ValueToObjectCast[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.ValueToObjectCast<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Casts.ValueToObjectCast<>"

    def __init__(self, input_: str | INodeValueOutput[I] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Input reference (targets INodeValueOutput[I])."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | INodeValueOutput[I] | None) -> None:
        """Set the Input reference by target ID or INodeValueOutput[I] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<I>'),
            )

