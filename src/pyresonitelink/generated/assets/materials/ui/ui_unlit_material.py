"""Generated component: UI_UnlitMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icommon_material import ICommonMaterial
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UI_UnlitMaterial(GeneratedComponent, ICommonMaterial, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UI_UnlitMaterial.

    Category: Assets/Materials/UI
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UI_UnlitMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, rect: primitives.Rect | None = None, rect_clip: primitives.Bool | None = None, stencil_id: primitives.Byte | None = None, stencil_write_mask: primitives.Byte | None = None, stencil_read_mask: primitives.Byte | None = None, render_queue: primitives.Int | None = None, shader: str | IAssetProvider[Shader] | None = None, texture: str | IAssetProvider[ITexture2D] | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, tint: primitives.ColorX | None = None, overlay: primitives.Bool | None = None, overlay_tint: primitives.ColorX | None = None, alpha_cutoff: primitives.Float | None = None, alpha_clip: primitives.Bool | None = None, mask_texture: str | IAssetProvider[ITexture2D] | None = None, mask_scale: primitives.Float2 | None = None, mask_offset: primitives.Float2 | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            rect: Initial value for Rect.
            rect_clip: Initial value for RectClip.
            stencil_id: Initial value for StencilID.
            stencil_write_mask: Initial value for StencilWriteMask.
            stencil_read_mask: Initial value for StencilReadMask.
            render_queue: Initial value for RenderQueue.
            shader: Initial value for _shader.
            texture: Initial value for Texture.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            tint: Initial value for Tint.
            overlay: Initial value for Overlay.
            overlay_tint: Initial value for OverlayTint.
            alpha_cutoff: Initial value for AlphaCutoff.
            alpha_clip: Initial value for AlphaClip.
            mask_texture: Initial value for MaskTexture.
            mask_scale: Initial value for MaskScale.
            mask_offset: Initial value for MaskOffset.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
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
        if render_queue is not None:
            self.render_queue = render_queue
        if shader is not None:
            self.shader = shader
        if texture is not None:
            self.texture = texture
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if tint is not None:
            self.tint = tint
        if overlay is not None:
            self.overlay = overlay
        if overlay_tint is not None:
            self.overlay_tint = overlay_tint
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if alpha_clip is not None:
            self.alpha_clip = alpha_clip
        if mask_texture is not None:
            self.mask_texture = mask_texture
        if mask_scale is not None:
            self.mask_scale = mask_scale
        if mask_offset is not None:
            self.mask_offset = mask_offset
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units

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
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def texture_scale(self) -> primitives.Float2 | None:
        """The TextureScale field value."""
        member = self.get_member("TextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_scale.setter
    def texture_scale(self, value: primitives.Float2) -> None:
        """Set the TextureScale field value."""
        member = self.get_member("TextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def texture_offset(self) -> primitives.Float2 | None:
        """The TextureOffset field value."""
        member = self.get_member("TextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_offset.setter
    def texture_offset(self, value: primitives.Float2) -> None:
        """Set the TextureOffset field value."""
        member = self.get_member("TextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def tint(self) -> primitives.ColorX | None:
        """The Tint field value."""
        member = self.get_member("Tint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint.setter
    def tint(self, value: primitives.ColorX) -> None:
        """Set the Tint field value."""
        member = self.get_member("Tint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tint", fields.FieldColorX(value=value)
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
    def alpha_cutoff(self) -> primitives.Float | None:
        """The AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_cutoff.setter
    def alpha_cutoff(self, value: primitives.Float) -> None:
        """Set the AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaCutoff", fields.FieldFloat(value=value)
            )

    @property
    def alpha_clip(self) -> primitives.Bool | None:
        """The AlphaClip field value."""
        member = self.get_member("AlphaClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_clip.setter
    def alpha_clip(self, value: primitives.Bool) -> None:
        """Set the AlphaClip field value."""
        member = self.get_member("AlphaClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaClip", fields.FieldBool(value=value)
            )

    @property
    def texture_mode(self) -> members.FieldEnum | None:
        """The TextureMode member."""
        member = self.get_member("TextureMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @texture_mode.setter
    def texture_mode(self, value: members.FieldEnum) -> None:
        """Set the TextureMode member."""
        self.set_member("TextureMode", value)

    @property
    def mask_texture(self) -> str | None:
        """Target ID of the MaskTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MaskTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mask_texture.setter
    def mask_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MaskTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MaskTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaskTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def mask_scale(self) -> primitives.Float2 | None:
        """The MaskScale field value."""
        member = self.get_member("MaskScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mask_scale.setter
    def mask_scale(self, value: primitives.Float2) -> None:
        """Set the MaskScale field value."""
        member = self.get_member("MaskScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaskScale", fields.FieldFloat2(value=value)
            )

    @property
    def mask_offset(self) -> primitives.Float2 | None:
        """The MaskOffset field value."""
        member = self.get_member("MaskOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mask_offset.setter
    def mask_offset(self, value: primitives.Float2) -> None:
        """Set the MaskOffset field value."""
        member = self.get_member("MaskOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaskOffset", fields.FieldFloat2(value=value)
            )

    @property
    def mask_mode(self) -> members.FieldEnum | None:
        """The MaskMode member."""
        member = self.get_member("MaskMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mask_mode.setter
    def mask_mode(self, value: members.FieldEnum) -> None:
        """Set the MaskMode member."""
        self.set_member("MaskMode", value)

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

