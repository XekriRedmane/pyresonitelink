"""Generated component: DebugVector."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugVector(GeneratedComponent, IMappableNode, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The DebugVector component shows a vector using a thin line.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Debug
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugVector"

    def __init__(self, next: str | INodeOperation | None = None, position: str | INodeValueOutput[primitives.Float3] | None = None, vector: str | INodeValueOutput[primitives.Float3] | None = None, color: str | INodeValueOutput[primitives.ColorX] | None = None, radius_ratio: str | INodeValueOutput[primitives.Float] | None = None, duration: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            position: Initial value for Position.
            vector: Initial value for Vector.
            color: Initial value for Color.
            radius_ratio: Initial value for RadiusRatio.
            duration: Initial value for Duration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if position is not None:
            self.position = position
        if vector is not None:
            self.vector = vector
        if color is not None:
            self.color = color
        if radius_ratio is not None:
            self.radius_ratio = radius_ratio
        if duration is not None:
            self.duration = duration

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def position(self) -> str | None:
        """Target ID of the Position reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Position reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def vector(self) -> str | None:
        """the vector to debug."""
        member = self.get_member("Vector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @vector.setter
    def vector(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the Vector reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Vector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Vector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

    @property
    def color(self) -> str | None:
        """The color of the debug vector line."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the Color reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def radius_ratio(self) -> str | None:
        """Target ID of the RadiusRatio reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("RadiusRatio")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @radius_ratio.setter
    def radius_ratio(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the RadiusRatio reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RadiusRatio")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RadiusRatio",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def duration(self) -> str | None:
        """Target ID of the Duration reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @duration.setter
    def duration(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Duration reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Duration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

