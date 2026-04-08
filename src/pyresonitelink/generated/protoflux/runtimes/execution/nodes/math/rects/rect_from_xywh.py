"""Generated component: RectFromXYWH."""

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


class RectFromXYWH(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectFromXYWH.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rects
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectFromXYWH"

    def __init__(self, x: str | INodeValueOutput[primitives.Float] | None = None, y: str | INodeValueOutput[primitives.Float] | None = None, width: str | INodeValueOutput[primitives.Float] | None = None, height: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            x: Initial value for X.
            y: Initial value for Y.
            width: Initial value for Width.
            height: Initial value for Height.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height

    @property
    def x(self) -> str | None:
        """Target ID of the X reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x.setter
    def x(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the X reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("X")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "X",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def y(self) -> str | None:
        """Target ID of the Y reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y.setter
    def y(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Y reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Y")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Y",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def width(self) -> str | None:
        """Target ID of the Width reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Width")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @width.setter
    def width(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Width reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Width")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Width",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def height(self) -> str | None:
        """Target ID of the Height reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Height")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height.setter
    def height(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Height reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Height")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Height",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

