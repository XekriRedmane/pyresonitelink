"""Generated component: UserFromUsername."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserFromUsername(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node returns a user object from a username.

This will only work for users present in the session.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Users
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.UserFromUsername"

    def __init__(self, username: str | INodeObjectOutput[primitives.String] | None = None, ignore_case: str | INodeValueOutput[primitives.Bool] | None = None, allow_partial_match: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            username: Initial value for Username.
            ignore_case: Initial value for IgnoreCase.
            allow_partial_match: Initial value for AllowPartialMatch.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if username is not None:
            self.username = username
        if ignore_case is not None:
            self.ignore_case = ignore_case
        if allow_partial_match is not None:
            self.allow_partial_match = allow_partial_match

    @property
    def username(self) -> str | None:
        """The username of the user you need."""
        member = self.get_member("Username")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @username.setter
    def username(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Username reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Username")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Username",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def ignore_case(self) -> str | None:
        """Target ID of the IgnoreCase reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("IgnoreCase")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_case.setter
    def ignore_case(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the IgnoreCase reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("IgnoreCase")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IgnoreCase",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def allow_partial_match(self) -> str | None:
        """Target ID of the AllowPartialMatch reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("AllowPartialMatch")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @allow_partial_match.setter
    def allow_partial_match(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the AllowPartialMatch reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("AllowPartialMatch")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AllowPartialMatch",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

