"""Generated component: LocalAudioDeviceStream."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalAudioDeviceStream(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """The LocalAudioDeviceStream component can be used as a source of streamed audio data kind of like a player or a video for use with audio output components. This component Outputs locally the audio for a specified audio input Device by index number.

    Can be used to listen to a specified audio device index using an audio
    output. Can be used in world space and isn't limited to userspace.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalAudioDeviceStream"

    def __init__(self, audio_device_index: primitives.Int | None = None, use_filtered_data: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_device_index: Initial value for AudioDeviceIndex.
            use_filtered_data: Initial value for UseFilteredData.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_device_index is not None:
            self.audio_device_index = audio_device_index
        if use_filtered_data is not None:
            self.use_filtered_data = use_filtered_data

    @property
    def audio_device_index(self) -> primitives.Int | None:
        """The audio device to gather audio samples from."""
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
    def use_filtered_data(self) -> primitives.Bool | None:
        """Whether to use raw audio samples or filter them."""
        member = self.get_member("UseFilteredData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_filtered_data.setter
    def use_filtered_data(self, value: primitives.Bool) -> None:
        """Set the UseFilteredData field value."""
        member = self.get_member("UseFilteredData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFilteredData", fields.FieldBool(value=value)
            )

