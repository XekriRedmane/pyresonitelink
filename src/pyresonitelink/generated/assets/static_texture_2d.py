"""Generated component: StaticTexture2D."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.texture_wrap_mode import TextureWrapMode
from pyresonitelink.generated._enums.filtering import Filtering
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticTexture2D(GeneratedComponent, ITexture2DProvider, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The StaticTexture2D Component stores a reference to a static asset representing a 2D Texture.

    Category: Assets

    By default ``Filter`` is set to Bilinear Filtering, however Anisotropic
    Filtering results in a much better appearance at very steep angles, and
    only has a very minor performance impact. If visual fidelity of your
    texture is a concern, you should set ``Filter`` to Anisotropic, and
    ``AnisotropicLevel`` to 4 or 8.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticTexture2D"

    def __init__(self, url: str | None = None, anisotropic_level: primitives.Int | None = None, uncompressed: primitives.Bool | None = None, direct_load: primitives.Bool | None = None, force_exact_variant: primitives.Bool | None = None, mip_map_bias: primitives.Float | None = None, is_normal_map: primitives.Bool | None = None, wrap_mode_u: TextureWrapMode | str | None = None, wrap_mode_v: TextureWrapMode | str | None = None, power_of_two_align_threshold: primitives.Float | None = None, crunch_compressed: primitives.Bool | None = None, min_size: primitives.Int | None = None, max_size: primitives.Int | None = None, mip_maps: primitives.Bool | None = None, keep_original_mip_maps: primitives.Bool | None = None, mip_map_filter: Filtering | str | None = None, readable: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            anisotropic_level: Initial value for AnisotropicLevel.
            uncompressed: Initial value for Uncompressed.
            direct_load: Initial value for DirectLoad.
            force_exact_variant: Initial value for ForceExactVariant.
            mip_map_bias: Initial value for MipMapBias.
            is_normal_map: Initial value for IsNormalMap.
            wrap_mode_u: Initial value for WrapModeU.
            wrap_mode_v: Initial value for WrapModeV.
            power_of_two_align_threshold: Initial value for PowerOfTwoAlignThreshold.
            crunch_compressed: Initial value for CrunchCompressed.
            min_size: Initial value for MinSize.
            max_size: Initial value for MaxSize.
            mip_maps: Initial value for MipMaps.
            keep_original_mip_maps: Initial value for KeepOriginalMipMaps.
            mip_map_filter: Initial value for MipMapFilter.
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
        if is_normal_map is not None:
            self.is_normal_map = is_normal_map
        if wrap_mode_u is not None:
            self.wrap_mode_u = wrap_mode_u
        if wrap_mode_v is not None:
            self.wrap_mode_v = wrap_mode_v
        if power_of_two_align_threshold is not None:
            self.power_of_two_align_threshold = power_of_two_align_threshold
        if crunch_compressed is not None:
            self.crunch_compressed = crunch_compressed
        if min_size is not None:
            self.min_size = min_size
        if max_size is not None:
            self.max_size = max_size
        if mip_maps is not None:
            self.mip_maps = mip_maps
        if keep_original_mip_maps is not None:
            self.keep_original_mip_maps = keep_original_mip_maps
        if mip_map_filter is not None:
            self.mip_map_filter = mip_map_filter
        if readable is not None:
            self.readable = readable

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
        """Whether to load the image directly from it's URI source and to not cache it locally."""
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
        """The format to use for texture compression rather than the auto picked one. See Texture Compression Formats for more details."""
        member = self.get_member("PreferredFormat")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preferred_format.setter
    def preferred_format(self, value: members.FieldEnum) -> None:
        """Set PreferredFormat. The format to use for texture compression rather than the auto picked one. See Texture Compression Formats for more details."""
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
    def is_normal_map(self) -> primitives.Bool | None:
        """This texture should be interpreted as a Normal Map"""
        member = self.get_member("IsNormalMap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_normal_map.setter
    def is_normal_map(self, value: primitives.Bool) -> None:
        """Set the IsNormalMap field value."""
        member = self.get_member("IsNormalMap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsNormalMap", fields.FieldBool(value=value)
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
    def power_of_two_align_threshold(self) -> primitives.Float | None:
        """The threshold for pixel count from range [0.0,1.0] before scaling both axes to a power of 2."""
        member = self.get_member("PowerOfTwoAlignThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power_of_two_align_threshold.setter
    def power_of_two_align_threshold(self, value: primitives.Float) -> None:
        """Set the PowerOfTwoAlignThreshold field value."""
        member = self.get_member("PowerOfTwoAlignThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PowerOfTwoAlignThreshold", fields.FieldFloat(value=value)
            )

    @property
    def crunch_compressed(self) -> primitives.Bool | None:
        """Whether the texture should be lossily compressed using Crunch. This goes on top of the compression set in PreferredFormat and doesn't decrease VRAM usage, only download size."""
        member = self.get_member("CrunchCompressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @crunch_compressed.setter
    def crunch_compressed(self, value: primitives.Bool) -> None:
        """Set the CrunchCompressed field value."""
        member = self.get_member("CrunchCompressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CrunchCompressed", fields.FieldBool(value=value)
            )

    @property
    def min_size(self) -> primitives.Int | None:
        """The miniumum size to show to the user, which scaled versions are generated by the cloud on the fly from the original and sent as part of the Asset Variant System"""
        member = self.get_member("MinSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_size.setter
    def min_size(self, value: primitives.Int) -> None:
        """Set the MinSize field value."""
        member = self.get_member("MinSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSize", fields.FieldNullableInt(value=value)
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

    @property
    def mip_maps(self) -> primitives.Bool | None:
        """The MipMaps field value."""
        member = self.get_member("MipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_maps.setter
    def mip_maps(self, value: primitives.Bool) -> None:
        """Set the MipMaps field value."""
        member = self.get_member("MipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMaps", fields.FieldBool(value=value)
            )

    @property
    def keep_original_mip_maps(self) -> primitives.Bool | None:
        """Whether to use the original mipmaps that came with the image data (yes you could have rainbow mipmaps at further distances) or not."""
        member = self.get_member("KeepOriginalMipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @keep_original_mip_maps.setter
    def keep_original_mip_maps(self, value: primitives.Bool) -> None:
        """Set the KeepOriginalMipMaps field value."""
        member = self.get_member("KeepOriginalMipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KeepOriginalMipMaps", fields.FieldBool(value=value)
            )

    @property
    def mip_map_filter(self) -> Filtering | None:
        """How to apply filtering to the image's mipmaps. please see Filtering!"""
        member = self.get_member("MipMapFilter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Filtering(member.value)
        return None

    @mip_map_filter.setter
    def mip_map_filter(self, value: Filtering | str) -> None:
        """Set MipMapFilter. How to apply filtering to the image's mipmaps. please see Filtering!"""
        member = self.get_member("MipMapFilter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MipMapFilter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def readable(self) -> primitives.Bool | None:
        """Whether this can be read per pixel via things like ProtoFlux"""
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

    async def bleed_color_to_alpha(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """extends the color data of the texture out into transparent areas from non transparent areas.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BleedColorToAlpha", {}, debug,
        )

    async def flip_horizontal(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Flips the image horizontal

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "FlipHorizontal", {}, debug,
        )

    async def flip_vertical(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Flips the image vertical

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "FlipVertical", {}, debug,
        )

    async def rotate90_cw(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Rotates the image by 90° clockwise

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Rotate90CW", {}, debug,
        )

    async def rotate90_ccw(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Rotates the image by 90° counterclockwise

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Rotate90CCW", {}, debug,
        )

    async def rotate180(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Rotates the image by 180°

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Rotate180", {}, debug,
        )

    async def make_square(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Resizes the image to make it square.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "MakeSquare", {}, debug,
        )

    async def tile_loop(self, resolink: protocols.ResoniteLinkClient, transition: primitives.Float2, debug: bool = False) -> dict:
        """Tiles the image X times on the width and height directions

        Args:
            resolink: Connected ResoniteLink client.
            transition: The transition parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TileLoop", {"transition": transition}, debug,
        )

    async def tile_mirror(self, resolink: protocols.ResoniteLinkClient, transition: primitives.Float2, debug: bool = False) -> dict:
        """Tiles the image X times on the width and height directions, mirroring the image every other tiling.

        Args:
            resolink: Connected ResoniteLink client.
            transition: The transition parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TileMirror", {"transition": transition}, debug,
        )

    async def rescale(self, resolink: protocols.ResoniteLinkClient, size: primitives.Int, filtering: str, debug: bool = False) -> dict:
        """Resizes the image up or down.

        Args:
            resolink: Connected ResoniteLink client.
            size: The size parameter.
            filtering: The filtering parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Rescale", {"size": size, "filtering": filtering}, debug,
        )

    async def rescale_2(self, resolink: protocols.ResoniteLinkClient, size: primitives.Int2, filtering: str, debug: bool = False) -> dict:
        """Resizes the image up or down.

        Args:
            resolink: Connected ResoniteLink client.
            size: The size parameter.
            filtering: The filtering parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Rescale", {"size": size, "filtering": filtering}, debug,
        )

    async def crop(self, resolink: protocols.ResoniteLinkClient, position: primitives.Int2, size: primitives.Int2, debug: bool = False) -> dict:
        """Crops the image to a new area in pixels.

        Args:
            resolink: Connected ResoniteLink client.
            position: The position parameter.
            size: The size parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Crop", {"position": position, "size": size}, debug,
        )

    async def trim(self, resolink: protocols.ResoniteLinkClient, color: primitives.Color, debug: bool = False) -> dict:
        """Trims the image from the edges. for example, this can be used to trim a black and white mask image to get rid of extra white around the edges of the image.

        Args:
            resolink: Connected ResoniteLink client.
            color: The color parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Trim", {"color": color}, debug,
        )

    async def trim_1(self, resolink: protocols.ResoniteLinkClient, color: primitives.Color32, debug: bool = False) -> dict:
        """Trims the image from the edges. for example, this can be used to trim a black and white mask image to get rid of extra white around the edges of the image.

        Args:
            resolink: Connected ResoniteLink client.
            color: The color parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Trim", {"color": color}, debug,
        )

    async def trim_transparent(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Trims the transparent areas off of the edges of an image.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimTransparent", {}, debug,
        )

    async def trim_by_corner_color(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Stretches the image such that both sides are equal to the longest side

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "TrimByCornerColor", {}, debug,
        )

    async def luminance_threshold(self, resolink: protocols.ResoniteLinkClient, threshold: primitives.Float, debug: bool = False) -> dict:
        """Call the LuminanceThreshold sync method.

        Args:
            resolink: Connected ResoniteLink client.
            threshold: The threshold parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "LuminanceThreshold", {"threshold": threshold}, debug,
        )

    async def luminance_threshold_3(self, resolink: protocols.ResoniteLinkClient, threshold: primitives.Float, above: primitives.Color, below: primitives.Color, debug: bool = False) -> dict:
        """Call the LuminanceThreshold sync method.

        Args:
            resolink: Connected ResoniteLink client.
            threshold: The threshold parameter.
            above: The above parameter.
            below: The below parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "LuminanceThreshold", {"threshold": threshold, "above": above, "below": below}, debug,
        )

    async def localized_luminance_threshold(self, resolink: protocols.ResoniteLinkClient, threshold: primitives.Float, range_: primitives.Int, debug: bool = False) -> dict:
        """Call the LocalizedLuminanceThreshold sync method.

        Args:
            resolink: Connected ResoniteLink client.
            threshold: The threshold parameter.
            range_: The range parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "LocalizedLuminanceThreshold", {"threshold": threshold, "range": range_}, debug,
        )

    async def localized_luminance_threshold_4(self, resolink: protocols.ResoniteLinkClient, threshold: primitives.Float, range_: primitives.Int, above: primitives.Color, below: primitives.Color, debug: bool = False) -> dict:
        """Call the LocalizedLuminanceThreshold sync method.

        Args:
            resolink: Connected ResoniteLink client.
            threshold: The threshold parameter.
            range_: The range parameter.
            above: The above parameter.
            below: The below parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "LocalizedLuminanceThreshold", {"threshold": threshold, "range": range_, "above": above, "below": below}, debug,
        )

    async def kmeans_cluster(self, resolink: protocols.ResoniteLinkClient, k: primitives.Int, position_weight: primitives.Float, batch_size: primitives.Int, passes_over_data: primitives.Float, debug: bool = False) -> dict:
        """This can be used to make the image into a vorroni version of it. is used to compress the color usage of an image to make it easily compressable. can also be used for art effects.

        Args:
            resolink: Connected ResoniteLink client.
            k: The k parameter.
            position_weight: The positionWeight parameter.
            batch_size: The batchSize parameter.
            passes_over_data: The passesOverData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "KMeansCluster", {"k": k, "positionWeight": position_weight, "batchSize": batch_size, "passesOverData": passes_over_data}, debug,
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

