"""Generated component: AudioDeviceVolume."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioDeviceVolume(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AudioDeviceVolume component only functions in dash space. If ``AudioDeviceIndex`` is negative, then it uses the user's set default audio device. This component is used to manage the volume of an input device like a microphone for one example. This is a settings component.

    Category: Userspace
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioDeviceVolume"

    def __init__(self, audio_device_index: primitives.Int | None = None, volume: primitives.Float | None = None, normalized_volume: primitives.Float | None = None, smoothing: primitives.Float | None = None, power: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_device_index: Initial value for AudioDeviceIndex.
            volume: Initial value for Volume.
            normalized_volume: Initial value for NormalizedVolume.
            smoothing: Initial value for Smoothing.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_device_index is not None:
            self.audio_device_index = audio_device_index
        if volume is not None:
            self.volume = volume
        if normalized_volume is not None:
            self.normalized_volume = normalized_volume
        if smoothing is not None:
            self.smoothing = smoothing
        if power is not None:
            self.power = power

    @property
    def audio_device_index(self) -> primitives.Int | None:
        """The audio input device by OS audio manager index to modify the volume for."""
        member = self.get_member("AudioDeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @audio_device_index.setter
    def audio_device_index(self, value: primitives.Int) -> None:
        """Set the AudioDeviceIndex field value."""
        member = self.get_member("AudioDeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AudioDeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def volume(self) -> primitives.Float | None:
        """The volume the input device should have."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: primitives.Float) -> None:
        """Set the Volume field value."""
        member = self.get_member("Volume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Volume", fields.FieldFloat(value=value)
            )

    @property
    def normalized_volume(self) -> primitives.Float | None:
        """The component uses this value to boost the output noise to a higher volume when it is too quiet or reduce the volume when it is too loud."""
        member = self.get_member("NormalizedVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normalized_volume.setter
    def normalized_volume(self, value: primitives.Float) -> None:
        """Set the NormalizedVolume field value."""
        member = self.get_member("NormalizedVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalizedVolume", fields.FieldFloat(value=value)
            )

    @property
    def smoothing(self) -> primitives.Float | None:
        """How fast to reduce or increase the volume when it gets too loud or quiet"""
        member = self.get_member("Smoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothing.setter
    def smoothing(self, value: primitives.Float) -> None:
        """Set the Smoothing field value."""
        member = self.get_member("Smoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothing", fields.FieldFloat(value=value)
            )

    @property
    def power(self) -> primitives.Float | None:
        """The amount to boost the volume overall before normalization."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: primitives.Float) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

