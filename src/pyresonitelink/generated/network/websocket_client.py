"""Generated component: WebsocketClient."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WebsocketClient(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WebsocketClient.

    Category: Network
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WebsocketClient"

    def __init__(self, url: str | None = None, access_reason: str | None = None, connect_retry_interval: np.float32 | None = None, is_connected: bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """The URL field value."""
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
        """The HandlingUser member."""
        member = self.get_member("HandlingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @handling_user.setter
    def handling_user(self, value: members.SyncObject) -> None:
        """Set the HandlingUser member."""
        self.set_member("HandlingUser", value)

    @property
    def access_reason(self) -> str | None:
        """The AccessReason field value."""
        member = self.get_member("AccessReason")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @access_reason.setter
    def access_reason(self, value: str) -> None:
        """Set the AccessReason field value."""
        member = self.get_member("AccessReason")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccessReason", fields.FieldString(value=value)
            )

    @property
    def connect_retry_interval(self) -> np.float32 | None:
        """The ConnectRetryInterval field value."""
        member = self.get_member("ConnectRetryInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @connect_retry_interval.setter
    def connect_retry_interval(self, value: np.float32) -> None:
        """Set the ConnectRetryInterval field value."""
        member = self.get_member("ConnectRetryInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ConnectRetryInterval", fields.FieldFloat(value=value)
            )

    @property
    def is_connected(self) -> bool | None:
        """The IsConnected field value."""
        member = self.get_member("IsConnected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_connected.setter
    def is_connected(self, value: bool) -> None:
        """Set the IsConnected field value."""
        member = self.get_member("IsConnected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsConnected", fields.FieldBool(value=value)
            )

