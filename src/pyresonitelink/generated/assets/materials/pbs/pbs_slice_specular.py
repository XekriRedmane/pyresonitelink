"""Generated component: PBS_SliceSpecular."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.ipbs_specular import IPBS_Specular
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_SliceSpecular(GeneratedComponent, IPBS_Specular, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_SliceSpecular.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_SliceSpecular"

    def __init__(self, high_priority_integration: bool | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, albedo_color: primitives.ColorX | None = None, edge_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, edge_emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: np.float32 | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, detail_texture_scale: primitives.Float2 | None = None, detail_texture_offset: primitives.Float2 | None = None, detail_albedo_texture: str | IAssetProvider[ITexture2D] | None = None, detail_normal_map: str | IAssetProvider[ITexture2D] | None = None, detail_normal_scale: np.float32 | None = None, hide_slicers: bool | None = None, local_space: bool | None = None, edge_transition_start: np.float32 | None = None, edge_transition_end: np.float32 | None = None, use_alpha_clip: bool | None = None, alpha_clip: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, specular_color: primitives.ColorX | None = None, specular_map: str | IAssetProvider[ITexture2D] | None = None, regular: str | IAssetProvider[Shader] | None = None, transparent: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            albedo_color: Initial value for AlbedoColor.
            edge_color: Initial value for EdgeColor.
            albedo_texture: Initial value for AlbedoTexture.
            emissive_color: Initial value for EmissiveColor.
            edge_emissive_color: Initial value for EdgeEmissiveColor.
            emissive_map: Initial value for EmissiveMap.
            normal_map: Initial value for NormalMap.
            normal_scale: Initial value for NormalScale.
            occlusion_map: Initial value for OcclusionMap.
            detail_texture_scale: Initial value for DetailTextureScale.
            detail_texture_offset: Initial value for DetailTextureOffset.
            detail_albedo_texture: Initial value for DetailAlbedoTexture.
            detail_normal_map: Initial value for DetailNormalMap.
            detail_normal_scale: Initial value for DetailNormalScale.
            hide_slicers: Initial value for HideSlicers.
            local_space: Initial value for LocalSpace.
            edge_transition_start: Initial value for EdgeTransitionStart.
            edge_transition_end: Initial value for EdgeTransitionEnd.
            use_alpha_clip: Initial value for _useAlphaClip.
            alpha_clip: Initial value for AlphaClip.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            specular_color: Initial value for SpecularColor.
            specular_map: Initial value for SpecularMap.
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
        if edge_color is not None:
            self.edge_color = edge_color
        if albedo_texture is not None:
            self.albedo_texture = albedo_texture
        if emissive_color is not None:
            self.emissive_color = emissive_color
        if edge_emissive_color is not None:
            self.edge_emissive_color = edge_emissive_color
        if emissive_map is not None:
            self.emissive_map = emissive_map
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_scale is not None:
            self.normal_scale = normal_scale
        if occlusion_map is not None:
            self.occlusion_map = occlusion_map
        if detail_texture_scale is not None:
            self.detail_texture_scale = detail_texture_scale
        if detail_texture_offset is not None:
            self.detail_texture_offset = detail_texture_offset
        if detail_albedo_texture is not None:
            self.detail_albedo_texture = detail_albedo_texture
        if detail_normal_map is not None:
            self.detail_normal_map = detail_normal_map
        if detail_normal_scale is not None:
            self.detail_normal_scale = detail_normal_scale
        if hide_slicers is not None:
            self.hide_slicers = hide_slicers
        if local_space is not None:
            self.local_space = local_space
        if edge_transition_start is not None:
            self.edge_transition_start = edge_transition_start
        if edge_transition_end is not None:
            self.edge_transition_end = edge_transition_end
        if use_alpha_clip is not None:
            self.use_alpha_clip = use_alpha_clip
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
    def edge_color(self) -> primitives.ColorX | None:
        """The EdgeColor field value."""
        member = self.get_member("EdgeColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_color.setter
    def edge_color(self, value: primitives.ColorX) -> None:
        """Set the EdgeColor field value."""
        member = self.get_member("EdgeColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeColor", fields.FieldColorX(value=value)
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
    def edge_emissive_color(self) -> primitives.ColorX | None:
        """The EdgeEmissiveColor field value."""
        member = self.get_member("EdgeEmissiveColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_emissive_color.setter
    def edge_emissive_color(self, value: primitives.ColorX) -> None:
        """Set the EdgeEmissiveColor field value."""
        member = self.get_member("EdgeEmissiveColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeEmissiveColor", fields.FieldColorX(value=value)
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
    def detail_texture_scale(self) -> primitives.Float2 | None:
        """The DetailTextureScale field value."""
        member = self.get_member("DetailTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @detail_texture_scale.setter
    def detail_texture_scale(self, value: primitives.Float2) -> None:
        """Set the DetailTextureScale field value."""
        member = self.get_member("DetailTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DetailTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def detail_texture_offset(self) -> primitives.Float2 | None:
        """The DetailTextureOffset field value."""
        member = self.get_member("DetailTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @detail_texture_offset.setter
    def detail_texture_offset(self, value: primitives.Float2) -> None:
        """Set the DetailTextureOffset field value."""
        member = self.get_member("DetailTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DetailTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def detail_albedo_texture(self) -> str | None:
        """Target ID of the DetailAlbedoTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("DetailAlbedoTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_albedo_texture.setter
    def detail_albedo_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the DetailAlbedoTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("DetailAlbedoTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DetailAlbedoTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def detail_normal_map(self) -> str | None:
        """Target ID of the DetailNormalMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("DetailNormalMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_normal_map.setter
    def detail_normal_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the DetailNormalMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("DetailNormalMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DetailNormalMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def detail_normal_scale(self) -> np.float32 | None:
        """The DetailNormalScale field value."""
        member = self.get_member("DetailNormalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @detail_normal_scale.setter
    def detail_normal_scale(self, value: np.float32) -> None:
        """Set the DetailNormalScale field value."""
        member = self.get_member("DetailNormalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DetailNormalScale", fields.FieldFloat(value=value)
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
    def hide_slicers(self) -> bool | None:
        """The HideSlicers field value."""
        member = self.get_member("HideSlicers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_slicers.setter
    def hide_slicers(self, value: bool) -> None:
        """Set the HideSlicers field value."""
        member = self.get_member("HideSlicers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideSlicers", fields.FieldBool(value=value)
            )

    @property
    def slicers(self) -> members.SyncList | None:
        """The Slicers member."""
        member = self.get_member("Slicers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @slicers.setter
    def slicers(self, value: members.SyncList) -> None:
        """Set the Slicers member."""
        self.set_member("Slicers", value)

    @property
    def local_space(self) -> bool | None:
        """The LocalSpace field value."""
        member = self.get_member("LocalSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_space.setter
    def local_space(self, value: bool) -> None:
        """Set the LocalSpace field value."""
        member = self.get_member("LocalSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalSpace", fields.FieldBool(value=value)
            )

    @property
    def edge_transition_start(self) -> np.float32 | None:
        """The EdgeTransitionStart field value."""
        member = self.get_member("EdgeTransitionStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_transition_start.setter
    def edge_transition_start(self, value: np.float32) -> None:
        """Set the EdgeTransitionStart field value."""
        member = self.get_member("EdgeTransitionStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeTransitionStart", fields.FieldFloat(value=value)
            )

    @property
    def edge_transition_end(self) -> np.float32 | None:
        """The EdgeTransitionEnd field value."""
        member = self.get_member("EdgeTransitionEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_transition_end.setter
    def edge_transition_end(self, value: np.float32) -> None:
        """Set the EdgeTransitionEnd field value."""
        member = self.get_member("EdgeTransitionEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeTransitionEnd", fields.FieldFloat(value=value)
            )

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
    def use_alpha_clip(self) -> bool | None:
        """The _useAlphaClip field value."""
        member = self.get_member("_useAlphaClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_alpha_clip.setter
    def use_alpha_clip(self, value: bool) -> None:
        """Set the _useAlphaClip field value."""
        member = self.get_member("_useAlphaClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_useAlphaClip", fields.FieldBool(value=value)
            )

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

