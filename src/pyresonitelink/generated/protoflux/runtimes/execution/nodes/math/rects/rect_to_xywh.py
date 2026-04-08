"""Generated component: RectToXYWH."""

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


class RectToXYWH(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Rect To XYWH node takes in a rect value and returns the split up information of the X position, Y position, Width of the rect, and height of the rect as a float.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rects
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectToXYWH"

    def __init__(self, rect: str | INodeValueOutput[primitives.Rect] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rect: Initial value for Rect.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rect is not None:
            self.rect = rect

    @property
    def rect(self) -> str | None:
        """Target ID of the Rect reference (targets INodeValueOutput[primitives.Rect])."""
        member = self.get_member("Rect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rect.setter
    def rect(self, target: str | INodeValueOutput[primitives.Rect] | None) -> None:
        """Set the Rect reference by target ID or INodeValueOutput[primitives.Rect] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Rect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<Rect>'),
            )

    @property
    def x(self) -> members.EmptyElement | None:
        """The X member."""
        member = self.get_member("X")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @x.setter
    def x(self, value: members.EmptyElement) -> None:
        """Set the X member."""
        self.set_member("X", value)

    @property
    def y(self) -> members.EmptyElement | None:
        """The Y member."""
        member = self.get_member("Y")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @y.setter
    def y(self, value: members.EmptyElement) -> None:
        """Set the Y member."""
        self.set_member("Y", value)

    @property
    def width(self) -> members.EmptyElement | None:
        """The Width member."""
        member = self.get_member("Width")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @width.setter
    def width(self, value: members.EmptyElement) -> None:
        """Set the Width member."""
        self.set_member("Width", value)

    @property
    def height(self) -> members.EmptyElement | None:
        """The Height member."""
        member = self.get_member("Height")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @height.setter
    def height(self, value: members.EmptyElement) -> None:
        """Set the Height member."""
        self.set_member("Height", value)

