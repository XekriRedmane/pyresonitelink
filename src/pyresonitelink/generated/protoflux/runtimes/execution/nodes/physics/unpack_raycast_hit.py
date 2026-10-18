"""Generated component: UnpackRaycastHit."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.raycast_hit import RaycastHit
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnpackRaycastHit(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Unpack Raycast Hit node takes in a RaycastHit and gives the separate components of that hit. One source of this data is RaycastAll.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.UnpackRaycastHit"

    def __init__(self, hit: str | INodeObjectOutput[RaycastHit] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hit: Initial value for Hit.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hit is not None:
            self.hit = hit

    @property
    def hit(self) -> str | None:
        """The hit to be separated."""
        member = self.get_member("Hit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hit.setter
    def hit(self, target: str | INodeObjectOutput[RaycastHit] | None) -> None:
        """Set the Hit reference by target ID or INodeObjectOutput[RaycastHit] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("Hit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Hit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.RaycastHit>'),
            )

    @property
    def hit_collider(self) -> members.EmptyElement | None:
        """The valid hit collider."""
        member = self.get_member("HitCollider")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_collider.setter
    def hit_collider(self, value: members.EmptyElement) -> None:
        """Set HitCollider. The valid hit collider."""
        self.set_member("HitCollider", value)

    @property
    def hit_distance(self) -> members.EmptyElement | None:
        """The distance from the Origin to the hit point in global coordinate space."""
        member = self.get_member("HitDistance")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_distance.setter
    def hit_distance(self, value: members.EmptyElement) -> None:
        """Set HitDistance. The distance from the Origin to the hit point in global coordinate space."""
        self.set_member("HitDistance", value)

    @property
    def hit_point(self) -> members.EmptyElement | None:
        """The global position at which the ray hit the collider."""
        member = self.get_member("HitPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_point.setter
    def hit_point(self, value: members.EmptyElement) -> None:
        """Set HitPoint. The global position at which the ray hit the collider."""
        self.set_member("HitPoint", value)

    @property
    def hit_normal(self) -> members.EmptyElement | None:
        """The facing normal direction of the hit collider at the hit point."""
        member = self.get_member("HitNormal")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_normal.setter
    def hit_normal(self, value: members.EmptyElement) -> None:
        """Set HitNormal. The facing normal direction of the hit collider at the hit point."""
        self.set_member("HitNormal", value)

    @property
    def hit_triangle_index(self) -> members.EmptyElement | None:
        """The triangle index on the mesh corresponding to the hit collider. This value is 0 unless the HitCollider is a MeshCollider."""
        member = self.get_member("HitTriangleIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_triangle_index.setter
    def hit_triangle_index(self, value: members.EmptyElement) -> None:
        """Set HitTriangleIndex. The triangle index on the mesh corresponding to the hit collider. This value is 0 unless the HitCollider is a MeshCollider."""
        self.set_member("HitTriangleIndex", value)

