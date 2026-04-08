"""Generated component: RaycastOne."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RaycastOne(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """There are a few ways in which the Raycast One node may not work as expected, particularly relating to directions and distances.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics

    There are a few ways in which the Raycast One node may not work as
    expected, particularly relating to directions and distances. Firstly,
    the global scale of the input Root slot is taken into account when
    calculating a raycast's path. For example, assume that the Root slot
    input has global position [0;0;0] and global scale [0.1;0.1;0.1]; if the
    Origin input is [0;0;0], the raycast will start at global [0;0;0],
    however, if the Origin input is [0;1;0] the raycast will start at global
    [0;0.1;0] not global [0;1;0]. Similarly, the input Root slot's global
    scale affects the Direction vector and MaxDistance values too. With the
    same example input Root slot, a Direction of [0;0;1] and a MaxDistance
    of 1 result in a ray which travels only 0.1 units. Secondly, the
    magnitude of the Direction vector affects the distance that the ray
    travels and the reported HitDistance output value. Assuming no input
    Root slot, a Direction input of [0;0;1] and MaxDistance of 1 will
    produce a ray 1 unit long. However, a Direction input of [0;0;2] and
    MaxDistance of 1 will produce a ray 2 units long. Additionally, the
    reported HitDistance value will be halved in the second case.
    ProtoFlux:Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.RaycastOne"

    def __init__(self, origin: str | INodeValueOutput[primitives.Float3] | None = None, direction: str | INodeValueOutput[primitives.Float3] | None = None, max_distance: str | INodeValueOutput[primitives.Float] | None = None, hit_triggers: str | INodeValueOutput[primitives.Bool] | None = None, users_only: str | INodeValueOutput[primitives.Bool] | None = None, debug_duration: str | INodeValueOutput[primitives.Float] | None = None, root: str | INodeObjectOutput[Slot] | None = None, on_hit: str | INodeOperation | None = None, on_miss: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            origin: Initial value for Origin.
            direction: Initial value for Direction.
            max_distance: Initial value for MaxDistance.
            hit_triggers: Initial value for HitTriggers.
            users_only: Initial value for UsersOnly.
            debug_duration: Initial value for DebugDuration.
            root: Initial value for Root.
            on_hit: Initial value for OnHit.
            on_miss: Initial value for OnMiss.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if origin is not None:
            self.origin = origin
        if direction is not None:
            self.direction = direction
        if max_distance is not None:
            self.max_distance = max_distance
        if hit_triggers is not None:
            self.hit_triggers = hit_triggers
        if users_only is not None:
            self.users_only = users_only
        if debug_duration is not None:
            self.debug_duration = debug_duration
        if root is not None:
            self.root = root
        if on_hit is not None:
            self.on_hit = on_hit
        if on_miss is not None:
            self.on_miss = on_miss

    @property
    def origin(self) -> str | None:
        """Target ID of the Origin reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @origin.setter
    def origin(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Origin reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Origin",
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
    def max_distance(self) -> str | None:
        """Target ID of the MaxDistance reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("MaxDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_distance.setter
    def max_distance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MaxDistance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MaxDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaxDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def hit_triggers(self) -> str | None:
        """Target ID of the HitTriggers reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("HitTriggers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hit_triggers.setter
    def hit_triggers(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the HitTriggers reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("HitTriggers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HitTriggers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def users_only(self) -> str | None:
        """Target ID of the UsersOnly reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("UsersOnly")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @users_only.setter
    def users_only(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the UsersOnly reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UsersOnly")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UsersOnly",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def debug_duration(self) -> str | None:
        """Target ID of the DebugDuration reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("DebugDuration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_duration.setter
    def debug_duration(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the DebugDuration reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DebugDuration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DebugDuration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Root reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def on_hit(self) -> str | None:
        """Target ID of the OnHit reference (targets INodeOperation)."""
        member = self.get_member("OnHit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_hit.setter
    def on_hit(self, target: str | INodeOperation | None) -> None:
        """Set the OnHit reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnHit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnHit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_miss(self) -> str | None:
        """Target ID of the OnMiss reference (targets INodeOperation)."""
        member = self.get_member("OnMiss")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_miss.setter
    def on_miss(self, target: str | INodeOperation | None) -> None:
        """Set the OnMiss reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnMiss")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnMiss",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def hit_collider(self) -> members.EmptyElement | None:
        """The HitCollider member."""
        member = self.get_member("HitCollider")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_collider.setter
    def hit_collider(self, value: members.EmptyElement) -> None:
        """Set the HitCollider member."""
        self.set_member("HitCollider", value)

    @property
    def hit_distance(self) -> members.EmptyElement | None:
        """The HitDistance member."""
        member = self.get_member("HitDistance")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_distance.setter
    def hit_distance(self, value: members.EmptyElement) -> None:
        """Set the HitDistance member."""
        self.set_member("HitDistance", value)

    @property
    def hit_point(self) -> members.EmptyElement | None:
        """The HitPoint member."""
        member = self.get_member("HitPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_point.setter
    def hit_point(self, value: members.EmptyElement) -> None:
        """Set the HitPoint member."""
        self.set_member("HitPoint", value)

    @property
    def hit_normal(self) -> members.EmptyElement | None:
        """The HitNormal member."""
        member = self.get_member("HitNormal")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_normal.setter
    def hit_normal(self, value: members.EmptyElement) -> None:
        """Set the HitNormal member."""
        self.set_member("HitNormal", value)

    @property
    def hit_triangle_index(self) -> members.EmptyElement | None:
        """The HitTriangleIndex member."""
        member = self.get_member("HitTriangleIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hit_triangle_index.setter
    def hit_triangle_index(self, value: members.EmptyElement) -> None:
        """Set the HitTriangleIndex member."""
        self.set_member("HitTriangleIndex", value)

