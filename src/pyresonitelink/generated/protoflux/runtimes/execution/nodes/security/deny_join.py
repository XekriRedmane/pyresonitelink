"""Generated component: DenyJoin."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.join_request_handle import JoinRequestHandle
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DenyJoin(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Deny Join node takes in a JoinRequestHandle and a deny reason, and if the world enabled a join verification system using the Verify Join Request node, this node will run and deny the user from joining and gives them a reason why.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Security
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.DenyJoin"

    def __init__(self, next: str | INodeOperation | None = None, handle: str | INodeObjectOutput[JoinRequestHandle] | None = None, deny_reason: str | INodeObjectOutput[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            handle: Initial value for Handle.
            deny_reason: Initial value for DenyReason.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if handle is not None:
            self.handle = handle
        if deny_reason is not None:
            self.deny_reason = deny_reason

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
    def handle(self) -> str | None:
        """Target ID of the Handle reference (targets INodeObjectOutput[JoinRequestHandle])."""
        member = self.get_member("Handle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle.setter
    def handle(self, target: str | INodeObjectOutput[JoinRequestHandle] | None) -> None:
        """Set the Handle reference by target ID or INodeObjectOutput[JoinRequestHandle] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Handle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Handle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[ProtoFlux.Nodes.FrooxEngine]ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Security.JoinRequestHandle>'),
            )

    @property
    def deny_reason(self) -> str | None:
        """Target ID of the DenyReason reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("DenyReason")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @deny_reason.setter
    def deny_reason(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the DenyReason reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("DenyReason")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DenyReason",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

