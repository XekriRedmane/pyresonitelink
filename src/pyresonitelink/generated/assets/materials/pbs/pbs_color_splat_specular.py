"""Generated component: PBS_ColorSplatSpecular."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBS_ColorSplatSpecular(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PBS_ColorSplatSpecular.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBS_ColorSplatSpecular"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, multi_value: bool | None = None, color_map: str | IAssetProvider[ITexture2D] | None = None, color_map_scale: primitives.Float2 | None = None, color_map_offset: primitives.Float2 | None = None, packed_height_map: str | IAssetProvider[ITexture2D] | None = None, height_transition_range: np.float32 | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, albedo_color0: primitives.ColorX | None = None, albedo_color1: primitives.ColorX | None = None, albedo_color2: primitives.ColorX | None = None, albedo_color3: primitives.ColorX | None = None, albedo_texture0: str | IAssetProvider[ITexture2D] | None = None, albedo_texture1: str | IAssetProvider[ITexture2D] | None = None, albedo_texture2: str | IAssetProvider[ITexture2D] | None = None, albedo_texture3: str | IAssetProvider[ITexture2D] | None = None, emissive_color0: primitives.ColorX | None = None, emissive_color1: primitives.ColorX | None = None, emissive_color2: primitives.ColorX | None = None, emissive_color3: primitives.ColorX | None = None, emissive_map0: str | IAssetProvider[ITexture2D] | None = None, emissive_map1: str | IAssetProvider[ITexture2D] | None = None, emissive_map2: str | IAssetProvider[ITexture2D] | None = None, emissive_map3: str | IAssetProvider[ITexture2D] | None = None, packed_emission_map: str | IAssetProvider[ITexture2D] | None = None, packed_normal_map01: str | IAssetProvider[ITexture2D] | None = None, packed_normal_map23: str | IAssetProvider[ITexture2D] | None = None, normal_scale0: np.float32 | None = None, normal_scale1: np.float32 | None = None, normal_scale2: np.float32 | None = None, normal_scale3: np.float32 | None = None, alpha_clip: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, specular_color0: primitives.ColorX | None = None, specular_color1: primitives.ColorX | None = None, specular_color2: primitives.ColorX | None = None, specular_color3: primitives.ColorX | None = None, specular_map0: str | IAssetProvider[ITexture2D] | None = None, specular_map1: str | IAssetProvider[ITexture2D] | None = None, specular_map2: str | IAssetProvider[ITexture2D] | None = None, specular_map3: str | IAssetProvider[ITexture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            multi_value: Initial value for MultiValue.
            color_map: Initial value for ColorMap.
            color_map_scale: Initial value for ColorMapScale.
            color_map_offset: Initial value for ColorMapOffset.
            packed_height_map: Initial value for PackedHeightMap.
            height_transition_range: Initial value for HeightTransitionRange.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            albedo_color0: Initial value for AlbedoColor0.
            albedo_color1: Initial value for AlbedoColor1.
            albedo_color2: Initial value for AlbedoColor2.
            albedo_color3: Initial value for AlbedoColor3.
            albedo_texture0: Initial value for AlbedoTexture0.
            albedo_texture1: Initial value for AlbedoTexture1.
            albedo_texture2: Initial value for AlbedoTexture2.
            albedo_texture3: Initial value for AlbedoTexture3.
            emissive_color0: Initial value for EmissiveColor0.
            emissive_color1: Initial value for EmissiveColor1.
            emissive_color2: Initial value for EmissiveColor2.
            emissive_color3: Initial value for EmissiveColor3.
            emissive_map0: Initial value for EmissiveMap0.
            emissive_map1: Initial value for EmissiveMap1.
            emissive_map2: Initial value for EmissiveMap2.
            emissive_map3: Initial value for EmissiveMap3.
            packed_emission_map: Initial value for PackedEmissionMap.
            packed_normal_map01: Initial value for PackedNormalMap01.
            packed_normal_map23: Initial value for PackedNormalMap23.
            normal_scale0: Initial value for NormalScale0.
            normal_scale1: Initial value for NormalScale1.
            normal_scale2: Initial value for NormalScale2.
            normal_scale3: Initial value for NormalScale3.
            alpha_clip: Initial value for AlphaClip.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            specular_color0: Initial value for SpecularColor0.
            specular_color1: Initial value for SpecularColor1.
            specular_color2: Initial value for SpecularColor2.
            specular_color3: Initial value for SpecularColor3.
            specular_map0: Initial value for SpecularMap0.
            specular_map1: Initial value for SpecularMap1.
            specular_map2: Initial value for SpecularMap2.
            specular_map3: Initial value for SpecularMap3.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if multi_value is not None:
            self.multi_value = multi_value
        if color_map is not None:
            self.color_map = color_map
        if color_map_scale is not None:
            self.color_map_scale = color_map_scale
        if color_map_offset is not None:
            self.color_map_offset = color_map_offset
        if packed_height_map is not None:
            self.packed_height_map = packed_height_map
        if height_transition_range is not None:
            self.height_transition_range = height_transition_range
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if albedo_color0 is not None:
            self.albedo_color0 = albedo_color0
        if albedo_color1 is not None:
            self.albedo_color1 = albedo_color1
        if albedo_color2 is not None:
            self.albedo_color2 = albedo_color2
        if albedo_color3 is not None:
            self.albedo_color3 = albedo_color3
        if albedo_texture0 is not None:
            self.albedo_texture0 = albedo_texture0
        if albedo_texture1 is not None:
            self.albedo_texture1 = albedo_texture1
        if albedo_texture2 is not None:
            self.albedo_texture2 = albedo_texture2
        if albedo_texture3 is not None:
            self.albedo_texture3 = albedo_texture3
        if emissive_color0 is not None:
            self.emissive_color0 = emissive_color0
        if emissive_color1 is not None:
            self.emissive_color1 = emissive_color1
        if emissive_color2 is not None:
            self.emissive_color2 = emissive_color2
        if emissive_color3 is not None:
            self.emissive_color3 = emissive_color3
        if emissive_map0 is not None:
            self.emissive_map0 = emissive_map0
        if emissive_map1 is not None:
            self.emissive_map1 = emissive_map1
        if emissive_map2 is not None:
            self.emissive_map2 = emissive_map2
        if emissive_map3 is not None:
            self.emissive_map3 = emissive_map3
        if packed_emission_map is not None:
            self.packed_emission_map = packed_emission_map
        if packed_normal_map01 is not None:
            self.packed_normal_map01 = packed_normal_map01
        if packed_normal_map23 is not None:
            self.packed_normal_map23 = packed_normal_map23
        if normal_scale0 is not None:
            self.normal_scale0 = normal_scale0
        if normal_scale1 is not None:
            self.normal_scale1 = normal_scale1
        if normal_scale2 is not None:
            self.normal_scale2 = normal_scale2
        if normal_scale3 is not None:
            self.normal_scale3 = normal_scale3
        if alpha_clip is not None:
            self.alpha_clip = alpha_clip
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if specular_color0 is not None:
            self.specular_color0 = specular_color0
        if specular_color1 is not None:
            self.specular_color1 = specular_color1
        if specular_color2 is not None:
            self.specular_color2 = specular_color2
        if specular_color3 is not None:
            self.specular_color3 = specular_color3
        if specular_map0 is not None:
            self.specular_map0 = specular_map0
        if specular_map1 is not None:
            self.specular_map1 = specular_map1
        if specular_map2 is not None:
            self.specular_map2 = specular_map2
        if specular_map3 is not None:
            self.specular_map3 = specular_map3

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
    def multi_value(self) -> bool | None:
        """The MultiValue field value."""
        member = self.get_member("MultiValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multi_value.setter
    def multi_value(self, value: bool) -> None:
        """Set the MultiValue field value."""
        member = self.get_member("MultiValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiValue", fields.FieldBool(value=value)
            )

    @property
    def color_map(self) -> str | None:
        """Target ID of the ColorMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ColorMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_map.setter
    def color_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ColorMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ColorMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColorMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def color_map_scale(self) -> primitives.Float2 | None:
        """The ColorMapScale field value."""
        member = self.get_member("ColorMapScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_map_scale.setter
    def color_map_scale(self, value: primitives.Float2) -> None:
        """Set the ColorMapScale field value."""
        member = self.get_member("ColorMapScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorMapScale", fields.FieldFloat2(value=value)
            )

    @property
    def color_map_offset(self) -> primitives.Float2 | None:
        """The ColorMapOffset field value."""
        member = self.get_member("ColorMapOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_map_offset.setter
    def color_map_offset(self, value: primitives.Float2) -> None:
        """Set the ColorMapOffset field value."""
        member = self.get_member("ColorMapOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorMapOffset", fields.FieldFloat2(value=value)
            )

    @property
    def packed_height_map(self) -> str | None:
        """Target ID of the PackedHeightMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("PackedHeightMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @packed_height_map.setter
    def packed_height_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the PackedHeightMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PackedHeightMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PackedHeightMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def height_transition_range(self) -> np.float32 | None:
        """The HeightTransitionRange field value."""
        member = self.get_member("HeightTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_transition_range.setter
    def height_transition_range(self, value: np.float32) -> None:
        """Set the HeightTransitionRange field value."""
        member = self.get_member("HeightTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightTransitionRange", fields.FieldFloat(value=value)
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
    def albedo_color0(self) -> primitives.ColorX | None:
        """The AlbedoColor0 field value."""
        member = self.get_member("AlbedoColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color0.setter
    def albedo_color0(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor0 field value."""
        member = self.get_member("AlbedoColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor0", fields.FieldColorX(value=value)
            )

    @property
    def albedo_color1(self) -> primitives.ColorX | None:
        """The AlbedoColor1 field value."""
        member = self.get_member("AlbedoColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color1.setter
    def albedo_color1(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor1 field value."""
        member = self.get_member("AlbedoColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor1", fields.FieldColorX(value=value)
            )

    @property
    def albedo_color2(self) -> primitives.ColorX | None:
        """The AlbedoColor2 field value."""
        member = self.get_member("AlbedoColor2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color2.setter
    def albedo_color2(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor2 field value."""
        member = self.get_member("AlbedoColor2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor2", fields.FieldColorX(value=value)
            )

    @property
    def albedo_color3(self) -> primitives.ColorX | None:
        """The AlbedoColor3 field value."""
        member = self.get_member("AlbedoColor3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @albedo_color3.setter
    def albedo_color3(self, value: primitives.ColorX) -> None:
        """Set the AlbedoColor3 field value."""
        member = self.get_member("AlbedoColor3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlbedoColor3", fields.FieldColorX(value=value)
            )

    @property
    def albedo_texture0(self) -> str | None:
        """Target ID of the AlbedoTexture0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("AlbedoTexture0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @albedo_texture0.setter
    def albedo_texture0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the AlbedoTexture0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AlbedoTexture0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AlbedoTexture0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def albedo_texture1(self) -> str | None:
        """Target ID of the AlbedoTexture1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("AlbedoTexture1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @albedo_texture1.setter
    def albedo_texture1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the AlbedoTexture1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AlbedoTexture1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AlbedoTexture1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def albedo_texture2(self) -> str | None:
        """Target ID of the AlbedoTexture2 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("AlbedoTexture2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @albedo_texture2.setter
    def albedo_texture2(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the AlbedoTexture2 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AlbedoTexture2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AlbedoTexture2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def albedo_texture3(self) -> str | None:
        """Target ID of the AlbedoTexture3 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("AlbedoTexture3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @albedo_texture3.setter
    def albedo_texture3(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the AlbedoTexture3 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AlbedoTexture3")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AlbedoTexture3",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emissive_color0(self) -> primitives.ColorX | None:
        """The EmissiveColor0 field value."""
        member = self.get_member("EmissiveColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color0.setter
    def emissive_color0(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor0 field value."""
        member = self.get_member("EmissiveColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor0", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color1(self) -> primitives.ColorX | None:
        """The EmissiveColor1 field value."""
        member = self.get_member("EmissiveColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color1.setter
    def emissive_color1(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor1 field value."""
        member = self.get_member("EmissiveColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor1", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color2(self) -> primitives.ColorX | None:
        """The EmissiveColor2 field value."""
        member = self.get_member("EmissiveColor2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color2.setter
    def emissive_color2(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor2 field value."""
        member = self.get_member("EmissiveColor2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor2", fields.FieldColorX(value=value)
            )

    @property
    def emissive_color3(self) -> primitives.ColorX | None:
        """The EmissiveColor3 field value."""
        member = self.get_member("EmissiveColor3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emissive_color3.setter
    def emissive_color3(self, value: primitives.ColorX) -> None:
        """Set the EmissiveColor3 field value."""
        member = self.get_member("EmissiveColor3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmissiveColor3", fields.FieldColorX(value=value)
            )

    @property
    def emissive_map0(self) -> str | None:
        """Target ID of the EmissiveMap0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissiveMap0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_map0.setter
    def emissive_map0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissiveMap0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissiveMap0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissiveMap0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emissive_map1(self) -> str | None:
        """Target ID of the EmissiveMap1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissiveMap1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_map1.setter
    def emissive_map1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissiveMap1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissiveMap1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissiveMap1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emissive_map2(self) -> str | None:
        """Target ID of the EmissiveMap2 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissiveMap2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_map2.setter
    def emissive_map2(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissiveMap2 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissiveMap2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissiveMap2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def emissive_map3(self) -> str | None:
        """Target ID of the EmissiveMap3 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("EmissiveMap3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emissive_map3.setter
    def emissive_map3(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the EmissiveMap3 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("EmissiveMap3")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EmissiveMap3",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def packed_emission_map(self) -> str | None:
        """Target ID of the PackedEmissionMap reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("PackedEmissionMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @packed_emission_map.setter
    def packed_emission_map(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the PackedEmissionMap reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PackedEmissionMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PackedEmissionMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def packed_normal_map01(self) -> str | None:
        """Target ID of the PackedNormalMap01 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("PackedNormalMap01")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @packed_normal_map01.setter
    def packed_normal_map01(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the PackedNormalMap01 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PackedNormalMap01")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PackedNormalMap01",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def packed_normal_map23(self) -> str | None:
        """Target ID of the PackedNormalMap23 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("PackedNormalMap23")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @packed_normal_map23.setter
    def packed_normal_map23(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the PackedNormalMap23 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PackedNormalMap23")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PackedNormalMap23",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def normal_scale0(self) -> np.float32 | None:
        """The NormalScale0 field value."""
        member = self.get_member("NormalScale0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale0.setter
    def normal_scale0(self, value: np.float32) -> None:
        """Set the NormalScale0 field value."""
        member = self.get_member("NormalScale0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale0", fields.FieldFloat(value=value)
            )

    @property
    def normal_scale1(self) -> np.float32 | None:
        """The NormalScale1 field value."""
        member = self.get_member("NormalScale1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale1.setter
    def normal_scale1(self, value: np.float32) -> None:
        """Set the NormalScale1 field value."""
        member = self.get_member("NormalScale1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale1", fields.FieldFloat(value=value)
            )

    @property
    def normal_scale2(self) -> np.float32 | None:
        """The NormalScale2 field value."""
        member = self.get_member("NormalScale2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale2.setter
    def normal_scale2(self, value: np.float32) -> None:
        """Set the NormalScale2 field value."""
        member = self.get_member("NormalScale2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale2", fields.FieldFloat(value=value)
            )

    @property
    def normal_scale3(self) -> np.float32 | None:
        """The NormalScale3 field value."""
        member = self.get_member("NormalScale3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale3.setter
    def normal_scale3(self, value: np.float32) -> None:
        """Set the NormalScale3 field value."""
        member = self.get_member("NormalScale3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale3", fields.FieldFloat(value=value)
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
    def specular_color0(self) -> primitives.ColorX | None:
        """The SpecularColor0 field value."""
        member = self.get_member("SpecularColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_color0.setter
    def specular_color0(self, value: primitives.ColorX) -> None:
        """Set the SpecularColor0 field value."""
        member = self.get_member("SpecularColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularColor0", fields.FieldColorX(value=value)
            )

    @property
    def specular_color1(self) -> primitives.ColorX | None:
        """The SpecularColor1 field value."""
        member = self.get_member("SpecularColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_color1.setter
    def specular_color1(self, value: primitives.ColorX) -> None:
        """Set the SpecularColor1 field value."""
        member = self.get_member("SpecularColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularColor1", fields.FieldColorX(value=value)
            )

    @property
    def specular_color2(self) -> primitives.ColorX | None:
        """The SpecularColor2 field value."""
        member = self.get_member("SpecularColor2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_color2.setter
    def specular_color2(self, value: primitives.ColorX) -> None:
        """Set the SpecularColor2 field value."""
        member = self.get_member("SpecularColor2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularColor2", fields.FieldColorX(value=value)
            )

    @property
    def specular_color3(self) -> primitives.ColorX | None:
        """The SpecularColor3 field value."""
        member = self.get_member("SpecularColor3")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @specular_color3.setter
    def specular_color3(self, value: primitives.ColorX) -> None:
        """Set the SpecularColor3 field value."""
        member = self.get_member("SpecularColor3")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpecularColor3", fields.FieldColorX(value=value)
            )

    @property
    def specular_map0(self) -> str | None:
        """Target ID of the SpecularMap0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SpecularMap0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @specular_map0.setter
    def specular_map0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SpecularMap0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SpecularMap0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpecularMap0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def specular_map1(self) -> str | None:
        """Target ID of the SpecularMap1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SpecularMap1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @specular_map1.setter
    def specular_map1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SpecularMap1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SpecularMap1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpecularMap1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def specular_map2(self) -> str | None:
        """Target ID of the SpecularMap2 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SpecularMap2")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @specular_map2.setter
    def specular_map2(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SpecularMap2 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SpecularMap2")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpecularMap2",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def specular_map3(self) -> str | None:
        """Target ID of the SpecularMap3 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SpecularMap3")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @specular_map3.setter
    def specular_map3(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SpecularMap3 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SpecularMap3")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpecularMap3",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

