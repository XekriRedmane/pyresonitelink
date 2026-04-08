"""Generated component: IsHostAccessAllowedUrl."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.host_access_scope import HostAccessScope
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class IsHostAccessAllowedUrl(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Is Host Access Allowed Url node takes in a host IP address (and optionally accessible port of that address if provided), and the scope of what type of connection this is. When everything is accurate, this node will return if the user has the host access to a service. This relates to the settings in the Dash that a user can look through to see what services they have access to.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.IsHostAccessAllowedUrl"

    def __init__(self, host: str | INodeObjectOutput[str] | None = None, scope: str | INodeValueOutput[HostAccessScope] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            host: Initial value for Host.
            scope: Initial value for Scope.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if host is not None:
            self.host = host
        if scope is not None:
            self.scope = scope

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

