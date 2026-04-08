"""Generated component: TransformBounds."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TransformBounds(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Transform Bounds node transforms the input bounding box from the local coordinate space of the SourceSpace slot to that of the TargetSpace slot.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Bounds
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Bounds.TransformBounds"

    def __init__(self, bounds: str | INodeValueOutput[primitives.BoundingBox] | None = None, source_space: str | INodeObjectOutput[Slot] | None = None, target_space: str | INodeObjectOutput[Slot] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bounds: Initial value for Bounds.
            source_space: Initial value for SourceSpace.
            target_space: Initial value for TargetSpace.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bounds is not None:
            self.bounds = bounds
        if source_space is not None:
            self.source_space = source_space
        if target_space is not None:
            self.target_space = target_space

    @property
    def bounds(self) -> str | None:
        """Target ID of the Bounds reference (targets INodeValueOutput[primitives.BoundingBox])."""
        member = self.get_member("Bounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounds.setter
    def bounds(self, target: str | INodeValueOutput[primitives.BoundingBox] | None) -> None:
        """Set the Bounds reference by target ID or INodeValueOutput[primitives.BoundingBox] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Bounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Bounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<BoundingBox>'),
            )

    @property
    def source_space(self) -> str | None:
        """Target ID of the SourceSpace reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("SourceSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_space.setter
    def source_space(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the SourceSpace reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("SourceSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def target_space(self) -> str | None:
        """Target ID of the TargetSpace reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("TargetSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_space.setter
    def target_space(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the TargetSpace reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("TargetSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

