"""Generated component: FresnelLerpMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.generated._enums.sidedness import Sidedness
from pyresonitelink.generated._enums.zwrite import ZWrite
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FresnelLerpMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The FresnelLerpMaterial component is a material that can be used to make a fresnel effect that can be lerped between two different preset frensel settings.

Far on this material is the geometry facing away from the camera and near is the geometry facing towards the camera.

    Category: Assets/Materials/Unlit

    Attach to a slot and put into the materials of a renderer like a
    SkinnedMeshRenderer or a MeshRenderer with a mesh to view what the
    material looks like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FresnelLerpMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, lerp: primitives.Float | None = None, lerp_texture: str | IAssetProvider[ITexture2D] | None = None, lerp_texture_scale: primitives.Float2 | None = None, lerp_texture_offset: primitives.Float2 | None = None, lerp_texture_polar_uv: primitives.Bool | None = None, lerp_texture_polar_power: primitives.Float | None = None, exponent0: primitives.Float | None = None, exponent1: primitives.Float | None = None, gamma_curve: primitives.Float | None = None, far_color0: primitives.ColorX | None = None, near_color0: primitives.ColorX | None = None, far_color1: primitives.ColorX | None = None, near_color1: primitives.ColorX | None = None, far_texture0: str | IAssetProvider[ITexture2D] | None = None, near_texture0: str | IAssetProvider[ITexture2D] | None = None, far_texture1: str | IAssetProvider[ITexture2D] | None = None, near_texture1: str | IAssetProvider[ITexture2D] | None = None, normal_map0: str | IAssetProvider[ITexture2D] | None = None, normal_map1: str | IAssetProvider[ITexture2D] | None = None, blend_mode: BlendMode | str | None = None, sidedness: Sidedness | str | None = None, zwrite: ZWrite | str | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            lerp: Initial value for Lerp.
            lerp_texture: Initial value for LerpTexture.
            lerp_texture_scale: Initial value for LerpTextureScale.
            lerp_texture_offset: Initial value for LerpTextureOffset.
            lerp_texture_polar_uv: Initial value for LerpTexturePolarUV.
            lerp_texture_polar_power: Initial value for LerpTexturePolarPower.
            exponent0: Initial value for Exponent0.
            exponent1: Initial value for Exponent1.
            gamma_curve: Initial value for GammaCurve.
            far_color0: Initial value for FarColor0.
            near_color0: Initial value for NearColor0.
            far_color1: Initial value for FarColor1.
            near_color1: Initial value for NearColor1.
            far_texture0: Initial value for FarTexture0.
            near_texture0: Initial value for NearTexture0.
            far_texture1: Initial value for FarTexture1.
            near_texture1: Initial value for NearTexture1.
            normal_map0: Initial value for NormalMap0.
            normal_map1: Initial value for NormalMap1.
            blend_mode: Initial value for BlendMode.
            sidedness: Initial value for Sidedness.
            zwrite: Initial value for ZWrite.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
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
        if lerp_texture_polar_uv is not None:
            self.lerp_texture_polar_uv = lerp_texture_polar_uv
        if lerp_texture_polar_power is not None:
            self.lerp_texture_polar_power = lerp_texture_polar_power
        if exponent0 is not None:
            self.exponent0 = exponent0
        if exponent1 is not None:
            self.exponent1 = exponent1
        if gamma_curve is not None:
            self.gamma_curve = gamma_curve
        if far_color0 is not None:
            self.far_color0 = far_color0
        if near_color0 is not None:
            self.near_color0 = near_color0
        if far_color1 is not None:
            self.far_color1 = far_color1
        if near_color1 is not None:
            self.near_color1 = near_color1
        if far_texture0 is not None:
            self.far_texture0 = far_texture0
        if near_texture0 is not None:
            self.near_texture0 = near_texture0
        if far_texture1 is not None:
            self.far_texture1 = far_texture1
        if near_texture1 is not None:
            self.near_texture1 = near_texture1
        if normal_map0 is not None:
            self.normal_map0 = normal_map0
        if normal_map1 is not None:
            self.normal_map1 = normal_map1
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if sidedness is not None:
            self.sidedness = sidedness
        if zwrite is not None:
            self.zwrite = zwrite
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue

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
    def lerp_texture_polar_uv(self) -> primitives.Bool | None:
        """The LerpTexturePolarUV field value."""
        member = self.get_member("LerpTexturePolarUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_texture_polar_uv.setter
    def lerp_texture_polar_uv(self, value: primitives.Bool) -> None:
        """Set the LerpTexturePolarUV field value."""
        member = self.get_member("LerpTexturePolarUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpTexturePolarUV", fields.FieldBool(value=value)
            )

    @property
    def lerp_texture_polar_power(self) -> primitives.Float | None:
        """The LerpTexturePolarPower field value."""
        member = self.get_member("LerpTexturePolarPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp_texture_polar_power.setter
    def lerp_texture_polar_power(self, value: primitives.Float) -> None:
        """Set the LerpTexturePolarPower field value."""
        member = self.get_member("LerpTexturePolarPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LerpTexturePolarPower", fields.FieldFloat(value=value)
            )

    @property
    def exponent0(self) -> primitives.Float | None:
        """The Exponent0 field value."""
        member = self.get_member("Exponent0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exponent0.setter
    def exponent0(self, value: primitives.Float) -> None:
        """Set the Exponent0 field value."""
        member = self.get_member("Exponent0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exponent0", fields.FieldFloat(value=value)
            )

    @property
    def exponent1(self) -> primitives.Float | None:
        """The Exponent1 field value."""
        member = self.get_member("Exponent1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exponent1.setter
    def exponent1(self, value: primitives.Float) -> None:
        """Set the Exponent1 field value."""
        member = self.get_member("Exponent1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exponent1", fields.FieldFloat(value=value)
            )

    @property
    def gamma_curve(self) -> primitives.Float | None:
        """The GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gamma_curve.setter
    def gamma_curve(self, value: primitives.Float) -> None:
        """Set the GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GammaCurve", fields.FieldFloat(value=value)
            )

    @property
    def far_color0(self) -> primitives.ColorX | None:
        """The FarColor0 field value."""
        member = self.get_member("FarColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_color0.setter
    def far_color0(self, value: primitives.ColorX) -> None:
        """Set the FarColor0 field value."""
        member = self.get_member("FarColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarColor0", fields.FieldColorX(value=value)
            )

    @property
    def near_color0(self) -> primitives.ColorX | None:
        """The NearColor0 field value."""
        member = self.get_member("NearColor0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_color0.setter
    def near_color0(self, value: primitives.ColorX) -> None:
        """Set the NearColor0 field value."""
        member = self.get_member("NearColor0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearColor0", fields.FieldColorX(value=value)
            )

    @property
    def far_color1(self) -> primitives.ColorX | None:
        """The FarColor1 field value."""
        member = self.get_member("FarColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_color1.setter
    def far_color1(self, value: primitives.ColorX) -> None:
        """Set the FarColor1 field value."""
        member = self.get_member("FarColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarColor1", fields.FieldColorX(value=value)
            )

    @property
    def near_color1(self) -> primitives.ColorX | None:
        """The NearColor1 field value."""
        member = self.get_member("NearColor1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_color1.setter
    def near_color1(self, value: primitives.ColorX) -> None:
        """Set the NearColor1 field value."""
        member = self.get_member("NearColor1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearColor1", fields.FieldColorX(value=value)
            )

    @property
    def far_texture0(self) -> str | None:
        """Target ID of the FarTexture0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FarTexture0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @far_texture0.setter
    def far_texture0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FarTexture0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FarTexture0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FarTexture0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def near_texture0(self) -> str | None:
        """Target ID of the NearTexture0 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NearTexture0")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @near_texture0.setter
    def near_texture0(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NearTexture0 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NearTexture0")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NearTexture0",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def far_texture1(self) -> str | None:
        """Target ID of the FarTexture1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FarTexture1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @far_texture1.setter
    def far_texture1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FarTexture1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FarTexture1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FarTexture1",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def near_texture1(self) -> str | None:
        """Target ID of the NearTexture1 reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NearTexture1")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @near_texture1.setter
    def near_texture1(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NearTexture1 reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NearTexture1")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NearTexture1",
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
    def sidedness(self) -> Sidedness | None:
        """The Sidedness enum value."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Sidedness(member.value)
        return None

    @sidedness.setter
    def sidedness(self, value: Sidedness | str) -> None:
        """Set the Sidedness enum value."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Sidedness",
                members.FieldEnum(value=str(value)),
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

