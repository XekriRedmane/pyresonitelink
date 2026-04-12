"""Generated component: TextRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.text_horizontal_alignment import TextHorizontalAlignment
from pyresonitelink.generated._enums.text_vertical_alignment import TextVerticalAlignment
from pyresonitelink.generated._enums.alignment_mode import AlignmentMode
from pyresonitelink.generated._enums.alignment import Alignment
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.font_set import FontSet
from pyresonitelink.generated._types.font_material import FontMaterial
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.itext import IText
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextRenderer(GeneratedComponent, IBounded, IText, IRenderable, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The TextRenderer component shows Text in the world. An example can be created from the Create New menu, Text, then Basic or Outline.

    Category: Rendering

    **See also**: UIX Text
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextRenderer"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, font: str | IAssetProvider[FontSet] | None = None, text: primitives.String | None = None, parse_rich_text: primitives.Bool | None = None, null_text: primitives.String | None = None, size: primitives.Float | None = None, horizontal_align: TextHorizontalAlignment | str | None = None, vertical_align: TextVerticalAlignment | str | None = None, alignment_mode: AlignmentMode | str | None = None, color: primitives.ColorX | None = None, line_height: primitives.Float | None = None, bounded: primitives.Bool | None = None, bounds_size: primitives.Float2 | None = None, bounds_alignment: Alignment | str | None = None, mask_pattern: primitives.String | None = None, horizontal_auto_size: primitives.Bool | None = None, vertical_auto_size: primitives.Bool | None = None, caret_position: primitives.Int | None = None, selection_start: primitives.Int | None = None, caret_color: primitives.ColorX | None = None, selection_color: primitives.ColorX | None = None, legacy_font_material: str | FontMaterial | None = None, legacy_align: Alignment | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            font: Initial value for Font.
            text: Initial value for Text.
            parse_rich_text: Initial value for ParseRichText.
            null_text: Initial value for NullText.
            size: Initial value for Size.
            horizontal_align: Initial value for HorizontalAlign.
            vertical_align: Initial value for VerticalAlign.
            alignment_mode: Initial value for AlignmentMode.
            color: Initial value for Color.
            line_height: Initial value for LineHeight.
            bounded: Initial value for Bounded.
            bounds_size: Initial value for BoundsSize.
            bounds_alignment: Initial value for BoundsAlignment.
            mask_pattern: Initial value for MaskPattern.
            horizontal_auto_size: Initial value for HorizontalAutoSize.
            vertical_auto_size: Initial value for VerticalAutoSize.
            caret_position: Initial value for CaretPosition.
            selection_start: Initial value for SelectionStart.
            caret_color: Initial value for CaretColor.
            selection_color: Initial value for SelectionColor.
            legacy_font_material: Initial value for _legacyFontMaterial.
            legacy_align: Initial value for _legacyAlign.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if profile is not None:
            self.profile = profile
        if font is not None:
            self.font = font
        if text is not None:
            self.text = text
        if parse_rich_text is not None:
            self.parse_rich_text = parse_rich_text
        if null_text is not None:
            self.null_text = null_text
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
        if bounded is not None:
            self.bounded = bounded
        if bounds_size is not None:
            self.bounds_size = bounds_size
        if bounds_alignment is not None:
            self.bounds_alignment = bounds_alignment
        if mask_pattern is not None:
            self.mask_pattern = mask_pattern
        if horizontal_auto_size is not None:
            self.horizontal_auto_size = horizontal_auto_size
        if vertical_auto_size is not None:
            self.vertical_auto_size = vertical_auto_size
        if caret_position is not None:
            self.caret_position = caret_position
        if selection_start is not None:
            self.selection_start = selection_start
        if caret_color is not None:
            self.caret_color = caret_color
        if selection_color is not None:
            self.selection_color = selection_color
        if legacy_font_material is not None:
            self.legacy_font_material = legacy_font_material
        if legacy_align is not None:
            self.legacy_align = legacy_align

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> primitives.Bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: primitives.Bool) -> None:
        """Set the OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideBoundingBox", fields.FieldBool(value=value)
            )

    @property
    def overriden_bounding_box(self) -> primitives.BoundingBox | None:
        """The OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overriden_bounding_box.setter
    def overriden_bounding_box(self, value: primitives.BoundingBox) -> None:
        """Set the OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverridenBoundingBox", fields.FieldBoundingBox(value=value)
            )

    @property
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def font(self) -> str | None:
        """The font set to use to render the text. For example, Times new Roman, or Avali Scratch."""
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
    def text(self) -> primitives.String | None:
        """The text to display. For example, "Hello world!"."""
        member = self.get_member("Text")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @text.setter
    def text(self, value: primitives.String) -> None:
        """Set the Text field value."""
        member = self.get_member("Text")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Text", fields.FieldString(value=value)
            )

    @property
    def parse_rich_text(self) -> primitives.Bool | None:
        """Whether or not to interpret text formatting tags like "" for bold and "" for itallic."""
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
    def null_text(self) -> primitives.String | None:
        """the text to display if ``Text`` is null. (Empty text doesn't count)"""
        member = self.get_member("NullText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @null_text.setter
    def null_text(self, value: primitives.String) -> None:
        """Set the NullText field value."""
        member = self.get_member("NullText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NullText", fields.FieldString(value=value)
            )

    @property
    def size(self) -> primitives.Float | None:
        """how big to render the text as."""
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
        """How to align the text horizontally."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextHorizontalAlignment(member.value)
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: TextHorizontalAlignment | str) -> None:
        """Set HorizontalAlign. How to align the text horizontally."""
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
        """how to align the text vertically."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TextVerticalAlignment(member.value)
        return None

    @vertical_align.setter
    def vertical_align(self, value: TextVerticalAlignment | str) -> None:
        """Set VerticalAlign. how to align the text vertically."""
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
        """how to align the text within the bounding box"""
        member = self.get_member("AlignmentMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AlignmentMode(member.value)
        return None

    @alignment_mode.setter
    def alignment_mode(self, value: AlignmentMode | str) -> None:
        """Set AlignmentMode. how to align the text within the bounding box"""
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
        """what color to render the text in."""
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
        """what materials to render the text as. Really only works with Unlit Text Material type."""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set Materials. what materials to render the text as. Really only works with Unlit Text Material type."""
        self.set_member("Materials", value)

    @property
    def line_height(self) -> primitives.Float | None:
        """how much space each text line should take up"""
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
    def bounded(self) -> primitives.Bool | None:
        """whether to restrict the text within a certain area"""
        member = self.get_member("Bounded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bounded.setter
    def bounded(self, value: primitives.Bool) -> None:
        """Set the Bounded field value."""
        member = self.get_member("Bounded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Bounded", fields.FieldBool(value=value)
            )

    @property
    def bounds_size(self) -> primitives.Float2 | None:
        """the area to use if ``Bounded`` is enabled."""
        member = self.get_member("BoundsSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bounds_size.setter
    def bounds_size(self, value: primitives.Float2) -> None:
        """Set the BoundsSize field value."""
        member = self.get_member("BoundsSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoundsSize", fields.FieldFloat2(value=value)
            )

    @property
    def bounds_alignment(self) -> Alignment | None:
        """how to align the text to the bounds and therefore how to handle text that spills out."""
        member = self.get_member("BoundsAlignment")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Alignment(member.value)
        return None

    @bounds_alignment.setter
    def bounds_alignment(self, value: Alignment | str) -> None:
        """Set BoundsAlignment. how to align the text to the bounds and therefore how to handle text that spills out."""
        member = self.get_member("BoundsAlignment")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BoundsAlignment",
                members.FieldEnum(value=str(value)),
            )

    @property
    def mask_pattern(self) -> primitives.String | None:
        """a string to replace every character in ``Text`` with when rendering. Useful for password fields."""
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
        """whether to scale the text to fit the bounds horizontally"""
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
        """whether to scale the text to fit the bounds vertically"""
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
    def caret_position(self) -> primitives.Int | None:
        """Where the typing cursor position is within the text by character index."""
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
        """where the selection starts if the text is being edited currently."""
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
        """the color of the typing cursor"""
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
        """the color of the typing selection."""
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
    def legacy_font_material(self) -> str | None:
        """Internal."""
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
        """Internal."""
        member = self.get_member("_legacyAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Alignment(member.value)
        return None

    @legacy_align.setter
    def legacy_align(self, value: Alignment | str) -> None:
        """Set _legacyAlign. Internal."""
        member = self.get_member("_legacyAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_legacyAlign",
                members.FieldEnum(value=str(value)),
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

