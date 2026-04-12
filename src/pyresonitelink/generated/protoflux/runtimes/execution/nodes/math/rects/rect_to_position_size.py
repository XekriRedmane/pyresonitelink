"""Generated component: RectToPositionSize."""

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


class RectToPositionSize(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Rect To Position Size node takes in a rect value and returns 2 specific float2 values giving a position of the rect's ``X`` and ``Y`` position, and giving the size of the rect with the literal ``Width`` and ``Height``. In contrast to the Rect To Min Max node where it adds the position and size to get a rect's bounding data.

If you need to split a rect into specific and separated outputs, use the Rect To XYWH node instead.|suggestion}}

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rects
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectToPositionSize"

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
        """The rect value."""
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
    def position(self) -> members.EmptyElement | None:
        """Returns the ``X`` and ``Y`` position of this rect."""
        member = self.get_member("Position")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @position.setter
    def position(self, value: members.EmptyElement) -> None:
        """Set Position. Returns the ``X`` and ``Y`` position of this rect."""
        self.set_member("Position", value)

    @property
    def size(self) -> members.EmptyElement | None:
        """Returns the literal ``Width`` and ``Height`` size of this rect."""
        member = self.get_member("Size")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @size.setter
    def size(self, value: members.EmptyElement) -> None:
        """Set Size. Returns the literal ``Width`` and ``Height`` size of this rect."""
        self.set_member("Size", value)

