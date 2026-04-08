"""Generated component: IsHostAccessAllowed."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class IsHostAccessAllowed(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Is Host Access Allowed node takes in a Host IP address, an accessible port of that address, and the scope of what type of connection this is. When everything is accurate, this node will return if the user has the host access to a service. This relates to the settings in the Dash that a user can look through to see what services they have access to.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.IsHostAccessAllowed"

    def __init__(self, host: str | INodeObjectOutput[primitives.String] | None = None, port: str | INodeValueOutput[primitives.Int] | None = None, scope: str | INodeValueOutput[HostAccessScope] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            host: Initial value for Host.
            port: Initial value for Port.
            scope: Initial value for Scope.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if scope is not None:
            self.scope = scope

    @property
    def host(self) -> str | None:
        """Target ID of the Host reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Host")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @host.setter
    def host(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Host reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Host")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Host",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def port(self) -> str | None:
        """Target ID of the Port reference (targets INodeValueOutput[primitives.Int])."""
        member = self.get_member("Port")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @port.setter
    def port(self, target: str | INodeValueOutput[primitives.Int] | None) -> None:
        """Set the Port reference by target ID or INodeValueOutput[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Port")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Port",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
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

