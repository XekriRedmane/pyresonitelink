"""Generated component: AudioVolumeSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioVolumeSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioVolumeSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioVolumeSettings"

    def __init__(self, master_volume: np.float32 | None = None, sound_effect_volume: np.float32 | None = None, multimedia_volume: np.float32 | None = None, voice_volume: np.float32 | None = None, user_interface_volume: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            master_volume: Initial value for MasterVolume.
            sound_effect_volume: Initial value for SoundEffectVolume.
            multimedia_volume: Initial value for MultimediaVolume.
            voice_volume: Initial value for VoiceVolume.
            user_interface_volume: Initial value for UserInterfaceVolume.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if master_volume is not None:
            self.master_volume = master_volume
        if sound_effect_volume is not None:
            self.sound_effect_volume = sound_effect_volume
        if multimedia_volume is not None:
            self.multimedia_volume = multimedia_volume
        if voice_volume is not None:
            self.voice_volume = voice_volume
        if user_interface_volume is not None:
            self.user_interface_volume = user_interface_volume

    @property
    def master_volume(self) -> np.float32 | None:
        """The MasterVolume field value."""
        member = self.get_member("MasterVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @master_volume.setter
    def master_volume(self, value: np.float32) -> None:
        """Set the MasterVolume field value."""
        member = self.get_member("MasterVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MasterVolume", fields.FieldFloat(value=value)
            )

    @property
    def sound_effect_volume(self) -> np.float32 | None:
        """The SoundEffectVolume field value."""
        member = self.get_member("SoundEffectVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sound_effect_volume.setter
    def sound_effect_volume(self, value: np.float32) -> None:
        """Set the SoundEffectVolume field value."""
        member = self.get_member("SoundEffectVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SoundEffectVolume", fields.FieldFloat(value=value)
            )

    @property
    def multimedia_volume(self) -> np.float32 | None:
        """The MultimediaVolume field value."""
        member = self.get_member("MultimediaVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multimedia_volume.setter
    def multimedia_volume(self, value: np.float32) -> None:
        """Set the MultimediaVolume field value."""
        member = self.get_member("MultimediaVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultimediaVolume", fields.FieldFloat(value=value)
            )

    @property
    def voice_volume(self) -> np.float32 | None:
        """The VoiceVolume field value."""
        member = self.get_member("VoiceVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @voice_volume.setter
    def voice_volume(self, value: np.float32) -> None:
        """Set the VoiceVolume field value."""
        member = self.get_member("VoiceVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VoiceVolume", fields.FieldFloat(value=value)
            )

    @property
    def user_interface_volume(self) -> np.float32 | None:
        """The UserInterfaceVolume field value."""
        member = self.get_member("UserInterfaceVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_interface_volume.setter
    def user_interface_volume(self, value: np.float32) -> None:
        """Set the UserInterfaceVolume field value."""
        member = self.get_member("UserInterfaceVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserInterfaceVolume", fields.FieldFloat(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

