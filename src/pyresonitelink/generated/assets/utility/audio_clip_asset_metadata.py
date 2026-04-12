"""Generated component: AudioClipAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.channel_configuration import ChannelConfiguration
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioClipAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Audio Clip Asset Metadata is a component that will populate itself with different small bits of information about an audio clip, also known as metadata.
The metadata will be the default values until an audio clip is provided, which will then populate the data.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioClipAssetMetadata"

    def __init__(self, audio_clip: str | IAssetProvider[AudioClip] | None = None, sample_rate: primitives.Int | None = None, channels: ChannelConfiguration | str | None = None, channel_count: primitives.Int | None = None, sample_count: primitives.Int | None = None, duration: primitives.Double | None = None, extension: primitives.String | None = None, codec_info: primitives.String | None = None, fully_decoded: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_clip: Initial value for AudioClip.
            sample_rate: Initial value for SampleRate.
            channels: Initial value for Channels.
            channel_count: Initial value for ChannelCount.
            sample_count: Initial value for SampleCount.
            duration: Initial value for Duration.
            extension: Initial value for Extension.
            codec_info: Initial value for CodecInfo.
            fully_decoded: Initial value for FullyDecoded.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_clip is not None:
            self.audio_clip = audio_clip
        if sample_rate is not None:
            self.sample_rate = sample_rate
        if channels is not None:
            self.channels = channels
        if channel_count is not None:
            self.channel_count = channel_count
        if sample_count is not None:
            self.sample_count = sample_count
        if duration is not None:
            self.duration = duration
        if extension is not None:
            self.extension = extension
        if codec_info is not None:
            self.codec_info = codec_info
        if fully_decoded is not None:
            self.fully_decoded = fully_decoded

    @property
    def audio_clip(self) -> str | None:
        """The audio clip to read metadata from"""
        member = self.get_member("AudioClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_clip.setter
    def audio_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the AudioClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AudioClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AudioClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def sample_rate(self) -> primitives.Int | None:
        """The Hz the audio is sampled at."""
        member = self.get_member("SampleRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sample_rate.setter
    def sample_rate(self, value: primitives.Int) -> None:
        """Set the SampleRate field value."""
        member = self.get_member("SampleRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SampleRate", fields.FieldInt(value=value)
            )

    @property
    def channels(self) -> ChannelConfiguration | None:
        """The audio channel configuration the audio was recorded in."""
        member = self.get_member("Channels")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ChannelConfiguration(member.value)
        return None

    @channels.setter
    def channels(self, value: ChannelConfiguration | str) -> None:
        """Set Channels. The audio channel configuration the audio was recorded in."""
        member = self.get_member("Channels")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Channels",
                members.FieldEnum(value=str(value)),
            )

    @property
    def channel_count(self) -> primitives.Int | None:
        """How many channels are in the audio recording. usually 1 channel for mono or 2 channels for L and R Stereo."""
        member = self.get_member("ChannelCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @channel_count.setter
    def channel_count(self, value: primitives.Int) -> None:
        """Set the ChannelCount field value."""
        member = self.get_member("ChannelCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChannelCount", fields.FieldInt(value=value)
            )

    @property
    def sample_count(self) -> primitives.Int | None:
        """how many total samples the audio clip has"""
        member = self.get_member("SampleCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sample_count.setter
    def sample_count(self, value: primitives.Int) -> None:
        """Set the SampleCount field value."""
        member = self.get_member("SampleCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SampleCount", fields.FieldInt(value=value)
            )

    @property
    def duration(self) -> primitives.Double | None:
        """How long the audio clip is in seconds."""
        member = self.get_member("Duration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @duration.setter
    def duration(self, value: primitives.Double) -> None:
        """Set the Duration field value."""
        member = self.get_member("Duration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Duration", fields.FieldDouble(value=value)
            )

    @property
    def extension(self) -> primitives.String | None:
        """the extension of the file type the audio was recorded in."""
        member = self.get_member("Extension")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @extension.setter
    def extension(self, value: primitives.String) -> None:
        """Set the Extension field value."""
        member = self.get_member("Extension")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Extension", fields.FieldString(value=value)
            )

    @property
    def codec_info(self) -> primitives.String | None:
        """The codec the audio is written in like WAV or FLAC and the quality of the audio."""
        member = self.get_member("CodecInfo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @codec_info.setter
    def codec_info(self, value: primitives.String) -> None:
        """Set the CodecInfo field value."""
        member = self.get_member("CodecInfo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CodecInfo", fields.FieldString(value=value)
            )

    @property
    def fully_decoded(self) -> primitives.Bool | None:
        """If the audio is loaded or not and decoded (Waveform visible)"""
        member = self.get_member("FullyDecoded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fully_decoded.setter
    def fully_decoded(self, value: primitives.Bool) -> None:
        """Set the FullyDecoded field value."""
        member = self.get_member("FullyDecoded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullyDecoded", fields.FieldBool(value=value)
            )

