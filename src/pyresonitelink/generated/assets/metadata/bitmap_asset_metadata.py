"""Generated component: BitmapAssetMetadata."""

from pyresonitelink.data import members
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

    def __init__(self, asset: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            asset: Initial value for Asset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if asset is not None:
            self.asset = asset

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
    def width(self) -> members.EmptyElement | None:
        """The Width member."""
        member = self.get_member("Width")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @width.setter
    def width(self, value: members.EmptyElement) -> None:
        """Set the Width member."""
        self.set_member("Width", value)

    @property
    def height(self) -> members.EmptyElement | None:
        """The Height member."""
        member = self.get_member("Height")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @height.setter
    def height(self, value: members.EmptyElement) -> None:
        """Set the Height member."""
        self.set_member("Height", value)

    @property
    def base_format(self) -> members.EmptyElement | None:
        """The BaseFormat member."""
        member = self.get_member("BaseFormat")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @base_format.setter
    def base_format(self, value: members.EmptyElement) -> None:
        """Set the BaseFormat member."""
        self.set_member("BaseFormat", value)

    @property
    def color_data(self) -> members.EmptyElement | None:
        """The ColorData member."""
        member = self.get_member("ColorData")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @color_data.setter
    def color_data(self, value: members.EmptyElement) -> None:
        """Set the ColorData member."""
        self.set_member("ColorData", value)

    @property
    def alpha_data(self) -> members.EmptyElement | None:
        """The AlphaData member."""
        member = self.get_member("AlphaData")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @alpha_data.setter
    def alpha_data(self, value: members.EmptyElement) -> None:
        """Set the AlphaData member."""
        self.set_member("AlphaData", value)

    @property
    def bits_per_pixel(self) -> members.EmptyElement | None:
        """The BitsPerPixel member."""
        member = self.get_member("BitsPerPixel")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @bits_per_pixel.setter
    def bits_per_pixel(self, value: members.EmptyElement) -> None:
        """Set the BitsPerPixel member."""
        self.set_member("BitsPerPixel", value)

    @property
    def channel_count(self) -> members.EmptyElement | None:
        """The ChannelCount member."""
        member = self.get_member("ChannelCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @channel_count.setter
    def channel_count(self, value: members.EmptyElement) -> None:
        """Set the ChannelCount member."""
        self.set_member("ChannelCount", value)

    @property
    def average_color(self) -> members.EmptyElement | None:
        """The AverageColor member."""
        member = self.get_member("AverageColor")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @average_color.setter
    def average_color(self, value: members.EmptyElement) -> None:
        """Set the AverageColor member."""
        self.set_member("AverageColor", value)

    @property
    def average_visible_color(self) -> members.EmptyElement | None:
        """The AverageVisibleColor member."""
        member = self.get_member("AverageVisibleColor")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @average_visible_color.setter
    def average_visible_color(self, value: members.EmptyElement) -> None:
        """Set the AverageVisibleColor member."""
        self.set_member("AverageVisibleColor", value)

    @property
    def average_hsv(self) -> members.EmptyElement | None:
        """The AverageHSV member."""
        member = self.get_member("AverageHSV")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @average_hsv.setter
    def average_hsv(self, value: members.EmptyElement) -> None:
        """Set the AverageHSV member."""
        self.set_member("AverageHSV", value)

    @property
    def average_visible_hsv(self) -> members.EmptyElement | None:
        """The AverageVisibleHSV member."""
        member = self.get_member("AverageVisibleHSV")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @average_visible_hsv.setter
    def average_visible_hsv(self, value: members.EmptyElement) -> None:
        """Set the AverageVisibleHSV member."""
        self.set_member("AverageVisibleHSV", value)

    @property
    def invalid_pixel_count(self) -> members.EmptyElement | None:
        """The InvalidPixelCount member."""
        member = self.get_member("InvalidPixelCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @invalid_pixel_count.setter
    def invalid_pixel_count(self, value: members.EmptyElement) -> None:
        """Set the InvalidPixelCount member."""
        self.set_member("InvalidPixelCount", value)

