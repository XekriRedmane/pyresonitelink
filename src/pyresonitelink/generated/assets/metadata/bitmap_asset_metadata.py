"""Generated component: BitmapAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BitmapAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BitmapAssetMetadata.

    Category: Assets/Metadata
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BitmapAssetMetadata"

    def __init__(self, asset: str | IAssetProvider[Texture2D] | None = None, width: primitives.Int | None = None, height: primitives.Int | None = None, base_format: primitives.String | None = None, bits_per_pixel: primitives.Double | None = None, channel_count: primitives.Int | None = None, average_color: primitives.ColorX | None = None, average_visible_color: primitives.ColorX | None = None, average_hsv: primitives.ColorX | None = None, average_visible_hsv: primitives.ColorX | None = None, invalid_pixel_count: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            asset: Initial value for Asset.
            width: Initial value for Width.
            height: Initial value for Height.
            base_format: Initial value for BaseFormat.
            bits_per_pixel: Initial value for BitsPerPixel.
            channel_count: Initial value for ChannelCount.
            average_color: Initial value for AverageColor.
            average_visible_color: Initial value for AverageVisibleColor.
            average_hsv: Initial value for AverageHSV.
            average_visible_hsv: Initial value for AverageVisibleHSV.
            invalid_pixel_count: Initial value for InvalidPixelCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if asset is not None:
            self.asset = asset
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if base_format is not None:
            self.base_format = base_format
        if bits_per_pixel is not None:
            self.bits_per_pixel = bits_per_pixel
        if channel_count is not None:
            self.channel_count = channel_count
        if average_color is not None:
            self.average_color = average_color
        if average_visible_color is not None:
            self.average_visible_color = average_visible_color
        if average_hsv is not None:
            self.average_hsv = average_hsv
        if average_visible_hsv is not None:
            self.average_visible_hsv = average_visible_hsv
        if invalid_pixel_count is not None:
            self.invalid_pixel_count = invalid_pixel_count

    @property
    def asset(self) -> str | None:
        """Target ID of the Asset reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset.setter
    def asset(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Asset reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Asset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def width(self) -> primitives.Int | None:
        """The Width field value."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Int) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldInt(value=value)
            )

    @property
    def height(self) -> primitives.Int | None:
        """The Height field value."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Int) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldInt(value=value)
            )

    @property
    def base_format(self) -> primitives.String | None:
        """The BaseFormat field value."""
        member = self.get_member("BaseFormat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_format.setter
    def base_format(self, value: primitives.String) -> None:
        """Set the BaseFormat field value."""
        member = self.get_member("BaseFormat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseFormat", fields.FieldString(value=value)
            )

    @property
    def color_data(self) -> members.FieldEnum | None:
        """The ColorData member."""
        member = self.get_member("ColorData")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @color_data.setter
    def color_data(self, value: members.FieldEnum) -> None:
        """Set the ColorData member."""
        self.set_member("ColorData", value)

    @property
    def alpha_data(self) -> members.FieldEnum | None:
        """The AlphaData member."""
        member = self.get_member("AlphaData")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @alpha_data.setter
    def alpha_data(self, value: members.FieldEnum) -> None:
        """Set the AlphaData member."""
        self.set_member("AlphaData", value)

    @property
    def bits_per_pixel(self) -> primitives.Double | None:
        """The BitsPerPixel field value."""
        member = self.get_member("BitsPerPixel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bits_per_pixel.setter
    def bits_per_pixel(self, value: primitives.Double) -> None:
        """Set the BitsPerPixel field value."""
        member = self.get_member("BitsPerPixel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BitsPerPixel", fields.FieldDouble(value=value)
            )

    @property
    def channel_count(self) -> primitives.Int | None:
        """The ChannelCount field value."""
        member = self.get_member("ChannelCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @channel_count.setter
    def channel_count(self, value: primitives.Int) -> None:
        """Set the ChannelCount field value."""
        member = self.get_member("ChannelCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChannelCount", fields.FieldInt(value=value)
            )

    @property
    def average_color(self) -> primitives.ColorX | None:
        """The AverageColor field value."""
        member = self.get_member("AverageColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_color.setter
    def average_color(self, value: primitives.ColorX) -> None:
        """Set the AverageColor field value."""
        member = self.get_member("AverageColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageColor", fields.FieldColorX(value=value)
            )

    @property
    def average_visible_color(self) -> primitives.ColorX | None:
        """The AverageVisibleColor field value."""
        member = self.get_member("AverageVisibleColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_visible_color.setter
    def average_visible_color(self, value: primitives.ColorX) -> None:
        """Set the AverageVisibleColor field value."""
        member = self.get_member("AverageVisibleColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageVisibleColor", fields.FieldColorX(value=value)
            )

    @property
    def average_hsv(self) -> primitives.ColorX | None:
        """The AverageHSV field value."""
        member = self.get_member("AverageHSV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_hsv.setter
    def average_hsv(self, value: primitives.ColorX) -> None:
        """Set the AverageHSV field value."""
        member = self.get_member("AverageHSV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageHSV", fields.FieldColorX(value=value)
            )

    @property
    def average_visible_hsv(self) -> primitives.ColorX | None:
        """The AverageVisibleHSV field value."""
        member = self.get_member("AverageVisibleHSV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_visible_hsv.setter
    def average_visible_hsv(self, value: primitives.ColorX) -> None:
        """Set the AverageVisibleHSV field value."""
        member = self.get_member("AverageVisibleHSV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageVisibleHSV", fields.FieldColorX(value=value)
            )

    @property
    def invalid_pixel_count(self) -> primitives.Int | None:
        """The InvalidPixelCount field value."""
        member = self.get_member("InvalidPixelCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @invalid_pixel_count.setter
    def invalid_pixel_count(self, value: primitives.Int) -> None:
        """Set the InvalidPixelCount field value."""
        member = self.get_member("InvalidPixelCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InvalidPixelCount", fields.FieldInt(value=value)
            )

