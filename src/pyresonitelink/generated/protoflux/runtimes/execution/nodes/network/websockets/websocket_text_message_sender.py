"""Generated component: WebsocketTextMessageSender."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.websocket_client import WebsocketClient
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WebsocketTextMessageSender(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketTextMessageSender.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Websockets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketTextMessageSender"

    def __init__(self, client: str | INodeObjectOutput[WebsocketClient] | None = None, data: str | INodeObjectOutput[primitives.String] | None = None, on_send_start: str | INodeOperation | None = None, on_sent: str | INodeOperation | None = None, on_send_error: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            client: Initial value for Client.
            data: Initial value for Data.
            on_send_start: Initial value for OnSendStart.
            on_sent: Initial value for OnSent.
            on_send_error: Initial value for OnSendError.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if client is not None:
            self.client = client
        if data is not None:
            self.data = data
        if on_send_start is not None:
            self.on_send_start = on_send_start
        if on_sent is not None:
            self.on_sent = on_sent
        if on_send_error is not None:
            self.on_send_error = on_send_error

    @property
    def client(self) -> str | None:
        """Target ID of the Client reference (targets INodeObjectOutput[WebsocketClient])."""
        member = self.get_member("Client")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @client.setter
    def client(self, target: str | INodeObjectOutput[WebsocketClient] | None) -> None:
        """Set the Client reference by target ID or INodeObjectOutput[WebsocketClient] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Client")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Client",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.WebsocketClient>'),
            )

    @property
    def data(self) -> str | None:
        """Target ID of the Data reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("Data")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @data.setter
    def data(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the Data reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Data")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Data",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def on_send_start(self) -> str | None:
        """Target ID of the OnSendStart reference (targets INodeOperation)."""
        member = self.get_member("OnSendStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_send_start.setter
    def on_send_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnSendStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSendStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSendStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_sent(self) -> str | None:
        """Target ID of the OnSent reference (targets INodeOperation)."""
        member = self.get_member("OnSent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_sent.setter
    def on_sent(self, target: str | INodeOperation | None) -> None:
        """Set the OnSent reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_send_error(self) -> str | None:
        """Target ID of the OnSendError reference (targets INodeOperation)."""
        member = self.get_member("OnSendError")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_send_error.setter
    def on_send_error(self, target: str | INodeOperation | None) -> None:
        """Set the OnSendError reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnSendError")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnSendError",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

