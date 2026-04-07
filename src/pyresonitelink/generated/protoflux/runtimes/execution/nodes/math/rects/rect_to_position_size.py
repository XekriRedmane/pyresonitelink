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
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.RectToPositionSize.

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
    def position(self) -> members.EmptyElement | None:
        """The Position member."""
        member = self.get_member("Position")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @position.setter
    def position(self, value: members.EmptyElement) -> None:
        """Set the Position member."""
        self.set_member("Position", value)

    @property
    def size(self) -> members.EmptyElement | None:
        """The Size member."""
        member = self.get_member("Size")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @size.setter
    def size(self, value: members.EmptyElement) -> None:
        """Set the Size member."""
        self.set_member("Size", value)

