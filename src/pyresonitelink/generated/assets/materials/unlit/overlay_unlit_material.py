"""Generated component: OverlayUnlitMaterial."""

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


class OverlayUnlitMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.OverlayUnlitMaterial.

    Category: Assets/Materials/Unlit
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OverlayUnlitMaterial"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, behind_tint_color: primitives.ColorX | None = None, front_tint_color: primitives.ColorX | None = None, behind_texture: str | IAssetProvider[ITexture2D] | None = None, behind_texture_scale: primitives.Float2 | None = None, behind_texture_offset: primitives.Float2 | None = None, front_texture: str | IAssetProvider[ITexture2D] | None = None, front_texture_scale: primitives.Float2 | None = None, front_texture_offset: primitives.Float2 | None = None, alpha_cutoff: np.float32 | None = None, use_vertex_colors: bool | None = None, polar_uvmapping: bool | None = None, polar_power: np.float32 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            behind_tint_color: Initial value for BehindTintColor.
            front_tint_color: Initial value for FrontTintColor.
            behind_texture: Initial value for BehindTexture.
            behind_texture_scale: Initial value for BehindTextureScale.
            behind_texture_offset: Initial value for BehindTextureOffset.
            front_texture: Initial value for FrontTexture.
            front_texture_scale: Initial value for FrontTextureScale.
            front_texture_offset: Initial value for FrontTextureOffset.
            alpha_cutoff: Initial value for AlphaCutoff.
            use_vertex_colors: Initial value for UseVertexColors.
            polar_uvmapping: Initial value for PolarUVmapping.
            polar_power: Initial value for PolarPower.
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
        if behind_tint_color is not None:
            self.behind_tint_color = behind_tint_color
        if front_tint_color is not None:
            self.front_tint_color = front_tint_color
        if behind_texture is not None:
            self.behind_texture = behind_texture
        if behind_texture_scale is not None:
            self.behind_texture_scale = behind_texture_scale
        if behind_texture_offset is not None:
            self.behind_texture_offset = behind_texture_offset
        if front_texture is not None:
            self.front_texture = front_texture
        if front_texture_scale is not None:
            self.front_texture_scale = front_texture_scale
        if front_texture_offset is not None:
            self.front_texture_offset = front_texture_offset
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if polar_uvmapping is not None:
            self.polar_uvmapping = polar_uvmapping
        if polar_power is not None:
            self.polar_power = polar_power
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue

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
    def behind_tint_color(self) -> primitives.ColorX | None:
        """The BehindTintColor field value."""
        member = self.get_member("BehindTintColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_tint_color.setter
    def behind_tint_color(self, value: primitives.ColorX) -> None:
        """Set the BehindTintColor field value."""
        member = self.get_member("BehindTintColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindTintColor", fields.FieldColorX(value=value)
            )

    @property
    def front_tint_color(self) -> primitives.ColorX | None:
        """The FrontTintColor field value."""
        member = self.get_member("FrontTintColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_tint_color.setter
    def front_tint_color(self, value: primitives.ColorX) -> None:
        """Set the FrontTintColor field value."""
        member = self.get_member("FrontTintColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontTintColor", fields.FieldColorX(value=value)
            )

    @property
    def behind_texture(self) -> str | None:
        """Target ID of the BehindTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("BehindTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @behind_texture.setter
    def behind_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the BehindTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("BehindTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BehindTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def behind_texture_scale(self) -> primitives.Float2 | None:
        """The BehindTextureScale field value."""
        member = self.get_member("BehindTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_texture_scale.setter
    def behind_texture_scale(self, value: primitives.Float2) -> None:
        """Set the BehindTextureScale field value."""
        member = self.get_member("BehindTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def behind_texture_offset(self) -> primitives.Float2 | None:
        """The BehindTextureOffset field value."""
        member = self.get_member("BehindTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @behind_texture_offset.setter
    def behind_texture_offset(self, value: primitives.Float2) -> None:
        """Set the BehindTextureOffset field value."""
        member = self.get_member("BehindTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BehindTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def front_texture(self) -> str | None:
        """Target ID of the FrontTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("FrontTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @front_texture.setter
    def front_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the FrontTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("FrontTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FrontTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def front_texture_scale(self) -> primitives.Float2 | None:
        """The FrontTextureScale field value."""
        member = self.get_member("FrontTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_texture_scale.setter
    def front_texture_scale(self, value: primitives.Float2) -> None:
        """Set the FrontTextureScale field value."""
        member = self.get_member("FrontTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def front_texture_offset(self) -> primitives.Float2 | None:
        """The FrontTextureOffset field value."""
        member = self.get_member("FrontTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @front_texture_offset.setter
    def front_texture_offset(self, value: primitives.Float2) -> None:
        """Set the FrontTextureOffset field value."""
        member = self.get_member("FrontTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrontTextureOffset", fields.FieldFloat2(value=value)
            )

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

