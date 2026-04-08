"""Generated component: PBS_IntersectMetallic."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.ipbs_metallic import IPBS_Metallic
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_IntersectMetallic(GeneratedComponent, IPBS_Metallic, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_IntersectMetallic.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_IntersectMetallic"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, begin_transition_start: np.float32 | None = None, begin_transition_end: np.float32 | None = None, end_transition_start: np.float32 | None = None, end_transition_end: np.float32 | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, albedo_color: primitives.ColorX | None = None, intersect_albedo_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, intersect_emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: np.float32 | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, metallic: np.float32 | None = None, smoothness: np.float32 | None = None, metallic_map: str | IAssetProvider[ITexture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            begin_transition_start: Initial value for BeginTransitionStart.
            begin_transition_end: Initial value for BeginTransitionEnd.
            end_transition_start: Initial value for EndTransitionStart.
            end_transition_end: Initial value for EndTransitionEnd.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            albedo_color: Initial value for AlbedoColor.
            intersect_albedo_color: Initial value for IntersectAlbedoColor.
            albedo_texture: Initial value for AlbedoTexture.
            emissive_color: Initial value for EmissiveColor.
            intersect_emissive_color: Initial value for IntersectEmissiveColor.
            emissive_map: Initial value for EmissiveMap.
            normal_map: Initial value for NormalMap.
            normal_scale: Initial value for NormalScale.
            occlusion_map: Initial value for OcclusionMap.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            metallic: Initial value for Metallic.
            smoothness: Initial value for Smoothness.
            metallic_map: Initial value for MetallicMap.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if begin_transition_start is not None:
            self.begin_transition_start = begin_transition_start
        if begin_transition_end is not None:
            self.begin_transition_end = begin_transition_end
        if end_transition_start is not None:
            self.end_transition_start = end_transition_start
        if end_transition_end is not None:
            self.end_transition_end = end_transition_end
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if albedo_color is not None:
            self.albedo_color = albedo_color
        if intersect_albedo_color is not None:
            self.intersect_albedo_color = intersect_albedo_color
        if albedo_texture is not None:
            self.albedo_texture = albedo_texture
        if emissive_color is not None:
            self.emissive_color = emissive_color
        if intersect_emissive_color is not None:
            self.intersect_emissive_color = intersect_emissive_color
        if emissive_map is not None:
            self.emissive_map = emissive_map
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_scale is not None:
            self.normal_scale = normal_scale
        if occlusion_map is not None:
            self.occlusion_map = occlusion_map
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
    def begin_transition_start(self) -> np.float32 | None:
        """The BeginTransitionStart field value."""
        member = self.get_member("BeginTransitionStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @begin_transition_start.setter
    def begin_transition_start(self, value: np.float32) -> None:
        """Set the BeginTransitionStart field value."""
        member = self.get_member("BeginTransitionStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BeginTransitionStart", fields.FieldFloat(value=value)
            )

    @property
    def begin_transition_end(self) -> np.float32 | None:
        """The BeginTransitionEnd field value."""
        member = self.get_member("BeginTransitionEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @begin_transition_end.setter
    def begin_transition_end(self, value: np.float32) -> None:
        """Set the BeginTransitionEnd field value."""
        member = self.get_member("BeginTransitionEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BeginTransitionEnd", fields.FieldFloat(value=value)
            )

    @property
    def end_transition_start(self) -> np.float32 | None:
        """The EndTransitionStart field value."""
        member = self.get_member("EndTransitionStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_transition_start.setter
    def end_transition_start(self, value: np.float32) -> None:
        """Set the EndTransitionStart field value."""
        member = self.get_member("EndTransitionStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndTransitionStart", fields.FieldFloat(value=value)
            )

    @property
    def end_transition_end(self) -> np.float32 | None:
        """The EndTransitionEnd field value."""
        member = self.get_member("EndTransitionEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_transition_end.setter
    def end_transition_end(self, value: np.float32) -> None:
        """Set the EndTransitionEnd field value."""
        member = self.get_member("EndTransitionEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndTransitionEnd", fields.FieldFloat(value=value)
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
    def intersect_albedo_color(self) -> primitives.ColorX | None:
        """The IntersectAlbedoColor field value."""
        member = self.get_member("IntersectAlbedoColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intersect_albedo_color.setter
    def intersect_albedo_color(self, value: primitives.ColorX) -> None:
        """Set the IntersectAlbedoColor field value."""
        member = self.get_member("IntersectAlbedoColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IntersectAlbedoColor", fields.FieldColorX(value=value)
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
    def intersect_emissive_color(self) -> primitives.ColorX | None:
        """The IntersectEmissiveColor field value."""
        member = self.get_member("IntersectEmissiveColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intersect_emissive_color.setter
    def intersect_emissive_color(self, value: primitives.ColorX) -> None:
        """Set the IntersectEmissiveColor field value."""
        member = self.get_member("IntersectEmissiveColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IntersectEmissiveColor", fields.FieldColorX(value=value)
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

