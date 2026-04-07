"""Generated component: ControllerSlot."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.user_root import UserRoot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.chirality import Chirality
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ControllerSlot(GeneratedComponent, INodeObjectOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.ControllerSlot.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Users/User Root
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Users.Roots.ControllerSlot"

    def __init__(self, user_root: str | INodeObjectOutput[UserRoot] | None = None, side: str | INodeValueOutput[Chirality] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user_root: Initial value for UserRoot.
            side: Initial value for Side.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user_root is not None:
            self.user_root = user_root
        if side is not None:
            self.side = side

    @property
    def user_root(self) -> str | None:
        """Target ID of the UserRoot reference (targets INodeObjectOutput[UserRoot])."""
        member = self.get_member("UserRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_root.setter
    def user_root(self, target: str | INodeObjectOutput[UserRoot] | None) -> None:
        """Set the UserRoot reference by target ID or INodeObjectOutput[UserRoot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("UserRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UserRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.UserRoot>'),
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

