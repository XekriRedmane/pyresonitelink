"""Generated component: VideoTextureProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
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

    def __init__(self, url: str | None = None, stream: primitives.Bool | None = None, volume: primitives.Float | None = None, force_playback_engine: primitives.String | None = None, force_video_streaming_service_parsing: primitives.Bool | None = None, video_title: primitives.String | None = None, current_playback_engine: primitives.String | None = None, current_clock_error: primitives.Float | None = None, anisotropic_level: primitives.Int | None = None, audio_track_index: primitives.Int | None = None, prefer_audio_only: primitives.Bool | None = None, max_width: primitives.Int | None = None, max_height: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            stream: Initial value for Stream.
            volume: Initial value for Volume.
            force_playback_engine: Initial value for ForcePlaybackEngine.
            force_video_streaming_service_parsing: Initial value for ForceVideoStreamingServiceParsing.
            video_title: Initial value for VideoTitle.
            current_playback_engine: Initial value for CurrentPlaybackEngine.
            current_clock_error: Initial value for CurrentClockError.
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
        if video_title is not None:
            self.video_title = video_title
        if current_playback_engine is not None:
            self.current_playback_engine = current_playback_engine
        if current_clock_error is not None:
            self.current_clock_error = current_clock_error
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
    def stream(self) -> primitives.Bool | None:
        """The Stream field value."""
        member = self.get_member("Stream")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stream.setter
    def stream(self, value: primitives.Bool) -> None:
        """Set the Stream field value."""
        member = self.get_member("Stream")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Stream", fields.FieldBool(value=value)
            )

    @property
    def volume(self) -> primitives.Float | None:
        """The Volume field value."""
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
    def force_playback_engine(self) -> primitives.String | None:
        """The ForcePlaybackEngine field value."""
        member = self.get_member("ForcePlaybackEngine")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_playback_engine.setter
    def force_playback_engine(self, value: primitives.String) -> None:
        """Set the ForcePlaybackEngine field value."""
        member = self.get_member("ForcePlaybackEngine")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForcePlaybackEngine", fields.FieldString(value=value)
            )

    @property
    def force_video_streaming_service_parsing(self) -> primitives.Bool | None:
        """The ForceVideoStreamingServiceParsing field value."""
        member = self.get_member("ForceVideoStreamingServiceParsing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_video_streaming_service_parsing.setter
    def force_video_streaming_service_parsing(self, value: primitives.Bool) -> None:
        """Set the ForceVideoStreamingServiceParsing field value."""
        member = self.get_member("ForceVideoStreamingServiceParsing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceVideoStreamingServiceParsing", fields.FieldBool(value=value)
            )

    @property
    def video_title(self) -> primitives.String | None:
        """The VideoTitle field value."""
        member = self.get_member("VideoTitle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @video_title.setter
    def video_title(self, value: primitives.String) -> None:
        """Set the VideoTitle field value."""
        member = self.get_member("VideoTitle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VideoTitle", fields.FieldString(value=value)
            )

    @property
    def current_playback_engine(self) -> primitives.String | None:
        """The CurrentPlaybackEngine field value."""
        member = self.get_member("CurrentPlaybackEngine")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_playback_engine.setter
    def current_playback_engine(self, value: primitives.String) -> None:
        """Set the CurrentPlaybackEngine field value."""
        member = self.get_member("CurrentPlaybackEngine")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentPlaybackEngine", fields.FieldString(value=value)
            )

    @property
    def current_clock_error(self) -> primitives.Float | None:
        """The CurrentClockError field value."""
        member = self.get_member("CurrentClockError")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_clock_error.setter
    def current_clock_error(self, value: primitives.Float) -> None:
        """Set the CurrentClockError field value."""
        member = self.get_member("CurrentClockError")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentClockError", fields.FieldFloat(value=value)
            )

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
    def anisotropic_level(self) -> primitives.Int | None:
        """The AnisotropicLevel field value."""
        member = self.get_member("AnisotropicLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anisotropic_level.setter
    def anisotropic_level(self, value: primitives.Int) -> None:
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
    def audio_track_index(self) -> primitives.Int | None:
        """The AudioTrackIndex field value."""
        member = self.get_member("AudioTrackIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @audio_track_index.setter
    def audio_track_index(self, value: primitives.Int) -> None:
        """Set the AudioTrackIndex field value."""
        member = self.get_member("AudioTrackIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AudioTrackIndex", fields.FieldNullableInt(value=value)
            )

    @property
    def prefer_audio_only(self) -> primitives.Bool | None:
        """The PreferAudioOnly field value."""
        member = self.get_member("PreferAudioOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @prefer_audio_only.setter
    def prefer_audio_only(self, value: primitives.Bool) -> None:
        """Set the PreferAudioOnly field value."""
        member = self.get_member("PreferAudioOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreferAudioOnly", fields.FieldBool(value=value)
            )

    @property
    def max_width(self) -> primitives.Int | None:
        """The MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_width.setter
    def max_width(self, value: primitives.Int) -> None:
        """Set the MaxWidth field value."""
        member = self.get_member("MaxWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxWidth", fields.FieldNullableInt(value=value)
            )

    @property
    def max_height(self) -> primitives.Int | None:
        """The MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_height.setter
    def max_height(self, value: primitives.Int) -> None:
        """Set the MaxHeight field value."""
        member = self.get_member("MaxHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxHeight", fields.FieldNullableInt(value=value)
            )

