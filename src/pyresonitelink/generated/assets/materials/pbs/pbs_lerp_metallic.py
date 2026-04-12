"""Generated component: PBSLerpMetallic."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.generated._enums.zwrite import ZWrite
from pyresonitelink.generated._enums.ztest import ZTest
from pyresonitelink.generated._enums.culling import Culling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PBSLerpMetallic(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The PBSLerpMetallic component also known as . Is a material that can switch textures and texture sets.

If you want to switch between more than two sets of textures, please see MultiTextureFader.

To see detailed info on the textures not unique to this material like albedo and metallic, please see PBS_Metallic.

    Category: Assets/Materials/PBS
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PBSLerpMetallic"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, lerp: primitives.Float | None = None, lerp_texture: str | IAssetProvider[ITexture2D] | None = None, lerp_texture_scale: primitives.Float2 | None = None, lerp_texture_offset: primitives.Float2 | None = None, texture0_scale: primitives.Float2 | None = None, texture0_offset: primitives.Float2 | None = None, texture1_scale: primitives.Float2 | None = None, texture1_offset: primitives.Float2 | None = None, albedo_color0: primitives.ColorX | None = None, albedo_color1: primitives.ColorX | None = None, albedo_texture0: str | IAssetProvider[ITexture2D] | None = None, albedo_texture1: str | IAssetProvider[ITexture2D] | None = None, emissive_color0: primitives.ColorX | None = None, emissive_color1: primitives.ColorX | None = None, emissive_map0: str | IAssetProvider[ITexture2D] | None = None, emissive_map1: str | IAssetProvider[ITexture2D] | None = None, normal_map0: str | IAssetProvider[ITexture2D] | None = None, normal_map1: str | IAssetProvider[ITexture2D] | None = None, normal_scale0: primitives.Float | None = None, normal_scale1: primitives.Float | None = None, multi_value: primitives.Bool | None = None, occlusion_map0: str | IAssetProvider[ITexture2D] | None = None, occlusion_map1: str | IAssetProvider[ITexture2D] | None = None, blend_mode: BlendMode | str | None = None, alpha_cutoff: primitives.Float | None = None, zwrite: ZWrite | str | None = None, ztest: ZTest | str | None = None, culling: Culling | str | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, metallic0: primitives.Float | None = None, metallic1: primitives.Float | None = None, smoothness0: primitives.Float | None = None, smoothness1: primitives.Float | None = None, metallic_map0: str | IAssetProvider[ITexture2D] | None = None, metallic_map1: str | IAssetProvider[ITexture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            lerp: Initial value for Lerp.
            lerp_texture: Initial value for LerpTexture.
            lerp_texture_scale: Initial value for LerpTextureScale.
            lerp_texture_offset: Initial value for LerpTextureOffset.
            texture0_scale: Initial value for Texture0Scale.
            texture0_offset: Initial value for Texture0Offset.
            texture1_scale: Initial value for Texture1Scale.
            texture1_offset: Initial value for Texture1Offset.
            albedo_color0: Initial value for AlbedoColor0.
            albedo_color1: Initial value for AlbedoColor1.
            albedo_texture0: Initial value for AlbedoTexture0.
            albedo_texture1: Initial value for AlbedoTexture1.
            emissive_color0: Initial value for EmissiveColor0.
            emissive_color1: Initial value for EmissiveColor1.
            emissive_map0: Initial value for EmissiveMap0.
            emissive_map1: Initial value for EmissiveMap1.
            normal_map0: Initial value for NormalMap0.
            normal_map1: Initial value for NormalMap1.
            normal_scale0: Initial value for NormalScale0.
            normal_scale1: Initial value for NormalScale1.
            multi_value: Initial value for MultiValue.
            occlusion_map0: Initial value for OcclusionMap0.
            occlusion_map1: Initial value for OcclusionMap1.
            blend_mode: Initial value for BlendMode.
            alpha_cutoff: Initial value for AlphaCutoff.
            zwrite: Initial value for ZWrite.
            ztest: Initial value for ZTest.
            culling: Initial value for Culling.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            metallic0: Initial value for Metallic0.
            metallic1: Initial value for Metallic1.
            smoothness0: Initial value for Smoothness0.
            smoothness1: Initial value for Smoothness1.
            metallic_map0: Initial value for MetallicMap0.
            metallic_map1: Initial value for MetallicMap1.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if lerp is not None:
            self.lerp = lerp
        if lerp_texture is not None:
            self.lerp_texture = lerp_texture
        if lerp_texture_scale is not None:
            self.lerp_texture_scale = lerp_texture_scale
        if lerp_texture_offset is not None:
            self.lerp_texture_offset = lerp_texture_offset
        if texture0_scale is not None:
            self.texture0_scale = texture0_scale
        if texture0_offset is not None:
            self.texture0_offset = texture0_offset
        if texture1_scale is not None:
            self.texture1_scale = texture1_scale
        if texture1_offset is not None:
            self.texture1_offset = texture1_offset
        if albedo_color0 is not None:
            self.albedo_color0 = albedo_color0
        if albedo_color1 is not None:
            self.albedo_color1 = albedo_color1
        if albedo_texture0 is not None:
            self.albedo_texture0 = albedo_texture0
        if albedo_texture1 is not None:
            self.albedo_texture1 = albedo_texture1
        if emissive_color0 is not None:
            self.emissive_color0 = emissive_color0
        if emissive_color1 is not None:
            self.emissive_color1 = emissive_color1
        if emissive_map0 is not None:
            self.emissive_map0 = emissive_map0
        if emissive_map1 is not None:
            self.emissive_map1 = emissive_map1
        if normal_map0 is not None:
            self.normal_map0 = normal_map0
        if normal_map1 is not None:
            self.normal_map1 = normal_map1
        if normal_scale0 is not None:
            self.normal_scale0 = normal_scale0
        if normal_scale1 is not None:
            self.normal_scale1 = normal_scale1
        if multi_value is not None:
            self.multi_value = multi_value
        if occlusion_map0 is not None:
            self.occlusion_map0 = occlusion_map0
        if occlusion_map1 is not None:
            self.occlusion_map1 = occlusion_map1
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if zwrite is not None:
            self.zwrite = zwrite
        if ztest is not None:
            self.ztest = ztest
        if culling is not None:
            self.culling = culling
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if metallic0 is not None:
            self.metallic0 = metallic0
        if metallic1 is not None:
            self.metallic1 = metallic1
        if smoothness0 is not None:
            self.smoothness0 = smoothness0
        if smoothness1 is not None:
            self.smoothness1 = smoothness1
        if metallic_map0 is not None:
            self.metallic_map0 = metallic_map0
        if metallic_map1 is not None:
            self.metallic_map1 = metallic_map1

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
    def lerp(self) -> primitives.Float | None:
        """The Lerp field value."""
        member = self.get_member("Lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: primitives.Float) -> None:
        """Set the Lerp field value."""
        member = self.get_member("Lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Lerp", fields.FieldFloat(value=value)
            )

    @property
    def lerp_texture(self) -> str | None:
        """Target ID of the LerpTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("LerpTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lerp_texture.setter
    def lerp_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the LerpTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("LerpTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LerpTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def lerp_texture_scale(self) -> primitives.Float2 | None:
        """The LerpTextureScale field value."""
        member = self.get_member("LerpTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_texture_scale.setter
    def lerp_texture_scale(self, value: primitives.Float2) -> None:
        """Set the LerpTextureScale field value."""
        member = self.get_member("LerpTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def lerp_texture_offset(self) -> primitives.Float2 | None:
        """The LerpTextureOffset field value."""
        member = self.get_member("LerpTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_texture_offset.setter
    def lerp_texture_offset(self, value: primitives.Float2) -> None:
        """Set the LerpTextureOffset field value."""
        member = self.get_member("LerpTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def texture0_scale(self) -> primitives.Float2 | None:
        """The Texture0Scale field value."""
        member = self.get_member("Texture0Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture0_scale.setter
    def texture0_scale(self, value: primitives.Float2) -> None:
        """Set the Texture0Scale field value."""
        member = self.get_member("Texture0Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Texture0Scale", fields.FieldFloat2(value=value)
            )

    @property
    def texture0_offset(self) -> primitives.Float2 | None:
        """The Texture0Offset field value."""
        member = self.get_member("Texture0Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture0_offset.setter
    def texture0_offset(self, value: primitives.Float2) -> None:
        """Set the Texture0Offset field value."""
        member = self.get_member("Texture0Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Texture0Offset", fields.FieldFloat2(value=value)
            )

    @property
    def texture1_scale(self) -> primitives.Float2 | None:
        """The Texture1Scale field value."""
        member = self.get_member("Texture1Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture1_scale.setter
    def texture1_scale(self, value: primitives.Float2) -> None:
        """Set the Texture1Scale field value."""
        member = self.get_member("Texture1Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Texture1Scale", fields.FieldFloat2(value=value)
            )

    @property
    def texture1_offset(self) -> primitives.Float2 | None:
        """The Texture1Offset field value."""
        member = self.get_member("Texture1Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture1_offset.setter
    def texture1_offset(self, value: primitives.Float2) -> None:
        """Set the Texture1Offset field value."""
        member = self.get_member("Texture1Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Texture1Offset", fields.FieldFloat2(value=value)
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
    def normal_map0(self) -> str | None:
        """Target ID of the NormalMap0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NormalMap0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normal_map0.setter
    def normal_map0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NormalMap0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NormalMap0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalMap0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def normal_map1(self) -> str | None:
        """Target ID of the NormalMap1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NormalMap1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @normal_map1.setter
    def normal_map1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NormalMap1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NormalMap1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NormalMap1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def normal_scale0(self) -> primitives.Float | None:
        """The NormalScale0 field value."""
        member = self.get_member("NormalScale0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale0.setter
    def normal_scale0(self, value: primitives.Float) -> None:
        """Set the NormalScale0 field value."""
        member = self.get_member("NormalScale0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale0", fields.FieldFloat(value=value)
            )

    @property
    def normal_scale1(self) -> primitives.Float | None:
        """The NormalScale1 field value."""
        member = self.get_member("NormalScale1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_scale1.setter
    def normal_scale1(self, value: primitives.Float) -> None:
        """Set the NormalScale1 field value."""
        member = self.get_member("NormalScale1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalScale1", fields.FieldFloat(value=value)
            )

    @property
    def multi_value(self) -> primitives.Bool | None:
        """The MultiValue field value."""
        member = self.get_member("MultiValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multi_value.setter
    def multi_value(self, value: primitives.Bool) -> None:
        """Set the MultiValue field value."""
        member = self.get_member("MultiValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiValue", fields.FieldBool(value=value)
            )

    @property
    def occlusion_map0(self) -> str | None:
        """Target ID of the OcclusionMap0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OcclusionMap0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @occlusion_map0.setter
    def occlusion_map0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OcclusionMap0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OcclusionMap0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OcclusionMap0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def occlusion_map1(self) -> str | None:
        """Target ID of the OcclusionMap1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OcclusionMap1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @occlusion_map1.setter
    def occlusion_map1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OcclusionMap1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OcclusionMap1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OcclusionMap1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def blend_mode(self) -> BlendMode | None:
        """The BlendMode enum value."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BlendMode(member.value)
        return None

    @blend_mode.setter
    def blend_mode(self, value: BlendMode | str) -> None:
        """Set the BlendMode enum value."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BlendMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def alpha_cutoff(self) -> primitives.Float | None:
        """The AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_cutoff.setter
    def alpha_cutoff(self, value: primitives.Float) -> None:
        """Set the AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaCutoff", fields.FieldFloat(value=value)
            )

    @property
    def zwrite(self) -> ZWrite | None:
        """The ZWrite enum value."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ZWrite(member.value)
        return None

    @zwrite.setter
    def zwrite(self, value: ZWrite | str) -> None:
        """Set the ZWrite enum value."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ZWrite",
                members.FieldEnum(value=str(value)),
            )

    @property
    def ztest(self) -> ZTest | None:
        """The ZTest enum value."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ZTest(member.value)
        return None

    @ztest.setter
    def ztest(self, value: ZTest | str) -> None:
        """Set the ZTest enum value."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ZTest",
                members.FieldEnum(value=str(value)),
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
    def metallic0(self) -> primitives.Float | None:
        """The Metallic0 field value."""
        member = self.get_member("Metallic0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic0.setter
    def metallic0(self, value: primitives.Float) -> None:
        """Set the Metallic0 field value."""
        member = self.get_member("Metallic0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Metallic0", fields.FieldFloat(value=value)
            )

    @property
    def metallic1(self) -> primitives.Float | None:
        """The Metallic1 field value."""
        member = self.get_member("Metallic1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @metallic1.setter
    def metallic1(self, value: primitives.Float) -> None:
        """Set the Metallic1 field value."""
        member = self.get_member("Metallic1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Metallic1", fields.FieldFloat(value=value)
            )

    @property
    def smoothness0(self) -> primitives.Float | None:
        """The Smoothness0 field value."""
        member = self.get_member("Smoothness0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothness0.setter
    def smoothness0(self, value: primitives.Float) -> None:
        """Set the Smoothness0 field value."""
        member = self.get_member("Smoothness0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothness0", fields.FieldFloat(value=value)
            )

    @property
    def smoothness1(self) -> primitives.Float | None:
        """The Smoothness1 field value."""
        member = self.get_member("Smoothness1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothness1.setter
    def smoothness1(self, value: primitives.Float) -> None:
        """Set the Smoothness1 field value."""
        member = self.get_member("Smoothness1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothness1", fields.FieldFloat(value=value)
            )

    @property
    def metallic_map0(self) -> str | None:
        """Target ID of the MetallicMap0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MetallicMap0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @metallic_map0.setter
    def metallic_map0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MetallicMap0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MetallicMap0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MetallicMap0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def metallic_map1(self) -> str | None:
        """Target ID of the MetallicMap1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MetallicMap1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @metallic_map1.setter
    def metallic_map1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MetallicMap1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MetallicMap1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MetallicMap1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

