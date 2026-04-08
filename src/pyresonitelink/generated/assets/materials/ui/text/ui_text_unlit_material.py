"""Generated component: UI_TextUnlitMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.itext_material import ITextMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UI_TextUnlitMaterial(GeneratedComponent, IUIX_Material, ITextMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UI_TextUnlitMaterial.

    Category: Assets/Materials/UI/Text
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UI_TextUnlitMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, font_atlas: str | IAssetProvider[ITexture2D] | None = None, tint_color: primitives.ColorX | None = None, outline_color: primitives.ColorX | None = None, background_color: primitives.ColorX | None = None, auto_background_color: primitives.Bool | None = None, pixel_range: primitives.Float | None = None, face_dilate: primitives.Float | None = None, outline_thickness: primitives.Float | None = None, face_softness: primitives.Float | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, overlay: primitives.Bool | None = None, overlay_tint: primitives.ColorX | None = None, rect: primitives.Rect | None = None, rect_clip: primitives.Bool | None = None, stencil_id: primitives.Byte | None = None, stencil_write_mask: primitives.Byte | None = None, stencil_read_mask: primitives.Byte | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            font_atlas: Initial value for FontAtlas.
            tint_color: Initial value for TintColor.
            outline_color: Initial value for OutlineColor.
            background_color: Initial value for BackgroundColor.
            auto_background_color: Initial value for AutoBackgroundColor.
            pixel_range: Initial value for PixelRange.
            face_dilate: Initial value for FaceDilate.
            outline_thickness: Initial value for OutlineThickness.
            face_softness: Initial value for FaceSoftness.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            overlay: Initial value for Overlay.
            overlay_tint: Initial value for OverlayTint.
            rect: Initial value for Rect.
            rect_clip: Initial value for RectClip.
            stencil_id: Initial value for StencilID.
            stencil_write_mask: Initial value for StencilWriteMask.
            stencil_read_mask: Initial value for StencilReadMask.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if font_atlas is not None:
            self.font_atlas = font_atlas
        if tint_color is not None:
            self.tint_color = tint_color
        if outline_color is not None:
            self.outline_color = outline_color
        if background_color is not None:
            self.background_color = background_color
        if auto_background_color is not None:
            self.auto_background_color = auto_background_color
        if pixel_range is not None:
            self.pixel_range = pixel_range
        if face_dilate is not None:
            self.face_dilate = face_dilate
        if outline_thickness is not None:
            self.outline_thickness = outline_thickness
        if face_softness is not None:
            self.face_softness = face_softness
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if overlay is not None:
            self.overlay = overlay
        if overlay_tint is not None:
            self.overlay_tint = overlay_tint
        if rect is not None:
            self.rect = rect
        if rect_clip is not None:
            self.rect_clip = rect_clip
        if stencil_id is not None:
            self.stencil_id = stencil_id
        if stencil_write_mask is not None:
            self.stencil_write_mask = stencil_write_mask
        if stencil_read_mask is not None:
            self.stencil_read_mask = stencil_read_mask

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
    def shader(self) -> str | None:
        """Target ID of the _shader reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shader.setter
    def shader(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _shader reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shader",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def font_atlas(self) -> str | None:
        """Target ID of the FontAtlas reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FontAtlas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font_atlas.setter
    def font_atlas(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FontAtlas reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FontAtlas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FontAtlas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def tint_color(self) -> primitives.ColorX | None:
        """The TintColor field value."""
        member = self.get_member("TintColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_color.setter
    def tint_color(self, value: primitives.ColorX) -> None:
        """Set the TintColor field value."""
        member = self.get_member("TintColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintColor", fields.FieldColorX(value=value)
            )

    @property
    def outline_color(self) -> primitives.ColorX | None:
        """The OutlineColor field value."""
        member = self.get_member("OutlineColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_color.setter
    def outline_color(self, value: primitives.ColorX) -> None:
        """Set the OutlineColor field value."""
        member = self.get_member("OutlineColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineColor", fields.FieldColorX(value=value)
            )

    @property
    def background_color(self) -> primitives.ColorX | None:
        """The BackgroundColor field value."""
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
    def auto_background_color(self) -> primitives.Bool | None:
        """The AutoBackgroundColor field value."""
        member = self.get_member("AutoBackgroundColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_background_color.setter
    def auto_background_color(self, value: primitives.Bool) -> None:
        """Set the AutoBackgroundColor field value."""
        member = self.get_member("AutoBackgroundColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoBackgroundColor", fields.FieldBool(value=value)
            )

    @property
    def glyph_render_method(self) -> members.FieldEnum | None:
        """The GlyphRenderMethod member."""
        member = self.get_member("GlyphRenderMethod")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @glyph_render_method.setter
    def glyph_render_method(self, value: members.FieldEnum) -> None:
        """Set the GlyphRenderMethod member."""
        self.set_member("GlyphRenderMethod", value)

    @property
    def pixel_range(self) -> primitives.Float | None:
        """The PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pixel_range.setter
    def pixel_range(self, value: primitives.Float) -> None:
        """Set the PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PixelRange", fields.FieldFloat(value=value)
            )

    @property
    def face_dilate(self) -> primitives.Float | None:
        """The FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_dilate.setter
    def face_dilate(self, value: primitives.Float) -> None:
        """Set the FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceDilate", fields.FieldFloat(value=value)
            )

    @property
    def outline_thickness(self) -> primitives.Float | None:
        """The OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_thickness.setter
    def outline_thickness(self, value: primitives.Float) -> None:
        """Set the OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineThickness", fields.FieldFloat(value=value)
            )

    @property
    def face_softness(self) -> primitives.Float | None:
        """The FaceSoftness field value."""
        member = self.get_member("FaceSoftness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_softness.setter
    def face_softness(self, value: primitives.Float) -> None:
        """Set the FaceSoftness field value."""
        member = self.get_member("FaceSoftness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceSoftness", fields.FieldFloat(value=value)
            )

    @property
    def blend_mode(self) -> members.FieldEnum | None:
        """The BlendMode member."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @blend_mode.setter
    def blend_mode(self, value: members.FieldEnum) -> None:
        """Set the BlendMode member."""
        self.set_member("BlendMode", value)

    @property
    def sidedness(self) -> members.FieldEnum | None:
        """The Sidedness member."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sidedness.setter
    def sidedness(self, value: members.FieldEnum) -> None:
        """Set the Sidedness member."""
        self.set_member("Sidedness", value)

    @property
    def zwrite(self) -> members.FieldEnum | None:
        """The ZWrite member."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @zwrite.setter
    def zwrite(self, value: members.FieldEnum) -> None:
        """Set the ZWrite member."""
        self.set_member("ZWrite", value)

    @property
    def ztest(self) -> members.FieldEnum | None:
        """The ZTest member."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ztest.setter
    def ztest(self, value: members.FieldEnum) -> None:
        """Set the ZTest member."""
        self.set_member("ZTest", value)

    @property
    def offset_factor(self) -> primitives.Float | None:
        """The OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_factor.setter
    def offset_factor(self, value: primitives.Float) -> None:
        """Set the OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetFactor", fields.FieldFloat(value=value)
            )

    @property
    def offset_units(self) -> primitives.Float | None:
        """The OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_units.setter
    def offset_units(self, value: primitives.Float) -> None:
        """Set the OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetUnits", fields.FieldFloat(value=value)
            )

    @property
    def render_queue(self) -> primitives.Int | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: primitives.Int) -> None:
        """Set the RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderQueue", fields.FieldInt(value=value)
            )

    @property
    def overlay(self) -> primitives.Bool | None:
        """The Overlay field value."""
        member = self.get_member("Overlay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overlay.setter
    def overlay(self, value: primitives.Bool) -> None:
        """Set the Overlay field value."""
        member = self.get_member("Overlay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Overlay", fields.FieldBool(value=value)
            )

    @property
    def overlay_tint(self) -> primitives.ColorX | None:
        """The OverlayTint field value."""
        member = self.get_member("OverlayTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overlay_tint.setter
    def overlay_tint(self, value: primitives.ColorX) -> None:
        """Set the OverlayTint field value."""
        member = self.get_member("OverlayTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverlayTint", fields.FieldColorX(value=value)
            )

    @property
    def rect(self) -> primitives.Rect | None:
        """The Rect field value."""
        member = self.get_member("Rect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect.setter
    def rect(self, value: primitives.Rect) -> None:
        """Set the Rect field value."""
        member = self.get_member("Rect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rect", fields.FieldRect(value=value)
            )

    @property
    def rect_clip(self) -> primitives.Bool | None:
        """The RectClip field value."""
        member = self.get_member("RectClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect_clip.setter
    def rect_clip(self, value: primitives.Bool) -> None:
        """Set the RectClip field value."""
        member = self.get_member("RectClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RectClip", fields.FieldBool(value=value)
            )

    @property
    def color_mask(self) -> members.FieldEnum | None:
        """The ColorMask member."""
        member = self.get_member("ColorMask")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @color_mask.setter
    def color_mask(self, value: members.FieldEnum) -> None:
        """Set the ColorMask member."""
        self.set_member("ColorMask", value)

    @property
    def stencil_comparison(self) -> members.FieldEnum | None:
        """The StencilComparison member."""
        member = self.get_member("StencilComparison")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @stencil_comparison.setter
    def stencil_comparison(self, value: members.FieldEnum) -> None:
        """Set the StencilComparison member."""
        self.set_member("StencilComparison", value)

    @property
    def stencil_operation(self) -> members.FieldEnum | None:
        """The StencilOperation member."""
        member = self.get_member("StencilOperation")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @stencil_operation.setter
    def stencil_operation(self, value: members.FieldEnum) -> None:
        """Set the StencilOperation member."""
        self.set_member("StencilOperation", value)

    @property
    def stencil_id(self) -> primitives.Byte | None:
        """The StencilID field value."""
        member = self.get_member("StencilID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_id.setter
    def stencil_id(self, value: primitives.Byte) -> None:
        """Set the StencilID field value."""
        member = self.get_member("StencilID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilID", fields.FieldByte(value=value)
            )

    @property
    def stencil_write_mask(self) -> primitives.Byte | None:
        """The StencilWriteMask field value."""
        member = self.get_member("StencilWriteMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_write_mask.setter
    def stencil_write_mask(self, value: primitives.Byte) -> None:
        """Set the StencilWriteMask field value."""
        member = self.get_member("StencilWriteMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilWriteMask", fields.FieldByte(value=value)
            )

    @property
    def stencil_read_mask(self) -> primitives.Byte | None:
        """The StencilReadMask field value."""
        member = self.get_member("StencilReadMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_read_mask.setter
    def stencil_read_mask(self, value: primitives.Byte) -> None:
        """Set the StencilReadMask field value."""
        member = self.get_member("StencilReadMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilReadMask", fields.FieldByte(value=value)
            )

