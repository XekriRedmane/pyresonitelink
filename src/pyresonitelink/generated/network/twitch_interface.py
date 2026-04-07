"""Generated component: TwitchInterface."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TwitchInterface(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TwitchInterface.

    Category: Network
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TwitchInterface"

    def __init__(self, channel: str | None = None, connected: bool | None = None, stream_live: bool | None = None, viewer_count: np.int32 | None = None, follow_timeout_seconds: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
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
        """The TargetUser member."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set the TargetUser member."""
        self.set_member("TargetUser", value)

    @property
    def channel(self) -> str | None:
        """The Channel field value."""
        member = self.get_member("Channel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @channel.setter
    def channel(self, value: str) -> None:
        """Set the Channel field value."""
        member = self.get_member("Channel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Channel", fields.FieldString(value=value)
            )

    @property
    def connected(self) -> bool | None:
        """The Connected field value."""
        member = self.get_member("Connected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @connected.setter
    def connected(self, value: bool) -> None:
        """Set the Connected field value."""
        member = self.get_member("Connected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Connected", fields.FieldBool(value=value)
            )

    @property
    def stream_live(self) -> bool | None:
        """The StreamLive field value."""
        member = self.get_member("StreamLive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stream_live.setter
    def stream_live(self, value: bool) -> None:
        """Set the StreamLive field value."""
        member = self.get_member("StreamLive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StreamLive", fields.FieldBool(value=value)
            )

    @property
    def viewer_count(self) -> np.int32 | None:
        """The ViewerCount field value."""
        member = self.get_member("ViewerCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @viewer_count.setter
    def viewer_count(self, value: np.int32) -> None:
        """Set the ViewerCount field value."""
        member = self.get_member("ViewerCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ViewerCount", fields.FieldInt(value=value)
            )

    @property
    def follow_timeout_seconds(self) -> np.float32 | None:
        """The FollowTimeoutSeconds field value."""
        member = self.get_member("FollowTimeoutSeconds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @follow_timeout_seconds.setter
    def follow_timeout_seconds(self, value: np.float32) -> None:
        """Set the FollowTimeoutSeconds field value."""
        member = self.get_member("FollowTimeoutSeconds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FollowTimeoutSeconds", fields.FieldFloat(value=value)
            )

