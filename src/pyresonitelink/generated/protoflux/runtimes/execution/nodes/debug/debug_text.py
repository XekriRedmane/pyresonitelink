"""Generated component: DebugText."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugText(GeneratedComponent, IMappableNode, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugText.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Debug
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Debugging.DebugText"

    def __init__(self, next: str | INodeOperation | None = None, position: str | INodeValueOutput[primitives.Float3] | None = None, text: str | INodeObjectOutput[str] | None = None, size: str | INodeValueOutput[np.float32] | None = None, color: str | INodeValueOutput[primitives.ColorX] | None = None, duration: str | INodeValueOutput[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            position: Initial value for Position.
            text: Initial value for Text.
            size: Initial value for Size.
            color: Initial value for Color.
            duration: Initial value for Duration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if position is not None:
            self.position = position
        if text is not None:
            self.text = text
        if size is not None:
            self.size = size
        if color is not None:
            self.color = color
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
    def text(self) -> str | None:
        """Target ID of the Text reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Text reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def size(self) -> str | None:
        """Target ID of the Size reference (targets INodeValueOutput[np.float32])."""
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size.setter
    def size(self, target: str | INodeValueOutput[np.float32] | None) -> None:
        """Set the Size reference by target ID or INodeValueOutput[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Size",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def color(self) -> str | None:
        """Target ID of the Color reference (targets INodeValueOutput[primitives.ColorX])."""
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

