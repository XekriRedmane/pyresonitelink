"""Generated component: Projection360Material."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.cubemap import Cubemap
from pyresonitelink.generated._types.istereo_material import IStereoMaterial
from pyresonitelink.generated._types.iskybox_material import ISkyboxMaterial
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Projection360Material(GeneratedComponent, IStereoMaterial, ISkyboxMaterial, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Projection360Material.

    Category: Assets/Materials/Unlit
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Projection360Material"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, texture: str | IAssetProvider[ITexture2D] | None = None, secondary_texture: str | IAssetProvider[ITexture2D] | None = None, cubemap: str | IAssetProvider[Cubemap] | None = None, secondary_cubemap: str | IAssetProvider[Cubemap] | None = None, cubemap_lod: np.float32 | None = None, texture_lerp: np.float32 | None = None, field_of_view: primitives.Float2 | None = None, angle_offset: primitives.Float2 | None = None, perspective_field_of_view: primitives.Float2 | None = None, perspective_angle_offset: primitives.Float2 | None = None, tint: primitives.ColorX | None = None, exposure: np.float32 | None = None, gamma: np.float32 | None = None, tint_texture: str | IAssetProvider[ITexture2D] | None = None, tint_texture_scale: primitives.Float2 | None = None, tint_texture_offset: primitives.Float2 | None = None, tint0: primitives.ColorX | None = None, tint1: primitives.ColorX | None = None, outside_color: primitives.ColorX | None = None, texture_offset: primitives.Float2 | None = None, texture_scale: primitives.Float2 | None = None, stereo_texture_transform: bool | None = None, right_eye_texture_offset: primitives.Float2 | None = None, right_eye_texture_scale: primitives.Float2 | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, max_intensity: np.float32 | None = None, rect: primitives.Rect | None = None, rect_clip: bool | None = None, offset_texture: str | IAssetProvider[ITexture2D] | None = None, offset_mask: str | IAssetProvider[ITexture2D] | None = None, offset_texture_offset: primitives.Float2 | None = None, offset_texture_scale: primitives.Float2 | None = None, offset_magnitude: primitives.Float2 | None = None, stencil_id: np.uint8 | None = None, stencil_write_mask: np.uint8 | None = None, stencil_read_mask: np.uint8 | None = None, render_queue: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            texture: Initial value for Texture.
            secondary_texture: Initial value for SecondaryTexture.
            cubemap: Initial value for Cubemap.
            secondary_cubemap: Initial value for SecondaryCubemap.
            cubemap_lod: Initial value for CubemapLOD.
            texture_lerp: Initial value for TextureLerp.
            field_of_view: Initial value for FieldOfView.
            angle_offset: Initial value for AngleOffset.
            perspective_field_of_view: Initial value for PerspectiveFieldOfView.
            perspective_angle_offset: Initial value for PerspectiveAngleOffset.
            tint: Initial value for Tint.
            exposure: Initial value for Exposure.
            gamma: Initial value for Gamma.
            tint_texture: Initial value for TintTexture.
            tint_texture_scale: Initial value for TintTextureScale.
            tint_texture_offset: Initial value for TintTextureOffset.
            tint0: Initial value for Tint0.
            tint1: Initial value for Tint1.
            outside_color: Initial value for OutsideColor.
            texture_offset: Initial value for TextureOffset.
            texture_scale: Initial value for TextureScale.
            stereo_texture_transform: Initial value for StereoTextureTransform.
            right_eye_texture_offset: Initial value for RightEyeTextureOffset.
            right_eye_texture_scale: Initial value for RightEyeTextureScale.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            max_intensity: Initial value for MaxIntensity.
            rect: Initial value for Rect.
            rect_clip: Initial value for RectClip.
            offset_texture: Initial value for OffsetTexture.
            offset_mask: Initial value for OffsetMask.
            offset_texture_offset: Initial value for OffsetTextureOffset.
            offset_texture_scale: Initial value for OffsetTextureScale.
            offset_magnitude: Initial value for OffsetMagnitude.
            stencil_id: Initial value for StencilID.
            stencil_write_mask: Initial value for StencilWriteMask.
            stencil_read_mask: Initial value for StencilReadMask.
            render_queue: Initial value for RenderQueue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if texture is not None:
            self.texture = texture
        if secondary_texture is not None:
            self.secondary_texture = secondary_texture
        if cubemap is not None:
            self.cubemap = cubemap
        if secondary_cubemap is not None:
            self.secondary_cubemap = secondary_cubemap
        if cubemap_lod is not None:
            self.cubemap_lod = cubemap_lod
        if texture_lerp is not None:
            self.texture_lerp = texture_lerp
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if angle_offset is not None:
            self.angle_offset = angle_offset
        if perspective_field_of_view is not None:
            self.perspective_field_of_view = perspective_field_of_view
        if perspective_angle_offset is not None:
            self.perspective_angle_offset = perspective_angle_offset
        if tint is not None:
            self.tint = tint
        if exposure is not None:
            self.exposure = exposure
        if gamma is not None:
            self.gamma = gamma
        if tint_texture is not None:
            self.tint_texture = tint_texture
        if tint_texture_scale is not None:
            self.tint_texture_scale = tint_texture_scale
        if tint_texture_offset is not None:
            self.tint_texture_offset = tint_texture_offset
        if tint0 is not None:
            self.tint0 = tint0
        if tint1 is not None:
            self.tint1 = tint1
        if outside_color is not None:
            self.outside_color = outside_color
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if stereo_texture_transform is not None:
            self.stereo_texture_transform = stereo_texture_transform
        if right_eye_texture_offset is not None:
            self.right_eye_texture_offset = right_eye_texture_offset
        if right_eye_texture_scale is not None:
            self.right_eye_texture_scale = right_eye_texture_scale
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if max_intensity is not None:
            self.max_intensity = max_intensity
        if rect is not None:
            self.rect = rect
        if rect_clip is not None:
            self.rect_clip = rect_clip
        if offset_texture is not None:
            self.offset_texture = offset_texture
        if offset_mask is not None:
            self.offset_mask = offset_mask
        if offset_texture_offset is not None:
            self.offset_texture_offset = offset_texture_offset
        if offset_texture_scale is not None:
            self.offset_texture_scale = offset_texture_scale
        if offset_magnitude is not None:
            self.offset_magnitude = offset_magnitude
        if stencil_id is not None:
            self.stencil_id = stencil_id
        if stencil_write_mask is not None:
            self.stencil_write_mask = stencil_write_mask
        if stencil_read_mask is not None:
            self.stencil_read_mask = stencil_read_mask
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
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def secondary_texture(self) -> str | None:
        """Target ID of the SecondaryTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SecondaryTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_texture.setter
    def secondary_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SecondaryTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def cubemap(self) -> str | None:
        """Target ID of the Cubemap reference (targets IAssetProvider[Cubemap])."""
        member = self.get_member("Cubemap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cubemap.setter
    def cubemap(self, target: str | IAssetProvider[Cubemap] | None) -> None:
        """Set the Cubemap reference by target ID or IAssetProvider[Cubemap] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Cubemap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Cubemap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Cubemap>'),
            )

    @property
    def secondary_cubemap(self) -> str | None:
        """Target ID of the SecondaryCubemap reference (targets IAssetProvider[Cubemap])."""
        member = self.get_member("SecondaryCubemap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_cubemap.setter
    def secondary_cubemap(self, target: str | IAssetProvider[Cubemap] | None) -> None:
        """Set the SecondaryCubemap reference by target ID or IAssetProvider[Cubemap] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryCubemap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryCubemap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Cubemap>'),
            )

    @property
    def cubemap_lod(self) -> np.float32 | None:
        """The CubemapLOD field value."""
        member = self.get_member("CubemapLOD")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cubemap_lod.setter
    def cubemap_lod(self, value: np.float32) -> None:
        """Set the CubemapLOD field value."""
        member = self.get_member("CubemapLOD")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CubemapLOD", fields.FieldNullableFloat(value=value)
            )

    @property
    def texture_lerp(self) -> np.float32 | None:
        """The TextureLerp field value."""
        member = self.get_member("TextureLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @texture_lerp.setter
    def texture_lerp(self, value: np.float32) -> None:
        """Set the TextureLerp field value."""
        member = self.get_member("TextureLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TextureLerp", fields.FieldFloat(value=value)
            )

    @property
    def projection(self) -> members.FieldEnum | None:
        """The Projection member."""
        member = self.get_member("Projection")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @projection.setter
    def projection(self, value: members.FieldEnum) -> None:
        """Set the Projection member."""
        self.set_member("Projection", value)

    @property
    def field_of_view(self) -> primitives.Float2 | None:
        """The FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: primitives.Float2) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat2(value=value)
            )

    @property
    def angle_offset(self) -> primitives.Float2 | None:
        """The AngleOffset field value."""
        member = self.get_member("AngleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_offset.setter
    def angle_offset(self, value: primitives.Float2) -> None:
        """Set the AngleOffset field value."""
        member = self.get_member("AngleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngleOffset", fields.FieldFloat2(value=value)
            )

    @property
    def perspective_field_of_view(self) -> primitives.Float2 | None:
        """The PerspectiveFieldOfView field value."""
        member = self.get_member("PerspectiveFieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @perspective_field_of_view.setter
    def perspective_field_of_view(self, value: primitives.Float2) -> None:
        """Set the PerspectiveFieldOfView field value."""
        member = self.get_member("PerspectiveFieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerspectiveFieldOfView", fields.FieldFloat2(value=value)
            )

    @property
    def perspective_angle_offset(self) -> primitives.Float2 | None:
        """The PerspectiveAngleOffset field value."""
        member = self.get_member("PerspectiveAngleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @perspective_angle_offset.setter
    def perspective_angle_offset(self, value: primitives.Float2) -> None:
        """Set the PerspectiveAngleOffset field value."""
        member = self.get_member("PerspectiveAngleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerspectiveAngleOffset", fields.FieldFloat2(value=value)
            )

    @property
    def tint(self) -> primitives.ColorX | None:
        """The Tint field value."""
        member = self.get_member("Tint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint.setter
    def tint(self, value: primitives.ColorX) -> None:
        """Set the Tint field value."""
        member = self.get_member("Tint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tint", fields.FieldColorX(value=value)
            )

    @property
    def exposure(self) -> np.float32 | None:
        """The Exposure field value."""
        member = self.get_member("Exposure")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exposure.setter
    def exposure(self, value: np.float32) -> None:
        """Set the Exposure field value."""
        member = self.get_member("Exposure")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exposure", fields.FieldFloat(value=value)
            )

    @property
    def gamma(self) -> np.float32 | None:
        """The Gamma field value."""
        member = self.get_member("Gamma")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gamma.setter
    def gamma(self, value: np.float32) -> None:
        """Set the Gamma field value."""
        member = self.get_member("Gamma")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gamma", fields.FieldFloat(value=value)
            )

    @property
    def tint_texture(self) -> str | None:
        """Target ID of the TintTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("TintTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tint_texture.setter
    def tint_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the TintTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("TintTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TintTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def tint_texture_scale(self) -> primitives.Float2 | None:
        """The TintTextureScale field value."""
        member = self.get_member("TintTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_texture_scale.setter
    def tint_texture_scale(self, value: primitives.Float2) -> None:
        """Set the TintTextureScale field value."""
        member = self.get_member("TintTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def tint_texture_offset(self) -> primitives.Float2 | None:
        """The TintTextureOffset field value."""
        member = self.get_member("TintTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_texture_offset.setter
    def tint_texture_offset(self, value: primitives.Float2) -> None:
        """Set the TintTextureOffset field value."""
        member = self.get_member("TintTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def tint_texture_mode(self) -> members.FieldEnum | None:
        """The TintTextureMode member."""
        member = self.get_member("TintTextureMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @tint_texture_mode.setter
    def tint_texture_mode(self, value: members.FieldEnum) -> None:
        """Set the TintTextureMode member."""
        self.set_member("TintTextureMode", value)

    @property
    def tint0(self) -> primitives.ColorX | None:
        """The Tint0 field value."""
        member = self.get_member("Tint0")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint0.setter
    def tint0(self, value: primitives.ColorX) -> None:
        """Set the Tint0 field value."""
        member = self.get_member("Tint0")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tint0", fields.FieldColorX(value=value)
            )

    @property
    def tint1(self) -> primitives.ColorX | None:
        """The Tint1 field value."""
        member = self.get_member("Tint1")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint1.setter
    def tint1(self, value: primitives.ColorX) -> None:
        """Set the Tint1 field value."""
        member = self.get_member("Tint1")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tint1", fields.FieldColorX(value=value)
            )

    @property
    def outside_mode(self) -> members.FieldEnum | None:
        """The OutsideMode member."""
        member = self.get_member("OutsideMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @outside_mode.setter
    def outside_mode(self, value: members.FieldEnum) -> None:
        """Set the OutsideMode member."""
        self.set_member("OutsideMode", value)

    @property
    def outside_color(self) -> primitives.ColorX | None:
        """The OutsideColor field value."""
        member = self.get_member("OutsideColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @outside_color.setter
    def outside_color(self, value: primitives.ColorX) -> None:
        """Set the OutsideColor field value."""
        member = self.get_member("OutsideColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OutsideColor", fields.FieldColorX(value=value)
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
    def stereo_texture_transform(self) -> bool | None:
        """The StereoTextureTransform field value."""
        member = self.get_member("StereoTextureTransform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stereo_texture_transform.setter
    def stereo_texture_transform(self, value: bool) -> None:
        """Set the StereoTextureTransform field value."""
        member = self.get_member("StereoTextureTransform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StereoTextureTransform", fields.FieldBool(value=value)
            )

    @property
    def right_eye_texture_offset(self) -> primitives.Float2 | None:
        """The RightEyeTextureOffset field value."""
        member = self.get_member("RightEyeTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_texture_offset.setter
    def right_eye_texture_offset(self, value: primitives.Float2) -> None:
        """Set the RightEyeTextureOffset field value."""
        member = self.get_member("RightEyeTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def right_eye_texture_scale(self) -> primitives.Float2 | None:
        """The RightEyeTextureScale field value."""
        member = self.get_member("RightEyeTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_texture_scale.setter
    def right_eye_texture_scale(self, value: primitives.Float2) -> None:
        """Set the RightEyeTextureScale field value."""
        member = self.get_member("RightEyeTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeTextureScale", fields.FieldFloat2(value=value)
            )

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
    def max_intensity(self) -> np.float32 | None:
        """The MaxIntensity field value."""
        member = self.get_member("MaxIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_intensity.setter
    def max_intensity(self, value: np.float32) -> None:
        """Set the MaxIntensity field value."""
        member = self.get_member("MaxIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxIntensity", fields.FieldNullableFloat(value=value)
            )

    @property
    def rect(self) -> primitives.Rect | None:
        """The Rect field value."""
        member = self.get_member("Rect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect.setter
    def rect(self, value: primitives.Rect) -> None:
        """Set the Rect field value."""
        member = self.get_member("Rect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rect", fields.FieldRect(value=value)
            )

    @property
    def rect_clip(self) -> bool | None:
        """The RectClip field value."""
        member = self.get_member("RectClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect_clip.setter
    def rect_clip(self, value: bool) -> None:
        """Set the RectClip field value."""
        member = self.get_member("RectClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RectClip", fields.FieldBool(value=value)
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
    def offset_texture(self) -> str | None:
        """Target ID of the OffsetTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OffsetTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset_texture.setter
    def offset_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OffsetTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OffsetTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OffsetTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def offset_mask(self) -> str | None:
        """Target ID of the OffsetMask reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("OffsetMask")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @offset_mask.setter
    def offset_mask(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the OffsetMask reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("OffsetMask")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OffsetMask",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def offset_texture_offset(self) -> primitives.Float2 | None:
        """The OffsetTextureOffset field value."""
        member = self.get_member("OffsetTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_texture_offset.setter
    def offset_texture_offset(self, value: primitives.Float2) -> None:
        """Set the OffsetTextureOffset field value."""
        member = self.get_member("OffsetTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def offset_texture_scale(self) -> primitives.Float2 | None:
        """The OffsetTextureScale field value."""
        member = self.get_member("OffsetTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_texture_scale.setter
    def offset_texture_scale(self, value: primitives.Float2) -> None:
        """Set the OffsetTextureScale field value."""
        member = self.get_member("OffsetTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def offset_magnitude(self) -> primitives.Float2 | None:
        """The OffsetMagnitude field value."""
        member = self.get_member("OffsetMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset_magnitude.setter
    def offset_magnitude(self, value: primitives.Float2) -> None:
        """Set the OffsetMagnitude field value."""
        member = self.get_member("OffsetMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OffsetMagnitude", fields.FieldFloat2(value=value)
            )

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

