"""Generated component: DebugAxes."""

import numpy as np

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
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugAxes.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Debug
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugAxes"

    def __init__(self, next: str | INodeOperation | None = None, position: str | INodeValueOutput[primitives.Float3] | None = None, rotation: str | INodeValueOutput[primitives.FloatQ] | None = None, length: str | INodeValueOutput[np.float32] | None = None, right_color: str | INodeValueOutput[primitives.ColorX] | None = None, up_color: str | INodeValueOutput[primitives.ColorX] | None = None, forward_color: str | INodeValueOutput[primitives.ColorX] | None = None, duration: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
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
    def rotation(self) -> str | None:
        """Target ID of the Rotation reference (targets INodeValueOutput[primitives.FloatQ])."""
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
        """Target ID of the Length reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Length")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @length.setter
    def length(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Length reference by target ID or INodeValueOutput[np.float32] instance."""
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
        """Target ID of the RightColor reference (targets INodeValueOutput[primitives.ColorX])."""
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
        """Target ID of the UpColor reference (targets INodeValueOutput[primitives.ColorX])."""
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
        """Target ID of the ForwardColor reference (targets INodeValueOutput[primitives.ColorX])."""
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
        """Target ID of the Duration reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @duration.setter
    def duration(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Duration reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Duration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Duration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

