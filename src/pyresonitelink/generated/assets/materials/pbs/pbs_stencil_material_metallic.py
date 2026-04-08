"""Generated component: PBS_StencilMaterialMetallic."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_StencilMaterialMetallic(GeneratedComponent, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_StencilMaterialMetallic.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_StencilMaterialMetallic"

    def __init__(self, high_priority_integration: bool | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, albedo_color: primitives.ColorX | None = None, albedo_texture: str | IAssetProvider[ITexture2D] | None = None, emissive_color: primitives.ColorX | None = None, emissive_map: str | IAssetProvider[ITexture2D] | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: np.float32 | None = None, occlusion_map: str | IAssetProvider[ITexture2D] | None = None, stencil_id: np.uint8 | None = None, stencil_write_mask: np.uint8 | None = None, stencil_read_mask: np.uint8 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, rect_dummy: primitives.Rect | None = None, rect_clip_dummy: bool | None = None, metallic: np.float32 | None = None, smoothness: np.float32 | None = None, metallic_map: str | IAssetProvider[ITexture2D] | None = None, regular: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
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
            stencil_id: Initial value for StencilID.
            stencil_write_mask: Initial value for StencilWriteMask.
            stencil_read_mask: Initial value for StencilReadMask.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            rect_dummy: Initial value for __rectDummy.
            rect_clip_dummy: Initial value for __rectClipDummy.
            metallic: Initial value for Metallic.
            smoothness: Initial value for Smoothness.
            metallic_map: Initial value for MetallicMap.
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
        if stencil_id is not None:
            self.stencil_id = stencil_id
        if stencil_write_mask is not None:
            self.stencil_write_mask = stencil_write_mask
        if stencil_read_mask is not None:
            self.stencil_read_mask = stencil_read_mask
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if rect_dummy is not None:
            self.rect_dummy = rect_dummy
        if rect_clip_dummy is not None:
            self.rect_clip_dummy = rect_clip_dummy
        if metallic is not None:
            self.metallic = metallic
        if smoothness is not None:
            self.smoothness = smoothness
        if metallic_map is not None:
            self.metallic_map = metallic_map
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
    def stencil_id(self) -> np.uint8 | None:
        """The StencilID field value."""
        member = self.get_member("StencilID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_id.setter
    def stencil_id(self, value: np.uint8) -> None:
        """Set the StencilID field value."""
        member = self.get_member("StencilID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilID", fields.FieldByte(value=value)
            )

    @property
    def stencil_write_mask(self) -> np.uint8 | None:
        """The StencilWriteMask field value."""
        member = self.get_member("StencilWriteMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_write_mask.setter
    def stencil_write_mask(self, value: np.uint8) -> None:
        """Set the StencilWriteMask field value."""
        member = self.get_member("StencilWriteMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilWriteMask", fields.FieldByte(value=value)
            )

    @property
    def stencil_read_mask(self) -> np.uint8 | None:
        """The StencilReadMask field value."""
        member = self.get_member("StencilReadMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_read_mask.setter
    def stencil_read_mask(self, value: np.uint8) -> None:
        """Set the StencilReadMask field value."""
        member = self.get_member("StencilReadMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilReadMask", fields.FieldByte(value=value)
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
    def rect_dummy(self) -> primitives.Rect | None:
        """The __rectDummy field value."""
        member = self.get_member("__rectDummy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect_dummy.setter
    def rect_dummy(self, value: primitives.Rect) -> None:
        """Set the __rectDummy field value."""
        member = self.get_member("__rectDummy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__rectDummy", fields.FieldRect(value=value)
            )

    @property
    def rect_clip_dummy(self) -> bool | None:
        """The __rectClipDummy field value."""
        member = self.get_member("__rectClipDummy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect_clip_dummy.setter
    def rect_clip_dummy(self, value: bool) -> None:
        """Set the __rectClipDummy field value."""
        member = self.get_member("__rectClipDummy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__rectClipDummy", fields.FieldBool(value=value)
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

