"""Generated component: XiexeToonMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.icommon_material import ICommonMaterial
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class XiexeToonMaterial(GeneratedComponent, ICommonMaterial, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.XiexeToonMaterial.

    Category: Assets/Materials
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.XiexeToonMaterial"

    def __init__(self, high_priority_integration: bool | None = None, main_texture: str | IAssetProvider[ITexture2D] | None = None, color: primitives.ColorX | None = None, use_vertex_colors: bool | None = None, alpha_clip: np.float32 | None = None, main_texture_scale: primitives.Float2 | None = None, main_texture_offset: primitives.Float2 | None = None, saturation: np.float32 | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_map_scale: primitives.Float2 | None = None, normal_map_offset: primitives.Float2 | None = None, normal_scale: np.float32 | None = None, metallic: np.float32 | None = None, glossiness: np.float32 | None = None, reflectivity: np.float32 | None = None, metallic_gloss_map: str | IAssetProvider[ITexture2D] | None = None, metallic_gloss_map_scale: primitives.Float2 | None = None, metallic_gloss_map_offset: primitives.Float2 | None = None, emission_map: str | IAssetProvider[ITexture2D] | None = None, emission_color: primitives.ColorX | None = None, emission_map_scale: primitives.Float2 | None = None, emission_map_offset: primitives.Float2 | None = None, rim_color: primitives.ColorX | None = None, rim_albedo_tint: np.float32 | None = None, rim_attenuation_effect: np.float32 | None = None, rim_intensity: np.float32 | None = None, rim_range: np.float32 | None = None, rim_threshold: np.float32 | None = None, rim_sharpness: np.float32 | None = None, specular_intensity: np.float32 | None = None, specular_area: np.float32 | None = None, matcap: str | IAssetProvider[ITexture2D] | None = None, matcap_tint: primitives.ColorX | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, occlusion_map_scale: primitives.Float2 | None = None, occlusion_map_offset: primitives.Float2 | None = None, occlusion_color: primitives.ColorX | None = None, outline_width: np.float32 | None = None, outline_color: primitives.ColorX | None = None, outline_albedo_tint: bool | None = None, outline_mask: str | IAssetProvider[ITexture2D] | None = None, shadow_ramp: str | IAssetProvider[ITexture2D] | None = None, shadow_ramp_mask: str | IAssetProvider[ITexture2D] | None = None, shadow_ramp_mask_scale: primitives.Float2 | None = None, shadow_ramp_mask_offset: primitives.Float2 | None = None, shadow_rim: primitives.ColorX | None = None, shadow_sharpness: np.float32 | None = None, shadow_rim_range: np.float32 | None = None, shadow_rim_threshold: np.float32 | None = None, shadow_rim_sharpness: np.float32 | None = None, shadow_rim_albedo_tint: np.float32 | None = None, thickness_map: str | IAssetProvider[ITexture2D] | None = None, thickness_map_scale: primitives.Float2 | None = None, thickness_map_offset: primitives.Float2 | None = None, subsurface_color: primitives.ColorX | None = None, subsurface_distortion: np.float32 | None = None, subsurface_power: np.float32 | None = None, subsurface_scale: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, albedo_uv: np.int32 | None = None, normal_uv: np.int32 | None = None, metallic_uv: np.int32 | None = None, thickness_uv: np.int32 | None = None, occlusion_uv: np.int32 | None = None, emission_uv: np.int32 | None = None, render_queue: np.int32 | None = None, legacy_cutout: bool | None = None, regular: str | IAssetProvider[Shader] | None = None, outline: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            main_texture: Initial value for MainTexture.
            color: Initial value for Color.
            use_vertex_colors: Initial value for UseVertexColors.
            alpha_clip: Initial value for AlphaClip.
            main_texture_scale: Initial value for MainTextureScale.
            main_texture_offset: Initial value for MainTextureOffset.
            saturation: Initial value for Saturation.
            normal_map: Initial value for NormalMap.
            normal_map_scale: Initial value for NormalMapScale.
            normal_map_offset: Initial value for NormalMapOffset.
            normal_scale: Initial value for NormalScale.
            metallic: Initial value for Metallic.
            glossiness: Initial value for Glossiness.
            reflectivity: Initial value for Reflectivity.
            metallic_gloss_map: Initial value for MetallicGlossMap.
            metallic_gloss_map_scale: Initial value for MetallicGlossMapScale.
            metallic_gloss_map_offset: Initial value for MetallicGlossMapOffset.
            emission_map: Initial value for EmissionMap.
            emission_color: Initial value for EmissionColor.
            emission_map_scale: Initial value for EmissionMapScale.
            emission_map_offset: Initial value for EmissionMapOffset.
            rim_color: Initial value for RimColor.
            rim_albedo_tint: Initial value for RimAlbedoTint.
            rim_attenuation_effect: Initial value for RimAttenuationEffect.
            rim_intensity: Initial value for RimIntensity.
            rim_range: Initial value for RimRange.
            rim_threshold: Initial value for RimThreshold.
            rim_sharpness: Initial value for RimSharpness.
            specular_intensity: Initial value for SpecularIntensity.
            specular_area: Initial value for SpecularArea.
            matcap: Initial value for Matcap.
            matcap_tint: Initial value for MatcapTint.
            occlusion_map: Initial value for OcclusionMap.
            occlusion_map_scale: Initial value for OcclusionMapScale.
            occlusion_map_offset: Initial value for OcclusionMapOffset.
            occlusion_color: Initial value for OcclusionColor.
            outline_width: Initial value for OutlineWidth.
            outline_color: Initial value for OutlineColor.
            outline_albedo_tint: Initial value for OutlineAlbedoTint.
            outline_mask: Initial value for OutlineMask.
            shadow_ramp: Initial value for ShadowRamp.
            shadow_ramp_mask: Initial value for ShadowRampMask.
            shadow_ramp_mask_scale: Initial value for ShadowRampMaskScale.
            shadow_ramp_mask_offset: Initial value for ShadowRampMaskOffset.
            shadow_rim: Initial value for ShadowRim.
            shadow_sharpness: Initial value for ShadowSharpness.
            shadow_rim_range: Initial value for ShadowRimRange.
            shadow_rim_threshold: Initial value for ShadowRimThreshold.
            shadow_rim_sharpness: Initial value for ShadowRimSharpness.
            shadow_rim_albedo_tint: Initial value for ShadowRimAlbedoTint.
            thickness_map: Initial value for ThicknessMap.
            thickness_map_scale: Initial value for ThicknessMapScale.
            thickness_map_offset: Initial value for ThicknessMapOffset.
            subsurface_color: Initial value for SubsurfaceColor.
            subsurface_distortion: Initial value for SubsurfaceDistortion.
            subsurface_power: Initial value for SubsurfacePower.
            subsurface_scale: Initial value for SubsurfaceScale.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            albedo_uv: Initial value for AlbedoUV.
            normal_uv: Initial value for NormalUV.
            metallic_uv: Initial value for MetallicUV.
            thickness_uv: Initial value for ThicknessUV.
            occlusion_uv: Initial value for OcclusionUV.
            emission_uv: Initial value for EmissionUV.
            render_queue: Initial value for RenderQueue.
            legacy_cutout: Initial value for __legacyCutout.
            regular: Initial value for _regular.
            outline: Initial value for _outline.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if main_texture is not None:
            self.main_texture = main_texture
        if color is not None:
            self.color = color
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if alpha_clip is not None:
            self.alpha_clip = alpha_clip
        if main_texture_scale is not None:
            self.main_texture_scale = main_texture_scale
        if main_texture_offset is not None:
            self.main_texture_offset = main_texture_offset
        if saturation is not None:
            self.saturation = saturation
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_map_scale is not None:
            self.normal_map_scale = normal_map_scale
        if normal_map_offset is not None:
            self.normal_map_offset = normal_map_offset
        if normal_scale is not None:
            self.normal_scale = normal_scale
        if metallic is not None:
            self.metallic = metallic
        if glossiness is not None:
            self.glossiness = glossiness
        if reflectivity is not None:
            self.reflectivity = reflectivity
        if metallic_gloss_map is not None:
            self.metallic_gloss_map = metallic_gloss_map
        if metallic_gloss_map_scale is not None:
            self.metallic_gloss_map_scale = metallic_gloss_map_scale
        if metallic_gloss_map_offset is not None:
            self.metallic_gloss_map_offset = metallic_gloss_map_offset
        if emission_map is not None:
            self.emission_map = emission_map
        if emission_color is not None:
            self.emission_color = emission_color
        if emission_map_scale is not None:
            self.emission_map_scale = emission_map_scale
        if emission_map_offset is not None:
            self.emission_map_offset = emission_map_offset
        if rim_color is not None:
            self.rim_color = rim_color
        if rim_albedo_tint is not None:
            self.rim_albedo_tint = rim_albedo_tint
        if rim_attenuation_effect is not None:
            self.rim_attenuation_effect = rim_attenuation_effect
        if rim_intensity is not None:
            self.rim_intensity = rim_intensity
        if rim_range is not None:
            self.rim_range = rim_range
        if rim_threshold is not None:
            self.rim_threshold = rim_threshold
        if rim_sharpness is not None:
            self.rim_sharpness = rim_sharpness
        if specular_intensity is not None:
            self.specular_intensity = specular_intensity
        if specular_area is not None:
            self.specular_area = specular_area
        if matcap is not None:
            self.matcap = matcap
        if matcap_tint is not None:
            self.matcap_tint = matcap_tint
        if occlusion_map is not None:
            self.occlusion_map = occlusion_map
        if occlusion_map_scale is not None:
            self.occlusion_map_scale = occlusion_map_scale
        if occlusion_map_offset is not None:
            self.occlusion_map_offset = occlusion_map_offset
        if occlusion_color is not None:
            self.occlusion_color = occlusion_color
        if outline_width is not None:
            self.outline_width = outline_width
        if outline_color is not None:
            self.outline_color = outline_color
        if outline_albedo_tint is not None:
            self.outline_albedo_tint = outline_albedo_tint
        if outline_mask is not None:
            self.outline_mask = outline_mask
        if shadow_ramp is not None:
            self.shadow_ramp = shadow_ramp
        if shadow_ramp_mask is not None:
            self.shadow_ramp_mask = shadow_ramp_mask
        if shadow_ramp_mask_scale is not None:
            self.shadow_ramp_mask_scale = shadow_ramp_mask_scale
        if shadow_ramp_mask_offset is not None:
            self.shadow_ramp_mask_offset = shadow_ramp_mask_offset
        if shadow_rim is not None:
            self.shadow_rim = shadow_rim
        if shadow_sharpness is not None:
            self.shadow_sharpness = shadow_sharpness
        if shadow_rim_range is not None:
            self.shadow_rim_range = shadow_rim_range
        if shadow_rim_threshold is not None:
            self.shadow_rim_threshold = shadow_rim_threshold
        if shadow_rim_sharpness is not None:
            self.shadow_rim_sharpness = shadow_rim_sharpness
        if shadow_rim_albedo_tint is not None:
            self.shadow_rim_albedo_tint = shadow_rim_albedo_tint
        if thickness_map is not None:
            self.thickness_map = thickness_map
        if thickness_map_scale is not None:
            self.thickness_map_scale = thickness_map_scale
        if thickness_map_offset is not None:
            self.thickness_map_offset = thickness_map_offset
        if subsurface_color is not None:
            self.subsurface_color = subsurface_color
        if subsurface_distortion is not None:
            self.subsurface_distortion = subsurface_distortion
        if subsurface_power is not None:
            self.subsurface_power = subsurface_power
        if subsurface_scale is not None:
            self.subsurface_scale = subsurface_scale
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if albedo_uv is not None:
            self.albedo_uv = albedo_uv
        if normal_uv is not None:
            self.normal_uv = normal_uv
        if metallic_uv is not None:
            self.metallic_uv = metallic_uv
        if thickness_uv is not None:
            self.thickness_uv = thickness_uv
        if occlusion_uv is not None:
            self.occlusion_uv = occlusion_uv
        if emission_uv is not None:
            self.emission_uv = emission_uv
        if render_queue is not None:
            self.render_queue = render_queue
        if legacy_cutout is not None:
            self.legacy_cutout = legacy_cutout
        if regular is not None:
            self.regular = regular
        if outline is not None:
            self.outline = outline

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
    def use_vertex_colors(self) -> bool | None:
        """The UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def vertex_color_interpolation_space(self) -> members.FieldEnum | None:
        """The VertexColorInterpolationSpace member."""
        member = self.get_member("VertexColorInterpolationSpace")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertex_color_interpolation_space.setter
    def vertex_color_interpolation_space(self, value: members.FieldEnum) -> None:
        """Set the VertexColorInterpolationSpace member."""
        self.set_member("VertexColorInterpolationSpace", value)

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
    def alpha_clip(self) -> np.float32 | None:
        """The AlphaClip field value."""
        member = self.get_member("AlphaClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_clip.setter
    def alpha_clip(self, value: np.float32) -> None:
        """Set the AlphaClip field value."""
        member = self.get_member("AlphaClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaClip", fields.FieldFloat(value=value)
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
    def saturation(self) -> np.float32 | None:
        """The Saturation field value."""
        member = self.get_member("Saturation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saturation.setter
    def saturation(self, value: np.float32) -> None:
        """Set the Saturation field value."""
        member = self.get_member("Saturation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Saturation", fields.FieldFloat(value=value)
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
    def normal_scale(self) -> np.float32 | None:
        """The NormalScale field value."""
        member = self.get_member("NormalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale.setter
    def normal_scale(self, value: np.float32) -> None:
        """Set the NormalScale field value."""
        member = self.get_member("NormalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale", fields.FieldFloat(value=value)
            )

    @property
    def metallic(self) -> np.float32 | None:
        """The Metallic field value."""
        member = self.get_member("Metallic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic.setter
    def metallic(self, value: np.float32) -> None:
        """Set the Metallic field value."""
        member = self.get_member("Metallic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Metallic", fields.FieldFloat(value=value)
            )

    @property
    def glossiness(self) -> np.float32 | None:
        """The Glossiness field value."""
        member = self.get_member("Glossiness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @glossiness.setter
    def glossiness(self, value: np.float32) -> None:
        """Set the Glossiness field value."""
        member = self.get_member("Glossiness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Glossiness", fields.FieldFloat(value=value)
            )

    @property
    def reflectivity(self) -> np.float32 | None:
        """The Reflectivity field value."""
        member = self.get_member("Reflectivity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reflectivity.setter
    def reflectivity(self, value: np.float32) -> None:
        """Set the Reflectivity field value."""
        member = self.get_member("Reflectivity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Reflectivity", fields.FieldFloat(value=value)
            )

    @property
    def metallic_gloss_map(self) -> str | None:
        """Target ID of the MetallicGlossMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MetallicGlossMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @metallic_gloss_map.setter
    def metallic_gloss_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MetallicGlossMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MetallicGlossMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MetallicGlossMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def metallic_gloss_map_scale(self) -> primitives.Float2 | None:
        """The MetallicGlossMapScale field value."""
        member = self.get_member("MetallicGlossMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic_gloss_map_scale.setter
    def metallic_gloss_map_scale(self, value: primitives.Float2) -> None:
        """Set the MetallicGlossMapScale field value."""
        member = self.get_member("MetallicGlossMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MetallicGlossMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def metallic_gloss_map_offset(self) -> primitives.Float2 | None:
        """The MetallicGlossMapOffset field value."""
        member = self.get_member("MetallicGlossMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic_gloss_map_offset.setter
    def metallic_gloss_map_offset(self, value: primitives.Float2) -> None:
        """Set the MetallicGlossMapOffset field value."""
        member = self.get_member("MetallicGlossMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MetallicGlossMapOffset", fields.FieldFloat2(value=value)
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
    def rim_color(self) -> primitives.ColorX | None:
        """The RimColor field value."""
        member = self.get_member("RimColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_color.setter
    def rim_color(self, value: primitives.ColorX) -> None:
        """Set the RimColor field value."""
        member = self.get_member("RimColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimColor", fields.FieldColorX(value=value)
            )

    @property
    def rim_albedo_tint(self) -> np.float32 | None:
        """The RimAlbedoTint field value."""
        member = self.get_member("RimAlbedoTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_albedo_tint.setter
    def rim_albedo_tint(self, value: np.float32) -> None:
        """Set the RimAlbedoTint field value."""
        member = self.get_member("RimAlbedoTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimAlbedoTint", fields.FieldFloat(value=value)
            )

    @property
    def rim_attenuation_effect(self) -> np.float32 | None:
        """The RimAttenuationEffect field value."""
        member = self.get_member("RimAttenuationEffect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_attenuation_effect.setter
    def rim_attenuation_effect(self, value: np.float32) -> None:
        """Set the RimAttenuationEffect field value."""
        member = self.get_member("RimAttenuationEffect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimAttenuationEffect", fields.FieldFloat(value=value)
            )

    @property
    def rim_intensity(self) -> np.float32 | None:
        """The RimIntensity field value."""
        member = self.get_member("RimIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_intensity.setter
    def rim_intensity(self, value: np.float32) -> None:
        """Set the RimIntensity field value."""
        member = self.get_member("RimIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimIntensity", fields.FieldFloat(value=value)
            )

    @property
    def rim_range(self) -> np.float32 | None:
        """The RimRange field value."""
        member = self.get_member("RimRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_range.setter
    def rim_range(self, value: np.float32) -> None:
        """Set the RimRange field value."""
        member = self.get_member("RimRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimRange", fields.FieldFloat(value=value)
            )

    @property
    def rim_threshold(self) -> np.float32 | None:
        """The RimThreshold field value."""
        member = self.get_member("RimThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_threshold.setter
    def rim_threshold(self, value: np.float32) -> None:
        """Set the RimThreshold field value."""
        member = self.get_member("RimThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimThreshold", fields.FieldFloat(value=value)
            )

    @property
    def rim_sharpness(self) -> np.float32 | None:
        """The RimSharpness field value."""
        member = self.get_member("RimSharpness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rim_sharpness.setter
    def rim_sharpness(self, value: np.float32) -> None:
        """Set the RimSharpness field value."""
        member = self.get_member("RimSharpness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RimSharpness", fields.FieldFloat(value=value)
            )

    @property
    def specular_intensity(self) -> np.float32 | None:
        """The SpecularIntensity field value."""
        member = self.get_member("SpecularIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_intensity.setter
    def specular_intensity(self, value: np.float32) -> None:
        """Set the SpecularIntensity field value."""
        member = self.get_member("SpecularIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularIntensity", fields.FieldFloat(value=value)
            )

    @property
    def specular_area(self) -> np.float32 | None:
        """The SpecularArea field value."""
        member = self.get_member("SpecularArea")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_area.setter
    def specular_area(self, value: np.float32) -> None:
        """Set the SpecularArea field value."""
        member = self.get_member("SpecularArea")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularArea", fields.FieldFloat(value=value)
            )

    @property
    def matcap(self) -> str | None:
        """Target ID of the Matcap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Matcap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @matcap.setter
    def matcap(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Matcap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Matcap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Matcap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def matcap_tint(self) -> primitives.ColorX | None:
        """The MatcapTint field value."""
        member = self.get_member("MatcapTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @matcap_tint.setter
    def matcap_tint(self, value: primitives.ColorX) -> None:
        """Set the MatcapTint field value."""
        member = self.get_member("MatcapTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MatcapTint", fields.FieldColorX(value=value)
            )

    @property
    def occlusion_map(self) -> str | None:
        """Target ID of the OcclusionMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OcclusionMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @occlusion_map.setter
    def occlusion_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OcclusionMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OcclusionMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OcclusionMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def occlusion_map_scale(self) -> primitives.Float2 | None:
        """The OcclusionMapScale field value."""
        member = self.get_member("OcclusionMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_map_scale.setter
    def occlusion_map_scale(self, value: primitives.Float2) -> None:
        """Set the OcclusionMapScale field value."""
        member = self.get_member("OcclusionMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def occlusion_map_offset(self) -> primitives.Float2 | None:
        """The OcclusionMapOffset field value."""
        member = self.get_member("OcclusionMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_map_offset.setter
    def occlusion_map_offset(self, value: primitives.Float2) -> None:
        """Set the OcclusionMapOffset field value."""
        member = self.get_member("OcclusionMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def occlusion_color(self) -> primitives.ColorX | None:
        """The OcclusionColor field value."""
        member = self.get_member("OcclusionColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_color.setter
    def occlusion_color(self, value: primitives.ColorX) -> None:
        """Set the OcclusionColor field value."""
        member = self.get_member("OcclusionColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionColor", fields.FieldColorX(value=value)
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
    def outline_albedo_tint(self) -> bool | None:
        """The OutlineAlbedoTint field value."""
        member = self.get_member("OutlineAlbedoTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outline_albedo_tint.setter
    def outline_albedo_tint(self, value: bool) -> None:
        """Set the OutlineAlbedoTint field value."""
        member = self.get_member("OutlineAlbedoTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutlineAlbedoTint", fields.FieldBool(value=value)
            )

    @property
    def outline_mask(self) -> str | None:
        """Target ID of the OutlineMask reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OutlineMask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outline_mask.setter
    def outline_mask(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OutlineMask reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OutlineMask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OutlineMask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def shadow_ramp(self) -> str | None:
        """Target ID of the ShadowRamp reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ShadowRamp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shadow_ramp.setter
    def shadow_ramp(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ShadowRamp reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ShadowRamp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ShadowRamp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def shadow_ramp_mask(self) -> str | None:
        """Target ID of the ShadowRampMask reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ShadowRampMask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shadow_ramp_mask.setter
    def shadow_ramp_mask(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ShadowRampMask reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ShadowRampMask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ShadowRampMask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def shadow_ramp_mask_scale(self) -> primitives.Float2 | None:
        """The ShadowRampMaskScale field value."""
        member = self.get_member("ShadowRampMaskScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_ramp_mask_scale.setter
    def shadow_ramp_mask_scale(self, value: primitives.Float2) -> None:
        """Set the ShadowRampMaskScale field value."""
        member = self.get_member("ShadowRampMaskScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRampMaskScale", fields.FieldFloat2(value=value)
            )

    @property
    def shadow_ramp_mask_offset(self) -> primitives.Float2 | None:
        """The ShadowRampMaskOffset field value."""
        member = self.get_member("ShadowRampMaskOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_ramp_mask_offset.setter
    def shadow_ramp_mask_offset(self, value: primitives.Float2) -> None:
        """Set the ShadowRampMaskOffset field value."""
        member = self.get_member("ShadowRampMaskOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRampMaskOffset", fields.FieldFloat2(value=value)
            )

    @property
    def shadow_rim(self) -> primitives.ColorX | None:
        """The ShadowRim field value."""
        member = self.get_member("ShadowRim")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_rim.setter
    def shadow_rim(self, value: primitives.ColorX) -> None:
        """Set the ShadowRim field value."""
        member = self.get_member("ShadowRim")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRim", fields.FieldColorX(value=value)
            )

    @property
    def shadow_sharpness(self) -> np.float32 | None:
        """The ShadowSharpness field value."""
        member = self.get_member("ShadowSharpness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_sharpness.setter
    def shadow_sharpness(self, value: np.float32) -> None:
        """Set the ShadowSharpness field value."""
        member = self.get_member("ShadowSharpness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowSharpness", fields.FieldFloat(value=value)
            )

    @property
    def shadow_rim_range(self) -> np.float32 | None:
        """The ShadowRimRange field value."""
        member = self.get_member("ShadowRimRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_rim_range.setter
    def shadow_rim_range(self, value: np.float32) -> None:
        """Set the ShadowRimRange field value."""
        member = self.get_member("ShadowRimRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRimRange", fields.FieldFloat(value=value)
            )

    @property
    def shadow_rim_threshold(self) -> np.float32 | None:
        """The ShadowRimThreshold field value."""
        member = self.get_member("ShadowRimThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_rim_threshold.setter
    def shadow_rim_threshold(self, value: np.float32) -> None:
        """Set the ShadowRimThreshold field value."""
        member = self.get_member("ShadowRimThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRimThreshold", fields.FieldFloat(value=value)
            )

    @property
    def shadow_rim_sharpness(self) -> np.float32 | None:
        """The ShadowRimSharpness field value."""
        member = self.get_member("ShadowRimSharpness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_rim_sharpness.setter
    def shadow_rim_sharpness(self, value: np.float32) -> None:
        """Set the ShadowRimSharpness field value."""
        member = self.get_member("ShadowRimSharpness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRimSharpness", fields.FieldFloat(value=value)
            )

    @property
    def shadow_rim_albedo_tint(self) -> np.float32 | None:
        """The ShadowRimAlbedoTint field value."""
        member = self.get_member("ShadowRimAlbedoTint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_rim_albedo_tint.setter
    def shadow_rim_albedo_tint(self, value: np.float32) -> None:
        """Set the ShadowRimAlbedoTint field value."""
        member = self.get_member("ShadowRimAlbedoTint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowRimAlbedoTint", fields.FieldFloat(value=value)
            )

    @property
    def thickness_map(self) -> str | None:
        """Target ID of the ThicknessMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ThicknessMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @thickness_map.setter
    def thickness_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ThicknessMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ThicknessMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ThicknessMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def thickness_map_scale(self) -> primitives.Float2 | None:
        """The ThicknessMapScale field value."""
        member = self.get_member("ThicknessMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness_map_scale.setter
    def thickness_map_scale(self, value: primitives.Float2) -> None:
        """Set the ThicknessMapScale field value."""
        member = self.get_member("ThicknessMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThicknessMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def thickness_map_offset(self) -> primitives.Float2 | None:
        """The ThicknessMapOffset field value."""
        member = self.get_member("ThicknessMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness_map_offset.setter
    def thickness_map_offset(self, value: primitives.Float2) -> None:
        """Set the ThicknessMapOffset field value."""
        member = self.get_member("ThicknessMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThicknessMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def subsurface_color(self) -> primitives.ColorX | None:
        """The SubsurfaceColor field value."""
        member = self.get_member("SubsurfaceColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsurface_color.setter
    def subsurface_color(self, value: primitives.ColorX) -> None:
        """Set the SubsurfaceColor field value."""
        member = self.get_member("SubsurfaceColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsurfaceColor", fields.FieldColorX(value=value)
            )

    @property
    def subsurface_distortion(self) -> np.float32 | None:
        """The SubsurfaceDistortion field value."""
        member = self.get_member("SubsurfaceDistortion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsurface_distortion.setter
    def subsurface_distortion(self, value: np.float32) -> None:
        """Set the SubsurfaceDistortion field value."""
        member = self.get_member("SubsurfaceDistortion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsurfaceDistortion", fields.FieldFloat(value=value)
            )

    @property
    def subsurface_power(self) -> np.float32 | None:
        """The SubsurfacePower field value."""
        member = self.get_member("SubsurfacePower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsurface_power.setter
    def subsurface_power(self, value: np.float32) -> None:
        """Set the SubsurfacePower field value."""
        member = self.get_member("SubsurfacePower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsurfacePower", fields.FieldFloat(value=value)
            )

    @property
    def subsurface_scale(self) -> np.float32 | None:
        """The SubsurfaceScale field value."""
        member = self.get_member("SubsurfaceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @subsurface_scale.setter
    def subsurface_scale(self, value: np.float32) -> None:
        """Set the SubsurfaceScale field value."""
        member = self.get_member("SubsurfaceScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SubsurfaceScale", fields.FieldFloat(value=value)
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
    def culling(self) -> members.FieldEnum | None:
        """The Culling member."""
        member = self.get_member("Culling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @culling.setter
    def culling(self, value: members.FieldEnum) -> None:
        """Set the Culling member."""
        self.set_member("Culling", value)

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
    def albedo_uv(self) -> np.int32 | None:
        """The AlbedoUV field value."""
        member = self.get_member("AlbedoUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_uv.setter
    def albedo_uv(self, value: np.int32) -> None:
        """Set the AlbedoUV field value."""
        member = self.get_member("AlbedoUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoUV", fields.FieldInt(value=value)
            )

    @property
    def normal_uv(self) -> np.int32 | None:
        """The NormalUV field value."""
        member = self.get_member("NormalUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_uv.setter
    def normal_uv(self, value: np.int32) -> None:
        """Set the NormalUV field value."""
        member = self.get_member("NormalUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalUV", fields.FieldInt(value=value)
            )

    @property
    def metallic_uv(self) -> np.int32 | None:
        """The MetallicUV field value."""
        member = self.get_member("MetallicUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic_uv.setter
    def metallic_uv(self, value: np.int32) -> None:
        """Set the MetallicUV field value."""
        member = self.get_member("MetallicUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MetallicUV", fields.FieldInt(value=value)
            )

    @property
    def thickness_uv(self) -> np.int32 | None:
        """The ThicknessUV field value."""
        member = self.get_member("ThicknessUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness_uv.setter
    def thickness_uv(self, value: np.int32) -> None:
        """Set the ThicknessUV field value."""
        member = self.get_member("ThicknessUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThicknessUV", fields.FieldInt(value=value)
            )

    @property
    def occlusion_uv(self) -> np.int32 | None:
        """The OcclusionUV field value."""
        member = self.get_member("OcclusionUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_uv.setter
    def occlusion_uv(self, value: np.int32) -> None:
        """Set the OcclusionUV field value."""
        member = self.get_member("OcclusionUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionUV", fields.FieldInt(value=value)
            )

    @property
    def emission_uv(self) -> np.int32 | None:
        """The EmissionUV field value."""
        member = self.get_member("EmissionUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_uv.setter
    def emission_uv(self, value: np.int32) -> None:
        """Set the EmissionUV field value."""
        member = self.get_member("EmissionUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionUV", fields.FieldInt(value=value)
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

    @property
    def legacy_cutout(self) -> bool | None:
        """The __legacyCutout field value."""
        member = self.get_member("__legacyCutout")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_cutout.setter
    def legacy_cutout(self, value: bool) -> None:
        """Set the __legacyCutout field value."""
        member = self.get_member("__legacyCutout")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyCutout", fields.FieldBool(value=value)
            )

    @property
    def regular(self) -> str | None:
        """Target ID of the _regular reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_regular")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @regular.setter
    def regular(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _regular reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_regular")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_regular",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def outline(self) -> str | None:
        """Target ID of the _outline reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_outline")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outline.setter
    def outline(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _outline reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_outline")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_outline",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

