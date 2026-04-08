"""Generated component: ClosestPointOnLine."""

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


class ClosestPointOnLine(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Closest Point On Line node takes in the line parameters (2 points in 3D space), and a provided point to check. Then it returns the point that it is closest to on the line, based on the defined parameters.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointOnLine"

    def __init__(self, line_point0: str | INodeValueOutput[primitives.Float3] | None = None, line_point1: str | INodeValueOutput[primitives.Float3] | None = None, point: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            line_point0: Initial value for LinePoint0.
            line_point1: Initial value for LinePoint1.
            point: Initial value for Point.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if line_point0 is not None:
            self.line_point0 = line_point0
        if line_point1 is not None:
            self.line_point1 = line_point1
        if point is not None:
            self.point = point

    @property
    def line_point0(self) -> str | None:
        """Target ID of the LinePoint0 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("LinePoint0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point0.setter
    def line_point0(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LinePoint0 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def line_point1(self) -> str | None:
        """Target ID of the LinePoint1 reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("LinePoint1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point1.setter
    def line_point1(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LinePoint1 reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint1",
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

