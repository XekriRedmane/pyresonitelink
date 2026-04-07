"""Generated component: RayRectangleIntersection."""

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


class RayRectangleIntersection(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayRectangleIntersection.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 2D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.RayRectangleIntersection"

    def __init__(self, origin: str | INodeValueOutput[primitives.Float2] | None = None, direction: str | INodeValueOutput[primitives.Float2] | None = None, rectangle: str | INodeValueOutput[primitives.Rect] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            origin: Initial value for Origin.
            direction: Initial value for Direction.
            rectangle: Initial value for Rectangle.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if origin is not None:
            self.origin = origin
        if direction is not None:
            self.direction = direction
        if rectangle is not None:
            self.rectangle = rectangle

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
    def rectangle(self) -> str | None:
        """Target ID of the Rectangle reference (targets INodeValueOutput[primitives.Rect])."""
        member = self.get_member("Rectangle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rectangle.setter
    def rectangle(self, target: str | INodeValueOutput[primitives.Rect] | None) -> None:
        """Set the Rectangle reference by target ID or INodeValueOutput[primitives.Rect] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Rectangle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rectangle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<Rect>'),
            )

    @property
    def intersection(self) -> members.EmptyElement | None:
        """The Intersection member."""
        member = self.get_member("Intersection")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection.setter
    def intersection(self, value: members.EmptyElement) -> None:
        """Set the Intersection member."""
        self.set_member("Intersection", value)

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

