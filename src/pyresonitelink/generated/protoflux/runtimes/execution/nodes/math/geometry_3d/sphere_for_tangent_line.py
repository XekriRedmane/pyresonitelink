"""Generated component: SphereForTangentLine."""

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


class SphereForTangentLine(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Sphere For Tangent Line node takes a line point for our sphere point, a line in 3D space, and point for the line, creating a sphere in 3D space. Then it returns the point and radius of a sphere, similar to a reversed Tan node.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.SphereForTangentLine"

    def __init__(self, line_point: str | INodeValueOutput[primitives.Float3] | None = None, line_direction: str | INodeValueOutput[primitives.Float3] | None = None, sphere_center: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            line_point: Initial value for LinePoint.
            line_direction: Initial value for LineDirection.
            sphere_center: Initial value for SphereCenter.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if line_point is not None:
            self.line_point = line_point
        if line_direction is not None:
            self.line_direction = line_direction
        if sphere_center is not None:
            self.sphere_center = sphere_center

    @property
    def line_point(self) -> str | None:
        """The point where the line is."""
        member = self.get_member("LinePoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_point.setter
    def line_point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LinePoint reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LinePoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LinePoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def line_direction(self) -> str | None:
        """The direction of a line provided."""
        member = self.get_member("LineDirection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @line_direction.setter
    def line_direction(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the LineDirection reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LineDirection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LineDirection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def sphere_center(self) -> str | None:
        """The sphere point we want to make (in some distance away from the line)."""
        member = self.get_member("SphereCenter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sphere_center.setter
    def sphere_center(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the SphereCenter reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SphereCenter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SphereCenter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def tangent_point(self) -> members.EmptyElement | None:
        """Returns the tangent point where the line and sphere touch."""
        member = self.get_member("TangentPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @tangent_point.setter
    def tangent_point(self, value: members.EmptyElement) -> None:
        """Set TangentPoint. Returns the tangent point where the line and sphere touch."""
        self.set_member("TangentPoint", value)

    @property
    def radius(self) -> members.EmptyElement | None:
        """Returns the radius of the sphere that is created by this calculation."""
        member = self.get_member("Radius")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @radius.setter
    def radius(self, value: members.EmptyElement) -> None:
        """Set Radius. Returns the radius of the sphere that is created by this calculation."""
        self.set_member("Radius", value)

