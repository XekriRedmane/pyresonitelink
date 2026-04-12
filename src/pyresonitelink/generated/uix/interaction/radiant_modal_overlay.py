"""Generated component: RadiantModalOverlay."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.blur_material import BlurMaterial
from pyresonitelink.generated._types.raw_graphic import RawGraphic
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iui_interactable import IUIInteractable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadiantModalOverlay(GeneratedComponent, IUIInteractable, IWorldEventReceiver):
    """The RadiantModalOverlay component is similar to the ModalOverlay, but with the dash menu. This also can be duplicated as a template in the ModalOverlayManager component.

    Category: UIX/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadiantModalOverlay"

    def __init__(self, show_lerp: primitives.Float | None = None, animation_time: primitives.Float | None = None, size_root: str | RectTransform | None = None, content_root: str | RectTransform | None = None, close_on_context_menu_action: primitives.Bool | None = None, close_on_click: primitives.Bool | None = None, blur_spread: primitives.Float | None = None, background_color: primitives.ColorX | None = None, content_animation_scale_offset: primitives.Float | None = None, header_size: primitives.Float | None = None, padding: primitives.Float | None = None, title: str | Text | None = None, blur: str | BlurMaterial | None = None, blur_graphic: str | RawGraphic | None = None, mask_rect: str | IField[primitives.Rect] | None = None, header_offset_min: str | IField[primitives.Float2] | None = None, header_offset_max: str | IField[primitives.Float2] | None = None, content_offset_min: str | IField[primitives.Float2] | None = None, content_offset_max: str | IField[primitives.Float2] | None = None, title_offset_min: str | IField[primitives.Float2] | None = None, title_offset_max: str | IField[primitives.Float2] | None = None, close_offset_min: str | IField[primitives.Float2] | None = None, close_offset_max: str | IField[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_lerp: Initial value for ShowLerp.
            animation_time: Initial value for AnimationTime.
            size_root: Initial value for SizeRoot.
            content_root: Initial value for ContentRoot.
            close_on_context_menu_action: Initial value for CloseOnContextMenuAction.
            close_on_click: Initial value for CloseOnClick.
            blur_spread: Initial value for BlurSpread.
            background_color: Initial value for BackgroundColor.
            content_animation_scale_offset: Initial value for ContentAnimationScaleOffset.
            header_size: Initial value for HeaderSize.
            padding: Initial value for Padding.
            title: Initial value for _title.
            blur: Initial value for _blur.
            blur_graphic: Initial value for _blurGraphic.
            mask_rect: Initial value for _maskRect.
            header_offset_min: Initial value for _headerOffsetMin.
            header_offset_max: Initial value for _headerOffsetMax.
            content_offset_min: Initial value for _contentOffsetMin.
            content_offset_max: Initial value for _contentOffsetMax.
            title_offset_min: Initial value for _titleOffsetMin.
            title_offset_max: Initial value for _titleOffsetMax.
            close_offset_min: Initial value for _closeOffsetMin.
            close_offset_max: Initial value for _closeOffsetMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show_lerp is not None:
            self.show_lerp = show_lerp
        if animation_time is not None:
            self.animation_time = animation_time
        if size_root is not None:
            self.size_root = size_root
        if content_root is not None:
            self.content_root = content_root
        if close_on_context_menu_action is not None:
            self.close_on_context_menu_action = close_on_context_menu_action
        if close_on_click is not None:
            self.close_on_click = close_on_click
        if blur_spread is not None:
            self.blur_spread = blur_spread
        if background_color is not None:
            self.background_color = background_color
        if content_animation_scale_offset is not None:
            self.content_animation_scale_offset = content_animation_scale_offset
        if header_size is not None:
            self.header_size = header_size
        if padding is not None:
            self.padding = padding
        if title is not None:
            self.title = title
        if blur is not None:
            self.blur = blur
        if blur_graphic is not None:
            self.blur_graphic = blur_graphic
        if mask_rect is not None:
            self.mask_rect = mask_rect
        if header_offset_min is not None:
            self.header_offset_min = header_offset_min
        if header_offset_max is not None:
            self.header_offset_max = header_offset_max
        if content_offset_min is not None:
            self.content_offset_min = content_offset_min
        if content_offset_max is not None:
            self.content_offset_max = content_offset_max
        if title_offset_min is not None:
            self.title_offset_min = title_offset_min
        if title_offset_max is not None:
            self.title_offset_max = title_offset_max
        if close_offset_min is not None:
            self.close_offset_min = close_offset_min
        if close_offset_max is not None:
            self.close_offset_max = close_offset_max

    @property
    def show_lerp(self) -> primitives.Float | None:
        """The lerp amount for this modal."""
        member = self.get_member("ShowLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_lerp.setter
    def show_lerp(self, value: primitives.Float) -> None:
        """Set the ShowLerp field value."""
        member = self.get_member("ShowLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowLerp", fields.FieldFloat(value=value)
            )

    @property
    def animation_time(self) -> primitives.Float | None:
        """The lerp time for this modal."""
        member = self.get_member("AnimationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_time.setter
    def animation_time(self, value: primitives.Float) -> None:
        """Set the AnimationTime field value."""
        member = self.get_member("AnimationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationTime", fields.FieldFloat(value=value)
            )

    @property
    def size_root(self) -> str | None:
        """The size of this modal."""
        member = self.get_member("SizeRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size_root.setter
    def size_root(self, target: str | RectTransform | None) -> None:
        """Set the SizeRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("SizeRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SizeRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def content_root(self) -> str | None:
        """The center root of this modal."""
        member = self.get_member("ContentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | RectTransform | None) -> None:
        """Set the ContentRoot reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("ContentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ContentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def close_on_context_menu_action(self) -> primitives.Bool | None:
        """Closes the modal when the user's context menu closes."""
        member = self.get_member("CloseOnContextMenuAction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_on_context_menu_action.setter
    def close_on_context_menu_action(self, value: primitives.Bool) -> None:
        """Set the CloseOnContextMenuAction field value."""
        member = self.get_member("CloseOnContextMenuAction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseOnContextMenuAction", fields.FieldBool(value=value)
            )

    @property
    def close_on_click(self) -> primitives.Bool | None:
        """Closes this modal when it is clicked on."""
        member = self.get_member("CloseOnClick")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_on_click.setter
    def close_on_click(self, value: primitives.Bool) -> None:
        """Set the CloseOnClick field value."""
        member = self.get_member("CloseOnClick")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseOnClick", fields.FieldBool(value=value)
            )

    @property
    def blur_spread(self) -> primitives.Float | None:
        """The blur effect amount."""
        member = self.get_member("BlurSpread")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blur_spread.setter
    def blur_spread(self, value: primitives.Float) -> None:
        """Set the BlurSpread field value."""
        member = self.get_member("BlurSpread")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlurSpread", fields.FieldFloat(value=value)
            )

    @property
    def background_color(self) -> primitives.ColorX | None:
        """The background color of this RadiantModalOverlay."""
        member = self.get_member("BackgroundColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @background_color.setter
    def background_color(self, value: primitives.ColorX) -> None:
        """Set the BackgroundColor field value."""
        member = self.get_member("BackgroundColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackgroundColor", fields.FieldColorX(value=value)
            )

    @property
    def content_animation_scale_offset(self) -> primitives.Float | None:
        """Offests the content animation for this RadiantModalOverlay."""
        member = self.get_member("ContentAnimationScaleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @content_animation_scale_offset.setter
    def content_animation_scale_offset(self, value: primitives.Float) -> None:
        """Set the ContentAnimationScaleOffset field value."""
        member = self.get_member("ContentAnimationScaleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ContentAnimationScaleOffset", fields.FieldFloat(value=value)
            )

    @property
    def header_size(self) -> primitives.Float | None:
        """The header size of this RadiantModalOverlay."""
        member = self.get_member("HeaderSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @header_size.setter
    def header_size(self, value: primitives.Float) -> None:
        """Set the HeaderSize field value."""
        member = self.get_member("HeaderSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeaderSize", fields.FieldFloat(value=value)
            )

    @property
    def padding(self) -> primitives.Float | None:
        """The padding amount for this RadiantModalOverlay."""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: primitives.Float) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldFloat(value=value)
            )

    @property
    def title(self) -> str | None:
        """The title of this RadiantModalOverlay."""
        member = self.get_member("_title")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title.setter
    def title(self, target: str | Text | None) -> None:
        """Set the _title reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_title")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_title",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def blur(self) -> str | None:
        """The blur of this RadiantModalOverlay."""
        member = self.get_member("_blur")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @blur.setter
    def blur(self, target: str | BlurMaterial | None) -> None:
        """Set the _blur reference by target ID or BlurMaterial instance."""
        target_id: str | None = target.id if isinstance(target, BlurMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_blur")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_blur",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BlurMaterial'),
            )

    @property
    def blur_graphic(self) -> str | None:
        """The blur graphic of this RadiantModalOverlay."""
        member = self.get_member("_blurGraphic")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @blur_graphic.setter
    def blur_graphic(self, target: str | RawGraphic | None) -> None:
        """Set the _blurGraphic reference by target ID or RawGraphic instance."""
        target_id: str | None = target.id if isinstance(target, RawGraphic) else target  # type: ignore[assignment]
        member = self.get_member("_blurGraphic")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_blurGraphic",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RawGraphic'),
            )

    @property
    def blur_spread(self) -> str | None:
        """The blur speed of this RadiantModalOverlay."""
        member = self.get_member("_blurSpread")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @blur_spread.setter
    def blur_spread(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _blurSpread reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_blurSpread")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_blurSpread",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def background_color(self) -> str | None:
        """The background color of this RadiantModalOverlay."""
        member = self.get_member("_backgroundColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @background_color.setter
    def background_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _backgroundColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_backgroundColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_backgroundColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def mask_rect(self) -> str | None:
        """The mask rect of this RadiantModalOverlay."""
        member = self.get_member("_maskRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mask_rect.setter
    def mask_rect(self, target: str | IField[primitives.Rect] | None) -> None:
        """Set the _maskRect reference by target ID or IField[primitives.Rect] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_maskRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maskRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Rect>'),
            )

    @property
    def header_offset_min(self) -> str | None:
        """The header offset min of this RadiantModalOverlay."""
        member = self.get_member("_headerOffsetMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_offset_min.setter
    def header_offset_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _headerOffsetMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headerOffsetMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerOffsetMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def header_offset_max(self) -> str | None:
        """The header offset max of this RadiantModalOverlay."""
        member = self.get_member("_headerOffsetMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_offset_max.setter
    def header_offset_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _headerOffsetMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headerOffsetMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerOffsetMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def content_offset_min(self) -> str | None:
        """The content offset min of this RadiantModalOverlay."""
        member = self.get_member("_contentOffsetMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_offset_min.setter
    def content_offset_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _contentOffsetMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_contentOffsetMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentOffsetMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def content_offset_max(self) -> str | None:
        """The content offset max of this RadiantModalOverlay."""
        member = self.get_member("_contentOffsetMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_offset_max.setter
    def content_offset_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _contentOffsetMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_contentOffsetMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentOffsetMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def title_offset_min(self) -> str | None:
        """The title offset min of this RadiantModalOverlay."""
        member = self.get_member("_titleOffsetMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title_offset_min.setter
    def title_offset_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _titleOffsetMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_titleOffsetMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_titleOffsetMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def title_offset_max(self) -> str | None:
        """The title offset max of this RadiantModalOverlay."""
        member = self.get_member("_titleOffsetMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title_offset_max.setter
    def title_offset_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _titleOffsetMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_titleOffsetMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_titleOffsetMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def close_offset_min(self) -> str | None:
        """The close offset min of this RadiantModalOverlay."""
        member = self.get_member("_closeOffsetMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @close_offset_min.setter
    def close_offset_min(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _closeOffsetMin reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_closeOffsetMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_closeOffsetMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def close_offset_max(self) -> str | None:
        """The close offset max of this RadiantModalOverlay."""
        member = self.get_member("_closeOffsetMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @close_offset_max.setter
    def close_offset_max(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _closeOffsetMax reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_closeOffsetMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_closeOffsetMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    async def construct(self, resolink: protocols.ResoniteLinkClient, slot: str, debug: bool = False) -> dict:
        """Call the Construct sync method.

        Args:
            resolink: Connected ResoniteLink client.
            slot: The slot parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Construct", {"slot": slot}, debug,
        )

