"""Generated component: DebugAxes."""

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


class DebugAxes(GeneratedComponent, IMappableNode, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Debug Axes is a ProtoFlux node that when called will make a 3 arrows visual similar to a Gizmo at the global coordinates with the arrows having the length provided and will appear for a duration in seconds. The visual will appear under the Root of a world. In most cases, the debug visuals will be drawn over most materials, letting you see them easily.

See also: Coordinate spaces

    Category: ProtoFlux/Runtimes/Execution/Nodes/Debug
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugAxes"

    def __init__(self, next: str | INodeOperation | None = None, position: str | INodeValueOutput[primitives.Float3] | None = None, rotation: str | INodeValueOutput[primitives.FloatQ] | None = None, length: str | INodeValueOutput[primitives.Float] | None = None, right_color: str | INodeValueOutput[primitives.ColorX] | None = None, up_color: str | INodeValueOutput[primitives.ColorX] | None = None, forward_color: str | INodeValueOutput[primitives.ColorX] | None = None, duration: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            position: Initial value for Position.
            rotation: Initial value for Rotation.
            length: Initial value for Length.
            right_color: Initial value for RightColor.
            up_color: Initial value for UpColor.
            forward_color: Initial value for ForwardColor.
            duration: Initial value for Duration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if length is not None:
            self.length = length
        if right_color is not None:
            self.right_color = right_color
        if up_color is not None:
            self.up_color = up_color
        if forward_color is not None:
            self.forward_color = forward_color
        if duration is not None:
            self.duration = duration

    @property
    def next(self) -> str | None:
        """Fires after * (Call) is impulsed and the gizmo was created successfully."""
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
        """The position in global space for the debug visual. Default at the node."""
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
    def rotation(self) -> str | None:
        """The Rotation in global space for the debug visual. Default at the node."""
        member = self.get_member("Rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | INodeValueOutput[primitives.FloatQ] | None) -> None:
        """Set the Rotation reference by target ID or INodeValueOutput[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>'),
            )

    @property
    def length(self) -> str | None:
        """The length of the arrows for the debug visual in meters."""
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @length.setter
    def length(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Length reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Length",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def right_color(self) -> str | None:
        """The color for the debug axes in the (1,0,0) direction. Also known as the red arrow on a Gizmo. Defaults to red."""
        member = self.get_member("RightColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_color.setter
    def right_color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the RightColor reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RightColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RightColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def up_color(self) -> str | None:
        """The color for the debug axes in the (0,1,0) direction. Also known as the green arrow on a Gizmo. Defaults to green."""
        member = self.get_member("UpColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @up_color.setter
    def up_color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the UpColor reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UpColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UpColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def forward_color(self) -> str | None:
        """The color for the debug axes in the (0,0,1) direction. Also known as the blue arrow on a Gizmo. Defaults to blue."""
        member = self.get_member("ForwardColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @forward_color.setter
    def forward_color(self, target: str | INodeValueOutput[primitives.ColorX] | None) -> None:
        """Set the ForwardColor reference by target ID or INodeValueOutput[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ForwardColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ForwardColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<colorX>'),
            )

    @property
    def duration(self) -> str | None:
        """How long the debug axes visual appears for in seconds."""
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

