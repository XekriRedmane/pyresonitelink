"""Generated component: ClosestPointOnConeSurface."""

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


class ClosestPointOnConeSurface(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Closest Point On Cone Surface node takes in the cone parameters (size and rotation) and a provided point to check. Then it returns the closest point on that cone's surface and if that point is within that cone's defined parameters.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.ClosestPointOnConeSurface"

    def __init__(self, cone_center: str | INodeValueOutput[primitives.Float3] | None = None, cone_orientation: str | INodeValueOutput[primitives.FloatQ] | None = None, cone_height: str | INodeValueOutput[primitives.Float] | None = None, cone_base_radius: str | INodeValueOutput[primitives.Float] | None = None, point: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            cone_center: Initial value for ConeCenter.
            cone_orientation: Initial value for ConeOrientation.
            cone_height: Initial value for ConeHeight.
            cone_base_radius: Initial value for ConeBaseRadius.
            point: Initial value for Point.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if cone_center is not None:
            self.cone_center = cone_center
        if cone_orientation is not None:
            self.cone_orientation = cone_orientation
        if cone_height is not None:
            self.cone_height = cone_height
        if cone_base_radius is not None:
            self.cone_base_radius = cone_base_radius
        if point is not None:
            self.point = point

    @property
    def cone_center(self) -> str | None:
        """The center of the cone (located at the center of the base of the cone)."""
        member = self.get_member("ConeCenter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cone_center.setter
    def cone_center(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the ConeCenter reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ConeCenter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConeCenter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def cone_orientation(self) -> str | None:
        """The rotation of the cone."""
        member = self.get_member("ConeOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cone_orientation.setter
    def cone_orientation(self, target: str | INodeValueOutput[primitives.FloatQ] | None) -> None:
        """Set the ConeOrientation reference by target ID or INodeValueOutput[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ConeOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConeOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>'),
            )

    @property
    def cone_height(self) -> str | None:
        """The height of the cone."""
        member = self.get_member("ConeHeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cone_height.setter
    def cone_height(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the ConeHeight reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ConeHeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConeHeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def cone_base_radius(self) -> str | None:
        """The size of the cone base's circle radius."""
        member = self.get_member("ConeBaseRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cone_base_radius.setter
    def cone_base_radius(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the ConeBaseRadius reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ConeBaseRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConeBaseRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def point(self) -> str | None:
        """The point we are checking."""
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
    def closest_point(self) -> members.EmptyElement | None:
        """Returns the point in the cone's surface compared with the point given."""
        member = self.get_member("ClosestPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @closest_point.setter
    def closest_point(self, value: members.EmptyElement) -> None:
        """Set ClosestPoint. Returns the point in the cone's surface compared with the point given."""
        self.set_member("ClosestPoint", value)

    @property
    def is_point_inside(self) -> members.EmptyElement | None:
        """Returns if the point is within this cone."""
        member = self.get_member("IsPointInside")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_point_inside.setter
    def is_point_inside(self, value: members.EmptyElement) -> None:
        """Set IsPointInside. Returns if the point is within this cone."""
        self.set_member("IsPointInside", value)

