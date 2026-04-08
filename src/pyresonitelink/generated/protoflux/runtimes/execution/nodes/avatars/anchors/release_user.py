"""Generated component: ReleaseUser."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iavatar_anchor import IAvatarAnchor
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReleaseUser(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Release User Is a ProtoFlux node that releases the user currently occupying an anchor.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Anchors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.ReleaseUser"

    def __init__(self, anchor: str | INodeObjectOutput[IAvatarAnchor] | None = None, on_released: str | INodeOperation | None = None, on_failure: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor: Initial value for Anchor.
            on_released: Initial value for OnReleased.
            on_failure: Initial value for OnFailure.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor is not None:
            self.anchor = anchor
        if on_released is not None:
            self.on_released = on_released
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
    def on_released(self) -> str | None:
        """Target ID of the OnReleased reference (targets INodeOperation)."""
        member = self.get_member("OnReleased")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_released.setter
    def on_released(self, target: str | INodeOperation | None) -> None:
        """Set the OnReleased reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReleased")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReleased",
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

