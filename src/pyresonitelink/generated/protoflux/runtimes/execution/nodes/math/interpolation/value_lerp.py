"""Generated component: ValueLerp."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueLerp(GenericComponent[T], INodeValueOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Interpolation

    Parameterize with a value type::

        ValueLerp[np.float32]
        ValueLerp[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.ValueLerp<>"

    def __init__(self, from_: str | INodeValueOutput[T] | None = None, to: str | INodeValueOutput[T] | None = None, lerp: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            from_: Initial value for From.
            to: Initial value for To.
            lerp: Initial value for Lerp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if from_ is not None:
            self.from_ = from_
        if to is not None:
            self.to = to
        if lerp is not None:
            self.lerp = lerp

    @property
    def from_(self) -> str | None:
        """Target ID of the From reference (targets INodeValueOutput[T])."""
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @from_.setter
    def from_(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the From reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "From",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def to(self) -> str | None:
        """Target ID of the To reference (targets INodeValueOutput[T])."""
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @to.setter
    def to(self, target: str | INodeValueOutput[T] | None) -> None:
        """Set the To reference by target ID or INodeValueOutput[T] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "To",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>'),
            )

    @property
    def lerp(self) -> str | None:
        """Target ID of the Lerp reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lerp.setter
    def lerp(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Lerp reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Lerp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

