"""Generated component: Text."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.text_horizontal_alignment import TextHorizontalAlignment
from pyresonitelink.generated._enums.text_vertical_alignment import TextVerticalAlignment
from pyresonitelink.generated._enums.alignment_mode import AlignmentMode
from pyresonitelink.generated._enums.alignment import Alignment
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.font_set import FontSet
from pyresonitelink.generated._types.font_material import FontMaterial
from pyresonitelink.generated._types.ilayout_element import ILayoutElement
from pyresonitelink.generated._types.itext import IText
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Text(GeneratedComponent, ILayoutElement, IText, IUIComputeComponent, IWorldEventReceiver):
    """Text can be used to explain something, to be descriptive, to notify, and many other things text can be used for.

    Category: UIX/Graphics

    Text can be used to explain something, to be descriptive, to notify, and
    many other things text can be used for. When being effective with text,
    basic graphic design principles apply even to something simple as text.

    **Related Components**: Text
Text
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Text"

    def __init__(self, font: str | IAssetProvider[FontSet] | None = None, content: primitives.String | None = None, parse_rich_text: primitives.Bool | None = None, null_content: primitives.String | None = None, size: primitives.Float | None = None, horizontal_align: TextHorizontalAlignment | str | None = None, vertical_align: TextVerticalAlignment | str | None = None, alignment_mode: AlignmentMode | str | None = None, color: primitives.ColorX | None = None, line_height: primitives.Float | None = None, mask_pattern: primitives.String | None = None, horizontal_auto_size: primitives.Bool | None = None, vertical_auto_size: primitives.Bool | None = None, auto_size_min: primitives.Float | None = None, auto_size_max: primitives.Float | None = None, caret_position: primitives.Int | None = None, selection_start: primitives.Int | None = None, caret_color: primitives.ColorX | None = None, selection_color: primitives.ColorX | None = None, interaction_target: primitives.Bool | None = None, legacy_font_material: str | FontMaterial | None = None, legacy_align: Alignment | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            font: Initial value for Font.
            content: Initial value for Content.
            parse_rich_text: Initial value for ParseRichText.
            null_content: Initial value for NullContent.
            size: Initial value for Size.
            horizontal_align: Initial value for HorizontalAlign.
            vertical_align: Initial value for VerticalAlign.
            alignment_mode: Initial value for AlignmentMode.
            color: Initial value for Color.
            line_height: Initial value for LineHeight.
            mask_pattern: Initial value for MaskPattern.
            horizontal_auto_size: Initial value for HorizontalAutoSize.
            vertical_auto_size: Initial value for VerticalAutoSize.
            auto_size_min: Initial value for AutoSizeMin.
            auto_size_max: Initial value for AutoSizeMax.
            caret_position: Initial value for CaretPosition.
            selection_start: Initial value for SelectionStart.
            caret_color: Initial value for CaretColor.
            selection_color: Initial value for SelectionColor.
            interaction_target: Initial value for InteractionTarget.
            legacy_font_material: Initial value for _legacyFontMaterial.
            legacy_align: Initial value for _legacyAlign.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if font is not None:
            self.font = font
        if content is not None:
            self.content = content
        if parse_rich_text is not None:
            self.parse_rich_text = parse_rich_text
        if null_content is not None:
            self.null_content = null_content
        if size is not None:
            self.size = size
        if horizontal_align is not None:
            self.horizontal_align = horizontal_align
        if vertical_align is not None:
            self.vertical_align = vertical_align
        if alignment_mode is not None:
            self.alignment_mode = alignment_mode
        if color is not None:
            self.color = color
        if line_height is not None:
            self.line_height = line_height
        if mask_pattern is not None:
            self.mask_pattern = mask_pattern
        if horizontal_auto_size is not None:
            self.horizontal_auto_size = horizontal_auto_size
        if vertical_auto_size is not None:
            self.vertical_auto_size = vertical_auto_size
        if auto_size_min is not None:
            self.auto_size_min = auto_size_min
        if auto_size_max is not None:
            self.auto_size_max = auto_size_max
        if caret_position is not None:
            self.caret_position = caret_position
        if selection_start is not None:
            self.selection_start = selection_start
        if caret_color is not None:
            self.caret_color = caret_color
        if selection_color is not None:
            self.selection_color = selection_color
        if interaction_target is not None:
            self.interaction_target = interaction_target
        if legacy_font_material is not None:
            self.legacy_font_material = legacy_font_material
        if legacy_align is not None:
            self.legacy_align = legacy_align

    @property
    def font(self) -> str | None:
        """The font to use"""
        member = self.get_member("Font")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font.setter
    def font(self, target: str | IAssetProvider[FontSet] | None) -> None:
        """Set the Font reference by target ID or IAssetProvider[FontSet] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Font")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Font",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.FontSet>'),
            )

    @property
    def content(self) -> primitives.String | None:
        """What string of text to display"""
        member = self.get_member("Content")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @content.setter
    def content(self, value: primitives.String) -> None:
        """Set the Content field value."""
        member = self.get_member("Content")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Content", fields.FieldString(value=value)
            )

    @property
    def parse_rich_text(self) -> primitives.Bool | None:
        """Whether or not to interpret text formatting"""
        member = self.get_member("ParseRichText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parse_rich_text.setter
    def parse_rich_text(self, value: primitives.Bool) -> None:
        """Set the ParseRichText field value."""
        member = self.get_member("ParseRichText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParseRichText", fields.FieldBool(value=value)
            )

    @property
    def null_content(self) -> primitives.String | None:
        """What to display if Content is empty"""
        member = self.get_member("NullContent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @null_content.setter
    def null_content(self, value: primitives.String) -> None:
        """Set the NullContent field value."""
        member = self.get_member("NullContent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NullContent", fields.FieldString(value=value)
            )

    @property
    def size(self) -> primitives.Float | None:
        """The size to render text at, in display units"""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_align(self) -> TextHorizontalAlignment | None:
        """How to align the text, horizontally"""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: TextHorizontalAlignment | str) -> None:
        """Set HorizontalAlign. How to align the text, horizontally"""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HorizontalAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def vertical_align(self) -> TextVerticalAlignment | None:
        """How to align the text, vertically"""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextVerticalAlignment(member.value)
        return None

    @vertical_align.setter
    def vertical_align(self, value: TextVerticalAlignment | str) -> None:
        """Set VerticalAlign. How to align the text, vertically"""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VerticalAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def alignment_mode(self) -> AlignmentMode | None:
        """How to compute alignment"""
        member = self.get_member("AlignmentMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AlignmentMode(member.value)
        return None

    @alignment_mode.setter
    def alignment_mode(self, value: AlignmentMode | str) -> None:
        """Set AlignmentMode. How to compute alignment"""
        member = self.get_member("AlignmentMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AlignmentMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The color to render the text with"""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def materials(self) -> members.SyncList | None:
        """The Material(s) to render with"""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set Materials. The Material(s) to render with"""
        self.set_member("Materials", value)

    @property
    def line_height(self) -> primitives.Float | None:
        """How high each line of text is"""
        member = self.get_member("LineHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_height.setter
    def line_height(self, value: primitives.Float) -> None:
        """Set the LineHeight field value."""
        member = self.get_member("LineHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LineHeight", fields.FieldFloat(value=value)
            )

    @property
    def mask_pattern(self) -> primitives.String | None:
        """Text entered here will mask each character with this exact string (example for a password field: *)"""
        member = self.get_member("MaskPattern")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mask_pattern.setter
    def mask_pattern(self, value: primitives.String) -> None:
        """Set the MaskPattern field value."""
        member = self.get_member("MaskPattern")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaskPattern", fields.FieldString(value=value)
            )

    @property
    def horizontal_auto_size(self) -> primitives.Bool | None:
        """Automatically adjusts the text's size to fit in its horizontal space"""
        member = self.get_member("HorizontalAutoSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_auto_size.setter
    def horizontal_auto_size(self, value: primitives.Bool) -> None:
        """Set the HorizontalAutoSize field value."""
        member = self.get_member("HorizontalAutoSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalAutoSize", fields.FieldBool(value=value)
            )

    @property
    def vertical_auto_size(self) -> primitives.Bool | None:
        """Automatically adjusts the text's size to fit in its vertical space"""
        member = self.get_member("VerticalAutoSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_auto_size.setter
    def vertical_auto_size(self, value: primitives.Bool) -> None:
        """Set the VerticalAutoSize field value."""
        member = self.get_member("VerticalAutoSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalAutoSize", fields.FieldBool(value=value)
            )

    @property
    def auto_size_min(self) -> primitives.Float | None:
        """The minimum size that can be reached via auto-sizing"""
        member = self.get_member("AutoSizeMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_size_min.setter
    def auto_size_min(self, value: primitives.Float) -> None:
        """Set the AutoSizeMin field value."""
        member = self.get_member("AutoSizeMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoSizeMin", fields.FieldFloat(value=value)
            )

    @property
    def auto_size_max(self) -> primitives.Float | None:
        """The maximum size that can be reached via auto-sizing"""
        member = self.get_member("AutoSizeMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_size_max.setter
    def auto_size_max(self, value: primitives.Float) -> None:
        """Set the AutoSizeMax field value."""
        member = self.get_member("AutoSizeMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoSizeMax", fields.FieldFloat(value=value)
            )

    @property
    def caret_position(self) -> primitives.Int | None:
        """The text cursor position on this text"""
        member = self.get_member("CaretPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @caret_position.setter
    def caret_position(self, value: primitives.Int) -> None:
        """Set the CaretPosition field value."""
        member = self.get_member("CaretPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CaretPosition", fields.FieldInt(value=value)
            )

    @property
    def selection_start(self) -> primitives.Int | None:
        """The starting point for this text cursor"""
        member = self.get_member("SelectionStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selection_start.setter
    def selection_start(self, value: primitives.Int) -> None:
        """Set the SelectionStart field value."""
        member = self.get_member("SelectionStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectionStart", fields.FieldInt(value=value)
            )

    @property
    def caret_color(self) -> primitives.ColorX | None:
        """The text cursor color"""
        member = self.get_member("CaretColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @caret_color.setter
    def caret_color(self, value: primitives.ColorX) -> None:
        """Set the CaretColor field value."""
        member = self.get_member("CaretColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CaretColor", fields.FieldColorX(value=value)
            )

    @property
    def selection_color(self) -> primitives.ColorX | None:
        """The text selection/highlight color"""
        member = self.get_member("SelectionColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selection_color.setter
    def selection_color(self, value: primitives.ColorX) -> None:
        """Set the SelectionColor field value."""
        member = self.get_member("SelectionColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectionColor", fields.FieldColorX(value=value)
            )

    @property
    def interaction_target(self) -> primitives.Bool | None:
        """Makes this text as the interaction target for this UIX."""
        member = self.get_member("InteractionTarget")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interaction_target.setter
    def interaction_target(self, value: primitives.Bool) -> None:
        """Set the InteractionTarget field value."""
        member = self.get_member("InteractionTarget")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InteractionTarget", fields.FieldBool(value=value)
            )

    @property
    def legacy_font_material(self) -> str | None:
        """Internal"""
        member = self.get_member("_legacyFontMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @legacy_font_material.setter
    def legacy_font_material(self, target: str | FontMaterial | None) -> None:
        """Set the _legacyFontMaterial reference by target ID or FontMaterial instance."""
        target_id: str | None = target.id if isinstance(target, FontMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_legacyFontMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_legacyFontMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FontMaterial'),
            )

    @property
    def legacy_align(self) -> Alignment | None:
        """Internal"""
        member = self.get_member("_legacyAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Alignment(member.value)
        return None

    @legacy_align.setter
    def legacy_align(self, value: Alignment | str) -> None:
        """Set _legacyAlign. Internal"""
        member = self.get_member("_legacyAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_legacyAlign",
                members.FieldEnum(value=str(value)),
            )

