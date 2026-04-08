"""Generated component: WebsocketConnect."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.websocket_client import WebsocketClient
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WebsocketConnect(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """This node allows you to connect to a websocket server via the WebSocketClient component.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network/Websockets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.WebsocketConnect"

    def __init__(self, next: str | INodeOperation | None = None, client: str | INodeObjectOutput[WebsocketClient] | None = None, url: str | INodeObjectOutput[str] | None = None, handling_user: str | INodeObjectOutput[User] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            client: Initial value for Client.
            url: Initial value for URL.
            handling_user: Initial value for HandlingUser.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if client is not None:
            self.client = client
        if url is not None:
            self.url = url
        if handling_user is not None:
            self.handling_user = handling_user

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
    def url(self) -> str | None:
        """Target ID of the URL reference (targets INodeObjectOutput[str])."""
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url.setter
    def url(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the URL reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "URL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>'),
            )

    @property
    def handling_user(self) -> str | None:
        """Target ID of the HandlingUser reference (targets INodeObjectOutput[User])."""
        member = self.get_member("HandlingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handling_user.setter
    def handling_user(self, target: str | INodeObjectOutput[User] | None) -> None:
        """Set the HandlingUser reference by target ID or INodeObjectOutput[User] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("HandlingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HandlingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.User>'),
            )

