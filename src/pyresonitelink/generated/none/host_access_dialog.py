"""Generated component: HostAccessDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.host_access_scope import HostAccessScope
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HostAccessDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """See Request Host Access ProtoFlux Node.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HostAccessDialog"

    def __init__(self, host: primitives.String | None = None, port: primitives.Int | None = None, access_type: HostAccessScope | str | None = None, host_text: str | Text | None = None, reason_text: str | Text | None = None, allow_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            host: Initial value for Host.
            port: Initial value for Port.
            access_type: Initial value for AccessType.
            host_text: Initial value for _hostText.
            reason_text: Initial value for _reasonText.
            allow_button: Initial value for _allowButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if host is not None:
            self.host = host
        if port is not None:
            self.port = port
        if access_type is not None:
            self.access_type = access_type
        if host_text is not None:
            self.host_text = host_text
        if reason_text is not None:
            self.reason_text = reason_text
        if allow_button is not None:
            self.allow_button = allow_button

    @property
    def host(self) -> primitives.String | None:
        """The host destination string being accessed."""
        member = self.get_member("Host")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @host.setter
    def host(self, value: primitives.String) -> None:
        """Set the Host field value."""
        member = self.get_member("Host")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Host", fields.FieldString(value=value)
            )

    @property
    def port(self) -> primitives.Int | None:
        """The port being asked for access."""
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
    def access_type(self) -> HostAccessScope | None:
        """The access type wanted for the port."""
        member = self.get_member("AccessType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return HostAccessScope(member.value)
        return None

    @access_type.setter
    def access_type(self, value: HostAccessScope | str) -> None:
        """Set AccessType. The access type wanted for the port."""
        member = self.get_member("AccessType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AccessType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def host_text(self) -> str | None:
        """The text field used to show the server wanting access for."""
        member = self.get_member("_hostText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @host_text.setter
    def host_text(self, target: str | Text | None) -> None:
        """Set the _hostText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_hostText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hostText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def reason_text(self) -> str | None:
        """The reason for accessing the server."""
        member = self.get_member("_reasonText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reason_text.setter
    def reason_text(self, target: str | Text | None) -> None:
        """Set the _reasonText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_reasonText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_reasonText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def allow_button(self) -> str | None:
        """The button to allow the server to be accessed through your client."""
        member = self.get_member("_allowButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @allow_button.setter
    def allow_button(self, target: str | Button | None) -> None:
        """Set the _allowButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_allowButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_allowButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

