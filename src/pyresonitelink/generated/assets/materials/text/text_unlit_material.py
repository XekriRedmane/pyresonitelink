"""Generated component: TextUnlitMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture2_d import ITexture2D
from pyresonitelink.generated._types.itext_material import ITextMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextUnlitMaterial(GeneratedComponent, ITextMaterial, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextUnlitMaterial.

    Category: Assets/Materials/Text
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextUnlitMaterial"

    def __init__(self, shader: str | IAssetProvider[Shader] | None = None, font_atlas: str | IAssetProvider[ITexture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            shader: Initial value for _shader.
            font_atlas: Initial value for FontAtlas.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if shader is not None:
            self.shader = shader
        if font_atlas is not None:
            self.font_atlas = font_atlas

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
    def auto_background_color(self) -> bool | None:
        """The AutoBackgroundColor field value."""
        member = self.get_member("AutoBackgroundColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_background_color.setter
    def auto_background_color(self, value: bool) -> None:
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
    def pixel_range(self) -> np.float32 | None:
        """The PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pixel_range.setter
    def pixel_range(self, value: np.float32) -> None:
        """Set the PixelRange field value."""
        member = self.get_member("PixelRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PixelRange", fields.FieldFloat(value=value)
            )

    @property
    def face_dilate(self) -> np.float32 | None:
        """The FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_dilate.setter
    def face_dilate(self, value: np.float32) -> None:
        """Set the FaceDilate field value."""
        member = self.get_member("FaceDilate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FaceDilate", fields.FieldFloat(value=value)
            )

    @property
    def outline_thickness(self) -> np.float32 | None:
        """The OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_thickness.setter
    def outline_thickness(self, value: np.float32) -> None:
        """Set the OutlineThickness field value."""
        member = self.get_member("OutlineThickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineThickness", fields.FieldFloat(value=value)
            )

    @property
    def face_softness(self) -> np.float32 | None:
        """The FaceSoftness field value."""
        member = self.get_member("FaceSoftness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @face_softness.setter
    def face_softness(self, value: np.float32) -> None:
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
    def offset_factor(self) -> np.float32 | None:
        """The OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_factor.setter
    def offset_factor(self, value: np.float32) -> None:
        """Set the OffsetFactor field value."""
        member = self.get_member("OffsetFactor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetFactor", fields.FieldFloat(value=value)
            )

    @property
    def offset_units(self) -> np.float32 | None:
        """The OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_units.setter
    def offset_units(self, value: np.float32) -> None:
        """Set the OffsetUnits field value."""
        member = self.get_member("OffsetUnits")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetUnits", fields.FieldFloat(value=value)
            )

    @property
    def render_queue(self) -> np.int32 | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: np.int32) -> None:
        """Set the RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderQueue", fields.FieldInt(value=value)
            )

