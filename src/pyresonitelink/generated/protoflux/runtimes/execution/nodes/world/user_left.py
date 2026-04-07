"""Generated component: UserLeft."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iproto_flux_engine_proxy_node import IProtoFluxEngineProxyNode
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserLeft(GeneratedComponent, IProtoFluxEngineProxyNode, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.UserLeft.

    Category: ProtoFlux/Runtimes/Execution/Nodes/World
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.UserLeft"

    def __init__(self, only_host: str | INodeValueOutput[bool] | None = None, on_left: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            only_host: Initial value for OnlyHost.
            on_left: Initial value for OnLeft.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if only_host is not None:
            self.only_host = only_host
        if on_left is not None:
            self.on_left = on_left

    @property
    def only_host(self) -> str | None:
        """Target ID of the OnlyHost reference (targets INodeValueOutput[bool])."""
        member = self.get_member("OnlyHost")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @only_host.setter
    def only_host(self, target: str | INodeValueOutput[bool] | None) -> None:
        """Set the OnlyHost reference by target ID or INodeValueOutput[bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("OnlyHost")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnlyHost",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def on_left(self) -> str | None:
        """Target ID of the OnLeft reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_left.setter
    def on_left(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnLeft reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def left_user(self) -> members.EmptyElement | None:
        """The LeftUser member."""
        member = self.get_member("LeftUser")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @left_user.setter
    def left_user(self, value: members.EmptyElement) -> None:
        """Set the LeftUser member."""
        self.set_member("LeftUser", value)

