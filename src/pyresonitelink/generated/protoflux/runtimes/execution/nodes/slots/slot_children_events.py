"""Generated component: SlotChildrenEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SlotChildrenEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Slot Children events is a ProtoFlux node that monitors a given Instance (Slot). It then sends impulses for OnChildAdded (Call) and OnChildRemoved (Call) when children are added or removed. When an event trigger happens, Child (Slot) is available for reading during the impulse.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Slots
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Slots.SlotChildrenEvents"

    def __init__(self, instance: str | IGlobalValueProxy[Slot] | None = None, on_user: str | INodeObjectOutput[User] | None = None, on_child_added: str | ISyncNodeOperation | None = None, on_child_removed: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            instance: Initial value for Instance.
            on_user: Initial value for OnUser.
            on_child_added: Initial value for OnChildAdded.
            on_child_removed: Initial value for OnChildRemoved.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if instance is not None:
            self.instance = instance
        if on_user is not None:
            self.on_user = on_user
        if on_child_added is not None:
            self.on_child_added = on_child_added
        if on_child_removed is not None:
            self.on_child_removed = on_child_removed

    @property
    def instance(self) -> str | None:
        """Target ID of the Instance reference (targets IGlobalValueProxy[Slot])."""
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @instance.setter
    def instance(self, target: str | IGlobalValueProxy[Slot] | None) -> None:
        """Set the Instance reference by target ID or IGlobalValueProxy[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Instance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Instance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def on_user(self) -> str | None:
        """Target ID of the OnUser reference (targets INodeObjectOutput[User])."""
        member = self.get_member("OnUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_user.setter
    def on_user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the OnUser reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def on_child_added(self) -> str | None:
        """Target ID of the OnChildAdded reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnChildAdded")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_child_added.setter
    def on_child_added(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnChildAdded reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnChildAdded")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnChildAdded",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def on_child_removed(self) -> str | None:
        """Target ID of the OnChildRemoved reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnChildRemoved")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_child_removed.setter
    def on_child_removed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnChildRemoved reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnChildRemoved")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnChildRemoved",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def child(self) -> members.EmptyElement | None:
        """The Child member."""
        member = self.get_member("Child")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @child.setter
    def child(self, value: members.EmptyElement) -> None:
        """Set the Child member."""
        self.set_member("Child", value)

