"""Generated component: InstallLocomotionModules."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InstallLocomotionModules(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.InstallLocomotionModules.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Locomotion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.InstallLocomotionModules"

    def __init__(self, next: str | INodeOperation | None = None, modules_root: str | INodeObjectOutput[Slot] | None = None, target_user: str | INodeObjectOutput[User] | None = None, clear_existing: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            modules_root: Initial value for ModulesRoot.
            target_user: Initial value for TargetUser.
            clear_existing: Initial value for ClearExisting.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if modules_root is not None:
            self.modules_root = modules_root
        if target_user is not None:
            self.target_user = target_user
        if clear_existing is not None:
            self.clear_existing = clear_existing

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
    def modules_root(self) -> str | None:
        """Target ID of the ModulesRoot reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("ModulesRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modules_root.setter
    def modules_root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the ModulesRoot reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("ModulesRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ModulesRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def target_user(self) -> str | None:
        """Target ID of the TargetUser reference (targets INodeObjectOutput[User])."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_user.setter
    def target_user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the TargetUser reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("TargetUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

    @property
    def clear_existing(self) -> str | None:
        """Target ID of the ClearExisting reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ClearExisting")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clear_existing.setter
    def clear_existing(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ClearExisting reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ClearExisting")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ClearExisting",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

