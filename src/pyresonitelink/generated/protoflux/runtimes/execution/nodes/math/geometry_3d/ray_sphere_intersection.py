"""Generated component: RaySphereIntersection."""

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


class RaySphereIntersection(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Ray Sphere Intersection node takes in ray paremeters and sphere parameters, and finds then returns an intersection at a point as well as if it intersected at all.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RaySphereIntersection"

    def __init__(self, center: str | INodeValueOutput[primitives.Float3] | None = None, radius: str | INodeValueOutput[primitives.Float] | None = None, ray_origin: str | INodeValueOutput[primitives.Float3] | None = None, ray_direction: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            center: Initial value for Center.
            radius: Initial value for Radius.
            ray_origin: Initial value for RayOrigin.
            ray_direction: Initial value for RayDirection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if center is not None:
            self.center = center
        if radius is not None:
            self.radius = radius
        if ray_origin is not None:
            self.ray_origin = ray_origin
        if ray_direction is not None:
            self.ray_direction = ray_direction

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
    def ray_origin(self) -> str | None:
        """Target ID of the RayOrigin reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("RayOrigin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ray_origin.setter
    def ray_origin(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the RayOrigin reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RayOrigin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RayOrigin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def ray_direction(self) -> str | None:
        """Target ID of the RayDirection reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("RayDirection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ray_direction.setter
    def ray_direction(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the RayDirection reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RayDirection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RayDirection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def point(self) -> members.EmptyElement | None:
        """The Point member."""
        member = self.get_member("Point")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @point.setter
    def point(self, value: members.EmptyElement) -> None:
        """Set the Point member."""
        self.set_member("Point", value)

    @property
    def is_intersecting(self) -> members.EmptyElement | None:
        """The IsIntersecting member."""
        member = self.get_member("IsIntersecting")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_intersecting.setter
    def is_intersecting(self, value: members.EmptyElement) -> None:
        """Set the IsIntersecting member."""
        self.set_member("IsIntersecting", value)

