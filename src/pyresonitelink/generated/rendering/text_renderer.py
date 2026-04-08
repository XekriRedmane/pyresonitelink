"""Generated component: TextRenderer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
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
    """Wrapper for [FrooxEngine]FrooxEngine.TextRenderer.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextRenderer"

    def __init__(self, high_priority_integration: bool | None = None, override_bounding_box: bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, font: str | IAssetProvider[FontSet] | None = None, text: str | None = None, parse_rich_text: bool | None = None, null_text: str | None = None, size: np.float32 | None = None, color: primitives.ColorX | None = None, line_height: np.float32 | None = None, bounded: bool | None = None, bounds_size: primitives.Float2 | None = None, mask_pattern: str | None = None, horizontal_auto_size: bool | None = None, vertical_auto_size: bool | None = None, caret_position: np.int32 | None = None, selection_start: np.int32 | None = None, caret_color: primitives.ColorX | None = None, selection_color: primitives.ColorX | None = None, legacy_font_material: str | FontMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            font: Initial value for Font.
            text: Initial value for Text.
            parse_rich_text: Initial value for ParseRichText.
            null_text: Initial value for NullText.
            size: Initial value for Size.
            color: Initial value for Color.
            line_height: Initial value for LineHeight.
            bounded: Initial value for Bounded.
            bounds_size: Initial value for BoundsSize.
            mask_pattern: Initial value for MaskPattern.
            horizontal_auto_size: Initial value for HorizontalAutoSize.
            vertical_auto_size: Initial value for VerticalAutoSize.
            caret_position: Initial value for CaretPosition.
            selection_start: Initial value for SelectionStart.
            caret_color: Initial value for CaretColor.
            selection_color: Initial value for SelectionColor.
            legacy_font_material: Initial value for _legacyFontMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
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
        if color is not None:
            self.color = color
        if line_height is not None:
            self.line_height = line_height
        if bounded is not None:
            self.bounded = bounded
        if bounds_size is not None:
            self.bounds_size = bounds_size
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

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: bool) -> None:
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
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def font(self) -> str | None:
        """Target ID of the Font reference (targets IAssetProvider[FontSet])."""
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
    def text(self) -> str | None:
        """The Text field value."""
        member = self.get_member("Text")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @text.setter
    def text(self, value: str) -> None:
        """Set the Text field value."""
        member = self.get_member("Text")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Text", fields.FieldString(value=value)
            )

    @property
    def parse_rich_text(self) -> bool | None:
        """The ParseRichText field value."""
        member = self.get_member("ParseRichText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @parse_rich_text.setter
    def parse_rich_text(self, value: bool) -> None:
        """Set the ParseRichText field value."""
        member = self.get_member("ParseRichText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParseRichText", fields.FieldBool(value=value)
            )

    @property
    def null_text(self) -> str | None:
        """The NullText field value."""
        member = self.get_member("NullText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @null_text.setter
    def null_text(self, value: str) -> None:
        """Set the NullText field value."""
        member = self.get_member("NullText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NullText", fields.FieldString(value=value)
            )

    @property
    def size(self) -> np.float32 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: np.float32) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_align(self) -> members.FieldEnum | None:
        """The HorizontalAlign member."""
        member = self.get_member("HorizontalAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @horizontal_align.setter
    def horizontal_align(self, value: members.FieldEnum) -> None:
        """Set the HorizontalAlign member."""
        self.set_member("HorizontalAlign", value)

    @property
    def vertical_align(self) -> members.FieldEnum | None:
        """The VerticalAlign member."""
        member = self.get_member("VerticalAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertical_align.setter
    def vertical_align(self, value: members.FieldEnum) -> None:
        """Set the VerticalAlign member."""
        self.set_member("VerticalAlign", value)

    @property
    def alignment_mode(self) -> members.FieldEnum | None:
        """The AlignmentMode member."""
        member = self.get_member("AlignmentMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @alignment_mode.setter
    def alignment_mode(self, value: members.FieldEnum) -> None:
        """Set the AlignmentMode member."""
        self.set_member("AlignmentMode", value)

    @property
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
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
        """The Materials member."""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set the Materials member."""
        self.set_member("Materials", value)

    @property
    def line_height(self) -> np.float32 | None:
        """The LineHeight field value."""
        member = self.get_member("LineHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_height.setter
    def line_height(self, value: np.float32) -> None:
        """Set the LineHeight field value."""
        member = self.get_member("LineHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LineHeight", fields.FieldFloat(value=value)
            )

    @property
    def bounded(self) -> bool | None:
        """The Bounded field value."""
        member = self.get_member("Bounded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bounded.setter
    def bounded(self, value: bool) -> None:
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
        """The BoundsSize field value."""
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
    def bounds_alignment(self) -> members.FieldEnum | None:
        """The BoundsAlignment member."""
        member = self.get_member("BoundsAlignment")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @bounds_alignment.setter
    def bounds_alignment(self, value: members.FieldEnum) -> None:
        """Set the BoundsAlignment member."""
        self.set_member("BoundsAlignment", value)

    @property
    def mask_pattern(self) -> str | None:
        """The MaskPattern field value."""
        member = self.get_member("MaskPattern")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mask_pattern.setter
    def mask_pattern(self, value: str) -> None:
        """Set the MaskPattern field value."""
        member = self.get_member("MaskPattern")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaskPattern", fields.FieldString(value=value)
            )

    @property
    def horizontal_auto_size(self) -> bool | None:
        """The HorizontalAutoSize field value."""
        member = self.get_member("HorizontalAutoSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_auto_size.setter
    def horizontal_auto_size(self, value: bool) -> None:
        """Set the HorizontalAutoSize field value."""
        member = self.get_member("HorizontalAutoSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalAutoSize", fields.FieldBool(value=value)
            )

    @property
    def vertical_auto_size(self) -> bool | None:
        """The VerticalAutoSize field value."""
        member = self.get_member("VerticalAutoSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical_auto_size.setter
    def vertical_auto_size(self, value: bool) -> None:
        """Set the VerticalAutoSize field value."""
        member = self.get_member("VerticalAutoSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VerticalAutoSize", fields.FieldBool(value=value)
            )

    @property
    def caret_position(self) -> np.int32 | None:
        """The CaretPosition field value."""
        member = self.get_member("CaretPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @caret_position.setter
    def caret_position(self, value: np.int32) -> None:
        """Set the CaretPosition field value."""
        member = self.get_member("CaretPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CaretPosition", fields.FieldInt(value=value)
            )

    @property
    def selection_start(self) -> np.int32 | None:
        """The SelectionStart field value."""
        member = self.get_member("SelectionStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selection_start.setter
    def selection_start(self, value: np.int32) -> None:
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
        """The CaretColor field value."""
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
        """The SelectionColor field value."""
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
        """Target ID of the _legacyFontMaterial reference (targets FontMaterial)."""
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
    def legacy_align(self) -> members.FieldEnum | None:
        """The _legacyAlign member."""
        member = self.get_member("_legacyAlign")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @legacy_align.setter
    def legacy_align(self, value: members.FieldEnum) -> None:
        """Set the _legacyAlign member."""
        self.set_member("_legacyAlign", value)

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

