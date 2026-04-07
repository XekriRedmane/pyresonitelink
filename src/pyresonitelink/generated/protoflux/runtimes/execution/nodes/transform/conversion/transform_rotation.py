"""Generated component: TransformRotation."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TransformRotation(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.TransformRotation.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Conversion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.TransformRotation"

    def __init__(self, from_space: str | INodeObjectOutput[Slot] | None = None, to_space: str | INodeObjectOutput[Slot] | None = None, source_rotation: str | INodeValueOutput[primitives.FloatQ] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            from_space: Initial value for FromSpace.
            to_space: Initial value for ToSpace.
            source_rotation: Initial value for SourceRotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if from_space is not None:
            self.from_space = from_space
        if to_space is not None:
            self.to_space = to_space
        if source_rotation is not None:
            self.source_rotation = source_rotation

    @property
    def from_space(self) -> str | None:
        """Target ID of the FromSpace reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("FromSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @from_space.setter
    def from_space(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the FromSpace reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FromSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FromSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def to_space(self) -> str | None:
        """Target ID of the ToSpace reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("ToSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @to_space.setter
    def to_space(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the ToSpace reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("ToSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ToSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def source_rotation(self) -> str | None:
        """Target ID of the SourceRotation reference (targets INodeValueOutput[primitives.FloatQ])."""
        member = self.get_member("SourceRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_rotation.setter
    def source_rotation(self, target: str | INodeValueOutput[primitives.FloatQ] | None) -> None:
        """Set the SourceRotation reference by target ID or INodeValueOutput[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SourceRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<floatQ>'),
            )

