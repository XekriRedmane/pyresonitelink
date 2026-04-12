"""Generated component: WebsocketTextMessageReceiver."""

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


class WebsocketTextMessageReceiver(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Websocket Text Message Receiver node allows you to receive text messages from a WebsocketClient.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Websockets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketTextMessageReceiver"

    def __init__(self, client: str | IGlobalValueProxy[WebsocketClient] | None = None, on_received: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            client: Initial value for Client.
            on_received: Initial value for OnReceived.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if client is not None:
            self.client = client
        if on_received is not None:
            self.on_received = on_received

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
    def on_received(self) -> str | None:
        """A Call triggered when a text message is received."""
        member = self.get_member("OnReceived")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_received.setter
    def on_received(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnReceived reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnReceived")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnReceived",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def data(self) -> members.EmptyElement | None:
        """The Data member."""
        member = self.get_member("Data")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @data.setter
    def data(self, value: members.EmptyElement) -> None:
        """Set the Data member."""
        self.set_member("Data", value)

