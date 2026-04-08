"""Generated component: OSC_Sender."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OSC_Sender(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.OSC_Sender.

    Category: Network/OSC
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OSC_Sender"

    def __init__(self, access_reason: primitives.String | None = None, url: str | None = None, local_port: primitives.Int | None = None, is_sending: primitives.Bool | None = None, auto_resend_interval: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            access_reason: Initial value for AccessReason.
            url: Initial value for URL.
            local_port: Initial value for LocalPort.
            is_sending: Initial value for IsSending.
            auto_resend_interval: Initial value for AutoResendInterval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if access_reason is not None:
            self.access_reason = access_reason
        if url is not None:
            self.url = url
        if local_port is not None:
            self.local_port = local_port
        if is_sending is not None:
            self.is_sending = is_sending
        if auto_resend_interval is not None:
            self.auto_resend_interval = auto_resend_interval

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
    def local_port(self) -> primitives.Int | None:
        """The LocalPort field value."""
        member = self.get_member("LocalPort")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_port.setter
    def local_port(self, value: primitives.Int) -> None:
        """Set the LocalPort field value."""
        member = self.get_member("LocalPort")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalPort", fields.FieldInt(value=value)
            )

    @property
    def is_sending(self) -> primitives.Bool | None:
        """The IsSending field value."""
        member = self.get_member("IsSending")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_sending.setter
    def is_sending(self, value: primitives.Bool) -> None:
        """Set the IsSending field value."""
        member = self.get_member("IsSending")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSending", fields.FieldBool(value=value)
            )

    @property
    def send_mode(self) -> members.FieldEnum | None:
        """The SendMode member."""
        member = self.get_member("SendMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @send_mode.setter
    def send_mode(self, value: members.FieldEnum) -> None:
        """Set the SendMode member."""
        self.set_member("SendMode", value)

    @property
    def auto_resend_interval(self) -> primitives.Float | None:
        """The AutoResendInterval field value."""
        member = self.get_member("AutoResendInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_resend_interval.setter
    def auto_resend_interval(self, value: primitives.Float) -> None:
        """Set the AutoResendInterval field value."""
        member = self.get_member("AutoResendInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoResendInterval", fields.FieldFloat(value=value)
            )

