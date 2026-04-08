"""Generated component: DebugAvatarBuilder."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugAvatarBuilder(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugAvatarBuilder.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugAvatarBuilder"

    def __init__(self, setup_server_voice: bool | None = None, setup_client_voice: bool | None = None, setup_server_tools: bool | None = None, setup_client_tools: bool | None = None, parent_clients_to_server: bool | None = None, align_tracking: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            setup_server_voice: Initial value for SetupServerVoice.
            setup_client_voice: Initial value for SetupClientVoice.
            setup_server_tools: Initial value for SetupServerTools.
            setup_client_tools: Initial value for SetupClientTools.
            parent_clients_to_server: Initial value for ParentClientsToServer.
            align_tracking: Initial value for AlignTracking.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if setup_server_voice is not None:
            self.setup_server_voice = setup_server_voice
        if setup_client_voice is not None:
            self.setup_client_voice = setup_client_voice
        if setup_server_tools is not None:
            self.setup_server_tools = setup_server_tools
        if setup_client_tools is not None:
            self.setup_client_tools = setup_client_tools
        if parent_clients_to_server is not None:
            self.parent_clients_to_server = parent_clients_to_server
        if align_tracking is not None:
            self.align_tracking = align_tracking

    @property
    def setup_server_voice(self) -> bool | None:
        """The SetupServerVoice field value."""
        member = self.get_member("SetupServerVoice")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_server_voice.setter
    def setup_server_voice(self, value: bool) -> None:
        """Set the SetupServerVoice field value."""
        member = self.get_member("SetupServerVoice")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupServerVoice", fields.FieldBool(value=value)
            )

    @property
    def setup_client_voice(self) -> bool | None:
        """The SetupClientVoice field value."""
        member = self.get_member("SetupClientVoice")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_client_voice.setter
    def setup_client_voice(self, value: bool) -> None:
        """Set the SetupClientVoice field value."""
        member = self.get_member("SetupClientVoice")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupClientVoice", fields.FieldBool(value=value)
            )

    @property
    def setup_server_tools(self) -> bool | None:
        """The SetupServerTools field value."""
        member = self.get_member("SetupServerTools")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_server_tools.setter
    def setup_server_tools(self, value: bool) -> None:
        """Set the SetupServerTools field value."""
        member = self.get_member("SetupServerTools")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupServerTools", fields.FieldBool(value=value)
            )

    @property
    def setup_client_tools(self) -> bool | None:
        """The SetupClientTools field value."""
        member = self.get_member("SetupClientTools")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_client_tools.setter
    def setup_client_tools(self, value: bool) -> None:
        """Set the SetupClientTools field value."""
        member = self.get_member("SetupClientTools")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetupClientTools", fields.FieldBool(value=value)
            )

    @property
    def parent_clients_to_server(self) -> bool | None:
        """The ParentClientsToServer field value."""
        member = self.get_member("ParentClientsToServer")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parent_clients_to_server.setter
    def parent_clients_to_server(self, value: bool) -> None:
        """Set the ParentClientsToServer field value."""
        member = self.get_member("ParentClientsToServer")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParentClientsToServer", fields.FieldBool(value=value)
            )

    @property
    def align_tracking(self) -> bool | None:
        """The AlignTracking field value."""
        member = self.get_member("AlignTracking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @align_tracking.setter
    def align_tracking(self, value: bool) -> None:
        """Set the AlignTracking field value."""
        member = self.get_member("AlignTracking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlignTracking", fields.FieldBool(value=value)
            )

