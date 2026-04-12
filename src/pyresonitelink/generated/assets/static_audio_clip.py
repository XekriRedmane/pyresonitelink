"""Generated component: StaticAudioClip."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.audio_load_mode import AudioLoadMode
from pyresonitelink.generated._enums.sample_rate_mode import SampleRateMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticAudioClip(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The StaticAudioClip component is what stores pre recorded audio data for components that play audio like AudioClipPlayer. This component is auto generated when a sound file is imported into the game as part of an audio clip object.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticAudioClip"

    def __init__(self, url: str | None = None, load_mode: AudioLoadMode | str | None = None, sample_rate_mode: SampleRateMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            load_mode: Initial value for LoadMode.
            sample_rate_mode: Initial value for SampleRateMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if load_mode is not None:
            self.load_mode = load_mode
        if sample_rate_mode is not None:
            self.sample_rate_mode = sample_rate_mode

    @property
    def url(self) -> str | None:
        """The audio clip data location to load."""
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
    def load_mode(self) -> AudioLoadMode | None:
        """How and when to load the audio"""
        member = self.get_member("LoadMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioLoadMode(member.value)
        return None

    @load_mode.setter
    def load_mode(self, value: AudioLoadMode | str) -> None:
        """Set LoadMode. How and when to load the audio"""
        member = self.get_member("LoadMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "LoadMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def sample_rate_mode(self) -> SampleRateMode | None:
        """How to sample the audio's audio data."""
        member = self.get_member("SampleRateMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SampleRateMode(member.value)
        return None

    @sample_rate_mode.setter
    def sample_rate_mode(self, value: SampleRateMode | str) -> None:
        """Set SampleRateMode. How to sample the audio's audio data."""
        member = self.get_member("SampleRateMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SampleRateMode",
                members.FieldEnum(value=str(value)),
            )

    async def normalize(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Makes the volume during the audio clip consistent.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Normalize", {}, debug,
        )

    async def adjust_volume(self, resolink: protocols.ResoniteLinkClient, ratio: primitives.Float, debug: bool = False) -> dict:
        """Makes the volume louder or quieter.

        Args:
            resolink: Connected ResoniteLink client.
            ratio: The ratio parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AdjustVolume", {"ratio": ratio}, debug,
        )

    async def extract_sides(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Split the audio into two or more clips for different audio tracks.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ExtractSides", {}, debug,
        )

    async def denoise(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Removes noise from the audio clip

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Denoise", {}, debug,
        )

    async def trim_silence(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """removes the silence from the start and end of the audio clip

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimSilence", {}, debug,
        )

    async def trim_start_silence(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """removes the silence from the start of the clip.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimStartSilence", {}, debug,
        )

    async def trim_end_silence(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """removes the silence from the end of the clip.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimEndSilence", {}, debug,
        )

    async def trim_start(self, resolink: protocols.ResoniteLinkClient, duration: primitives.Float, debug: bool = False) -> dict:
        """cuts off audio data from the start of the audio clip.

        Args:
            resolink: Connected ResoniteLink client.
            duration: The duration parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimStart", {"duration": duration}, debug,
        )

    async def trim_end(self, resolink: protocols.ResoniteLinkClient, duration: primitives.Float, debug: bool = False) -> dict:
        """cuts off audio data from the end of the audio clip.

        Args:
            resolink: Connected ResoniteLink client.
            duration: The duration parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimEnd", {"duration": duration}, debug,
        )

    async def fade_in(self, resolink: protocols.ResoniteLinkClient, duration: primitives.Float, debug: bool = False) -> dict:
        """Makes the audio fade in over x seconds.

        Args:
            resolink: Connected ResoniteLink client.
            duration: The duration parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "FadeIn", {"duration": duration}, debug,
        )

    async def fade_out(self, resolink: protocols.ResoniteLinkClient, duration: primitives.Float, debug: bool = False) -> dict:
        """Makes the audio fade out over x seconds.

        Args:
            resolink: Connected ResoniteLink client.
            duration: The duration parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "FadeOut", {"duration": duration}, debug,
        )

    async def make_fade_loop(self, resolink: protocols.ResoniteLinkClient, duration: primitives.Float, debug: bool = False) -> dict:
        """Makes the audio loopable, using a cross fade of x seconds.

        Args:
            resolink: Connected ResoniteLink client.
            duration: The duration parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MakeFadeLoop", {"duration": duration}, debug,
        )

    async def convert_to_wav(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """converts the audio clip type to Windows audio vodec.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToWAV", {}, debug,
        )

    async def convert_to_vorbis(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """converts the audio clip type to Vorbis.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToVorbis", {}, debug,
        )

    async def convert_to_flac(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Converts the audio clip type to FLAC.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToFLAC", {}, debug,
        )

    async def apply_zita_reverb(self, resolink: protocols.ResoniteLinkClient, filter: str, debug: bool = False) -> dict:
        """ZitaParameters]] to create a reverberation sound effect on this audio clip.

        Args:
            resolink: Connected ResoniteLink client.
            filter: The filter parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ApplyZitaReverb", {"filter": filter}, debug,
        )

