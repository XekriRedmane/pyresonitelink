"""Generated component: CreateTypeFieldUndoStep."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.sync_type import SyncType
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CreateTypeFieldUndoStep(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Create Type Field Undo Step will create an undo step in the Context Menu of the person who the impulse came from. The node will then send to the UndoManager component in the world the value that the field provided into Target should revert to. Or in more simpler terms, the current value the provided Target (Type Field) contains is what it will be reset to when undone via the context menu.

when this node is paired with an Undo Batch, it's description if has one, will be ignored, and will be part of the Undo Batch's undo step instead.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Undo
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Undo.CreateTypeFieldUndoStep"

    def __init__(self, next: str | INodeOperation | None = None, target: str | INodeObjectOutput[SyncType] | None = None, force_new: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            target: Initial value for Target.
            force_new: Initial value for ForceNew.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if target is not None:
            self.target = target
        if force_new is not None:
            self.force_new = force_new

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
        """The Type Field to undo for this undo step."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[SyncType] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[SyncType] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.SyncType>'),
            )

    @property
    def force_new(self) -> str | None:
        """Target ID of the ForceNew reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ForceNew")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @force_new.setter
    def force_new(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ForceNew reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ForceNew")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ForceNew",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

