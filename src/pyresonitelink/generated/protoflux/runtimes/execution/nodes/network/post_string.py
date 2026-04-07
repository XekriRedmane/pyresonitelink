"""Generated component: POST_String."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class POST_String(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.POST_String.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Network
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Network.POST_String"

    def __init__(self, url: str | INodeObjectOutput[str] | None = None, on_sent: str | INodeOperation | None = None, on_response: str | INodeOperation | None = None, on_error: str | INodeOperation | None = None, on_denied: str | INodeOperation | None = None, string: str | INodeObjectOutput[str] | None = None, media_type: str | INodeObjectOutput[str] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            on_sent: Initial value for OnSent.
            on_response: Initial value for OnResponse.
            on_error: Initial value for OnError.
            on_denied: Initial value for OnDenied.
            string: Initial value for String.
            media_type: Initial value for MediaType.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if on_sent is not None:
            self.on_sent = on_sent
        if on_response is not None:
            self.on_response = on_response
        if on_error is not None:
            self.on_error = on_error
        if on_denied is not None:
            self.on_denied = on_denied
        if string is not None:
            self.string = string
        if media_type is not None:
            self.media_type = media_type

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
    def status_code(self) -> members.EmptyElement | None:
        """The StatusCode member."""
        member = self.get_member("StatusCode")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @status_code.setter
    def status_code(self, value: members.EmptyElement) -> None:
        """Set the StatusCode member."""
        self.set_member("StatusCode", value)

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
    def on_response(self) -> str | None:
        """Target ID of the OnResponse reference (targets INodeOperation)."""
        member = self.get_member("OnResponse")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_response.setter
    def on_response(self, target: str | INodeOperation | None) -> None:
        """Set the OnResponse reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnResponse")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnResponse",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_error(self) -> str | None:
        """Target ID of the OnError reference (targets INodeOperation)."""
        member = self.get_member("OnError")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_error.setter
    def on_error(self, target: str | INodeOperation | None) -> None:
        """Set the OnError reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnError")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnError",
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
    def content(self) -> members.EmptyElement | None:
        """The Content member."""
        member = self.get_member("Content")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @content.setter
    def content(self, value: members.EmptyElement) -> None:
        """Set the Content member."""
        self.set_member("Content", value)

    @property
    def string(self) -> str | None:
        """Target ID of the String reference (targets INodeObjectOutput[str])."""
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @string.setter
    def string(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the String reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("String")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "String",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def media_type(self) -> str | None:
        """Target ID of the MediaType reference (targets INodeObjectOutput[str])."""
        member = self.get_member("MediaType")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @media_type.setter
    def media_type(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the MediaType reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("MediaType")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MediaType",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

