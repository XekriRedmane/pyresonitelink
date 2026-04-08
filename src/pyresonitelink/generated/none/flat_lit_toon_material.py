"""Generated component: FlatLitToonMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icommon_material import ICommonMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FlatLitToonMaterial(GeneratedComponent, ICommonMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FlatLitToonMaterial.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FlatLitToonMaterial"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, main_texture: str | IAssetProvider[ITexture2D] | None = None, color_mask: str | IAssetProvider[ITexture2D] | None = None, emission_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, main_texture_scale: primitives.Float2 | None = None, main_texture_offset: primitives.Float2 | None = None, color_mask_scale: primitives.Float2 | None = None, color_mask_offset: primitives.Float2 | None = None, emission_map_scale: primitives.Float2 | None = None, emission_map_offset: primitives.Float2 | None = None, normal_map_scale: primitives.Float2 | None = None, normal_map_offset: primitives.Float2 | None = None, alpha_cutoff: np.float32 | None = None, color: primitives.ColorX | None = None, emission_color: primitives.ColorX | None = None, shadow: np.float32 | None = None, outline_width: np.float32 | None = None, outline_color: primitives.ColorX | None = None, outline_tint: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            main_texture: Initial value for MainTexture.
            color_mask: Initial value for ColorMask.
            emission_map: Initial value for EmissionMap.
            normal_map: Initial value for NormalMap.
            main_texture_scale: Initial value for MainTextureScale.
            main_texture_offset: Initial value for MainTextureOffset.
            color_mask_scale: Initial value for ColorMaskScale.
            color_mask_offset: Initial value for ColorMaskOffset.
            emission_map_scale: Initial value for EmissionMapScale.
            emission_map_offset: Initial value for EmissionMapOffset.
            normal_map_scale: Initial value for NormalMapScale.
            normal_map_offset: Initial value for NormalMapOffset.
            alpha_cutoff: Initial value for AlphaCutoff.
            color: Initial value for Color.
            emission_color: Initial value for EmissionColor.
            shadow: Initial value for Shadow.
            outline_width: Initial value for OutlineWidth.
            outline_color: Initial value for OutlineColor.
            outline_tint: Initial value for OutlineTint.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if main_texture is not None:
            self.main_texture = main_texture
        if color_mask is not None:
            self.color_mask = color_mask
        if emission_map is not None:
            self.emission_map = emission_map
        if normal_map is not None:
            self.normal_map = normal_map
        if main_texture_scale is not None:
            self.main_texture_scale = main_texture_scale
        if main_texture_offset is not None:
            self.main_texture_offset = main_texture_offset
        if color_mask_scale is not None:
            self.color_mask_scale = color_mask_scale
        if color_mask_offset is not None:
            self.color_mask_offset = color_mask_offset
        if emission_map_scale is not None:
            self.emission_map_scale = emission_map_scale
        if emission_map_offset is not None:
            self.emission_map_offset = emission_map_offset
        if normal_map_scale is not None:
            self.normal_map_scale = normal_map_scale
        if normal_map_offset is not None:
            self.normal_map_offset = normal_map_offset
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if color is not None:
            self.color = color
        if emission_color is not None:
            self.emission_color = emission_color
        if shadow is not None:
            self.shadow = shadow
        if outline_width is not None:
            self.outline_width = outline_width
        if outline_color is not None:
            self.outline_color = outline_color
        if outline_tint is not None:
            self.outline_tint = outline_tint
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue

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
    def main_texture(self) -> str | None:
        """Target ID of the MainTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MainTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @main_texture.setter
    def main_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MainTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MainTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MainTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def color_mask(self) -> str | None:
        """Target ID of the ColorMask reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ColorMask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_mask.setter
    def color_mask(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ColorMask reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ColorMask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColorMask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emission_map(self) -> str | None:
        """Target ID of the EmissionMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissionMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emission_map.setter
    def emission_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissionMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissionMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissionMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def normal_map(self) -> str | None:
        """Target ID of the NormalMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NormalMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normal_map.setter
    def normal_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NormalMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NormalMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def main_texture_scale(self) -> primitives.Float2 | None:
        """The MainTextureScale field value."""
        member = self.get_member("MainTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @main_texture_scale.setter
    def main_texture_scale(self, value: primitives.Float2) -> None:
        """Set the MainTextureScale field value."""
        member = self.get_member("MainTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MainTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def main_texture_offset(self) -> primitives.Float2 | None:
        """The MainTextureOffset field value."""
        member = self.get_member("MainTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @main_texture_offset.setter
    def main_texture_offset(self, value: primitives.Float2) -> None:
        """Set the MainTextureOffset field value."""
        member = self.get_member("MainTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MainTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def color_mask_scale(self) -> primitives.Float2 | None:
        """The ColorMaskScale field value."""
        member = self.get_member("ColorMaskScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_mask_scale.setter
    def color_mask_scale(self, value: primitives.Float2) -> None:
        """Set the ColorMaskScale field value."""
        member = self.get_member("ColorMaskScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorMaskScale", fields.FieldFloat2(value=value)
            )

    @property
    def color_mask_offset(self) -> primitives.Float2 | None:
        """The ColorMaskOffset field value."""
        member = self.get_member("ColorMaskOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_mask_offset.setter
    def color_mask_offset(self, value: primitives.Float2) -> None:
        """Set the ColorMaskOffset field value."""
        member = self.get_member("ColorMaskOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorMaskOffset", fields.FieldFloat2(value=value)
            )

    @property
    def emission_map_scale(self) -> primitives.Float2 | None:
        """The EmissionMapScale field value."""
        member = self.get_member("EmissionMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_map_scale.setter
    def emission_map_scale(self, value: primitives.Float2) -> None:
        """Set the EmissionMapScale field value."""
        member = self.get_member("EmissionMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def emission_map_offset(self) -> primitives.Float2 | None:
        """The EmissionMapOffset field value."""
        member = self.get_member("EmissionMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_map_offset.setter
    def emission_map_offset(self, value: primitives.Float2) -> None:
        """Set the EmissionMapOffset field value."""
        member = self.get_member("EmissionMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def normal_map_scale(self) -> primitives.Float2 | None:
        """The NormalMapScale field value."""
        member = self.get_member("NormalMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_map_scale.setter
    def normal_map_scale(self, value: primitives.Float2) -> None:
        """Set the NormalMapScale field value."""
        member = self.get_member("NormalMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def normal_map_offset(self) -> primitives.Float2 | None:
        """The NormalMapOffset field value."""
        member = self.get_member("NormalMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_map_offset.setter
    def normal_map_offset(self, value: primitives.Float2) -> None:
        """Set the NormalMapOffset field value."""
        member = self.get_member("NormalMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def alpha_cutoff(self) -> np.float32 | None:
        """The AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_cutoff.setter
    def alpha_cutoff(self, value: np.float32) -> None:
        """Set the AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaCutoff", fields.FieldFloat(value=value)
            )

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
    def emission_color(self) -> primitives.ColorX | None:
        """The EmissionColor field value."""
        member = self.get_member("EmissionColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_color.setter
    def emission_color(self, value: primitives.ColorX) -> None:
        """Set the EmissionColor field value."""
        member = self.get_member("EmissionColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionColor", fields.FieldColorX(value=value)
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
    def shadow(self) -> np.float32 | None:
        """The Shadow field value."""
        member = self.get_member("Shadow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow.setter
    def shadow(self, value: np.float32) -> None:
        """Set the Shadow field value."""
        member = self.get_member("Shadow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Shadow", fields.FieldFloat(value=value)
            )

    @property
    def outline(self) -> members.FieldEnum | None:
        """The Outline member."""
        member = self.get_member("Outline")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @outline.setter
    def outline(self, value: members.FieldEnum) -> None:
        """Set the Outline member."""
        self.set_member("Outline", value)

    @property
    def outline_width(self) -> np.float32 | None:
        """The OutlineWidth field value."""
        member = self.get_member("OutlineWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_width.setter
    def outline_width(self, value: np.float32) -> None:
        """Set the OutlineWidth field value."""
        member = self.get_member("OutlineWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineWidth", fields.FieldFloat(value=value)
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
    def outline_tint(self) -> np.float32 | None:
        """The OutlineTint field value."""
        member = self.get_member("OutlineTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_tint.setter
    def outline_tint(self, value: np.float32) -> None:
        """Set the OutlineTint field value."""
        member = self.get_member("OutlineTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineTint", fields.FieldFloat(value=value)
            )

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

