"""Generated component: TransformVector."""

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


class TransformVector(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """ContinuouslyChanging nodes

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform/Conversion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.TransformVector"

    def __init__(self, from_space: str | INodeObjectOutput[Slot] | None = None, to_space: str | INodeObjectOutput[Slot] | None = None, source_vector: str | INodeValueOutput[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            from_space: Initial value for FromSpace.
            to_space: Initial value for ToSpace.
            source_vector: Initial value for SourceVector.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if from_space is not None:
            self.from_space = from_space
        if to_space is not None:
            self.to_space = to_space
        if source_vector is not None:
            self.source_vector = source_vector

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
    def source_vector(self) -> str | None:
        """Target ID of the SourceVector reference (targets INodeValueOutput[primitives.Float3])."""
        member = self.get_member("SourceVector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_vector.setter
    def source_vector(self, target: str | INodeValueOutput[primitives.Float3] | None) -> None:
        """Set the SourceVector reference by target ID or INodeValueOutput[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SourceVector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceVector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float3>'),
            )

