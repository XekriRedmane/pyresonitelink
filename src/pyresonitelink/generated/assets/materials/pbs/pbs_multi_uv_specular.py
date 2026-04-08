"""Generated component: PBS_MultiUV_Specular."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.ipbs_specular import IPBS_Specular
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_MultiUV_Specular(GeneratedComponent, IPBS_Specular, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_MultiUV_Specular.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_MultiUV_Specular"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, albedo_scale: primitives.Float2 | None = None, albedo_offset: primitives.Float2 | None = None, albedo_uv: primitives.Int | None = None, emission_map_scale: primitives.Float2 | None = None, emission_map_offset: primitives.Float2 | None = None, emission_map_uv: primitives.Int | None = None, normal_map_scale: primitives.Float2 | None = None, normal_map_offset: primitives.Float2 | None = None, normal_map_uv: primitives.Int | None = None, occlusion_map_scale: primitives.Float2 | None = None, occlusion_map_offset: primitives.Float2 | None = None, occlusion_map_uv: primitives.Int | None = None, secondary_albedo_scale: primitives.Float2 | None = None, secondary_albedo_offset: primitives.Float2 | None = None, secondary_albedo_uv: primitives.Int | None = None, secondary_emission_map_scale: primitives.Float2 | None = None, secondary_emission_map_offset: primitives.Float2 | None = None, secondary_emission_map_uv: primitives.Int | None = None, albedo_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: primitives.Float | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, secondary_albedo_texture: str | IAssetProvider[ITexture2D] | None = None, secondary_emissive_color: primitives.ColorX | None = None, secondary_emissive_map: str | IAssetProvider[ITexture2D] | None = None, alpha_clip: primitives.Float | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, specular_color: primitives.ColorX | None = None, specular_map: str | IAssetProvider[ITexture2D] | None = None, specular_map_scale: primitives.Float2 | None = None, specular_map_offset: primitives.Float2 | None = None, specular_map_uv: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
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
            alpha_clip: Initial value for AlphaClip.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            specular_color: Initial value for SpecularColor.
            specular_map: Initial value for SpecularMap.
            specular_map_scale: Initial value for SpecularMapScale.
            specular_map_offset: Initial value for SpecularMapOffset.
            specular_map_uv: Initial value for SpecularMapUV.
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
        if alpha_clip is not None:
            self.alpha_clip = alpha_clip
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if specular_color is not None:
            self.specular_color = specular_color
        if specular_map is not None:
            self.specular_map = specular_map
        if specular_map_scale is not None:
            self.specular_map_scale = specular_map_scale
        if specular_map_offset is not None:
            self.specular_map_offset = specular_map_offset
        if specular_map_uv is not None:
            self.specular_map_uv = specular_map_uv

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
    def alpha_handling(self) -> members.FieldEnum | None:
        """The AlphaHandling member."""
        member = self.get_member("AlphaHandling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @alpha_handling.setter
    def alpha_handling(self, value: members.FieldEnum) -> None:
        """Set the AlphaHandling member."""
        self.set_member("AlphaHandling", value)

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
    def specular_color(self) -> primitives.ColorX | None:
        """The SpecularColor field value."""
        member = self.get_member("SpecularColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_color.setter
    def specular_color(self, value: primitives.ColorX) -> None:
        """Set the SpecularColor field value."""
        member = self.get_member("SpecularColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularColor", fields.FieldColorX(value=value)
            )

    @property
    def specular_map(self) -> str | None:
        """Target ID of the SpecularMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SpecularMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @specular_map.setter
    def specular_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SpecularMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SpecularMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpecularMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def specular_map_scale(self) -> primitives.Float2 | None:
        """The SpecularMapScale field value."""
        member = self.get_member("SpecularMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_map_scale.setter
    def specular_map_scale(self, value: primitives.Float2) -> None:
        """Set the SpecularMapScale field value."""
        member = self.get_member("SpecularMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def specular_map_offset(self) -> primitives.Float2 | None:
        """The SpecularMapOffset field value."""
        member = self.get_member("SpecularMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_map_offset.setter
    def specular_map_offset(self, value: primitives.Float2) -> None:
        """Set the SpecularMapOffset field value."""
        member = self.get_member("SpecularMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def specular_map_uv(self) -> primitives.Int | None:
        """The SpecularMapUV field value."""
        member = self.get_member("SpecularMapUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_map_uv.setter
    def specular_map_uv(self, value: primitives.Int) -> None:
        """Set the SpecularMapUV field value."""
        member = self.get_member("SpecularMapUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularMapUV", fields.FieldInt(value=value)
            )

