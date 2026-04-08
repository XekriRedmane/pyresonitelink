"""Generated component: RayToLineIntersectionDistance."""

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


class RayToLineIntersectionDistance(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Ray To Line Intersection Distance node determines the distance from a ray origin to the point at which the ray intersects a line segment defined by two points. This node is functionally equivalent to using the ProtoFlux:Ray To Line Intersection node, then plugging the value used for Origin and the Intersection output into a Distancefloat2 node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 2D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayToLineIntersectionDistance"

    def __init__(self, origin: str | INodeValueOutput[primitives.Float2] | None = None, direction: str | INodeValueOutput[primitives.Float2] | None = None, line_point0: str | INodeValueOutput[primitives.Float2] | None = None, line_point1: str | INodeValueOutput[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            origin: Initial value for Origin.
            direction: Initial value for Direction.
            line_point0: Initial value for LinePoint0.
            line_point1: Initial value for LinePoint1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if origin is not None:
            self.origin = origin
        if direction is not None:
            self.direction = direction
        if line_point0 is not None:
            self.line_point0 = line_point0
        if line_point1 is not None:
            self.line_point1 = line_point1

    @property
    def origin(self) -> str | None:
        """Target ID of the Origin reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @origin.setter
    def origin(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the Origin reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Origin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def direction(self) -> str | None:
        """Target ID of the Direction reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction.setter
    def direction(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the Direction reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Direction",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def line_point0(self) -> str | None:
        """Target ID of the LinePoint0 reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("LinePoint0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point0.setter
    def line_point0(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the LinePoint0 reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def line_point1(self) -> str | None:
        """Target ID of the LinePoint1 reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("LinePoint1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point1.setter
    def line_point1(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the LinePoint1 reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def distance(self) -> members.EmptyElement | None:
        """The Distance member."""
        member = self.get_member("Distance")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @distance.setter
    def distance(self, value: members.EmptyElement) -> None:
        """Set the Distance member."""
        self.set_member("Distance", value)

    @property
    def intersects(self) -> members.EmptyElement | None:
        """The Intersects member."""
        member = self.get_member("Intersects")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersects.setter
    def intersects(self, value: members.EmptyElement) -> None:
        """Set the Intersects member."""
        self.set_member("Intersects", value)

