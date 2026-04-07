"""Generated component: UserFromID."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserFromID(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserFromID.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Users
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserFromID"

    def __init__(self, user_id: str | INodeObjectOutput[str] | None = None, machine_id: str | INodeObjectOutput[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_id: Initial value for UserId.
            machine_id: Initial value for MachineId.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_id is not None:
            self.user_id = user_id
        if machine_id is not None:
            self.machine_id = machine_id

    @property
    def user_id(self) -> str | None:
        """Target ID of the UserId reference (targets INodeObjectOutput[str])."""
        member = self.get_member("UserId")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_id.setter
    def user_id(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the UserId reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("UserId")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UserId",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def machine_id(self) -> str | None:
        """Target ID of the MachineId reference (targets INodeObjectOutput[str])."""
        member = self.get_member("MachineId")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @machine_id.setter
    def machine_id(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the MachineId reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("MachineId")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MachineId",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

