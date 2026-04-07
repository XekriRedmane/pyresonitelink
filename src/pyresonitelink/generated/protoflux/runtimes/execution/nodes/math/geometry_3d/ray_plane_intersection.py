"""Generated component: RayPlaneIntersection."""

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


class RayPlaneIntersection(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RayPlaneIntersection.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.RayPlaneIntersection"

    def __init__(self, ray_origin: str | INodeValueOutput[primitives.Float3] | None = None, ray_direction: str | INodeValueOutput[primitives.Float3] | None = None, plane_point: str | INodeValueOutput[primitives.Float3] | None = None, plane_normal: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ray_origin: Initial value for RayOrigin.
            ray_direction: Initial value for RayDirection.
            plane_point: Initial value for PlanePoint.
            plane_normal: Initial value for PlaneNormal.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ray_origin is not None:
            self.ray_origin = ray_origin
        if ray_direction is not None:
            self.ray_direction = ray_direction
        if plane_point is not None:
            self.plane_point = plane_point
        if plane_normal is not None:
            self.plane_normal = plane_normal

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
    def plane_point(self) -> str | None:
        """Target ID of the PlanePoint reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("PlanePoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @plane_point.setter
    def plane_point(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the PlanePoint reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("PlanePoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PlanePoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def plane_normal(self) -> str | None:
        """Target ID of the PlaneNormal reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("PlaneNormal")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @plane_normal.setter
    def plane_normal(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the PlaneNormal reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("PlaneNormal")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PlaneNormal",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

