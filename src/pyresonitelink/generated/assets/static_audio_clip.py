"""Generated component: StaticAudioClip."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticAudioClip(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StaticAudioClip.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticAudioClip"

    def __init__(self, url: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url

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
    def load_mode(self) -> members.FieldEnum | None:
        """The LoadMode member."""
        member = self.get_member("LoadMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @load_mode.setter
    def load_mode(self, value: members.FieldEnum) -> None:
        """Set the LoadMode member."""
        self.set_member("LoadMode", value)

    @property
    def sample_rate_mode(self) -> members.FieldEnum | None:
        """The SampleRateMode member."""
        member = self.get_member("SampleRateMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sample_rate_mode.setter
    def sample_rate_mode(self, value: members.FieldEnum) -> None:
        """Set the SampleRateMode member."""
        self.set_member("SampleRateMode", value)

    async def normalize(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Normalize sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Normalize", {}, debug,
        )

    async def adjust_volume(self, resolink: protocols.ResoniteLinkClient, ratio: primitives.Float, debug: bool = False) -> dict:
        """Call the AdjustVolume sync method.

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
        """Call the ExtractSides sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ExtractSides", {}, debug,
        )

    async def denoise(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Denoise sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Denoise", {}, debug,
        )

    async def trim_silence(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the TrimSilence sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimSilence", {}, debug,
        )

    async def trim_start_silence(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the TrimStartSilence sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimStartSilence", {}, debug,
        )

    async def trim_end_silence(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the TrimEndSilence sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimEndSilence", {}, debug,
        )

    async def trim_start(self, resolink: protocols.ResoniteLinkClient, duration: primitives.Float, debug: bool = False) -> dict:
        """Call the TrimStart sync method.

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
        """Call the TrimEnd sync method.

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
        """Call the FadeIn sync method.

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
        """Call the FadeOut sync method.

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
        """Call the MakeFadeLoop sync method.

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
        """Call the ConvertToWAV sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToWAV", {}, debug,
        )

    async def convert_to_vorbis(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ConvertToVorbis sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToVorbis", {}, debug,
        )

    async def convert_to_flac(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ConvertToFLAC sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ConvertToFLAC", {}, debug,
        )

    async def apply_zita_reverb(self, resolink: protocols.ResoniteLinkClient, filter: str, debug: bool = False) -> dict:
        """Call the ApplyZitaReverb sync method.

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

