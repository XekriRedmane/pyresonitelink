"""Generated component: TwitchInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TwitchInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Twitch interface is a component that is used to allow resonite to communicate to and recieve twitch API events from twitch for a given ``Channel`` through a User.

    Category: Network
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TwitchInterface"

    def __init__(self, channel: primitives.String | None = None, connected: primitives.Bool | None = None, stream_live: primitives.Bool | None = None, viewer_count: primitives.Int | None = None, follow_timeout_seconds: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            channel: Initial value for Channel.
            connected: Initial value for Connected.
            stream_live: Initial value for StreamLive.
            viewer_count: Initial value for ViewerCount.
            follow_timeout_seconds: Initial value for FollowTimeoutSeconds.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if channel is not None:
            self.channel = channel
        if connected is not None:
            self.connected = connected
        if stream_live is not None:
            self.stream_live = stream_live
        if viewer_count is not None:
            self.viewer_count = viewer_count
        if follow_timeout_seconds is not None:
            self.follow_timeout_seconds = follow_timeout_seconds

    @property
    def target_user(self) -> members.SyncObject | None:
        """The user to handle sending and receiving network packets to and from twitch. User will need to have agreed to communicate with Twitch for this component to work."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set TargetUser. The user to handle sending and receiving network packets to and from twitch. User will need to have agreed to communicate with Twitch for this component to work."""
        self.set_member("TargetUser", value)

    @property
    def channel(self) -> primitives.String | None:
        """The twitch channel to get communications from."""
        member = self.get_member("Channel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @channel.setter
    def channel(self, value: primitives.String) -> None:
        """Set the Channel field value."""
        member = self.get_member("Channel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Channel", fields.FieldString(value=value)
            )

    @property
    def connected(self) -> primitives.Bool | None:
        """Whether the connection to ``Channel`` is a success and is communicating."""
        member = self.get_member("Connected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @connected.setter
    def connected(self, value: primitives.Bool) -> None:
        """Set the Connected field value."""
        member = self.get_member("Connected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Connected", fields.FieldBool(value=value)
            )

    @property
    def stream_live(self) -> primitives.Bool | None:
        """Whether ``Channel`` is currently streaming."""
        member = self.get_member("StreamLive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stream_live.setter
    def stream_live(self, value: primitives.Bool) -> None:
        """Set the StreamLive field value."""
        member = self.get_member("StreamLive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StreamLive", fields.FieldBool(value=value)
            )

    @property
    def viewer_count(self) -> primitives.Int | None:
        """How many viewers are viewing ``Channel``'s stream."""
        member = self.get_member("ViewerCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @viewer_count.setter
    def viewer_count(self, value: primitives.Int) -> None:
        """Set the ViewerCount field value."""
        member = self.get_member("ViewerCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ViewerCount", fields.FieldInt(value=value)
            )

    @property
    def follow_timeout_seconds(self) -> primitives.Float | None:
        """How many seconds to wait before allowing another follow event through."""
        member = self.get_member("FollowTimeoutSeconds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @follow_timeout_seconds.setter
    def follow_timeout_seconds(self, value: primitives.Float) -> None:
        """Set the FollowTimeoutSeconds field value."""
        member = self.get_member("FollowTimeoutSeconds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FollowTimeoutSeconds", fields.FieldFloat(value=value)
            )

