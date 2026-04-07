"""Generated component: VectorDeltaAngle_Float2."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VectorDeltaAngle_Float2(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.VectorDeltaAngle_Float2.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Vectors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.VectorDeltaAngle_Float2"

    def __init__(self, from_: str | INodeValueOutput[primitives.Float2] | None = None, to: str | INodeValueOutput[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            from_: Initial value for From.
            to: Initial value for To.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if from_ is not None:
            self.from_ = from_
        if to is not None:
            self.to = to

    @property
    def from_(self) -> str | None:
        """Target ID of the From reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @from_.setter
    def from_(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the From reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "From",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def to(self) -> str | None:
        """Target ID of the To reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @to.setter
    def to(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the To reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "To",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

