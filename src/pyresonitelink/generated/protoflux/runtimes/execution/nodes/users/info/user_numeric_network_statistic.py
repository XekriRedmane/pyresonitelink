"""Generated component: UserNumericNetworkStatistic."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserNumericNetworkStatistic(GenericComponent[T], INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserNumericNetworkStatistic<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Users/Info

    Parameterize with a value type::

        UserNumericNetworkStatistic[np.float32]
        UserNumericNetworkStatistic[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserNumericNetworkStatistic<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserNumericNetworkStatistic<>"

    def __init__(self, name: str | INodeObjectOutput[str] | None = None, user: str | INodeObjectOutput[User] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            name: Initial value for Name.
            user: Initial value for User.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if name is not None:
            self.name = name
        if user is not None:
            self.user = user

    @property
    def name(self) -> str | None:
        """Target ID of the Name reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Name reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Name")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Name",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

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

