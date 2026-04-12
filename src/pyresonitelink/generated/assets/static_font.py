"""Generated component: StaticFont."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.filtering import Filtering
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticFont(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """This component is auto generated when importing new font files.

    Category: Assets

    This component is auto generated when importing new font files. Simply
    find a font file (.TTF or similar) and drop it into the Resonite game
    window or import through the file browser in the dash. The game will
    then generate this component on a font object, with the ``URL`` field
    filled with a valid font resource.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticFont"

    def __init__(self, url: str | None = None, padding: primitives.Int | None = None, pixel_range: primitives.Int | None = None, glyph_em_size: primitives.Int | None = None, mip_maps: primitives.Bool | None = None, mip_map_filtering: Filtering | str | None = None, lod_bias: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            padding: Initial value for Padding.
            pixel_range: Initial value for PixelRange.
            glyph_em_size: Initial value for GlyphEmSize.
            mip_maps: Initial value for MipMaps.
            mip_map_filtering: Initial value for MipMapFiltering.
            lod_bias: Initial value for LODBias.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if padding is not None:
            self.padding = padding
        if pixel_range is not None:
            self.pixel_range = pixel_range
        if glyph_em_size is not None:
            self.glyph_em_size = glyph_em_size
        if mip_maps is not None:
            self.mip_maps = mip_maps
        if mip_map_filtering is not None:
            self.mip_map_filtering = mip_map_filtering
        if lod_bias is not None:
            self.lod_bias = lod_bias

    @property
    def url(self) -> str | None:
        """The location of where to load the font from."""
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
    def padding(self) -> primitives.Int | None:
        """How many pixels of padding should be used between letters in the font."""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: primitives.Int) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldInt(value=value)
            )

    @property
    def pixel_range(self) -> primitives.Int | None:
        """Sets the distance field range in output pixels."""
        member = self.get_member("PixelRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pixel_range.setter
    def pixel_range(self, value: primitives.Int) -> None:
        """Set the PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PixelRange", fields.FieldInt(value=value)
            )

    @property
    def glyph_em_size(self) -> primitives.Int | None:
        """Sets the size of the glyphs in the atlas in pixels per em."""
        member = self.get_member("GlyphEmSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @glyph_em_size.setter
    def glyph_em_size(self, value: primitives.Int) -> None:
        """Set the GlyphEmSize field value."""
        member = self.get_member("GlyphEmSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlyphEmSize", fields.FieldInt(value=value)
            )

    @property
    def mip_maps(self) -> primitives.Bool | None:
        """Whether to display lower res versions of the font when it is further away to save on performance."""
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
    def mip_map_filtering(self) -> Filtering | None:
        """How to filter transitions between mipmaps when it is viewed at incremental distances further away."""
        member = self.get_member("MipMapFiltering")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Filtering(member.value)
        return None

    @mip_map_filtering.setter
    def mip_map_filtering(self, value: Filtering | str) -> None:
        """Set MipMapFiltering. How to filter transitions between mipmaps when it is viewed at incremental distances further away."""
        member = self.get_member("MipMapFiltering")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MipMapFiltering",
                members.FieldEnum(value=str(value)),
            )

    @property
    def lod_bias(self) -> primitives.Float | None:
        """Whether to see lower res versions at smaller distances to save performance."""
        member = self.get_member("LODBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lod_bias.setter
    def lod_bias(self, value: primitives.Float) -> None:
        """Set the LODBias field value."""
        member = self.get_member("LODBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LODBias", fields.FieldFloat(value=value)
            )

