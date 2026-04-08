"""Generated component: AnchorUser."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iavatar_anchor import IAvatarAnchor
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AnchorUser(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Anchor User is a ProtoFlux node that attempts to anchor a user to any anchor, which is provided to the node via the IAvatarAnchor type.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Anchors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorUser"

    def __init__(self, anchor: str | INodeObjectOutput[IAvatarAnchor] | None = None, user: str | INodeObjectOutput[User] | None = None, on_anchored: str | INodeOperation | None = None, on_failure: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor: Initial value for Anchor.
            user: Initial value for User.
            on_anchored: Initial value for OnAnchored.
            on_failure: Initial value for OnFailure.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor is not None:
            self.anchor = anchor
        if user is not None:
            self.user = user
        if on_anchored is not None:
            self.on_anchored = on_anchored
        if on_failure is not None:
            self.on_failure = on_failure

    @property
    def anchor(self) -> str | None:
        """Target ID of the Anchor reference (targets INodeObjectOutput[IAvatarAnchor])."""
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor.setter
    def anchor(self, target: str | INodeObjectOutput[IAvatarAnchor] | None) -> None:
        """Set the Anchor reference by target ID or INodeObjectOutput[IAvatarAnchor] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IAvatarAnchor>'),
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

    @property
    def on_anchored(self) -> str | None:
        """Target ID of the OnAnchored reference (targets INodeOperation)."""
        member = self.get_member("OnAnchored")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_anchored.setter
    def on_anchored(self, target: str | INodeOperation | None) -> None:
        """Set the OnAnchored reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnAnchored")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnAnchored",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_failure(self) -> str | None:
        """Target ID of the OnFailure reference (targets INodeOperation)."""
        member = self.get_member("OnFailure")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_failure.setter
    def on_failure(self, target: str | INodeOperation | None) -> None:
        """Set the OnFailure reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFailure")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFailure",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

