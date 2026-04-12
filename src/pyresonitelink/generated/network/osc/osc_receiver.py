"""Generated component: OSC_Receiver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OSC_Receiver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.OSC_Receiver.

    Category: Network/OSC
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OSC_Receiver"

    def __init__(self, access_reason: primitives.String | None = None, port: primitives.Int | None = None, is_listening: primitives.Bool | None = None, connection_error: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            access_reason: Initial value for AccessReason.
            port: Initial value for Port.
            is_listening: Initial value for IsListening.
            connection_error: Initial value for ConnectionError.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if access_reason is not None:
            self.access_reason = access_reason
        if port is not None:
            self.port = port
        if is_listening is not None:
            self.is_listening = is_listening
        if connection_error is not None:
            self.connection_error = connection_error

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
    def access_reason(self) -> primitives.String | None:
        """The AccessReason field value."""
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
    def port(self) -> primitives.Int | None:
        """The Port field value."""
        member = self.get_member("Port")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @port.setter
    def port(self, value: primitives.Int) -> None:
        """Set the Port field value."""
        member = self.get_member("Port")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Port", fields.FieldInt(value=value)
            )

    @property
    def is_listening(self) -> primitives.Bool | None:
        """The IsListening field value."""
        member = self.get_member("IsListening")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_listening.setter
    def is_listening(self, value: primitives.Bool) -> None:
        """Set the IsListening field value."""
        member = self.get_member("IsListening")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsListening", fields.FieldBool(value=value)
            )

    @property
    def connection_error(self) -> primitives.String | None:
        """The ConnectionError field value."""
        member = self.get_member("ConnectionError")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @connection_error.setter
    def connection_error(self, value: primitives.String) -> None:
        """Set the ConnectionError field value."""
        member = self.get_member("ConnectionError")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ConnectionError", fields.FieldString(value=value)
            )

