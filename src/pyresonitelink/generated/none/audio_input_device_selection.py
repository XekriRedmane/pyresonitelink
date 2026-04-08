"""Generated component: AudioInputDeviceSelection."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.local_audio_device_stream import LocalAudioDeviceStream
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.volume_meter import VolumeMeter
from pyresonitelink.generated._types.progress_bar import ProgressBar
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioInputDeviceSelection(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioInputDeviceSelection.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioInputDeviceSelection"

    def __init__(self, selected_device_index: primitives.Int | None = None, selected_device_name: primitives.String | None = None, use_filtered_data: primitives.Bool | None = None, device_button_root: str | Slot | None = None, audio_stream: str | LocalAudioDeviceStream | None = None, audio_output: str | AudioOutput | None = None, device_volume: str | VolumeMeter | None = None, volume_bar: str | ProgressBar | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selected_device_index: Initial value for SelectedDeviceIndex.
            selected_device_name: Initial value for SelectedDeviceName.
            use_filtered_data: Initial value for UseFilteredData.
            device_button_root: Initial value for _deviceButtonRoot.
            audio_stream: Initial value for _audioStream.
            audio_output: Initial value for _audioOutput.
            device_volume: Initial value for _deviceVolume.
            volume_bar: Initial value for _volumeBar.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selected_device_index is not None:
            self.selected_device_index = selected_device_index
        if selected_device_name is not None:
            self.selected_device_name = selected_device_name
        if use_filtered_data is not None:
            self.use_filtered_data = use_filtered_data
        if device_button_root is not None:
            self.device_button_root = device_button_root
        if audio_stream is not None:
            self.audio_stream = audio_stream
        if audio_output is not None:
            self.audio_output = audio_output
        if device_volume is not None:
            self.device_volume = device_volume
        if volume_bar is not None:
            self.volume_bar = volume_bar

    @property
    def selected_device_index(self) -> primitives.Int | None:
        """The SelectedDeviceIndex field value."""
        member = self.get_member("SelectedDeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_device_index.setter
    def selected_device_index(self, value: primitives.Int) -> None:
        """Set the SelectedDeviceIndex field value."""
        member = self.get_member("SelectedDeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedDeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def selected_device_name(self) -> primitives.String | None:
        """The SelectedDeviceName field value."""
        member = self.get_member("SelectedDeviceName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_device_name.setter
    def selected_device_name(self, value: primitives.String) -> None:
        """Set the SelectedDeviceName field value."""
        member = self.get_member("SelectedDeviceName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedDeviceName", fields.FieldString(value=value)
            )

    @property
    def use_filtered_data(self) -> primitives.Bool | None:
        """The UseFilteredData field value."""
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

    @property
    def device_button_root(self) -> str | None:
        """Target ID of the _deviceButtonRoot reference (targets Slot)."""
        member = self.get_member("_deviceButtonRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @device_button_root.setter
    def device_button_root(self, target: str | Slot | None) -> None:
        """Set the _deviceButtonRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_deviceButtonRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_deviceButtonRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def audio_stream(self) -> str | None:
        """Target ID of the _audioStream reference (targets LocalAudioDeviceStream)."""
        member = self.get_member("_audioStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_stream.setter
    def audio_stream(self, target: str | LocalAudioDeviceStream | None) -> None:
        """Set the _audioStream reference by target ID or LocalAudioDeviceStream instance."""
        target_id: str | None = target.id if isinstance(target, LocalAudioDeviceStream) else target  # type: ignore[assignment]
        member = self.get_member("_audioStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_audioStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LocalAudioDeviceStream'),
            )

    @property
    def audio_output(self) -> str | None:
        """Target ID of the _audioOutput reference (targets AudioOutput)."""
        member = self.get_member("_audioOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_output.setter
    def audio_output(self, target: str | AudioOutput | None) -> None:
        """Set the _audioOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("_audioOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_audioOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def device_volume(self) -> str | None:
        """Target ID of the _deviceVolume reference (targets VolumeMeter)."""
        member = self.get_member("_deviceVolume")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @device_volume.setter
    def device_volume(self, target: str | VolumeMeter | None) -> None:
        """Set the _deviceVolume reference by target ID or VolumeMeter instance."""
        target_id: str | None = target.id if isinstance(target, VolumeMeter) else target  # type: ignore[assignment]
        member = self.get_member("_deviceVolume")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_deviceVolume",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VolumeMeter'),
            )

    @property
    def volume_bar(self) -> str | None:
        """Target ID of the _volumeBar reference (targets ProgressBar)."""
        member = self.get_member("_volumeBar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_bar.setter
    def volume_bar(self, target: str | ProgressBar | None) -> None:
        """Set the _volumeBar reference by target ID or ProgressBar instance."""
        target_id: str | None = target.id if isinstance(target, ProgressBar) else target  # type: ignore[assignment]
        member = self.get_member("_volumeBar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volumeBar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.ProgressBar'),
            )

