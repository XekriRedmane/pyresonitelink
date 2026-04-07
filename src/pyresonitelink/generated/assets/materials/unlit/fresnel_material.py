"""Generated component: FresnelMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture2_d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FresnelMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FresnelMaterial.

    Category: Assets/Materials/Unlit
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FresnelMaterial"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, exponent: np.float32 | None = None, gamma_curve: np.float32 | None = None, far_color: primitives.ColorX | None = None, near_color: primitives.ColorX | None = None, far_texture: str | IAssetProvider[ITexture2D] | None = None, near_texture: str | IAssetProvider[ITexture2D] | None = None, far_texture_scale: primitives.Float2 | None = None, far_texture_offset: primitives.Float2 | None = None, near_texture_scale: primitives.Float2 | None = None, near_texture_offset: primitives.Float2 | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_scale: np.float32 | None = None, use_vertex_colors: bool | None = None, alpha_cutoff: np.float32 | None = None, mask_texture: str | IAssetProvider[ITexture2D] | None = None, mask_scale: primitives.Float2 | None = None, mask_offset: primitives.Float2 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, polar_uvmapping: bool | None = None, polar_power: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            exponent: Initial value for Exponent.
            gamma_curve: Initial value for GammaCurve.
            far_color: Initial value for FarColor.
            near_color: Initial value for NearColor.
            far_texture: Initial value for FarTexture.
            near_texture: Initial value for NearTexture.
            far_texture_scale: Initial value for FarTextureScale.
            far_texture_offset: Initial value for FarTextureOffset.
            near_texture_scale: Initial value for NearTextureScale.
            near_texture_offset: Initial value for NearTextureOffset.
            normal_map: Initial value for NormalMap.
            normal_scale: Initial value for NormalScale.
            use_vertex_colors: Initial value for UseVertexColors.
            alpha_cutoff: Initial value for AlphaCutoff.
            mask_texture: Initial value for MaskTexture.
            mask_scale: Initial value for MaskScale.
            mask_offset: Initial value for MaskOffset.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            polar_uvmapping: Initial value for PolarUVmapping.
            polar_power: Initial value for PolarPower.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if exponent is not None:
            self.exponent = exponent
        if gamma_curve is not None:
            self.gamma_curve = gamma_curve
        if far_color is not None:
            self.far_color = far_color
        if near_color is not None:
            self.near_color = near_color
        if far_texture is not None:
            self.far_texture = far_texture
        if near_texture is not None:
            self.near_texture = near_texture
        if far_texture_scale is not None:
            self.far_texture_scale = far_texture_scale
        if far_texture_offset is not None:
            self.far_texture_offset = far_texture_offset
        if near_texture_scale is not None:
            self.near_texture_scale = near_texture_scale
        if near_texture_offset is not None:
            self.near_texture_offset = near_texture_offset
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_scale is not None:
            self.normal_scale = normal_scale
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if mask_texture is not None:
            self.mask_texture = mask_texture
        if mask_scale is not None:
            self.mask_scale = mask_scale
        if mask_offset is not None:
            self.mask_offset = mask_offset
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if polar_uvmapping is not None:
            self.polar_uvmapping = polar_uvmapping
        if polar_power is not None:
            self.polar_power = polar_power

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
    def exponent(self) -> np.float32 | None:
        """The Exponent field value."""
        member = self.get_member("Exponent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exponent.setter
    def exponent(self, value: np.float32) -> None:
        """Set the Exponent field value."""
        member = self.get_member("Exponent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exponent", fields.FieldFloat(value=value)
            )

    @property
    def gamma_curve(self) -> np.float32 | None:
        """The GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gamma_curve.setter
    def gamma_curve(self, value: np.float32) -> None:
        """Set the GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GammaCurve", fields.FieldFloat(value=value)
            )

    @property
    def far_color(self) -> primitives.ColorX | None:
        """The FarColor field value."""
        member = self.get_member("FarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_color.setter
    def far_color(self, value: primitives.ColorX) -> None:
        """Set the FarColor field value."""
        member = self.get_member("FarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarColor", fields.FieldColorX(value=value)
            )

    @property
    def near_color(self) -> primitives.ColorX | None:
        """The NearColor field value."""
        member = self.get_member("NearColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_color.setter
    def near_color(self, value: primitives.ColorX) -> None:
        """Set the NearColor field value."""
        member = self.get_member("NearColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearColor", fields.FieldColorX(value=value)
            )

    @property
    def far_texture(self) -> str | None:
        """Target ID of the FarTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FarTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @far_texture.setter
    def far_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FarTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FarTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FarTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def near_texture(self) -> str | None:
        """Target ID of the NearTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("NearTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @near_texture.setter
    def near_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the NearTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NearTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NearTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def far_texture_scale(self) -> primitives.Float2 | None:
        """The FarTextureScale field value."""
        member = self.get_member("FarTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_texture_scale.setter
    def far_texture_scale(self, value: primitives.Float2) -> None:
        """Set the FarTextureScale field value."""
        member = self.get_member("FarTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def far_texture_offset(self) -> primitives.Float2 | None:
        """The FarTextureOffset field value."""
        member = self.get_member("FarTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_texture_offset.setter
    def far_texture_offset(self, value: primitives.Float2) -> None:
        """Set the FarTextureOffset field value."""
        member = self.get_member("FarTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def near_texture_scale(self) -> primitives.Float2 | None:
        """The NearTextureScale field value."""
        member = self.get_member("NearTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_texture_scale.setter
    def near_texture_scale(self, value: primitives.Float2) -> None:
        """Set the NearTextureScale field value."""
        member = self.get_member("NearTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def near_texture_offset(self) -> primitives.Float2 | None:
        """The NearTextureOffset field value."""
        member = self.get_member("NearTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_texture_offset.setter
    def near_texture_offset(self, value: primitives.Float2) -> None:
        """Set the NearTextureOffset field value."""
        member = self.get_member("NearTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearTextureOffset", fields.FieldFloat2(value=value)
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
    def use_vertex_colors(self) -> bool | None:
        """The UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def vertex_color_interpolation_space(self) -> members.FieldEnum | None:
        """The VertexColorInterpolationSpace member."""
        member = self.get_member("VertexColorInterpolationSpace")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @vertex_color_interpolation_space.setter
    def vertex_color_interpolation_space(self, value: members.FieldEnum) -> None:
        """Set the VertexColorInterpolationSpace member."""
        self.set_member("VertexColorInterpolationSpace", value)

    @property
    def blend_mode(self) -> members.FieldEnum | None:
        """The BlendMode member."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @blend_mode.setter
    def blend_mode(self, value: members.FieldEnum) -> None:
        """Set the BlendMode member."""
        self.set_member("BlendMode", value)

    @property
    def alpha_cutoff(self) -> np.float32 | None:
        """The AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @alpha_cutoff.setter
    def alpha_cutoff(self, value: np.float32) -> None:
        """Set the AlphaCutoff field value."""
        member = self.get_member("AlphaCutoff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlphaCutoff", fields.FieldFloat(value=value)
            )

    @property
    def mask_texture(self) -> str | None:
        """Target ID of the MaskTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("MaskTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mask_texture.setter
    def mask_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the MaskTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MaskTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaskTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def mask_scale(self) -> primitives.Float2 | None:
        """The MaskScale field value."""
        member = self.get_member("MaskScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mask_scale.setter
    def mask_scale(self, value: primitives.Float2) -> None:
        """Set the MaskScale field value."""
        member = self.get_member("MaskScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaskScale", fields.FieldFloat2(value=value)
            )

    @property
    def mask_offset(self) -> primitives.Float2 | None:
        """The MaskOffset field value."""
        member = self.get_member("MaskOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mask_offset.setter
    def mask_offset(self, value: primitives.Float2) -> None:
        """Set the MaskOffset field value."""
        member = self.get_member("MaskOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaskOffset", fields.FieldFloat2(value=value)
            )

    @property
    def mask_mode(self) -> members.FieldEnum | None:
        """The MaskMode member."""
        member = self.get_member("MaskMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mask_mode.setter
    def mask_mode(self, value: members.FieldEnum) -> None:
        """Set the MaskMode member."""
        self.set_member("MaskMode", value)

    @property
    def sidedness(self) -> members.FieldEnum | None:
        """The Sidedness member."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sidedness.setter
    def sidedness(self, value: members.FieldEnum) -> None:
        """Set the Sidedness member."""
        self.set_member("Sidedness", value)

    @property
    def zwrite(self) -> members.FieldEnum | None:
        """The ZWrite member."""
        member = self.get_member("ZWrite")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @zwrite.setter
    def zwrite(self, value: members.FieldEnum) -> None:
        """Set the ZWrite member."""
        self.set_member("ZWrite", value)

    @property
    def ztest(self) -> members.FieldEnum | None:
        """The ZTest member."""
        member = self.get_member("ZTest")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ztest.setter
    def ztest(self, value: members.FieldEnum) -> None:
        """Set the ZTest member."""
        self.set_member("ZTest", value)

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
    def polar_uvmapping(self) -> bool | None:
        """The PolarUVmapping field value."""
        member = self.get_member("PolarUVmapping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @polar_uvmapping.setter
    def polar_uvmapping(self, value: bool) -> None:
        """Set the PolarUVmapping field value."""
        member = self.get_member("PolarUVmapping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PolarUVmapping", fields.FieldBool(value=value)
            )

    @property
    def polar_power(self) -> np.float32 | None:
        """The PolarPower field value."""
        member = self.get_member("PolarPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @polar_power.setter
    def polar_power(self, value: np.float32) -> None:
        """Set the PolarPower field value."""
        member = self.get_member("PolarPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PolarPower", fields.FieldFloat(value=value)
            )

