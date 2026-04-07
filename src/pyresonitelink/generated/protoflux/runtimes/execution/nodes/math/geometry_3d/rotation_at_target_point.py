"""Generated component: RotationAtTargetPoint."""

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


class RotationAtTargetPoint(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RotationAtTargetPoint.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RotationAtTargetPoint"

    def __init__(self, pivot: str | INodeValueOutput[primitives.Float3] | None = None, point: str | INodeValueOutput[primitives.Float3] | None = None, direction: str | INodeValueOutput[primitives.Float3] | None = None, target_point: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            pivot: Initial value for Pivot.
            point: Initial value for Point.
            direction: Initial value for Direction.
            target_point: Initial value for TargetPoint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if pivot is not None:
            self.pivot = pivot
        if point is not None:
            self.point = point
        if direction is not None:
            self.direction = direction
        if target_point is not None:
            self.target_point = target_point

    @property
    def pivot(self) -> str | None:
        """Target ID of the Pivot reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Pivot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pivot.setter
    def pivot(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Pivot reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Pivot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pivot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def point(self) -> str | None:
        """Target ID of the Point reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @point.setter
    def point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Point reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Point")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Point",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def direction(self) -> str | None:
        """Target ID of the Direction reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction.setter
    def direction(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Direction reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Direction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def target_point(self) -> str | None:
        """Target ID of the TargetPoint reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("TargetPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_point.setter
    def target_point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the TargetPoint reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("TargetPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

