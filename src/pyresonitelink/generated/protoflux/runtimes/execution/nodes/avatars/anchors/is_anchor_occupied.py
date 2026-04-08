"""Generated component: IsAnchorOccupied."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iavatar_anchor import IAvatarAnchor
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IsAnchorOccupied(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Is Anchor Occupied Is a ProtoFlux node that returns whether an anchor has a user in it or not.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Anchors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.IsAnchorOccupied"

    def __init__(self, anchor: str | INodeObjectOutput[IAvatarAnchor] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor: Initial value for Anchor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor is not None:
            self.anchor = anchor

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

