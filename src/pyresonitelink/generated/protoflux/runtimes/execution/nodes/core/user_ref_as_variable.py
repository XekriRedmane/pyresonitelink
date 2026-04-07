"""Generated component: UserRefAsVariable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.ivariable import IVariable
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserRefAsVariable(GeneratedComponent, IVariable, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.UserRefAsVariable.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Core
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.FrooxEngine.ProtoFlux.CoreNodes.UserRefAsVariable"

    def __init__(self, user_ref: str | INodeObjectOutput[UserRef] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_ref: Initial value for UserRef.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_ref is not None:
            self.user_ref = user_ref

    @property
    def user_ref(self) -> str | None:
        """Target ID of the UserRef reference (targets INodeObjectOutput[UserRef])."""
        member = self.get_member("UserRef")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_ref.setter
    def user_ref(self, target: str | INodeObjectOutput[UserRef] | None) -> None:
        """Set the UserRef reference by target ID or INodeObjectOutput[UserRef] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("UserRef")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UserRef",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.UserRef>'),
            )

