"""Generated component: EquipAvatar."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EquipAvatar(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Equip Avatar is a ProtoFlux node that allows for making a User Equip an Avatar. A bit of caution should be used when using this node, since making people equip an avatar against their will without proper forewarning can be considered distasteful at best.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.EquipAvatar"

    def __init__(self, next: str | INodeOperation | None = None, user: str | INodeObjectOutput[User] | None = None, avatar_root: str | INodeObjectOutput[Slot] | None = None, destroy_old: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            user: Initial value for User.
            avatar_root: Initial value for AvatarRoot.
            destroy_old: Initial value for DestroyOld.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if user is not None:
            self.user = user
        if avatar_root is not None:
            self.avatar_root = avatar_root
        if destroy_old is not None:
            self.destroy_old = destroy_old

    @property
    def next(self) -> str | None:
        """Sends an impulse after * (Call) was called and the provided User (User) has equipped the provided AvatarRoot (Slot)."""
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
    def user(self) -> str | None:
        """The user that should equip the provided AvatarRoot (Slot)."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the User reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def avatar_root(self) -> str | None:
        """The Avatar the provided User (User) should equip. This slot is usually where the AvatarRoot component would be on an avatar which usually resides with the VRIK."""
        member = self.get_member("AvatarRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avatar_root.setter
    def avatar_root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the AvatarRoot reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("AvatarRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AvatarRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def destroy_old(self) -> str | None:
        """Whether the avatar the user was previously wearing should be destroyed. Only use this when nessary, because the avatar will be gone forever from the world when deleted."""
        member = self.get_member("DestroyOld")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @destroy_old.setter
    def destroy_old(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the DestroyOld reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DestroyOld")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DestroyOld",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

