"""Generated component: StaticCubemap."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_provider import ITextureProvider
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticCubemap(GeneratedComponent, ITextureProvider, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The StaticCubemap is a component that is used to store data for a 6 sided texture for use with skyboxes.

    Category: Assets

    Attach to a slot and insert into a Projection360Material to view what it
    would look like as a skybox.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticCubemap"

    def __init__(self, url: str | None = None, anisotropic_level: primitives.Int | None = None, uncompressed: primitives.Bool | None = None, direct_load: primitives.Bool | None = None, force_exact_variant: primitives.Bool | None = None, mip_map_bias: primitives.Float | None = None, max_size: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            anisotropic_level: Initial value for AnisotropicLevel.
            uncompressed: Initial value for Uncompressed.
            direct_load: Initial value for DirectLoad.
            force_exact_variant: Initial value for ForceExactVariant.
            mip_map_bias: Initial value for MipMapBias.
            max_size: Initial value for MaxSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if anisotropic_level is not None:
            self.anisotropic_level = anisotropic_level
        if uncompressed is not None:
            self.uncompressed = uncompressed
        if direct_load is not None:
            self.direct_load = direct_load
        if force_exact_variant is not None:
            self.force_exact_variant = force_exact_variant
        if mip_map_bias is not None:
            self.mip_map_bias = mip_map_bias
        if max_size is not None:
            self.max_size = max_size

    @property
    def url(self) -> str | None:
        """The Asset URI that references the raw texture data"""
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
                "AnisotropicLevel", fields.FieldNullableInt(value=value)
            )

    @property
    def uncompressed(self) -> primitives.Bool | None:
        """Do not use texture compression"""
        member = self.get_member("Uncompressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uncompressed.setter
    def uncompressed(self, value: primitives.Bool) -> None:
        """Set the Uncompressed field value."""
        member = self.get_member("Uncompressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Uncompressed", fields.FieldBool(value=value)
            )

    @property
    def direct_load(self) -> primitives.Bool | None:
        """Whether to load the cubemap directly from it's URI source and to not cache it locally."""
        member = self.get_member("DirectLoad")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direct_load.setter
    def direct_load(self, value: primitives.Bool) -> None:
        """Set the DirectLoad field value."""
        member = self.get_member("DirectLoad")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectLoad", fields.FieldBool(value=value)
            )

    @property
    def force_exact_variant(self) -> primitives.Bool | None:
        """Only allow one variant of the texture to exist, part of Asset Variant System."""
        member = self.get_member("ForceExactVariant")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_exact_variant.setter
    def force_exact_variant(self, value: primitives.Bool) -> None:
        """Set the ForceExactVariant field value."""
        member = self.get_member("ForceExactVariant")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceExactVariant", fields.FieldBool(value=value)
            )

    @property
    def preferred_format(self) -> members.FieldEnum | None:
        """The format to use for texture compression rather than the auto picked one"""
        member = self.get_member("PreferredFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preferred_format.setter
    def preferred_format(self, value: members.FieldEnum) -> None:
        """Set PreferredFormat. The format to use for texture compression rather than the auto picked one"""
        self.set_member("PreferredFormat", value)

    @property
    def preferred_profile(self) -> members.FieldEnum | None:
        """The color profile to use rather than the auto picked one. (usually linear)"""
        member = self.get_member("PreferredProfile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preferred_profile.setter
    def preferred_profile(self, value: members.FieldEnum) -> None:
        """Set PreferredProfile. The color profile to use rather than the auto picked one. (usually linear)"""
        self.set_member("PreferredProfile", value)

    @property
    def mip_map_bias(self) -> primitives.Float | None:
        """The MipMapBias field value."""
        member = self.get_member("MipMapBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_map_bias.setter
    def mip_map_bias(self, value: primitives.Float) -> None:
        """Set the MipMapBias field value."""
        member = self.get_member("MipMapBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMapBias", fields.FieldFloat(value=value)
            )

    @property
    def max_size(self) -> primitives.Int | None:
        """The maxiumum size to show to the user, which scaled versions are generated by the cloud on the fly from the original and sent as part of the Asset Variant System"""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: primitives.Int) -> None:
        """Set the MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSize", fields.FieldNullableInt(value=value)
            )

    async def invert_rgb(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the colors of the cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertRGB", {}, debug,
        )

    async def invert_r(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the red channel of the cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertR", {}, debug,
        )

    async def invert_g(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the green channel of the cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertG", {}, debug,
        )

    async def invert_b(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the blue channel of the cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertB", {}, debug,
        )

    async def invert_a(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the alpha channel of the cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertA", {}, debug,
        )

    async def color_to_alpha(self, resolink: protocols.ResoniteLinkClient, fill_color: primitives.ColorX, debug: bool = False) -> dict:
        """Turns the color data of the cubemap into transparency/alpha data.

        Args:
            resolink: Connected ResoniteLink client.
            fill_color: The fillColor parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ColorToAlpha", {"fillColor": fill_color}, debug,
        )

    async def alpha_from_intensity(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Makes alpha/transparency data depending on the color intensity of the cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AlphaFromIntensity", {}, debug,
        )

    async def alpha_to_mask(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Turns the alpha of the cubemap into a black and white cubemap.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AlphaToMask", {}, debug,
        )

    async def remove_alpha(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Removes the alpha data completely from the cubemap or makes it white.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveAlpha", {}, debug,
        )

    async def grayscale_average(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Make grayscale cubemap based on the average values for the colors per pixel.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GrayscaleAverage", {}, debug,
        )

    async def grayscale_luminance(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Make grayscale cubemap based on the color luminance per pixel.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GrayscaleLuminance", {}, debug,
        )

    async def swap_rg(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the red and green channels on the cubemap

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapRG", {}, debug,
        )

    async def swap_rb(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the red and blue channels on the cubemap

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapRB", {}, debug,
        )

    async def swap_ra(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the red and alpha channels on the cubemap

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapRA", {}, debug,
        )

    async def swap_gb(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the green and blue channels on the cubemap

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapGB", {}, debug,
        )

    async def swap_ga(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the green and alpha channels on the cubemap

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapGA", {}, debug,
        )

    async def swap_ba(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the blue and alpha channels on the cubemap

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapBA", {}, debug,
        )

    async def isolate_r(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the IsolateR sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "IsolateR", {}, debug,
        )

    async def isolate_g(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the IsolateG sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "IsolateG", {}, debug,
        )

    async def isolate_b(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the IsolateB sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "IsolateB", {}, debug,
        )

    async def isolate_a(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the IsolateA sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "IsolateA", {}, debug,
        )

    async def add_background(self, resolink: protocols.ResoniteLinkClient, color: primitives.ColorX, debug: bool = False) -> dict:
        """adds a background of a color to a transparent cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            color: The color parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AddBackground", {"color": color}, debug,
        )

    async def adjust_gamma(self, resolink: protocols.ResoniteLinkClient, gamma: primitives.Float, debug: bool = False) -> dict:
        """Adjusts the gamma of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            gamma: The gamma parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AdjustGamma", {"gamma": gamma}, debug,
        )

    async def adjust_alpha_gamma(self, resolink: protocols.ResoniteLinkClient, gamma: primitives.Float, debug: bool = False) -> dict:
        """Adjusts the gamma of the alpha channel of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            gamma: The gamma parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AdjustAlphaGamma", {"gamma": gamma}, debug,
        )

    async def shift_hue(self, resolink: protocols.ResoniteLinkClient, offset: primitives.Float, debug: bool = False) -> dict:
        """Shifts the hue of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            offset: The offset parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ShiftHue", {"offset": offset}, debug,
        )

    async def set_hue(self, resolink: protocols.ResoniteLinkClient, hue: primitives.Float, debug: bool = False) -> dict:
        """Sets the Hue of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            hue: The hue parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetHue", {"hue": hue}, debug,
        )

    async def set_saturation(self, resolink: protocols.ResoniteLinkClient, saturation: primitives.Float, debug: bool = False) -> dict:
        """Sets the saturation of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            saturation: The saturation parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetSaturation", {"saturation": saturation}, debug,
        )

    async def offset_saturation(self, resolink: protocols.ResoniteLinkClient, offset: primitives.Float, debug: bool = False) -> dict:
        """Adds to the saturation of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            offset: The offset parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OffsetSaturation", {"offset": offset}, debug,
        )

    async def mul_saturation(self, resolink: protocols.ResoniteLinkClient, ratio: primitives.Float, debug: bool = False) -> dict:
        """Multiplies the saturation of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            ratio: The ratio parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MulSaturation", {"ratio": ratio}, debug,
        )

    async def set_value(self, resolink: protocols.ResoniteLinkClient, value: primitives.Float, debug: bool = False) -> dict:
        """Sets the value of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            value: The value parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetValue", {"value": value}, debug,
        )

    async def mul_value(self, resolink: protocols.ResoniteLinkClient, ratio: primitives.Float, debug: bool = False) -> dict:
        """Multiplies the value of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            ratio: The ratio parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MulValue", {"ratio": ratio}, debug,
        )

    async def offset_value(self, resolink: protocols.ResoniteLinkClient, offset: primitives.Float, debug: bool = False) -> dict:
        """Adds to the value of HSV of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            offset: The offset parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OffsetValue", {"offset": offset}, debug,
        )

    async def offset_alpha(self, resolink: protocols.ResoniteLinkClient, offset: primitives.Float, debug: bool = False) -> dict:
        """Adds to the alpha of the cubemap.

        Args:
            resolink: Connected ResoniteLink client.
            offset: The offset parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OffsetAlpha", {"offset": offset}, debug,
        )

    async def normalize(self, resolink: protocols.ResoniteLinkClient, rgb_independently: primitives.Bool, normalize_alpha: primitives.Bool, normalize_min_value: primitives.Bool, debug: bool = False) -> dict:
        """Normalizes the colors of the cubemap, making it have a bigger color range usage.

        Args:
            resolink: Connected ResoniteLink client.
            rgb_independently: The rgbIndependently parameter.
            normalize_alpha: The normalizeAlpha parameter.
            normalize_min_value: The normalizeMinValue parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Normalize", {"rgbIndependently": rgb_independently, "normalizeAlpha": normalize_alpha, "normalizeMinValue": normalize_min_value}, debug,
        )

