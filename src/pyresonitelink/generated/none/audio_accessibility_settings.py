"""Generated component: AudioAccessibilitySettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioAccessibilitySettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioAccessibilitySettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioAccessibilitySettings"

    def __init__(self, whisper_volume: np.float32 | None = None, voice_message_volume: np.float32 | None = None, force_voice_audio_effects_off: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            whisper_volume: Initial value for WhisperVolume.
            voice_message_volume: Initial value for VoiceMessageVolume.
            force_voice_audio_effects_off: Initial value for ForceVoiceAudioEffectsOff.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if whisper_volume is not None:
            self.whisper_volume = whisper_volume
        if voice_message_volume is not None:
            self.voice_message_volume = voice_message_volume
        if force_voice_audio_effects_off is not None:
            self.force_voice_audio_effects_off = force_voice_audio_effects_off

    @property
    def whisper_volume(self) -> np.float32 | None:
        """The WhisperVolume field value."""
        member = self.get_member("WhisperVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @whisper_volume.setter
    def whisper_volume(self, value: np.float32) -> None:
        """Set the WhisperVolume field value."""
        member = self.get_member("WhisperVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WhisperVolume", fields.FieldFloat(value=value)
            )

    @property
    def voice_message_volume(self) -> np.float32 | None:
        """The VoiceMessageVolume field value."""
        member = self.get_member("VoiceMessageVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @voice_message_volume.setter
    def voice_message_volume(self, value: np.float32) -> None:
        """Set the VoiceMessageVolume field value."""
        member = self.get_member("VoiceMessageVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VoiceMessageVolume", fields.FieldFloat(value=value)
            )

    @property
    def force_voice_audio_effects_off(self) -> bool | None:
        """The ForceVoiceAudioEffectsOff field value."""
        member = self.get_member("ForceVoiceAudioEffectsOff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_voice_audio_effects_off.setter
    def force_voice_audio_effects_off(self, value: bool) -> None:
        """Set the ForceVoiceAudioEffectsOff field value."""
        member = self.get_member("ForceVoiceAudioEffectsOff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceVoiceAudioEffectsOff", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

