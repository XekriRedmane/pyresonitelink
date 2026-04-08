"""Generated component: DistanceFromSphericalSector."""

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


class DistanceFromSphericalSector(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Distance From Spherical Sector node takes a point in 3D space and computes the distance from a spherical sector defined by its center, direction, radius, and angle. Then it returns the distance from that sphere.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.DistanceFromSphericalSector"

    def __init__(self, center: str | INodeValueOutput[primitives.Float3] | None = None, direction: str | INodeValueOutput[primitives.Float3] | None = None, radius: str | INodeValueOutput[primitives.Float] | None = None, angle: str | INodeValueOutput[primitives.Float] | None = None, point: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            center: Initial value for Center.
            direction: Initial value for Direction.
            radius: Initial value for Radius.
            angle: Initial value for Angle.
            point: Initial value for Point.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if center is not None:
            self.center = center
        if direction is not None:
            self.direction = direction
        if radius is not None:
            self.radius = radius
        if angle is not None:
            self.angle = angle
        if point is not None:
            self.point = point

    @property
    def center(self) -> str | None:
        """Target ID of the Center reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @center.setter
    def center(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Center reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Center",
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
    def radius(self) -> str | None:
        """Target ID of the Radius reference (targets INodeValueOutput[primitives.Float])."""
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
    def angle(self) -> str | None:
        """Target ID of the Angle reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Angle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @angle.setter
    def angle(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Angle reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Angle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Angle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
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

