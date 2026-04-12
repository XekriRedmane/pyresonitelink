"""Generated component: StaticTexture3D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.texture_wrap_mode import TextureWrapMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_3d_provider import ITexture3DProvider
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticTexture3D(GeneratedComponent, ITexture3DProvider, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The StaticTexture3D component represents a bunch of textures stacked on top of each other to make a 3D grid of pixel values, as a Texture3D. These textures can be displayed in 3D, or sampled via 3D positions in a few different components or in ProtoFlux Nodes. When importing a Texture3D, this component is usually applied after the import.

    Category: Assets

    Is generated automatically when importing a folder of images that are
    slices of a cube stacked vertically. Insert into a VolumeUnlitMaterial
    to view the colors or a LUT Material to view it's affect as a filter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticTexture3D"

    def __init__(self, url: str | None = None, anisotropic_level: primitives.Int | None = None, uncompressed: primitives.Bool | None = None, direct_load: primitives.Bool | None = None, force_exact_variant: primitives.Bool | None = None, mip_map_bias: primitives.Float | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, wrap_mode_w: TextureWrapMode | str | None = None, readable: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            anisotropic_level: Initial value for AnisotropicLevel.
            uncompressed: Initial value for Uncompressed.
            direct_load: Initial value for DirectLoad.
            force_exact_variant: Initial value for ForceExactVariant.
            mip_map_bias: Initial value for MipMapBias.
            wrap_mode_u: Initial value for WrapModeU.
            wrap_mode_v: Initial value for WrapModeV.
            wrap_mode_w: Initial value for WrapModeW.
            readable: Initial value for Readable.
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
        if wrap_mode_u is not None:
            self.wrap_mode_u = wrap_mode_u
        if wrap_mode_v is not None:
            self.wrap_mode_v = wrap_mode_v
        if wrap_mode_w is not None:
            self.wrap_mode_w = wrap_mode_w
        if readable is not None:
            self.readable = readable

    @property
    def url(self) -> str | None:
        """The address of the texture asset"""
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
        """Whether to not compress the texture's size before loading into ram/vram. doesn't affect cloud size."""
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
        """Whether to not cache the texture in the local cache for Resonite"""
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
        """Whether to not generate variants for this texture and force a certain texture type"""
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
    def wrap_mode_u(self) -> TextureWrapMode | None:
        """The WrapModeU enum value."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_u.setter
    def wrap_mode_u(self, value: TextureWrapMode | str) -> None:
        """Set the WrapModeU enum value."""
        member = self.get_member("WrapModeU")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeU",
                members.FieldEnum(value=str(value)),
            )

    @property
    def wrap_mode_v(self) -> TextureWrapMode | None:
        """The WrapModeV enum value."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_v.setter
    def wrap_mode_v(self, value: TextureWrapMode | str) -> None:
        """Set the WrapModeV enum value."""
        member = self.get_member("WrapModeV")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeV",
                members.FieldEnum(value=str(value)),
            )

    @property
    def wrap_mode_w(self) -> TextureWrapMode | None:
        """The WrapModeW enum value."""
        member = self.get_member("WrapModeW")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextureWrapMode(member.value)
        return None

    @wrap_mode_w.setter
    def wrap_mode_w(self, value: TextureWrapMode | str) -> None:
        """Set the WrapModeW enum value."""
        member = self.get_member("WrapModeW")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapModeW",
                members.FieldEnum(value=str(value)),
            )

    @property
    def readable(self) -> primitives.Bool | None:
        """Whether or not the texture can be sampled via texture sampling ProtoFlux nodes"""
        member = self.get_member("Readable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @readable.setter
    def readable(self, value: primitives.Bool) -> None:
        """Set the Readable field value."""
        member = self.get_member("Readable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Readable", fields.FieldBool(value=value)
            )

    async def invert_rgb(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the colors of the image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertRGB", {}, debug,
        )

    async def invert_r(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the red channel of the image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertR", {}, debug,
        )

    async def invert_g(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the green channel of the image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertG", {}, debug,
        )

    async def invert_b(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the blue channel of the image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertB", {}, debug,
        )

    async def invert_a(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Inverts the alpha channel of the image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "InvertA", {}, debug,
        )

    async def color_to_alpha(self, resolink: protocols.ResoniteLinkClient, fill_color: primitives.ColorX, debug: bool = False) -> dict:
        """Turns the color data of the image into transparency/alpha data.

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
        """Makes alpha/transparency data depending on the color intensity of the image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AlphaFromIntensity", {}, debug,
        )

    async def alpha_to_mask(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Turns the alpha of the image into a black and white image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AlphaToMask", {}, debug,
        )

    async def remove_alpha(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Removes the alpha data completely from the image or makes it white.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveAlpha", {}, debug,
        )

    async def grayscale_average(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Make grayscale image based on the average values for the colors per pixel.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GrayscaleAverage", {}, debug,
        )

    async def grayscale_luminance(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Make grayscale image based on the color luminance per pixel.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GrayscaleLuminance", {}, debug,
        )

    async def swap_rg(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the red and green channels on the image

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapRG", {}, debug,
        )

    async def swap_rb(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the red and blue channels on the image

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapRB", {}, debug,
        )

    async def swap_ra(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the red and alpha channels on the image

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapRA", {}, debug,
        )

    async def swap_gb(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the green and blue channels on the image

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapGB", {}, debug,
        )

    async def swap_ga(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the green and alpha channels on the image

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SwapGA", {}, debug,
        )

    async def swap_ba(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Swaps the blue and alpha channels on the image

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
        """adds a background of a color to a transparent image.

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
        """Adjusts the gamma of the image.

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
        """Adjusts the gamma of the alpha channel of the image.

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
        """Shifts the hue of HSV of the image.

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
        """Sets the Hue of HSV of the image.

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
        """Sets the saturation of HSV of the image.

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
        """Adds to the saturation of HSV of the image.

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
        """Multiplies the saturation of HSV of the image.

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
        """Sets the value of HSV of the image.

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
        """Multiplies the value of HSV of the image.

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
        """Adds to the value of HSV of the image.

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
        """Adds to the alpha of the image.

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
        """Normalizes the colors of the image, making it have a bigger color range usage.

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

