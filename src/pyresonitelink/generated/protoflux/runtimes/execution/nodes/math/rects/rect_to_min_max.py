"""Generated component: RectToMinMax."""

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


class RectToMinMax(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Rect To Min Max node takes in a rect value and returns 2 specific float2 values, showing the minimum size of the rect, usually just at the X and Y position, and also returning the max size of this rect, which is usually X + Width and Y + Height. In contrast to the Rect To Position Size node where it takes the literal position and size to get a rect's bounding data.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rects
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectToMinMax"

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
    def min(self) -> members.EmptyElement | None:
        """The Min member."""
        member = self.get_member("Min")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @min.setter
    def min(self, value: members.EmptyElement) -> None:
        """Set the Min member."""
        self.set_member("Min", value)

    @property
    def max(self) -> members.EmptyElement | None:
        """The Max member."""
        member = self.get_member("Max")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @max.setter
    def max(self, value: members.EmptyElement) -> None:
        """Set the Max member."""
        self.set_member("Max", value)

