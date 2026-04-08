"""Generated component: LocalAudioDeviceStream."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocalAudioDeviceStream(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocalAudioDeviceStream.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocalAudioDeviceStream"

    def __init__(self, audio_device_index: np.int32 | None = None, use_filtered_data: bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def audio_device_index(self) -> np.int32 | None:
        """The AudioDeviceIndex field value."""
        member = self.get_member("AudioDeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @audio_device_index.setter
    def audio_device_index(self, value: np.int32) -> None:
        """Set the AudioDeviceIndex field value."""
        member = self.get_member("AudioDeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AudioDeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def use_filtered_data(self) -> bool | None:
        """The UseFilteredData field value."""
        member = self.get_member("UseFilteredData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_filtered_data.setter
    def use_filtered_data(self, value: bool) -> None:
        """Set the UseFilteredData field value."""
        member = self.get_member("UseFilteredData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFilteredData", fields.FieldBool(value=value)
            )

