"""Generated component: AudioStreamController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iaudio_stream import IAudioStream
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioStreamController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioStreamController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioStreamController"

    def __init__(self, stream: str | IAudioStream | None = None, audio_output: str | AudioOutput | None = None, is_playing_for_owner: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stream: Initial value for Stream.
            audio_output: Initial value for AudioOutput.
            is_playing_for_owner: Initial value for IsPlayingForOwner.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stream is not None:
            self.stream = stream
        if audio_output is not None:
            self.audio_output = audio_output
        if is_playing_for_owner is not None:
            self.is_playing_for_owner = is_playing_for_owner

    @property
    def stream(self) -> str | None:
        """Target ID of the Stream reference (targets IAudioStream)."""
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream.setter
    def stream(self, target: str | IAudioStream | None) -> None:
        """Set the Stream reference by target ID or IAudioStream instance."""
        target_id: str | None = target.id if isinstance(target, IAudioStream) else target  # type: ignore[assignment]
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAudioStream'),
            )

    @property
    def audio_output(self) -> str | None:
        """Target ID of the AudioOutput reference (targets AudioOutput)."""
        member = self.get_member("AudioOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_output.setter
    def audio_output(self, target: str | AudioOutput | None) -> None:
        """Set the AudioOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("AudioOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AudioOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def is_playing_for_owner(self) -> primitives.Bool | None:
        """The IsPlayingForOwner field value."""
        member = self.get_member("IsPlayingForOwner")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_playing_for_owner.setter
    def is_playing_for_owner(self, value: primitives.Bool) -> None:
        """Set the IsPlayingForOwner field value."""
        member = self.get_member("IsPlayingForOwner")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsPlayingForOwner", fields.FieldBool(value=value)
            )

    async def on_toggle_broadcast(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the OnToggleBroadcast sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OnToggleBroadcast", {"button": button, "eventData": event_data}, debug,
        )

    async def on_toggle_play_for_owner(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the OnTogglePlayForOwner sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OnTogglePlayForOwner", {"button": button, "eventData": event_data}, debug,
        )

