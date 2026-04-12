"""Generated component: WebsocketClient."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WebsocketClient(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This component must be used in conjunction with the Websocket Protoflux Nodes - it only exists to store state, and does not function on its own.

    Category: Network

    This component must be used in conjunction with the Websocket Protoflux
    Nodes - it only exists to store state, and does not function on its own.
    ``User`` should be a user that expects to be hosting the Websocket
    connection Assignments should generally be made in the following order,
    depending on which one is the most applicable: * The user wearing the
    avatar containing this Protoflux * A specifically defined user who is
    expected to be present for this connection to function * The user who
    spawned the object containing this Protoflux * The user who is currently
    interacting with the object * The host of the session You should not
    select a user who is not expecting the object to connect to an external
    service. It is possible they will deny the connection (especially if
    ``AccessReason`` isn't sufficiently convincing), which will cause the
    connection to fail. ``AccessReason`` should provide a clear and concise
    reason for wanting to connect to the external service - It should
    include an obvious title or description of the object that is attempting
    to establish the connection, so that the user is aware of what item in
    the world is prompting the connection. The object should have some way
    of indicating that it did not successfully connect to the target
    service, and that it will not function as intended, if at all. The
    websocket times out and disconnects if the remote server does not send
    any traffic (including heartbeat messages) at least every 60 seconds,
    for long running connections be sure to configure the keepalive interval
    on the server side.

    **Related Issues**: == Related Components ==
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WebsocketClient"

    def __init__(self, url: str | None = None, access_reason: primitives.String | None = None, connect_retry_interval: primitives.Float | None = None, is_connected: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            access_reason: Initial value for AccessReason.
            connect_retry_interval: Initial value for ConnectRetryInterval.
            is_connected: Initial value for IsConnected.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if access_reason is not None:
            self.access_reason = access_reason
        if connect_retry_interval is not None:
            self.connect_retry_interval = connect_retry_interval
        if is_connected is not None:
            self.is_connected = is_connected

    @property
    def url(self) -> str | None:
        """The Websocket server to target - either secure (``wss://``) or insecure (``ws://``)"""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def handling_user(self) -> members.SyncObject | None:
        """The user who will be responsible for establishing the connection, and transmitting data."""
        member = self.get_member("HandlingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @handling_user.setter
    def handling_user(self, value: members.SyncObject) -> None:
        """Set HandlingUser. The user who will be responsible for establishing the connection, and transmitting data."""
        self.set_member("HandlingUser", value)

    @property
    def access_reason(self) -> primitives.String | None:
        """A descriptive string explaining why this connection request should be granted"""
        member = self.get_member("AccessReason")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @access_reason.setter
    def access_reason(self, value: primitives.String) -> None:
        """Set the AccessReason field value."""
        member = self.get_member("AccessReason")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccessReason", fields.FieldString(value=value)
            )

    @property
    def connect_retry_interval(self) -> primitives.Float | None:
        """How often to retry the connection, if it fails for reasons other than being rejected by the user."""
        member = self.get_member("ConnectRetryInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @connect_retry_interval.setter
    def connect_retry_interval(self, value: primitives.Float) -> None:
        """Set the ConnectRetryInterval field value."""
        member = self.get_member("ConnectRetryInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ConnectRetryInterval", fields.FieldFloat(value=value)
            )

    @property
    def is_connected(self) -> primitives.Bool | None:
        """A read-only value indicating if this client has successfully connected to the target specified in ``URL``"""
        member = self.get_member("IsConnected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_connected.setter
    def is_connected(self, value: primitives.Bool) -> None:
        """Set the IsConnected field value."""
        member = self.get_member("IsConnected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsConnected", fields.FieldBool(value=value)
            )

