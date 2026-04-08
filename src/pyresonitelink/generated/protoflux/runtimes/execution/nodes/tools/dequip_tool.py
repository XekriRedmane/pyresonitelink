"""Generated component: DequipTool."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DequipTool(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.DequipTool.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Tools
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.Tools.DequipTool"

    def __init__(self, user: str | INodeObjectOutput[User] | None = None, side: str | INodeValueOutput[Chirality] | None = None, pop_off: str | INodeValueOutput[primitives.Bool] | None = None, on_dequipped: str | INodeOperation | None = None, on_dequip_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            side: Initial value for Side.
            pop_off: Initial value for PopOff.
            on_dequipped: Initial value for OnDequipped.
            on_dequip_fail: Initial value for OnDequipFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if side is not None:
            self.side = side
        if pop_off is not None:
            self.pop_off = pop_off
        if on_dequipped is not None:
            self.on_dequipped = on_dequipped
        if on_dequip_fail is not None:
            self.on_dequip_fail = on_dequip_fail

    @property
    def user(self) -> str | None:
        """Target ID of the User reference (targets INodeObjectOutput[User])."""
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
    def side(self) -> str | None:
        """Target ID of the Side reference (targets INodeValueOutput[Chirality])."""
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side.setter
    def side(self, target: str | INodeValueOutput[Chirality] | None) -> None:
        """Set the Side reference by target ID or INodeValueOutput[Chirality] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Side")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Side",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Chirality>'),
            )

    @property
    def pop_off(self) -> str | None:
        """Target ID of the PopOff reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("PopOff")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pop_off.setter
    def pop_off(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the PopOff reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("PopOff")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PopOff",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_dequipped(self) -> str | None:
        """Target ID of the OnDequipped reference (targets INodeOperation)."""
        member = self.get_member("OnDequipped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_dequipped.setter
    def on_dequipped(self, target: str | INodeOperation | None) -> None:
        """Set the OnDequipped reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnDequipped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDequipped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_dequip_fail(self) -> str | None:
        """Target ID of the OnDequipFail reference (targets INodeOperation)."""
        member = self.get_member("OnDequipFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_dequip_fail.setter
    def on_dequip_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnDequipFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnDequipFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDequipFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

