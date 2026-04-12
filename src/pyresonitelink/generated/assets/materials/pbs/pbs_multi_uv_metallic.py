"""Generated component: PBS_MultiUV_Metallic."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.culling import Culling
from pyresonitelink.generated._enums.alpha_handling import AlphaHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.ipbs_metallic import IPBS_Metallic
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_MultiUV_Metallic(GeneratedComponent, IPBS_Metallic, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """The PBS_MultiUVMetallic component is used as a material that can stack two different sets of material data except for shine maps. When this material's AlphaHandling mode is set to AlphaBlend, it behaves as if if were Opaque, which is a known bug.https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/825

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_MultiUV_Metallic"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, albedo_scale: primitives.Float2 | None = None, albedo_offset: primitives.Float2 | None = None, albedo_uv: primitives.Int | None = None, emission_map_scale: primitives.Float2 | None = None, emission_map_offset: primitives.Float2 | None = None, emission_map_uv: primitives.Int | None = None, normal_map_scale: primitives.Float2 | None = None, normal_map_offset: primitives.Float2 | None = None, normal_map_uv: primitives.Int | None = None, occlusion_map_scale: primitives.Float2 | None = None, occlusion_map_offset: primitives.Float2 | None = None, occlusion_map_uv: primitives.Int | None = None, secondary_albedo_scale: primitives.Float2 | None = None, secondary_albedo_offset: primitives.Float2 | None = None, secondary_albedo_uv: primitives.Int | None = None, secondary_emission_map_scale: primitives.Float2 | None = None, secondary_emission_map_offset: primitives.Float2 | None = None, secondary_emission_map_uv: primitives.Int | None = None, albedo_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: primitives.Float | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, secondary_albedo_texture: str | IAssetProvider[ITexture2D] | None = None, secondary_emissive_color: primitives.ColorX | None = None, secondary_emissive_map: str | IAssetProvider[ITexture2D] | None = None, culling: Culling | str | None = None, alpha_handling: AlphaHandling | str | None = None, alpha_clip: primitives.Float | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, metallic: primitives.Float | None = None, smoothness: primitives.Float | None = None, metallic_map: str | IAssetProvider[ITexture2D] | None = None, metallic_map_scale: primitives.Float2 | None = None, metallic_map_offset: primitives.Float2 | None = None, metallic_map_uv: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            albedo_scale: Initial value for AlbedoScale.
            albedo_offset: Initial value for AlbedoOffset.
            albedo_uv: Initial value for AlbedoUV.
            emission_map_scale: Initial value for EmissionMapScale.
            emission_map_offset: Initial value for EmissionMapOffset.
            emission_map_uv: Initial value for EmissionMapUV.
            normal_map_scale: Initial value for NormalMapScale.
            normal_map_offset: Initial value for NormalMapOffset.
            normal_map_uv: Initial value for NormalMapUV.
            occlusion_map_scale: Initial value for OcclusionMapScale.
            occlusion_map_offset: Initial value for OcclusionMapOffset.
            occlusion_map_uv: Initial value for OcclusionMapUV.
            secondary_albedo_scale: Initial value for SecondaryAlbedoScale.
            secondary_albedo_offset: Initial value for SecondaryAlbedoOffset.
            secondary_albedo_uv: Initial value for SecondaryAlbedoUV.
            secondary_emission_map_scale: Initial value for SecondaryEmissionMapScale.
            secondary_emission_map_offset: Initial value for SecondaryEmissionMapOffset.
            secondary_emission_map_uv: Initial value for SecondaryEmissionMapUV.
            albedo_color: Initial value for AlbedoColor.
            albedo_texture: Initial value for AlbedoTexture.
            emissive_color: Initial value for EmissiveColor.
            emissive_map: Initial value for EmissiveMap.
            normal_map: Initial value for NormalMap.
            normal_scale: Initial value for NormalScale.
            occlusion_map: Initial value for OcclusionMap.
            secondary_albedo_texture: Initial value for SecondaryAlbedoTexture.
            secondary_emissive_color: Initial value for SecondaryEmissiveColor.
            secondary_emissive_map: Initial value for SecondaryEmissiveMap.
            culling: Initial value for Culling.
            alpha_handling: Initial value for AlphaHandling.
            alpha_clip: Initial value for AlphaClip.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            metallic: Initial value for Metallic.
            smoothness: Initial value for Smoothness.
            metallic_map: Initial value for MetallicMap.
            metallic_map_scale: Initial value for MetallicMapScale.
            metallic_map_offset: Initial value for MetallicMapOffset.
            metallic_map_uv: Initial value for MetallicMapUV.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if albedo_scale is not None:
            self.albedo_scale = albedo_scale
        if albedo_offset is not None:
            self.albedo_offset = albedo_offset
        if albedo_uv is not None:
            self.albedo_uv = albedo_uv
        if emission_map_scale is not None:
            self.emission_map_scale = emission_map_scale
        if emission_map_offset is not None:
            self.emission_map_offset = emission_map_offset
        if emission_map_uv is not None:
            self.emission_map_uv = emission_map_uv
        if normal_map_scale is not None:
            self.normal_map_scale = normal_map_scale
        if normal_map_offset is not None:
            self.normal_map_offset = normal_map_offset
        if normal_map_uv is not None:
            self.normal_map_uv = normal_map_uv
        if occlusion_map_scale is not None:
            self.occlusion_map_scale = occlusion_map_scale
        if occlusion_map_offset is not None:
            self.occlusion_map_offset = occlusion_map_offset
        if occlusion_map_uv is not None:
            self.occlusion_map_uv = occlusion_map_uv
        if secondary_albedo_scale is not None:
            self.secondary_albedo_scale = secondary_albedo_scale
        if secondary_albedo_offset is not None:
            self.secondary_albedo_offset = secondary_albedo_offset
        if secondary_albedo_uv is not None:
            self.secondary_albedo_uv = secondary_albedo_uv
        if secondary_emission_map_scale is not None:
            self.secondary_emission_map_scale = secondary_emission_map_scale
        if secondary_emission_map_offset is not None:
            self.secondary_emission_map_offset = secondary_emission_map_offset
        if secondary_emission_map_uv is not None:
            self.secondary_emission_map_uv = secondary_emission_map_uv
        if albedo_color is not None:
            self.albedo_color = albedo_color
        if albedo_texture is not None:
            self.albedo_texture = albedo_texture
        if emissive_color is not None:
            self.emissive_color = emissive_color
        if emissive_map is not None:
            self.emissive_map = emissive_map
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_scale is not None:
            self.normal_scale = normal_scale
        if occlusion_map is not None:
            self.occlusion_map = occlusion_map
        if secondary_albedo_texture is not None:
            self.secondary_albedo_texture = secondary_albedo_texture
        if secondary_emissive_color is not None:
            self.secondary_emissive_color = secondary_emissive_color
        if secondary_emissive_map is not None:
            self.secondary_emissive_map = secondary_emissive_map
        if culling is not None:
            self.culling = culling
        if alpha_handling is not None:
            self.alpha_handling = alpha_handling
        if alpha_clip is not None:
            self.alpha_clip = alpha_clip
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if metallic is not None:
            self.metallic = metallic
        if smoothness is not None:
            self.smoothness = smoothness
        if metallic_map is not None:
            self.metallic_map = metallic_map
        if metallic_map_scale is not None:
            self.metallic_map_scale = metallic_map_scale
        if metallic_map_offset is not None:
            self.metallic_map_offset = metallic_map_offset
        if metallic_map_uv is not None:
            self.metallic_map_uv = metallic_map_uv

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
    def albedo_scale(self) -> primitives.Float2 | None:
        """The AlbedoScale field value."""
        member = self.get_member("AlbedoScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_scale.setter
    def albedo_scale(self, value: primitives.Float2) -> None:
        """Set the AlbedoScale field value."""
        member = self.get_member("AlbedoScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoScale", fields.FieldFloat2(value=value)
            )

    @property
    def albedo_offset(self) -> primitives.Float2 | None:
        """The AlbedoOffset field value."""
        member = self.get_member("AlbedoOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_offset.setter
    def albedo_offset(self, value: primitives.Float2) -> None:
        """Set the AlbedoOffset field value."""
        member = self.get_member("AlbedoOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoOffset", fields.FieldFloat2(value=value)
            )

    @property
    def albedo_uv(self) -> primitives.Int | None:
        """The AlbedoUV field value."""
        member = self.get_member("AlbedoUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_uv.setter
    def albedo_uv(self, value: primitives.Int) -> None:
        """Set the AlbedoUV field value."""
        member = self.get_member("AlbedoUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoUV", fields.FieldInt(value=value)
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
    def emission_map_uv(self) -> primitives.Int | None:
        """The EmissionMapUV field value."""
        member = self.get_member("EmissionMapUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_map_uv.setter
    def emission_map_uv(self, value: primitives.Int) -> None:
        """Set the EmissionMapUV field value."""
        member = self.get_member("EmissionMapUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionMapUV", fields.FieldInt(value=value)
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
    def normal_map_uv(self) -> primitives.Int | None:
        """The NormalMapUV field value."""
        member = self.get_member("NormalMapUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_map_uv.setter
    def normal_map_uv(self, value: primitives.Int) -> None:
        """Set the NormalMapUV field value."""
        member = self.get_member("NormalMapUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalMapUV", fields.FieldInt(value=value)
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
    def occlusion_map_uv(self) -> primitives.Int | None:
        """The OcclusionMapUV field value."""
        member = self.get_member("OcclusionMapUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_map_uv.setter
    def occlusion_map_uv(self, value: primitives.Int) -> None:
        """Set the OcclusionMapUV field value."""
        member = self.get_member("OcclusionMapUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionMapUV", fields.FieldInt(value=value)
            )

    @property
    def secondary_albedo_scale(self) -> primitives.Float2 | None:
        """The SecondaryAlbedoScale field value."""
        member = self.get_member("SecondaryAlbedoScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_albedo_scale.setter
    def secondary_albedo_scale(self, value: primitives.Float2) -> None:
        """Set the SecondaryAlbedoScale field value."""
        member = self.get_member("SecondaryAlbedoScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryAlbedoScale", fields.FieldFloat2(value=value)
            )

    @property
    def secondary_albedo_offset(self) -> primitives.Float2 | None:
        """The SecondaryAlbedoOffset field value."""
        member = self.get_member("SecondaryAlbedoOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_albedo_offset.setter
    def secondary_albedo_offset(self, value: primitives.Float2) -> None:
        """Set the SecondaryAlbedoOffset field value."""
        member = self.get_member("SecondaryAlbedoOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryAlbedoOffset", fields.FieldFloat2(value=value)
            )

    @property
    def secondary_albedo_uv(self) -> primitives.Int | None:
        """The SecondaryAlbedoUV field value."""
        member = self.get_member("SecondaryAlbedoUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_albedo_uv.setter
    def secondary_albedo_uv(self, value: primitives.Int) -> None:
        """Set the SecondaryAlbedoUV field value."""
        member = self.get_member("SecondaryAlbedoUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryAlbedoUV", fields.FieldInt(value=value)
            )

    @property
    def secondary_emission_map_scale(self) -> primitives.Float2 | None:
        """The SecondaryEmissionMapScale field value."""
        member = self.get_member("SecondaryEmissionMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_emission_map_scale.setter
    def secondary_emission_map_scale(self, value: primitives.Float2) -> None:
        """Set the SecondaryEmissionMapScale field value."""
        member = self.get_member("SecondaryEmissionMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryEmissionMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def secondary_emission_map_offset(self) -> primitives.Float2 | None:
        """The SecondaryEmissionMapOffset field value."""
        member = self.get_member("SecondaryEmissionMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_emission_map_offset.setter
    def secondary_emission_map_offset(self, value: primitives.Float2) -> None:
        """Set the SecondaryEmissionMapOffset field value."""
        member = self.get_member("SecondaryEmissionMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryEmissionMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def secondary_emission_map_uv(self) -> primitives.Int | None:
        """The SecondaryEmissionMapUV field value."""
        member = self.get_member("SecondaryEmissionMapUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_emission_map_uv.setter
    def secondary_emission_map_uv(self, value: primitives.Int) -> None:
        """Set the SecondaryEmissionMapUV field value."""
        member = self.get_member("SecondaryEmissionMapUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryEmissionMapUV", fields.FieldInt(value=value)
            )

    @property
    def albedo_color(self) -> primitives.ColorX | None:
        """The AlbedoColor field value."""
        member = self.get_member("AlbedoColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color.setter
    def albedo_color(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor field value."""
        member = self.get_member("AlbedoColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor", fields.FieldColorX(value=value)
            )

    @property
    def albedo_texture(self) -> str | None:
        """Target ID of the AlbedoTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("AlbedoTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @albedo_texture.setter
    def albedo_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the AlbedoTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AlbedoTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AlbedoTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emissive_color(self) -> primitives.ColorX | None:
        """The EmissiveColor field value."""
        member = self.get_member("EmissiveColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color.setter
    def emissive_color(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor field value."""
        member = self.get_member("EmissiveColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor", fields.FieldColorX(value=value)
            )

    @property
    def emissive_map(self) -> str | None:
        """Target ID of the EmissiveMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissiveMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_map.setter
    def emissive_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissiveMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissiveMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissiveMap",
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
    def normal_scale(self) -> primitives.Float | None:
        """The NormalScale field value."""
        member = self.get_member("NormalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale.setter
    def normal_scale(self, value: primitives.Float) -> None:
        """Set the NormalScale field value."""
        member = self.get_member("NormalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale", fields.FieldFloat(value=value)
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
    def secondary_albedo_texture(self) -> str | None:
        """Target ID of the SecondaryAlbedoTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SecondaryAlbedoTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_albedo_texture.setter
    def secondary_albedo_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SecondaryAlbedoTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryAlbedoTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryAlbedoTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def secondary_emissive_color(self) -> primitives.ColorX | None:
        """The SecondaryEmissiveColor field value."""
        member = self.get_member("SecondaryEmissiveColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary_emissive_color.setter
    def secondary_emissive_color(self, value: primitives.ColorX) -> None:
        """Set the SecondaryEmissiveColor field value."""
        member = self.get_member("SecondaryEmissiveColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SecondaryEmissiveColor", fields.FieldColorX(value=value)
            )

    @property
    def secondary_emissive_map(self) -> str | None:
        """Target ID of the SecondaryEmissiveMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SecondaryEmissiveMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_emissive_map.setter
    def secondary_emissive_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SecondaryEmissiveMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryEmissiveMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryEmissiveMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def culling(self) -> Culling | None:
        """The Culling enum value."""
        member = self.get_member("Culling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Culling(member.value)
        return None

    @culling.setter
    def culling(self, value: Culling | str) -> None:
        """Set the Culling enum value."""
        member = self.get_member("Culling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Culling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def alpha_handling(self) -> AlphaHandling | None:
        """The AlphaHandling enum value."""
        member = self.get_member("AlphaHandling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AlphaHandling(member.value)
        return None

    @alpha_handling.setter
    def alpha_handling(self, value: AlphaHandling | str) -> None:
        """Set the AlphaHandling enum value."""
        member = self.get_member("AlphaHandling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AlphaHandling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def alpha_clip(self) -> primitives.Float | None:
        """The AlphaClip field value."""
        member = self.get_member("AlphaClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_clip.setter
    def alpha_clip(self, value: primitives.Float) -> None:
        """Set the AlphaClip field value."""
        member = self.get_member("AlphaClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaClip", fields.FieldFloat(value=value)
            )

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
    def metallic(self) -> primitives.Float | None:
        """The Metallic field value."""
        member = self.get_member("Metallic")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic.setter
    def metallic(self, value: primitives.Float) -> None:
        """Set the Metallic field value."""
        member = self.get_member("Metallic")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Metallic", fields.FieldFloat(value=value)
            )

    @property
    def smoothness(self) -> primitives.Float | None:
        """The Smoothness field value."""
        member = self.get_member("Smoothness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothness.setter
    def smoothness(self, value: primitives.Float) -> None:
        """Set the Smoothness field value."""
        member = self.get_member("Smoothness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothness", fields.FieldFloat(value=value)
            )

    @property
    def metallic_map(self) -> str | None:
        """Target ID of the MetallicMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MetallicMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @metallic_map.setter
    def metallic_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MetallicMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MetallicMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MetallicMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def metallic_map_scale(self) -> primitives.Float2 | None:
        """The MetallicMapScale field value."""
        member = self.get_member("MetallicMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic_map_scale.setter
    def metallic_map_scale(self, value: primitives.Float2) -> None:
        """Set the MetallicMapScale field value."""
        member = self.get_member("MetallicMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MetallicMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def metallic_map_offset(self) -> primitives.Float2 | None:
        """The MetallicMapOffset field value."""
        member = self.get_member("MetallicMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic_map_offset.setter
    def metallic_map_offset(self, value: primitives.Float2) -> None:
        """Set the MetallicMapOffset field value."""
        member = self.get_member("MetallicMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MetallicMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def metallic_map_uv(self) -> primitives.Int | None:
        """The MetallicMapUV field value."""
        member = self.get_member("MetallicMapUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic_map_uv.setter
    def metallic_map_uv(self, value: primitives.Int) -> None:
        """Set the MetallicMapUV field value."""
        member = self.get_member("MetallicMapUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MetallicMapUV", fields.FieldInt(value=value)
            )

