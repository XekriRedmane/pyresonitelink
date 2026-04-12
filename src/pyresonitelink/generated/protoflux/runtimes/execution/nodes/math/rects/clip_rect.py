"""Generated component: ClipRect."""

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


class ClipRect(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Clip Rect node takes in 2 rect values, and returns a rect that is inside both of them into one rect.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Rects
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Rects.ClipRect"

    def __init__(self, rect: str | INodeValueOutput[primitives.Rect] | None = None, mask: str | INodeValueOutput[primitives.Rect] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rect: Initial value for Rect.
            mask: Initial value for Mask.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rect is not None:
            self.rect = rect
        if mask is not None:
            self.mask = mask

    @property
    def rect(self) -> str | None:
        """The first rect."""
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
    def mask(self) -> str | None:
        """The second rect, the one that overlaps the first rect."""
        member = self.get_member("Mask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mask.setter
    def mask(self, target: str | INodeValueOutput[primitives.Rect] | None) -> None:
        """Set the Mask reference by target ID or INodeValueOutput[primitives.Rect] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Mask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<Rect>'),
            )

