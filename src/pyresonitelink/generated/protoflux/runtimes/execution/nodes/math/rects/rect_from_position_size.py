"""Generated component: RectFromPositionSize."""

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


class RectFromPositionSize(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Rect From Position Size node takes in 2 specific float2 values, a position of the rect's X and Y position, and the size of the rect with the literal Width and Height, then returns a rect value. In contrast to the Rect From Min Max node where it adds the position and size to get a rect's bounding data.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rects
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectFromPositionSize"

    def __init__(self, position: str | INodeValueOutput[primitives.Float2] | None = None, size: str | INodeValueOutput[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position: Initial value for Position.
            size: Initial value for Size.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position is not None:
            self.position = position
        if size is not None:
            self.size = size

    @property
    def position(self) -> str | None:
        """Target ID of the Position reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the Position reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

    @property
    def size(self) -> str | None:
        """Target ID of the Size reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size.setter
    def size(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the Size reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Size",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

