"""Generated component: AudioClipAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioClipAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioClipAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioClipAssetMetadata"

    def __init__(self, audio_clip: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_clip: Initial value for AudioClip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_clip is not None:
            self.audio_clip = audio_clip

    @property
    def audio_clip(self) -> str | None:
        """Target ID of the AudioClip reference (targets IAssetProvider[AudioClip])."""
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
    def sample_rate(self) -> members.EmptyElement | None:
        """The SampleRate member."""
        member = self.get_member("SampleRate")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sample_rate.setter
    def sample_rate(self, value: members.EmptyElement) -> None:
        """Set the SampleRate member."""
        self.set_member("SampleRate", value)

    @property
    def channels(self) -> members.EmptyElement | None:
        """The Channels member."""
        member = self.get_member("Channels")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @channels.setter
    def channels(self, value: members.EmptyElement) -> None:
        """Set the Channels member."""
        self.set_member("Channels", value)

    @property
    def channel_count(self) -> members.EmptyElement | None:
        """The ChannelCount member."""
        member = self.get_member("ChannelCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @channel_count.setter
    def channel_count(self, value: members.EmptyElement) -> None:
        """Set the ChannelCount member."""
        self.set_member("ChannelCount", value)

    @property
    def sample_count(self) -> members.EmptyElement | None:
        """The SampleCount member."""
        member = self.get_member("SampleCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @sample_count.setter
    def sample_count(self, value: members.EmptyElement) -> None:
        """Set the SampleCount member."""
        self.set_member("SampleCount", value)

    @property
    def duration(self) -> members.EmptyElement | None:
        """The Duration member."""
        member = self.get_member("Duration")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @duration.setter
    def duration(self, value: members.EmptyElement) -> None:
        """Set the Duration member."""
        self.set_member("Duration", value)

    @property
    def extension(self) -> members.EmptyElement | None:
        """The Extension member."""
        member = self.get_member("Extension")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @extension.setter
    def extension(self, value: members.EmptyElement) -> None:
        """Set the Extension member."""
        self.set_member("Extension", value)

    @property
    def codec_info(self) -> members.EmptyElement | None:
        """The CodecInfo member."""
        member = self.get_member("CodecInfo")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @codec_info.setter
    def codec_info(self, value: members.EmptyElement) -> None:
        """Set the CodecInfo member."""
        self.set_member("CodecInfo", value)

    @property
    def fully_decoded(self) -> members.EmptyElement | None:
        """The FullyDecoded member."""
        member = self.get_member("FullyDecoded")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @fully_decoded.setter
    def fully_decoded(self, value: members.EmptyElement) -> None:
        """Set the FullyDecoded member."""
        self.set_member("FullyDecoded", value)

