"""Generated component: CubicLerp_Double3."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.tangent_point_double3 import TangentPointDouble3
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CubicLerp_Double3(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.CubicLerp_Double3.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Interpolation
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.CubicLerp_Double3"

    def __init__(self, from_: str | INodeValueOutput[TangentPointDouble3] | None = None, to: str | INodeValueOutput[TangentPointDouble3] | None = None, lerp: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the From reference (targets INodeValueOutput[TangentPointDouble3])."""
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @from_.setter
    def from_(self, target: str | INodeValueOutput[TangentPointDouble3] | None) -> None:
        """Set the From reference by target ID or INodeValueOutput[TangentPointDouble3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("From")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "From",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[ProtoFlux.Nodes.Core]ProtoFlux.Runtimes.Execution.Nodes.Math.TangentPointDouble3>'),
            )

    @property
    def to(self) -> str | None:
        """Target ID of the To reference (targets INodeValueOutput[TangentPointDouble3])."""
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @to.setter
    def to(self, target: str | INodeValueOutput[TangentPointDouble3] | None) -> None:
        """Set the To reference by target ID or INodeValueOutput[TangentPointDouble3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("To")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "To",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[ProtoFlux.Nodes.Core]ProtoFlux.Runtimes.Execution.Nodes.Math.TangentPointDouble3>'),
            )

    @property
    def lerp(self) -> str | None:
        """Target ID of the Lerp reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lerp.setter
    def lerp(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Lerp reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Lerp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

