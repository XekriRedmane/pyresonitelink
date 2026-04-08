"""Generated component: PBS_DisplaceMetallic."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.ipbs_metallic import IPBS_Metallic
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_DisplaceMetallic(GeneratedComponent, IPBS_Metallic, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_DisplaceMetallic.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_DisplaceMetallic"

    def __init__(self, high_priority_integration: bool | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, albedo_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: np.float32 | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, vertex_displace_map: str | IAssetProvider[ITexture2D] | None = None, vertex_displace_magnitude: np.float32 | None = None, vertex_displace_bias: np.float32 | None = None, vertex_displace_map_scale: primitives.Float2 | None = None, vertex_displace_map_offset: primitives.Float2 | None = None, uv_displace_map: str | IAssetProvider[ITexture2D] | None = None, uv_displace_magnitude: np.float32 | None = None, uv_displace_bias: np.float32 | None = None, uv_displace_map_scale: primitives.Float2 | None = None, uv_displace_map_offset: primitives.Float2 | None = None, worldspace_vertex_offset_map: str | IAssetProvider[ITexture2D] | None = None, worldspace_offset_magnitude: primitives.Float2 | None = None, worldspace_vertex_offset_map_scale: primitives.Float2 | None = None, worldspace_vertex_offset_map_offset: primitives.Float2 | None = None, worldspace_offset_per_vertex: bool | None = None, alpha_clip: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, metallic: np.float32 | None = None, smoothness: np.float32 | None = None, metallic_map: str | IAssetProvider[ITexture2D] | None = None, regular: str | IAssetProvider[Shader] | None = None, transparent: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            albedo_color: Initial value for AlbedoColor.
            albedo_texture: Initial value for AlbedoTexture.
            emissive_color: Initial value for EmissiveColor.
            emissive_map: Initial value for EmissiveMap.
            normal_map: Initial value for NormalMap.
            normal_scale: Initial value for NormalScale.
            occlusion_map: Initial value for OcclusionMap.
            vertex_displace_map: Initial value for VertexDisplaceMap.
            vertex_displace_magnitude: Initial value for VertexDisplaceMagnitude.
            vertex_displace_bias: Initial value for VertexDisplaceBias.
            vertex_displace_map_scale: Initial value for VertexDisplaceMapScale.
            vertex_displace_map_offset: Initial value for VertexDisplaceMapOffset.
            uv_displace_map: Initial value for UVDisplaceMap.
            uv_displace_magnitude: Initial value for UVDisplaceMagnitude.
            uv_displace_bias: Initial value for UVDisplaceBias.
            uv_displace_map_scale: Initial value for UVDisplaceMapScale.
            uv_displace_map_offset: Initial value for UVDisplaceMapOffset.
            worldspace_vertex_offset_map: Initial value for WorldspaceVertexOffsetMap.
            worldspace_offset_magnitude: Initial value for WorldspaceOffsetMagnitude.
            worldspace_vertex_offset_map_scale: Initial value for WorldspaceVertexOffsetMapScale.
            worldspace_vertex_offset_map_offset: Initial value for WorldspaceVertexOffsetMapOffset.
            worldspace_offset_per_vertex: Initial value for WorldspaceOffsetPerVertex.
            alpha_clip: Initial value for AlphaClip.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            metallic: Initial value for Metallic.
            smoothness: Initial value for Smoothness.
            metallic_map: Initial value for MetallicMap.
            regular: Initial value for _regular.
            transparent: Initial value for _transparent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
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
        if vertex_displace_map is not None:
            self.vertex_displace_map = vertex_displace_map
        if vertex_displace_magnitude is not None:
            self.vertex_displace_magnitude = vertex_displace_magnitude
        if vertex_displace_bias is not None:
            self.vertex_displace_bias = vertex_displace_bias
        if vertex_displace_map_scale is not None:
            self.vertex_displace_map_scale = vertex_displace_map_scale
        if vertex_displace_map_offset is not None:
            self.vertex_displace_map_offset = vertex_displace_map_offset
        if uv_displace_map is not None:
            self.uv_displace_map = uv_displace_map
        if uv_displace_magnitude is not None:
            self.uv_displace_magnitude = uv_displace_magnitude
        if uv_displace_bias is not None:
            self.uv_displace_bias = uv_displace_bias
        if uv_displace_map_scale is not None:
            self.uv_displace_map_scale = uv_displace_map_scale
        if uv_displace_map_offset is not None:
            self.uv_displace_map_offset = uv_displace_map_offset
        if worldspace_vertex_offset_map is not None:
            self.worldspace_vertex_offset_map = worldspace_vertex_offset_map
        if worldspace_offset_magnitude is not None:
            self.worldspace_offset_magnitude = worldspace_offset_magnitude
        if worldspace_vertex_offset_map_scale is not None:
            self.worldspace_vertex_offset_map_scale = worldspace_vertex_offset_map_scale
        if worldspace_vertex_offset_map_offset is not None:
            self.worldspace_vertex_offset_map_offset = worldspace_vertex_offset_map_offset
        if worldspace_offset_per_vertex is not None:
            self.worldspace_offset_per_vertex = worldspace_offset_per_vertex
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
        if regular is not None:
            self.regular = regular
        if transparent is not None:
            self.transparent = transparent

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
    def vertex_displace_map(self) -> str | None:
        """Target ID of the VertexDisplaceMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("VertexDisplaceMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @vertex_displace_map.setter
    def vertex_displace_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the VertexDisplaceMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("VertexDisplaceMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VertexDisplaceMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def vertex_displace_magnitude(self) -> np.float32 | None:
        """The VertexDisplaceMagnitude field value."""
        member = self.get_member("VertexDisplaceMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex_displace_magnitude.setter
    def vertex_displace_magnitude(self, value: np.float32) -> None:
        """Set the VertexDisplaceMagnitude field value."""
        member = self.get_member("VertexDisplaceMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VertexDisplaceMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def vertex_displace_bias(self) -> np.float32 | None:
        """The VertexDisplaceBias field value."""
        member = self.get_member("VertexDisplaceBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex_displace_bias.setter
    def vertex_displace_bias(self, value: np.float32) -> None:
        """Set the VertexDisplaceBias field value."""
        member = self.get_member("VertexDisplaceBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VertexDisplaceBias", fields.FieldFloat(value=value)
            )

    @property
    def vertex_displace_map_scale(self) -> primitives.Float2 | None:
        """The VertexDisplaceMapScale field value."""
        member = self.get_member("VertexDisplaceMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex_displace_map_scale.setter
    def vertex_displace_map_scale(self, value: primitives.Float2) -> None:
        """Set the VertexDisplaceMapScale field value."""
        member = self.get_member("VertexDisplaceMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VertexDisplaceMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def vertex_displace_map_offset(self) -> primitives.Float2 | None:
        """The VertexDisplaceMapOffset field value."""
        member = self.get_member("VertexDisplaceMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertex_displace_map_offset.setter
    def vertex_displace_map_offset(self, value: primitives.Float2) -> None:
        """Set the VertexDisplaceMapOffset field value."""
        member = self.get_member("VertexDisplaceMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VertexDisplaceMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def uv_displace_map(self) -> str | None:
        """Target ID of the UVDisplaceMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("UVDisplaceMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv_displace_map.setter
    def uv_displace_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the UVDisplaceMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("UVDisplaceMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UVDisplaceMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def uv_displace_magnitude(self) -> np.float32 | None:
        """The UVDisplaceMagnitude field value."""
        member = self.get_member("UVDisplaceMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_displace_magnitude.setter
    def uv_displace_magnitude(self, value: np.float32) -> None:
        """Set the UVDisplaceMagnitude field value."""
        member = self.get_member("UVDisplaceMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVDisplaceMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def uv_displace_bias(self) -> np.float32 | None:
        """The UVDisplaceBias field value."""
        member = self.get_member("UVDisplaceBias")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_displace_bias.setter
    def uv_displace_bias(self, value: np.float32) -> None:
        """Set the UVDisplaceBias field value."""
        member = self.get_member("UVDisplaceBias")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVDisplaceBias", fields.FieldFloat(value=value)
            )

    @property
    def uv_displace_map_scale(self) -> primitives.Float2 | None:
        """The UVDisplaceMapScale field value."""
        member = self.get_member("UVDisplaceMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_displace_map_scale.setter
    def uv_displace_map_scale(self, value: primitives.Float2) -> None:
        """Set the UVDisplaceMapScale field value."""
        member = self.get_member("UVDisplaceMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVDisplaceMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def uv_displace_map_offset(self) -> primitives.Float2 | None:
        """The UVDisplaceMapOffset field value."""
        member = self.get_member("UVDisplaceMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_displace_map_offset.setter
    def uv_displace_map_offset(self, value: primitives.Float2) -> None:
        """Set the UVDisplaceMapOffset field value."""
        member = self.get_member("UVDisplaceMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVDisplaceMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def worldspace_vertex_offset_map(self) -> str | None:
        """Target ID of the WorldspaceVertexOffsetMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("WorldspaceVertexOffsetMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @worldspace_vertex_offset_map.setter
    def worldspace_vertex_offset_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the WorldspaceVertexOffsetMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("WorldspaceVertexOffsetMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldspaceVertexOffsetMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def worldspace_offset_magnitude(self) -> primitives.Float2 | None:
        """The WorldspaceOffsetMagnitude field value."""
        member = self.get_member("WorldspaceOffsetMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @worldspace_offset_magnitude.setter
    def worldspace_offset_magnitude(self, value: primitives.Float2) -> None:
        """Set the WorldspaceOffsetMagnitude field value."""
        member = self.get_member("WorldspaceOffsetMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldspaceOffsetMagnitude", fields.FieldFloat2(value=value)
            )

    @property
    def worldspace_vertex_offset_map_scale(self) -> primitives.Float2 | None:
        """The WorldspaceVertexOffsetMapScale field value."""
        member = self.get_member("WorldspaceVertexOffsetMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @worldspace_vertex_offset_map_scale.setter
    def worldspace_vertex_offset_map_scale(self, value: primitives.Float2) -> None:
        """Set the WorldspaceVertexOffsetMapScale field value."""
        member = self.get_member("WorldspaceVertexOffsetMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldspaceVertexOffsetMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def worldspace_vertex_offset_map_offset(self) -> primitives.Float2 | None:
        """The WorldspaceVertexOffsetMapOffset field value."""
        member = self.get_member("WorldspaceVertexOffsetMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @worldspace_vertex_offset_map_offset.setter
    def worldspace_vertex_offset_map_offset(self, value: primitives.Float2) -> None:
        """Set the WorldspaceVertexOffsetMapOffset field value."""
        member = self.get_member("WorldspaceVertexOffsetMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldspaceVertexOffsetMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def worldspace_offset_per_vertex(self) -> bool | None:
        """The WorldspaceOffsetPerVertex field value."""
        member = self.get_member("WorldspaceOffsetPerVertex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @worldspace_offset_per_vertex.setter
    def worldspace_offset_per_vertex(self, value: bool) -> None:
        """Set the WorldspaceOffsetPerVertex field value."""
        member = self.get_member("WorldspaceOffsetPerVertex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldspaceOffsetPerVertex", fields.FieldBool(value=value)
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
    def smoothness(self) -> np.float32 | None:
        """The Smoothness field value."""
        member = self.get_member("Smoothness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothness.setter
    def smoothness(self, value: np.float32) -> None:
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
    def transparent(self) -> str | None:
        """Target ID of the _transparent reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_transparent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @transparent.setter
    def transparent(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _transparent reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_transparent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_transparent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

