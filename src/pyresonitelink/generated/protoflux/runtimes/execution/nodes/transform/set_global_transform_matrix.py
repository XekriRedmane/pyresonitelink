"""Generated component: SetGlobalTransformMatrix."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetGlobalTransformMatrix(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.SetGlobalTransformMatrix.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Transform
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Transform.SetGlobalTransformMatrix"

    def __init__(self, next: str | INodeOperation | None = None, instance: str | INodeObjectOutput[Slot] | None = None, matrix: str | INodeValueOutput[primitives.Float4x4] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            instance: Initial value for Instance.
            matrix: Initial value for Matrix.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if instance is not None:
            self.instance = instance
        if matrix is not None:
            self.matrix = matrix

    @property
    def next(self) -> str | None:
        """Target ID of the Next reference (targets INodeOperation)."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def instance(self) -> str | None:
        """Target ID of the Instance reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @instance.setter
    def instance(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Instance reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Instance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def matrix(self) -> str | None:
        """Target ID of the Matrix reference (targets INodeValueOutput[primitives.Float4x4])."""
        member = self.get_member("Matrix")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @matrix.setter
    def matrix(self, target: str | INodeValueOutput[primitives.Float4x4] | None) -> None:
        """Set the Matrix reference by target ID or INodeValueOutput[primitives.Float4x4] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Matrix")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Matrix",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float4x4>'),
            )

