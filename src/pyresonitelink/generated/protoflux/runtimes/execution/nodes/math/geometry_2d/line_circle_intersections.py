"""Generated component: LineCircleIntersections."""

import numpy as np

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
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.LineCircleIntersections.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 2D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry2D.LineCircleIntersections"

    def __init__(self, center: str | INodeValueOutput[primitives.Float2] | None = None, radius: str | INodeValueOutput[np.float32] | None = None, line_point0: str | INodeValueOutput[primitives.Float2] | None = None, line_point1: str | INodeValueOutput[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            center: Initial value for Center.
            radius: Initial value for Radius.
            line_point0: Initial value for LinePoint0.
            line_point1: Initial value for LinePoint1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if center is not None:
            self.center = center
        if radius is not None:
            self.radius = radius
        if line_point0 is not None:
            self.line_point0 = line_point0
        if line_point1 is not None:
            self.line_point1 = line_point1

    @property
    def center(self) -> str | None:
        """Target ID of the Center reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @center.setter
    def center(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
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
        """Target ID of the Radius reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Radius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @radius.setter
    def radius(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Radius reference by target ID or INodeValueOutput[np.float32] instance."""
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
    def intersection_count(self) -> members.EmptyElement | None:
        """The IntersectionCount member."""
        member = self.get_member("IntersectionCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection_count.setter
    def intersection_count(self, value: members.EmptyElement) -> None:
        """Set the IntersectionCount member."""
        self.set_member("IntersectionCount", value)

    @property
    def intersection0(self) -> members.EmptyElement | None:
        """The Intersection0 member."""
        member = self.get_member("Intersection0")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection0.setter
    def intersection0(self, value: members.EmptyElement) -> None:
        """Set the Intersection0 member."""
        self.set_member("Intersection0", value)

    @property
    def intersection1(self) -> members.EmptyElement | None:
        """The Intersection1 member."""
        member = self.get_member("Intersection1")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @intersection1.setter
    def intersection1(self, value: members.EmptyElement) -> None:
        """Set the Intersection1 member."""
        self.set_member("Intersection1", value)

