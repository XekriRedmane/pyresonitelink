"""Generated component: CreateTransformUndoStep."""

from pyresonitelink.data import members
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


class CreateTransformUndoStep(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateTransformUndoStep.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Undo
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateTransformUndoStep"

    def __init__(self, next: str | INodeOperation | None = None, target: str | INodeObjectOutput[Slot] | None = None, save_parent: str | INodeValueOutput[bool] | None = None, save_position: str | INodeValueOutput[bool] | None = None, save_rotation: str | INodeValueOutput[bool] | None = None, save_scale: str | INodeValueOutput[bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            target: Initial value for Target.
            save_parent: Initial value for SaveParent.
            save_position: Initial value for SavePosition.
            save_rotation: Initial value for SaveRotation.
            save_scale: Initial value for SaveScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if target is not None:
            self.target = target
        if save_parent is not None:
            self.save_parent = save_parent
        if save_position is not None:
            self.save_position = save_position
        if save_rotation is not None:
            self.save_rotation = save_rotation
        if save_scale is not None:
            self.save_scale = save_scale

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
    def target(self) -> str | None:
        """Target ID of the Target reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def save_parent(self) -> str | None:
        """Target ID of the SaveParent reference (targets INodeValueOutput[bool])."""
        member = self.get_member("SaveParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_parent.setter
    def save_parent(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the SaveParent reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SaveParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SaveParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def save_position(self) -> str | None:
        """Target ID of the SavePosition reference (targets INodeValueOutput[bool])."""
        member = self.get_member("SavePosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_position.setter
    def save_position(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the SavePosition reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SavePosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SavePosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def save_rotation(self) -> str | None:
        """Target ID of the SaveRotation reference (targets INodeValueOutput[bool])."""
        member = self.get_member("SaveRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_rotation.setter
    def save_rotation(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the SaveRotation reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SaveRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SaveRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def save_scale(self) -> str | None:
        """Target ID of the SaveScale reference (targets INodeValueOutput[bool])."""
        member = self.get_member("SaveScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @save_scale.setter
    def save_scale(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the SaveScale reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("SaveScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SaveScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

