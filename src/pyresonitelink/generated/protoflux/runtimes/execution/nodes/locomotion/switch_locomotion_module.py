"""Generated component: SwitchLocomotionModule."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SwitchLocomotionModule(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Switch Locomotion Module is a ProtoFlux node that switches a user to a locomotion by name.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Locomotion
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Locomotion.SwitchLocomotionModule"

    def __init__(self, target_user: str | INodeObjectOutput[User] | None = None, module_name: str | INodeObjectOutput[primitives.String] | None = None, exact_match: str | INodeValueOutput[primitives.Bool] | None = None, on_switched: str | INodeOperation | None = None, on_not_found: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_user: Initial value for TargetUser.
            module_name: Initial value for ModuleName.
            exact_match: Initial value for ExactMatch.
            on_switched: Initial value for OnSwitched.
            on_not_found: Initial value for OnNotFound.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_user is not None:
            self.target_user = target_user
        if module_name is not None:
            self.module_name = module_name
        if exact_match is not None:
            self.exact_match = exact_match
        if on_switched is not None:
            self.on_switched = on_switched
        if on_not_found is not None:
            self.on_not_found = on_not_found

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
    def module_name(self) -> str | None:
        """Target ID of the ModuleName reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("ModuleName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @module_name.setter
    def module_name(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the ModuleName reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("ModuleName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ModuleName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def exact_match(self) -> str | None:
        """Target ID of the ExactMatch reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("ExactMatch")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @exact_match.setter
    def exact_match(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the ExactMatch reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("ExactMatch")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ExactMatch",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_switched(self) -> str | None:
        """Target ID of the OnSwitched reference (targets INodeOperation)."""
        member = self.get_member("OnSwitched")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_switched.setter
    def on_switched(self, target: str | INodeOperation | None) -> None:
        """Set the OnSwitched reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSwitched")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSwitched",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_not_found(self) -> str | None:
        """Target ID of the OnNotFound reference (targets INodeOperation)."""
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_not_found.setter
    def on_not_found(self, target: str | INodeOperation | None) -> None:
        """Set the OnNotFound reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnNotFound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnNotFound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

