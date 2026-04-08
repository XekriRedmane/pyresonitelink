"""Generated component: VideoTextureProvider."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VideoTextureProvider(GeneratedComponent, ITexture2DProvider, IPlayable, IWorldAudioDataSource, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VideoTextureProvider.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VideoTextureProvider"

    def __init__(self, url: str | None = None, stream: bool | None = None, volume: np.float32 | None = None, force_playback_engine: str | None = None, force_video_streaming_service_parsing: bool | None = None, anisotropic_level: np.int32 | None = None, audio_track_index: np.int32 | None = None, prefer_audio_only: bool | None = None, max_width: np.int32 | None = None, max_height: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            stream: Initial value for Stream.
            volume: Initial value for Volume.
            force_playback_engine: Initial value for ForcePlaybackEngine.
            force_video_streaming_service_parsing: Initial value for ForceVideoStreamingServiceParsing.
            anisotropic_level: Initial value for AnisotropicLevel.
            audio_track_index: Initial value for AudioTrackIndex.
            prefer_audio_only: Initial value for PreferAudioOnly.
            max_width: Initial value for MaxWidth.
            max_height: Initial value for MaxHeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if stream is not None:
            self.stream = stream
        if volume is not None:
            self.volume = volume
        if force_playback_engine is not None:
            self.force_playback_engine = force_playback_engine
        if force_video_streaming_service_parsing is not None:
            self.force_video_streaming_service_parsing = force_video_streaming_service_parsing
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if audio_track_index is not None:
            self.audio_track_index = audio_track_index
        if prefer_audio_only is not None:
            self.prefer_audio_only = prefer_audio_only
        if max_width is not None:
            self.max_width = max_width
        if max_height is not None:
            self.max_height = max_height

    @property
    def playback(self) -> members.SyncPlayback | None:
        """The Playback member."""
        member = self.get_member("Playback")
        if isinstance(member, members.SyncPlayback):
            return member
        return None

    @playback.setter
    def playback(self, value: members.SyncPlayback) -> None:
        """Set the Playback member."""
        self.set_member("Playback", value)

    @property
    def url(self) -> str | None:
        """The URL field value."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def stream(self) -> bool | None:
        """The Stream field value."""
        member = self.get_member("Stream")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stream.setter
    def stream(self, value: bool) -> None:
        """Set the Stream field value."""
        member = self.get_member("Stream")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Stream", fields.FieldBool(value=value)
            )

    @property
    def volume(self) -> np.float32 | None:
        """The Volume field value."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: np.float32) -> None:
        """Set the Volume field value."""
        member = self.get_member("Volume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Volume", fields.FieldFloat(value=value)
            )

    @property
    def force_playback_engine(self) -> str | None:
        """The ForcePlaybackEngine field value."""
        member = self.get_member("ForcePlaybackEngine")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_playback_engine.setter
    def force_playback_engine(self, value: str) -> None:
        """Set the ForcePlaybackEngine field value."""
        member = self.get_member("ForcePlaybackEngine")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForcePlaybackEngine", fields.FieldString(value=value)
            )

    @property
    def force_video_streaming_service_parsing(self) -> bool | None:
        """The ForceVideoStreamingServiceParsing field value."""
        member = self.get_member("ForceVideoStreamingServiceParsing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_video_streaming_service_parsing.setter
    def force_video_streaming_service_parsing(self, value: bool) -> None:
        """Set the ForceVideoStreamingServiceParsing field value."""
        member = self.get_member("ForceVideoStreamingServiceParsing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceVideoStreamingServiceParsing", fields.FieldBool(value=value)
            )

    @property
    def video_title(self) -> members.EmptyElement | None:
        """The VideoTitle member."""
        member = self.get_member("VideoTitle")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @video_title.setter
    def video_title(self, value: members.EmptyElement) -> None:
        """Set the VideoTitle member."""
        self.set_member("VideoTitle", value)

    @property
    def current_playback_engine(self) -> members.EmptyElement | None:
        """The CurrentPlaybackEngine member."""
        member = self.get_member("CurrentPlaybackEngine")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @current_playback_engine.setter
    def current_playback_engine(self, value: members.EmptyElement) -> None:
        """Set the CurrentPlaybackEngine member."""
        self.set_member("CurrentPlaybackEngine", value)

    @property
    def current_clock_error(self) -> members.EmptyElement | None:
        """The CurrentClockError member."""
        member = self.get_member("CurrentClockError")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @current_clock_error.setter
    def current_clock_error(self, value: members.EmptyElement) -> None:
        """Set the CurrentClockError member."""
        self.set_member("CurrentClockError", value)

    @property
    def filter_mode(self) -> members.FieldEnum | None:
        """The FilterMode member."""
        member = self.get_member("FilterMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @filter_mode.setter
    def filter_mode(self, value: members.FieldEnum) -> None:
        """Set the FilterMode member."""
        self.set_member("FilterMode", value)

    @property
    def anisotropic_level(self) -> np.int32 | None:
        """The AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anisotropic_level.setter
    def anisotropic_level(self, value: np.int32) -> None:
        """Set the AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnisotropicLevel", fields.FieldInt(value=value)
            )

    @property
    def wrap_mode_u(self) -> members.FieldEnum | None:
        """The WrapModeU member."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: members.FieldEnum) -> None:
        """Set the WrapModeU member."""
        self.set_member("WrapModeU", value)

    @property
    def wrap_mode_v(self) -> members.FieldEnum | None:
        """The WrapModeV member."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: members.FieldEnum) -> None:
        """Set the WrapModeV member."""
        self.set_member("WrapModeV", value)

    @property
    def audio_track_index(self) -> np.int32 | None:
        """The AudioTrackIndex field value."""
        member = self.get_member("AudioTrackIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @audio_track_index.setter
    def audio_track_index(self, value: np.int32) -> None:
        """Set the AudioTrackIndex field value."""
        member = self.get_member("AudioTrackIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AudioTrackIndex", fields.FieldNullableInt(value=value)
            )

    @property
    def prefer_audio_only(self) -> bool | None:
        """The PreferAudioOnly field value."""
        member = self.get_member("PreferAudioOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @prefer_audio_only.setter
    def prefer_audio_only(self, value: bool) -> None:
        """Set the PreferAudioOnly field value."""
        member = self.get_member("PreferAudioOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreferAudioOnly", fields.FieldBool(value=value)
            )

    @property
    def max_width(self) -> np.int32 | None:
        """The MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_width.setter
    def max_width(self, value: np.int32) -> None:
        """Set the MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxWidth", fields.FieldNullableInt(value=value)
            )

    @property
    def max_height(self) -> np.int32 | None:
        """The MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_height.setter
    def max_height(self, value: np.int32) -> None:
        """Set the MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxHeight", fields.FieldNullableInt(value=value)
            )

