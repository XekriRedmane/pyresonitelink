"""Generated component: CloudServerStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CloudServerStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CloudServerStatus.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloudServerStatus"

    def __init__(self, response_time_milliseconds: primitives.Int | None = None, last_server_update_time: str | None = None, last_server_state_fetch: str | None = None, last_local_server_response_time: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            response_time_milliseconds: Initial value for ResponseTimeMilliseconds.
            last_server_update_time: Initial value for LastServerUpdateTime.
            last_server_state_fetch: Initial value for LastServerStateFetch.
            last_local_server_response_time: Initial value for LastLocalServerResponseTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if response_time_milliseconds is not None:
            self.response_time_milliseconds = response_time_milliseconds
        if last_server_update_time is not None:
            self.last_server_update_time = last_server_update_time
        if last_server_state_fetch is not None:
            self.last_server_state_fetch = last_server_state_fetch
        if last_local_server_response_time is not None:
            self.last_local_server_response_time = last_local_server_response_time

    @property
    def status(self) -> members.FieldEnum | None:
        """The Status member."""
        member = self.get_member("Status")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @status.setter
    def status(self, value: members.FieldEnum) -> None:
        """Set the Status member."""
        self.set_member("Status", value)

    @property
    def response_time_milliseconds(self) -> primitives.Int | None:
        """The ResponseTimeMilliseconds field value."""
        member = self.get_member("ResponseTimeMilliseconds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @response_time_milliseconds.setter
    def response_time_milliseconds(self, value: primitives.Int) -> None:
        """Set the ResponseTimeMilliseconds field value."""
        member = self.get_member("ResponseTimeMilliseconds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResponseTimeMilliseconds", fields.FieldInt(value=value)
            )

    @property
    def last_server_update_time(self) -> str | None:
        """The LastServerUpdateTime field value."""
        member = self.get_member("LastServerUpdateTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_server_update_time.setter
    def last_server_update_time(self, value: str) -> None:
        """Set the LastServerUpdateTime field value."""
        member = self.get_member("LastServerUpdateTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastServerUpdateTime", fields.FieldDateTime(value=value)
            )

    @property
    def last_server_state_fetch(self) -> str | None:
        """The LastServerStateFetch field value."""
        member = self.get_member("LastServerStateFetch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_server_state_fetch.setter
    def last_server_state_fetch(self, value: str) -> None:
        """Set the LastServerStateFetch field value."""
        member = self.get_member("LastServerStateFetch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastServerStateFetch", fields.FieldDateTime(value=value)
            )

    @property
    def last_local_server_response_time(self) -> str | None:
        """The LastLocalServerResponseTime field value."""
        member = self.get_member("LastLocalServerResponseTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_local_server_response_time.setter
    def last_local_server_response_time(self, value: str) -> None:
        """Set the LastLocalServerResponseTime field value."""
        member = self.get_member("LastLocalServerResponseTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastLocalServerResponseTime", fields.FieldDateTime(value=value)
            )

