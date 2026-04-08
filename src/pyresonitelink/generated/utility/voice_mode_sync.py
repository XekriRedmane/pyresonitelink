"""Generated component: VoiceModeSync."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VoiceModeSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VoiceModeSync.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VoiceModeSync"

    def __init__(self, global_mute: primitives.Bool | None = None, broadcast_allowed: primitives.Bool | None = None, shout_allowed: primitives.Bool | None = None, normal_allowed: primitives.Bool | None = None, whisper_allowed: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            global_mute: Initial value for GlobalMute.
            broadcast_allowed: Initial value for BroadcastAllowed.
            shout_allowed: Initial value for ShoutAllowed.
            normal_allowed: Initial value for NormalAllowed.
            whisper_allowed: Initial value for WhisperAllowed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if global_mute is not None:
            self.global_mute = global_mute
        if broadcast_allowed is not None:
            self.broadcast_allowed = broadcast_allowed
        if shout_allowed is not None:
            self.shout_allowed = shout_allowed
        if normal_allowed is not None:
            self.normal_allowed = normal_allowed
        if whisper_allowed is not None:
            self.whisper_allowed = whisper_allowed

    @property
    def focused_world_voice_mode(self) -> members.FieldEnum | None:
        """The FocusedWorldVoiceMode member."""
        member = self.get_member("FocusedWorldVoiceMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @focused_world_voice_mode.setter
    def focused_world_voice_mode(self, value: members.FieldEnum) -> None:
        """Set the FocusedWorldVoiceMode member."""
        self.set_member("FocusedWorldVoiceMode", value)

    @property
    def global_mute(self) -> primitives.Bool | None:
        """The GlobalMute field value."""
        member = self.get_member("GlobalMute")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_mute.setter
    def global_mute(self, value: primitives.Bool) -> None:
        """Set the GlobalMute field value."""
        member = self.get_member("GlobalMute")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalMute", fields.FieldBool(value=value)
            )

    @property
    def focused_world_max_allowed_voice_mode(self) -> members.FieldEnum | None:
        """The FocusedWorldMaxAllowedVoiceMode member."""
        member = self.get_member("FocusedWorldMaxAllowedVoiceMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @focused_world_max_allowed_voice_mode.setter
    def focused_world_max_allowed_voice_mode(self, value: members.FieldEnum) -> None:
        """Set the FocusedWorldMaxAllowedVoiceMode member."""
        self.set_member("FocusedWorldMaxAllowedVoiceMode", value)

    @property
    def broadcast_allowed(self) -> primitives.Bool | None:
        """The BroadcastAllowed field value."""
        member = self.get_member("BroadcastAllowed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @broadcast_allowed.setter
    def broadcast_allowed(self, value: primitives.Bool) -> None:
        """Set the BroadcastAllowed field value."""
        member = self.get_member("BroadcastAllowed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BroadcastAllowed", fields.FieldBool(value=value)
            )

    @property
    def shout_allowed(self) -> primitives.Bool | None:
        """The ShoutAllowed field value."""
        member = self.get_member("ShoutAllowed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shout_allowed.setter
    def shout_allowed(self, value: primitives.Bool) -> None:
        """Set the ShoutAllowed field value."""
        member = self.get_member("ShoutAllowed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShoutAllowed", fields.FieldBool(value=value)
            )

    @property
    def normal_allowed(self) -> primitives.Bool | None:
        """The NormalAllowed field value."""
        member = self.get_member("NormalAllowed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_allowed.setter
    def normal_allowed(self, value: primitives.Bool) -> None:
        """Set the NormalAllowed field value."""
        member = self.get_member("NormalAllowed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalAllowed", fields.FieldBool(value=value)
            )

    @property
    def whisper_allowed(self) -> primitives.Bool | None:
        """The WhisperAllowed field value."""
        member = self.get_member("WhisperAllowed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @whisper_allowed.setter
    def whisper_allowed(self, value: primitives.Bool) -> None:
        """Set the WhisperAllowed field value."""
        member = self.get_member("WhisperAllowed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WhisperAllowed", fields.FieldBool(value=value)
            )

