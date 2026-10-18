"""Generated component: RaycastAll."""

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


class RaycastAll(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Raycast All node performs a multi raycast check when an impulse is received and gives a Collection of hits. The input parameters determine from where, in what direction, and how far the ray should be cast as well as determining which colliders are valid hits. When a raycast detects a valid collider, it returns data pertaining to that hit and fires from the OnHit continuation output. If there is no valid hit, whether there were no colliders hit or the ones hit were not valid targets, the OnMiss continuation output fires.

The data output is a Collection that contains a list of every hit along it's trajectory. The result can be decoded(after something like ForEach) using UnpackRaycastHit.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.RaycastAll"

    def __init__(self, origin: str | INodeValueOutput[primitives.Float3] | None = None, direction: str | INodeValueOutput[primitives.Float3] | None = None, max_distance: str | INodeValueOutput[primitives.Float] | None = None, hit_triggers: str | INodeValueOutput[primitives.Bool] | None = None, debug_duration: str | INodeValueOutput[primitives.Float] | None = None, root: str | INodeObjectOutput[Slot] | None = None, on_hit: str | INodeOperation | None = None, on_miss: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            origin: Initial value for Origin.
            direction: Initial value for Direction.
            max_distance: Initial value for MaxDistance.
            hit_triggers: Initial value for HitTriggers.
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
        """The starting position from which the ray is cast. Default is [0;0;0]."""
        member = self.get_member("Origin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @origin.setter
    def origin(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Origin reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """The direction in which the ray is cast. Default is [0;0;0] which results in no ray being cast. (Use for example [0;0;1] for directly forward.)"""
        member = self.get_member("Direction")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @direction.setter
    def direction(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Direction reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """The maximum distance the raycast should travel from its origin. Default is the maximum float value which is extremely high."""
        member = self.get_member("MaxDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_distance.setter
    def max_distance(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the MaxDistance reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """Determines whether colliders with the Trigger, StaticTrigger or StaticTriggerAuto ColliderType value are valid hit targets. Default is False."""
        member = self.get_member("HitTriggers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hit_triggers.setter
    def hit_triggers(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the HitTriggers reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("HitTriggers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HitTriggers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def debug_duration(self) -> str | None:
        """Determines the duration in seconds that a debug visual will be shown after each raycast. Default is -1 which disables the debug visual. When enabled, the visual shows a yellow line indicating the full path of the raycast along with the hit point (red spheres) and hit normal direction (blue arrows)."""
        member = self.get_member("DebugDuration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_duration.setter
    def debug_duration(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the DebugDuration reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """The slot in whose coordinate space the Origin, Direction and MaxDistance values should be evaluated. Default is the world root slot, i.e. the values are treated as being in the global coordinate space."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Root reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """Fires an impulse if any valid hits were found when performing a raycast."""
        member = self.get_member("OnHit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_hit.setter
    def on_hit(self, target: str | INodeOperation | None) -> None:
        """Set the OnHit reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
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
        """Fires an impulse in any situation where no valid hits is not found when performing a raycast."""
        member = self.get_member("OnMiss")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_miss.setter
    def on_miss(self, target: str | INodeOperation | None) -> None:
        """Set the OnMiss reference by target ID or INodeOperation instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("OnMiss")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnMiss",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def hits(self) -> members.EmptyElement | None:
        """A List of every collider that the ray has hit."""
        member = self.get_member("Hits")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hits.setter
    def hits(self, value: members.EmptyElement) -> None:
        """Set Hits. A List of every collider that the ray has hit."""
        self.set_member("Hits", value)

