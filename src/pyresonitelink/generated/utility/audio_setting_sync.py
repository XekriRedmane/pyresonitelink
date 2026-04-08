"""Generated component: AudioSettingSync."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioSettingSync(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioSettingSync.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioSettingSync"

    def __init__(self, default_audio_input_device_index: primitives.Int | None = None, default_audio_output_device_index: primitives.Int | None = None, master_volume: primitives.Float | None = None, whisper_voice_volume: primitives.Float | None = None, noise_gate_threshold: primitives.Float | None = None, noise_gate_attack: primitives.Float | None = None, noise_gate_hold: primitives.Float | None = None, noise_gate_release: primitives.Float | None = None, normalization_threshold: primitives.Float | None = None, voice_normalization: primitives.Bool | None = None, noise_supression: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default_audio_input_device_index: Initial value for DefaultAudioInputDeviceIndex.
            default_audio_output_device_index: Initial value for DefaultAudioOutputDeviceIndex.
            master_volume: Initial value for MasterVolume.
            whisper_voice_volume: Initial value for WhisperVoiceVolume.
            noise_gate_threshold: Initial value for NoiseGateThreshold.
            noise_gate_attack: Initial value for NoiseGateAttack.
            noise_gate_hold: Initial value for NoiseGateHold.
            noise_gate_release: Initial value for NoiseGateRelease.
            normalization_threshold: Initial value for NormalizationThreshold.
            voice_normalization: Initial value for VoiceNormalization.
            noise_supression: Initial value for NoiseSupression.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default_audio_input_device_index is not None:
            self.default_audio_input_device_index = default_audio_input_device_index
        if default_audio_output_device_index is not None:
            self.default_audio_output_device_index = default_audio_output_device_index
        if master_volume is not None:
            self.master_volume = master_volume
        if whisper_voice_volume is not None:
            self.whisper_voice_volume = whisper_voice_volume
        if noise_gate_threshold is not None:
            self.noise_gate_threshold = noise_gate_threshold
        if noise_gate_attack is not None:
            self.noise_gate_attack = noise_gate_attack
        if noise_gate_hold is not None:
            self.noise_gate_hold = noise_gate_hold
        if noise_gate_release is not None:
            self.noise_gate_release = noise_gate_release
        if normalization_threshold is not None:
            self.normalization_threshold = normalization_threshold
        if voice_normalization is not None:
            self.voice_normalization = voice_normalization
        if noise_supression is not None:
            self.noise_supression = noise_supression

    @property
    def default_audio_input_device_index(self) -> primitives.Int | None:
        """The DefaultAudioInputDeviceIndex field value."""
        member = self.get_member("DefaultAudioInputDeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_audio_input_device_index.setter
    def default_audio_input_device_index(self, value: primitives.Int) -> None:
        """Set the DefaultAudioInputDeviceIndex field value."""
        member = self.get_member("DefaultAudioInputDeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultAudioInputDeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def default_audio_output_device_index(self) -> primitives.Int | None:
        """The DefaultAudioOutputDeviceIndex field value."""
        member = self.get_member("DefaultAudioOutputDeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_audio_output_device_index.setter
    def default_audio_output_device_index(self, value: primitives.Int) -> None:
        """Set the DefaultAudioOutputDeviceIndex field value."""
        member = self.get_member("DefaultAudioOutputDeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultAudioOutputDeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def master_volume(self) -> primitives.Float | None:
        """The MasterVolume field value."""
        member = self.get_member("MasterVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @master_volume.setter
    def master_volume(self, value: primitives.Float) -> None:
        """Set the MasterVolume field value."""
        member = self.get_member("MasterVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MasterVolume", fields.FieldFloat(value=value)
            )

    @property
    def whisper_voice_volume(self) -> primitives.Float | None:
        """The WhisperVoiceVolume field value."""
        member = self.get_member("WhisperVoiceVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @whisper_voice_volume.setter
    def whisper_voice_volume(self, value: primitives.Float) -> None:
        """Set the WhisperVoiceVolume field value."""
        member = self.get_member("WhisperVoiceVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WhisperVoiceVolume", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_threshold(self) -> primitives.Float | None:
        """The NoiseGateThreshold field value."""
        member = self.get_member("NoiseGateThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_threshold.setter
    def noise_gate_threshold(self, value: primitives.Float) -> None:
        """Set the NoiseGateThreshold field value."""
        member = self.get_member("NoiseGateThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateThreshold", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_attack(self) -> primitives.Float | None:
        """The NoiseGateAttack field value."""
        member = self.get_member("NoiseGateAttack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_attack.setter
    def noise_gate_attack(self, value: primitives.Float) -> None:
        """Set the NoiseGateAttack field value."""
        member = self.get_member("NoiseGateAttack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateAttack", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_hold(self) -> primitives.Float | None:
        """The NoiseGateHold field value."""
        member = self.get_member("NoiseGateHold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_hold.setter
    def noise_gate_hold(self, value: primitives.Float) -> None:
        """Set the NoiseGateHold field value."""
        member = self.get_member("NoiseGateHold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateHold", fields.FieldFloat(value=value)
            )

    @property
    def noise_gate_release(self) -> primitives.Float | None:
        """The NoiseGateRelease field value."""
        member = self.get_member("NoiseGateRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_gate_release.setter
    def noise_gate_release(self, value: primitives.Float) -> None:
        """Set the NoiseGateRelease field value."""
        member = self.get_member("NoiseGateRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseGateRelease", fields.FieldFloat(value=value)
            )

    @property
    def normalization_threshold(self) -> primitives.Float | None:
        """The NormalizationThreshold field value."""
        member = self.get_member("NormalizationThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalization_threshold.setter
    def normalization_threshold(self, value: primitives.Float) -> None:
        """Set the NormalizationThreshold field value."""
        member = self.get_member("NormalizationThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizationThreshold", fields.FieldFloat(value=value)
            )

    @property
    def voice_normalization(self) -> primitives.Bool | None:
        """The VoiceNormalization field value."""
        member = self.get_member("VoiceNormalization")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @voice_normalization.setter
    def voice_normalization(self, value: primitives.Bool) -> None:
        """Set the VoiceNormalization field value."""
        member = self.get_member("VoiceNormalization")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VoiceNormalization", fields.FieldBool(value=value)
            )

    @property
    def noise_supression(self) -> primitives.Bool | None:
        """The NoiseSupression field value."""
        member = self.get_member("NoiseSupression")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_supression.setter
    def noise_supression(self, value: primitives.Bool) -> None:
        """Set the NoiseSupression field value."""
        member = self.get_member("NoiseSupression")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseSupression", fields.FieldBool(value=value)
            )

