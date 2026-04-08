"""Generated component: WebsocketConnectionEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.websocket_client import WebsocketClient
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WebsocketConnectionEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node will allow you do detect when a WebSocket client is connected or disconnected.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Websockets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketConnectionEvents"

    def __init__(self, client: str | IGlobalValueProxy[WebsocketClient] | None = None, on_connected: str | ISyncNodeOperation | None = None, on_disconnected: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            client: Initial value for Client.
            on_connected: Initial value for OnConnected.
            on_disconnected: Initial value for OnDisconnected.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if client is not None:
            self.client = client
        if on_connected is not None:
            self.on_connected = on_connected
        if on_disconnected is not None:
            self.on_disconnected = on_disconnected

    @property
    def client(self) -> str | None:
        """Target ID of the Client reference (targets IGlobalValueProxy[WebsocketClient])."""
        member = self.get_member("Client")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @client.setter
    def client(self, target: str | IGlobalValueProxy[WebsocketClient] | None) -> None:
        """Set the Client reference by target ID or IGlobalValueProxy[WebsocketClient] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Client")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Client",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.WebsocketClient>'),
            )

    @property
    def on_connected(self) -> str | None:
        """Target ID of the OnConnected reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnConnected")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_connected.setter
    def on_connected(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnConnected reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnConnected")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnConnected",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def on_disconnected(self) -> str | None:
        """Target ID of the OnDisconnected reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnDisconnected")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_disconnected.setter
    def on_disconnected(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnDisconnected reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnDisconnected")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnDisconnected",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

