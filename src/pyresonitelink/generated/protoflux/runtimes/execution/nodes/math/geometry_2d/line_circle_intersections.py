"""Generated component: LineCircleIntersections."""

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


class LineCircleIntersections(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Line Circle Intersections node determines how many times a line defined by two points intersects a circle and where said intersections occur.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 2D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.LineCircleIntersections"

    def __init__(self, center_: str | INodeValueOutput[primitives.Float2] | None = None, radius: str | INodeValueOutput[primitives.Float] | None = None, line_point0: str | INodeValueOutput[primitives.Float2] | None = None, line_point1: str | INodeValueOutput[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            center_: Initial value for Center.
            radius: Initial value for Radius.
            line_point0: Initial value for LinePoint0.
            line_point1: Initial value for LinePoint1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if center_ is not None:
            self.center_ = center_
        if radius is not None:
            self.radius = radius
        if line_point0 is not None:
            self.line_point0 = line_point0
        if line_point1 is not None:
            self.line_point1 = line_point1

    @property
    def center_(self) -> str | None:
        """Center of the circle."""
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @center_.setter
    def center_(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the Center reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Center",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def radius(self) -> str | None:
        """Radius of the circle."""
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @radius.setter
    def radius(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Radius reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Radius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def line_point0(self) -> str | None:
        """First point of the line."""
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
        """Second point of the line."""
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
    def intersection_count(self) -> members.EmptyElement | None:
        """The amount of intersections of the defined line and circle. This is at most two."""
        member = self.get_member("IntersectionCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection_count.setter
    def intersection_count(self, value: members.EmptyElement) -> None:
        """Set IntersectionCount. The amount of intersections of the defined line and circle. This is at most two."""
        self.set_member("IntersectionCount", value)

    @property
    def intersection0(self) -> members.EmptyElement | None:
        """The first point of intersection between the line and circle. This is the point that occurs "later" in the intersection when tracing the line from ``LinePoint0`` to ``LinePoint1``. If there does not exist any intersection, this value is ``[NaN; NaN]``."""
        member = self.get_member("Intersection0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection0.setter
    def intersection0(self, value: members.EmptyElement) -> None:
        """Set Intersection0. The first point of intersection between the line and circle. This is the point that occurs "later" in the intersection when tracing the line from ``LinePoint0`` to ``LinePoint1``. If there does not exist any intersection, this value is ``[NaN; NaN]``."""
        self.set_member("Intersection0", value)

    @property
    def intersection1(self) -> members.EmptyElement | None:
        """The second point of intersection between the line and circle. This is the point that occurs "earlier" in the intersection when tracing the line from ``LinePoint0`` to ``LinePoint1``. If there are fewer than two intersections, this value is ``[NaN; NaN]``."""
        member = self.get_member("Intersection1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection1.setter
    def intersection1(self, value: members.EmptyElement) -> None:
        """Set Intersection1. The second point of intersection between the line and circle. This is the point that occurs "earlier" in the intersection when tracing the line from ``LinePoint0`` to ``LinePoint1``. If there are fewer than two intersections, this value is ``[NaN; NaN]``."""
        self.set_member("Intersection1", value)

