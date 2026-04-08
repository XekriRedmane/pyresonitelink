"""Generated component: StaticFont."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticFont(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StaticFont.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticFont"

    def __init__(self, url: str | None = None, padding: np.int32 | None = None, pixel_range: np.int32 | None = None, glyph_em_size: np.int32 | None = None, mip_maps: bool | None = None, lod_bias: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            padding: Initial value for Padding.
            pixel_range: Initial value for PixelRange.
            glyph_em_size: Initial value for GlyphEmSize.
            mip_maps: Initial value for MipMaps.
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
        if lod_bias is not None:
            self.lod_bias = lod_bias

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
    def padding(self) -> np.int32 | None:
        """The Padding field value."""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: np.int32) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldInt(value=value)
            )

    @property
    def pixel_range(self) -> np.int32 | None:
        """The PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pixel_range.setter
    def pixel_range(self, value: np.int32) -> None:
        """Set the PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PixelRange", fields.FieldInt(value=value)
            )

    @property
    def glyph_em_size(self) -> np.int32 | None:
        """The GlyphEmSize field value."""
        member = self.get_member("GlyphEmSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @glyph_em_size.setter
    def glyph_em_size(self, value: np.int32) -> None:
        """Set the GlyphEmSize field value."""
        member = self.get_member("GlyphEmSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlyphEmSize", fields.FieldInt(value=value)
            )

    @property
    def mip_maps(self) -> bool | None:
        """The MipMaps field value."""
        member = self.get_member("MipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mip_maps.setter
    def mip_maps(self, value: bool) -> None:
        """Set the MipMaps field value."""
        member = self.get_member("MipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MipMaps", fields.FieldBool(value=value)
            )

    @property
    def mip_map_filtering(self) -> members.FieldEnum | None:
        """The MipMapFiltering member."""
        member = self.get_member("MipMapFiltering")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mip_map_filtering.setter
    def mip_map_filtering(self, value: members.FieldEnum) -> None:
        """Set the MipMapFiltering member."""
        self.set_member("MipMapFiltering", value)

    @property
    def lod_bias(self) -> np.float32 | None:
        """The LODBias field value."""
        member = self.get_member("LODBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lod_bias.setter
    def lod_bias(self, value: np.float32) -> None:
        """Set the LODBias field value."""
        member = self.get_member("LODBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LODBias", fields.FieldFloat(value=value)
            )

