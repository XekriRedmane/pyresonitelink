"""Generated component: SetParent."""

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


class SetParent(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.SetParent.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.SetParent"

    def __init__(self, next: str | INodeOperation | None = None, instance: str | INodeObjectOutput[Slot] | None = None, new_parent: str | INodeObjectOutput[Slot] | None = None, preserve_global_position: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            instance: Initial value for Instance.
            new_parent: Initial value for NewParent.
            preserve_global_position: Initial value for PreserveGlobalPosition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if instance is not None:
            self.instance = instance
        if new_parent is not None:
            self.new_parent = new_parent
        if preserve_global_position is not None:
            self.preserve_global_position = preserve_global_position

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
    def new_parent(self) -> str | None:
        """Target ID of the NewParent reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("NewParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @new_parent.setter
    def new_parent(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the NewParent reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("NewParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NewParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def preserve_global_position(self) -> str | None:
        """Target ID of the PreserveGlobalPosition reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("PreserveGlobalPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preserve_global_position.setter
    def preserve_global_position(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the PreserveGlobalPosition reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("PreserveGlobalPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PreserveGlobalPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

