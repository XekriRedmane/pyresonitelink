"""Generated component: PBS_DistanceLerpSpecular."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_DistanceLerpSpecular(GeneratedComponent, ICullingMaterial, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_DistanceLerpSpecular.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_DistanceLerpSpecular"

    def __init__(self, high_priority_integration: bool | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, albedo_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: np.float32 | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, grid_size: primitives.Float3 | None = None, grid_offset: primitives.Float3 | None = None, displace_from: np.float32 | None = None, displace_to: np.float32 | None = None, displace_magnitude_from: np.float32 | None = None, displace_magnitude_to: np.float32 | None = None, emission_from: np.float32 | None = None, emission_to: np.float32 | None = None, emission_color_from: primitives.ColorX | None = None, emission_color_to: primitives.ColorX | None = None, override_displacement_direction: primitives.Float3 | None = None, local_space: bool | None = None, transparent: bool | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, specular_color: primitives.ColorX | None = None, specular_map: str | IAssetProvider[ITexture2D] | None = None, regular: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
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
            grid_size: Initial value for GridSize.
            grid_offset: Initial value for GridOffset.
            displace_from: Initial value for DisplaceFrom.
            displace_to: Initial value for DisplaceTo.
            displace_magnitude_from: Initial value for DisplaceMagnitudeFrom.
            displace_magnitude_to: Initial value for DisplaceMagnitudeTo.
            emission_from: Initial value for EmissionFrom.
            emission_to: Initial value for EmissionTo.
            emission_color_from: Initial value for EmissionColorFrom.
            emission_color_to: Initial value for EmissionColorTo.
            override_displacement_direction: Initial value for OverrideDisplacementDirection.
            local_space: Initial value for LocalSpace.
            transparent: Initial value for Transparent.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            specular_color: Initial value for SpecularColor.
            specular_map: Initial value for SpecularMap.
            regular: Initial value for _regular.
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
        if grid_size is not None:
            self.grid_size = grid_size
        if grid_offset is not None:
            self.grid_offset = grid_offset
        if displace_from is not None:
            self.displace_from = displace_from
        if displace_to is not None:
            self.displace_to = displace_to
        if displace_magnitude_from is not None:
            self.displace_magnitude_from = displace_magnitude_from
        if displace_magnitude_to is not None:
            self.displace_magnitude_to = displace_magnitude_to
        if emission_from is not None:
            self.emission_from = emission_from
        if emission_to is not None:
            self.emission_to = emission_to
        if emission_color_from is not None:
            self.emission_color_from = emission_color_from
        if emission_color_to is not None:
            self.emission_color_to = emission_color_to
        if override_displacement_direction is not None:
            self.override_displacement_direction = override_displacement_direction
        if local_space is not None:
            self.local_space = local_space
        if transparent is not None:
            self.transparent = transparent
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
    def grid_size(self) -> primitives.Float3 | None:
        """The GridSize field value."""
        member = self.get_member("GridSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grid_size.setter
    def grid_size(self, value: primitives.Float3) -> None:
        """Set the GridSize field value."""
        member = self.get_member("GridSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GridSize", fields.FieldFloat3(value=value)
            )

    @property
    def grid_offset(self) -> primitives.Float3 | None:
        """The GridOffset field value."""
        member = self.get_member("GridOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grid_offset.setter
    def grid_offset(self, value: primitives.Float3) -> None:
        """Set the GridOffset field value."""
        member = self.get_member("GridOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GridOffset", fields.FieldFloat3(value=value)
            )

    @property
    def displace_from(self) -> np.float32 | None:
        """The DisplaceFrom field value."""
        member = self.get_member("DisplaceFrom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @displace_from.setter
    def displace_from(self, value: np.float32) -> None:
        """Set the DisplaceFrom field value."""
        member = self.get_member("DisplaceFrom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplaceFrom", fields.FieldFloat(value=value)
            )

    @property
    def displace_to(self) -> np.float32 | None:
        """The DisplaceTo field value."""
        member = self.get_member("DisplaceTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @displace_to.setter
    def displace_to(self, value: np.float32) -> None:
        """Set the DisplaceTo field value."""
        member = self.get_member("DisplaceTo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplaceTo", fields.FieldFloat(value=value)
            )

    @property
    def displace_magnitude_from(self) -> np.float32 | None:
        """The DisplaceMagnitudeFrom field value."""
        member = self.get_member("DisplaceMagnitudeFrom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @displace_magnitude_from.setter
    def displace_magnitude_from(self, value: np.float32) -> None:
        """Set the DisplaceMagnitudeFrom field value."""
        member = self.get_member("DisplaceMagnitudeFrom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplaceMagnitudeFrom", fields.FieldFloat(value=value)
            )

    @property
    def displace_magnitude_to(self) -> np.float32 | None:
        """The DisplaceMagnitudeTo field value."""
        member = self.get_member("DisplaceMagnitudeTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @displace_magnitude_to.setter
    def displace_magnitude_to(self, value: np.float32) -> None:
        """Set the DisplaceMagnitudeTo field value."""
        member = self.get_member("DisplaceMagnitudeTo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplaceMagnitudeTo", fields.FieldFloat(value=value)
            )

    @property
    def emission_from(self) -> np.float32 | None:
        """The EmissionFrom field value."""
        member = self.get_member("EmissionFrom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_from.setter
    def emission_from(self, value: np.float32) -> None:
        """Set the EmissionFrom field value."""
        member = self.get_member("EmissionFrom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionFrom", fields.FieldFloat(value=value)
            )

    @property
    def emission_to(self) -> np.float32 | None:
        """The EmissionTo field value."""
        member = self.get_member("EmissionTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_to.setter
    def emission_to(self, value: np.float32) -> None:
        """Set the EmissionTo field value."""
        member = self.get_member("EmissionTo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionTo", fields.FieldFloat(value=value)
            )

    @property
    def emission_color_from(self) -> primitives.ColorX | None:
        """The EmissionColorFrom field value."""
        member = self.get_member("EmissionColorFrom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_color_from.setter
    def emission_color_from(self, value: primitives.ColorX) -> None:
        """Set the EmissionColorFrom field value."""
        member = self.get_member("EmissionColorFrom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionColorFrom", fields.FieldColorX(value=value)
            )

    @property
    def emission_color_to(self) -> primitives.ColorX | None:
        """The EmissionColorTo field value."""
        member = self.get_member("EmissionColorTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emission_color_to.setter
    def emission_color_to(self, value: primitives.ColorX) -> None:
        """Set the EmissionColorTo field value."""
        member = self.get_member("EmissionColorTo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissionColorTo", fields.FieldColorX(value=value)
            )

    @property
    def override_displacement_direction(self) -> primitives.Float3 | None:
        """The OverrideDisplacementDirection field value."""
        member = self.get_member("OverrideDisplacementDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_displacement_direction.setter
    def override_displacement_direction(self, value: primitives.Float3) -> None:
        """Set the OverrideDisplacementDirection field value."""
        member = self.get_member("OverrideDisplacementDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideDisplacementDirection", fields.FieldNullableFloat3(value=value)
            )

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
    def points(self) -> members.SyncList | None:
        """The Points member."""
        member = self.get_member("Points")
        if isinstance(member, members.SyncList):
            return member
        return None

    @points.setter
    def points(self, value: members.SyncList) -> None:
        """Set the Points member."""
        self.set_member("Points", value)

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
    def transparent(self) -> bool | None:
        """The Transparent field value."""
        member = self.get_member("Transparent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transparent.setter
    def transparent(self, value: bool) -> None:
        """Set the Transparent field value."""
        member = self.get_member("Transparent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Transparent", fields.FieldBool(value=value)
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

