"""Generated component: RequestHostAccessUrl."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.host_access_scope import HostAccessScope
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RequestHostAccessUrl(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.RequestHostAccessUrl.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.RequestHostAccessUrl"

    def __init__(self, on_granted: str | INodeOperation | None = None, on_denied: str | INodeOperation | None = None, on_ignored: str | INodeOperation | None = None, host: str | INodeObjectOutput[str] | None = None, reason: str | INodeObjectOutput[str] | None = None, scope: str | INodeValueOutput[HostAccessScope] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            on_granted: Initial value for OnGranted.
            on_denied: Initial value for OnDenied.
            on_ignored: Initial value for OnIgnored.
            host: Initial value for Host.
            reason: Initial value for Reason.
            scope: Initial value for Scope.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if on_granted is not None:
            self.on_granted = on_granted
        if on_denied is not None:
            self.on_denied = on_denied
        if on_ignored is not None:
            self.on_ignored = on_ignored
        if host is not None:
            self.host = host
        if reason is not None:
            self.reason = reason
        if scope is not None:
            self.scope = scope

    @property
    def on_granted(self) -> str | None:
        """Target ID of the OnGranted reference (targets INodeOperation)."""
        member = self.get_member("OnGranted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_granted.setter
    def on_granted(self, target: str | INodeOperation | None) -> None:
        """Set the OnGranted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnGranted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnGranted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_denied(self) -> str | None:
        """Target ID of the OnDenied reference (targets INodeOperation)."""
        member = self.get_member("OnDenied")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_denied.setter
    def on_denied(self, target: str | INodeOperation | None) -> None:
        """Set the OnDenied reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnDenied")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDenied",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_ignored(self) -> str | None:
        """Target ID of the OnIgnored reference (targets INodeOperation)."""
        member = self.get_member("OnIgnored")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_ignored.setter
    def on_ignored(self, target: str | INodeOperation | None) -> None:
        """Set the OnIgnored reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnIgnored")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnIgnored",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def host(self) -> str | None:
        """Target ID of the Host reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Host")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @host.setter
    def host(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Host reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Host")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Host",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>'),
            )

    @property
    def reason(self) -> str | None:
        """Target ID of the Reason reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Reason")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reason.setter
    def reason(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Reason reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Reason")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reason",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def scope(self) -> str | None:
        """Target ID of the Scope reference (targets INodeValueOutput[HostAccessScope])."""
        member = self.get_member("Scope")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scope.setter
    def scope(self, target: str | INodeValueOutput[HostAccessScope] | None) -> None:
        """Set the Scope reference by target ID or INodeValueOutput[HostAccessScope] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Scope")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Scope",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.HostAccessScope>'),
            )

