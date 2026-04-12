"""Generated component: ImageImportDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.image_projection import ImageProjection
from pyresonitelink.generated._enums.stereo_layout import StereoLayout
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ImageImportDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """See Image Import.

    See Image Import.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ImageImportDialog"

    def __init__(self, content_root: str | Slot | None = None, projection: ImageProjection | str | None = None, layout: StereoLayout | str | None = None, screenshot: primitives.Bool | None = None, point_filtering: primitives.Bool | None = None, uncompressed: primitives.Bool | None = None, alpha_bleed: primitives.Bool | None = None, lut: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            content_root: Initial value for _contentRoot.
            projection: Initial value for _projection.
            layout: Initial value for _layout.
            screenshot: Initial value for _screenshot.
            point_filtering: Initial value for _pointFiltering.
            uncompressed: Initial value for _uncompressed.
            alpha_bleed: Initial value for _alphaBleed.
            lut: Initial value for _lut.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if content_root is not None:
            self.content_root = content_root
        if projection is not None:
            self.projection = projection
        if layout is not None:
            self.layout = layout
        if screenshot is not None:
            self.screenshot = screenshot
        if point_filtering is not None:
            self.point_filtering = point_filtering
        if uncompressed is not None:
            self.uncompressed = uncompressed
        if alpha_bleed is not None:
            self.alpha_bleed = alpha_bleed
        if lut is not None:
            self.lut = lut

    @property
    def content_root(self) -> str | None:
        """Target ID of the _contentRoot reference (targets Slot)."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def projection(self) -> ImageProjection | None:
        """What image projection to import the image as."""
        member = self.get_member("_projection")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ImageProjection(member.value)
        return None

    @projection.setter
    def projection(self, value: ImageProjection | str) -> None:
        """Set _projection. What image projection to import the image as."""
        member = self.get_member("_projection")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_projection",
                members.FieldEnum(value=str(value)),
            )

    @property
    def layout(self) -> StereoLayout | None:
        """The image stereo layout for left and right to use."""
        member = self.get_member("_layout")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StereoLayout(member.value)
        return None

    @layout.setter
    def layout(self, value: StereoLayout | str) -> None:
        """Set _layout. The image stereo layout for left and right to use."""
        member = self.get_member("_layout")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_layout",
                members.FieldEnum(value=str(value)),
            )

    @property
    def screenshot(self) -> primitives.Bool | None:
        """whether to import the image as a screenshot."""
        member = self.get_member("_screenshot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screenshot.setter
    def screenshot(self, value: primitives.Bool) -> None:
        """Set the _screenshot field value."""
        member = self.get_member("_screenshot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_screenshot", fields.FieldBool(value=value)
            )

    @property
    def point_filtering(self) -> primitives.Bool | None:
        """Whether to import the image as pixel art or not."""
        member = self.get_member("_pointFiltering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @point_filtering.setter
    def point_filtering(self, value: primitives.Bool) -> None:
        """Set the _pointFiltering field value."""
        member = self.get_member("_pointFiltering")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_pointFiltering", fields.FieldBool(value=value)
            )

    @property
    def uncompressed(self) -> primitives.Bool | None:
        """Whether to import the image as uncompressed or not."""
        member = self.get_member("_uncompressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uncompressed.setter
    def uncompressed(self, value: primitives.Bool) -> None:
        """Set the _uncompressed field value."""
        member = self.get_member("_uncompressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_uncompressed", fields.FieldBool(value=value)
            )

    @property
    def alpha_bleed(self) -> primitives.Bool | None:
        """Whether to import the image with alpha bleed reduction or not."""
        member = self.get_member("_alphaBleed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_bleed.setter
    def alpha_bleed(self, value: primitives.Bool) -> None:
        """Set the _alphaBleed field value."""
        member = self.get_member("_alphaBleed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_alphaBleed", fields.FieldBool(value=value)
            )

    @property
    def lut(self) -> primitives.Bool | None:
        """Whether this image is a Look Up Table."""
        member = self.get_member("_lut")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lut.setter
    def lut(self, value: primitives.Bool) -> None:
        """Set the _lut field value."""
        member = self.get_member("_lut")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lut", fields.FieldBool(value=value)
            )

