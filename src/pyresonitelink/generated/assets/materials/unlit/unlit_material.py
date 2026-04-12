"""Generated component: UnlitMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.mask_texture_mode import MaskTextureMode
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.generated._enums.sidedness import Sidedness
from pyresonitelink.generated._enums.zwrite import ZWrite
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.icommon_material import ICommonMaterial
from pyresonitelink.generated._types.istereo_material import IStereoMaterial
from pyresonitelink.generated._types.ibillboard_material import IBillboardMaterial
from pyresonitelink.generated._types.iblend_mode_material import IBlendModeMaterial
from pyresonitelink.generated._types.iculling_material import ICullingMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnlitMaterial(GeneratedComponent, ICommonMaterial, IStereoMaterial, IBillboardMaterial, IBlendModeMaterial, ICullingMaterial, ICustomInspector, IWorldEventReceiver):
    """The UnlitMaterial component is a material that can render meshes without lighting at full bright. Optionally can render each vertex like a square that faces the user or a direction. It can also optionally render differently depending on which eye it is viewed from. This is used in the left and right cat item, and for 3D photos.

    Category: Assets/Materials/Unlit

    Attach to a slot and use the material Component in the list of materials
    on a MeshRenderer or a SkinnedMeshRenderer with a mesh to view what this
    material looks like.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UnlitMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, tint_color: primitives.ColorX | None = None, texture: str | IAssetProvider[ITexture2D] | None = None, texture_scale: primitives.Float2 | None = None, texture_offset: primitives.Float2 | None = None, mask_texture: str | IAssetProvider[ITexture2D] | None = None, mask_scale: primitives.Float2 | None = None, mask_offset: primitives.Float2 | None = None, mask_mode: MaskTextureMode | str | None = None, blend_mode: BlendMode | str | None = None, alpha_cutoff: primitives.Float | None = None, use_vertex_colors: primitives.Bool | None = None, vertex_color_interpolation_space: ColorProfile | str | None = None, sidedness: Sidedness | str | None = None, zwrite: ZWrite | str | None = None, offset_texture: str | IAssetProvider[ITexture2D] | None = None, offset_magnitude: primitives.Float2 | None = None, offset_texture_scale: primitives.Float2 | None = None, offset_texture_offset: primitives.Float2 | None = None, polar_uvmapping: primitives.Bool | None = None, polar_power: primitives.Float | None = None, stereo_texture_transform: primitives.Bool | None = None, right_eye_texture_scale: primitives.Float2 | None = None, right_eye_texture_offset: primitives.Float2 | None = None, decode_as_normal_map: primitives.Bool | None = None, use_billboard_geometry: primitives.Bool | None = None, use_per_billboard_scale: primitives.Bool | None = None, use_per_billboard_rotation: primitives.Bool | None = None, use_per_billboard_uv: primitives.Bool | None = None, billboard_size: primitives.Float2 | None = None, offset_factor: primitives.Float | None = None, offset_units: primitives.Float | None = None, render_queue: primitives.Int | None = None, unlit: str | IAssetProvider[Shader] | None = None, unlit_billboard: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            tint_color: Initial value for TintColor.
            texture: Initial value for Texture.
            texture_scale: Initial value for TextureScale.
            texture_offset: Initial value for TextureOffset.
            mask_texture: Initial value for MaskTexture.
            mask_scale: Initial value for MaskScale.
            mask_offset: Initial value for MaskOffset.
            mask_mode: Initial value for MaskMode.
            blend_mode: Initial value for BlendMode.
            alpha_cutoff: Initial value for AlphaCutoff.
            use_vertex_colors: Initial value for UseVertexColors.
            vertex_color_interpolation_space: Initial value for VertexColorInterpolationSpace.
            sidedness: Initial value for Sidedness.
            zwrite: Initial value for ZWrite.
            offset_texture: Initial value for OffsetTexture.
            offset_magnitude: Initial value for OffsetMagnitude.
            offset_texture_scale: Initial value for OffsetTextureScale.
            offset_texture_offset: Initial value for OffsetTextureOffset.
            polar_uvmapping: Initial value for PolarUVmapping.
            polar_power: Initial value for PolarPower.
            stereo_texture_transform: Initial value for StereoTextureTransform.
            right_eye_texture_scale: Initial value for RightEyeTextureScale.
            right_eye_texture_offset: Initial value for RightEyeTextureOffset.
            decode_as_normal_map: Initial value for DecodeAsNormalMap.
            use_billboard_geometry: Initial value for UseBillboardGeometry.
            use_per_billboard_scale: Initial value for UsePerBillboardScale.
            use_per_billboard_rotation: Initial value for UsePerBillboardRotation.
            use_per_billboard_uv: Initial value for UsePerBillboardUV.
            billboard_size: Initial value for BillboardSize.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            unlit: Initial value for _unlit.
            unlit_billboard: Initial value for _unlitBillboard.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if tint_color is not None:
            self.tint_color = tint_color
        if texture is not None:
            self.texture = texture
        if texture_scale is not None:
            self.texture_scale = texture_scale
        if texture_offset is not None:
            self.texture_offset = texture_offset
        if mask_texture is not None:
            self.mask_texture = mask_texture
        if mask_scale is not None:
            self.mask_scale = mask_scale
        if mask_offset is not None:
            self.mask_offset = mask_offset
        if mask_mode is not None:
            self.mask_mode = mask_mode
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if alpha_cutoff is not None:
            self.alpha_cutoff = alpha_cutoff
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if vertex_color_interpolation_space is not None:
            self.vertex_color_interpolation_space = vertex_color_interpolation_space
        if sidedness is not None:
            self.sidedness = sidedness
        if zwrite is not None:
            self.zwrite = zwrite
        if offset_texture is not None:
            self.offset_texture = offset_texture
        if offset_magnitude is not None:
            self.offset_magnitude = offset_magnitude
        if offset_texture_scale is not None:
            self.offset_texture_scale = offset_texture_scale
        if offset_texture_offset is not None:
            self.offset_texture_offset = offset_texture_offset
        if polar_uvmapping is not None:
            self.polar_uvmapping = polar_uvmapping
        if polar_power is not None:
            self.polar_power = polar_power
        if stereo_texture_transform is not None:
            self.stereo_texture_transform = stereo_texture_transform
        if right_eye_texture_scale is not None:
            self.right_eye_texture_scale = right_eye_texture_scale
        if right_eye_texture_offset is not None:
            self.right_eye_texture_offset = right_eye_texture_offset
        if decode_as_normal_map is not None:
            self.decode_as_normal_map = decode_as_normal_map
        if use_billboard_geometry is not None:
            self.use_billboard_geometry = use_billboard_geometry
        if use_per_billboard_scale is not None:
            self.use_per_billboard_scale = use_per_billboard_scale
        if use_per_billboard_rotation is not None:
            self.use_per_billboard_rotation = use_per_billboard_rotation
        if use_per_billboard_uv is not None:
            self.use_per_billboard_uv = use_per_billboard_uv
        if billboard_size is not None:
            self.billboard_size = billboard_size
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if unlit is not None:
            self.unlit = unlit
        if unlit_billboard is not None:
            self.unlit_billboard = unlit_billboard

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
    def tint_color(self) -> primitives.ColorX | None:
        """The TintColor field value."""
        member = self.get_member("TintColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tint_color.setter
    def tint_color(self, value: primitives.ColorX) -> None:
        """Set the TintColor field value."""
        member = self.get_member("TintColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TintColor", fields.FieldColorX(value=value)
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
    def mask_mode(self) -> MaskTextureMode | None:
        """The MaskMode enum value."""
        member = self.get_member("MaskMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MaskTextureMode(member.value)
        return None

    @mask_mode.setter
    def mask_mode(self, value: MaskTextureMode | str) -> None:
        """Set the MaskMode enum value."""
        member = self.get_member("MaskMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MaskMode",
                members.FieldEnum(value=str(value)),
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
    def use_vertex_colors(self) -> primitives.Bool | None:
        """The UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: primitives.Bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def vertex_color_interpolation_space(self) -> ColorProfile | None:
        """The VertexColorInterpolationSpace enum value."""
        member = self.get_member("VertexColorInterpolationSpace")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @vertex_color_interpolation_space.setter
    def vertex_color_interpolation_space(self, value: ColorProfile | str) -> None:
        """Set the VertexColorInterpolationSpace enum value."""
        member = self.get_member("VertexColorInterpolationSpace")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "VertexColorInterpolationSpace",
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
    def polar_uvmapping(self) -> primitives.Bool | None:
        """The PolarUVmapping field value."""
        member = self.get_member("PolarUVmapping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @polar_uvmapping.setter
    def polar_uvmapping(self, value: primitives.Bool) -> None:
        """Set the PolarUVmapping field value."""
        member = self.get_member("PolarUVmapping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PolarUVmapping", fields.FieldBool(value=value)
            )

    @property
    def polar_power(self) -> primitives.Float | None:
        """The PolarPower field value."""
        member = self.get_member("PolarPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @polar_power.setter
    def polar_power(self, value: primitives.Float) -> None:
        """Set the PolarPower field value."""
        member = self.get_member("PolarPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PolarPower", fields.FieldFloat(value=value)
            )

    @property
    def stereo_texture_transform(self) -> primitives.Bool | None:
        """The StereoTextureTransform field value."""
        member = self.get_member("StereoTextureTransform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stereo_texture_transform.setter
    def stereo_texture_transform(self, value: primitives.Bool) -> None:
        """Set the StereoTextureTransform field value."""
        member = self.get_member("StereoTextureTransform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StereoTextureTransform", fields.FieldBool(value=value)
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
    def decode_as_normal_map(self) -> primitives.Bool | None:
        """The DecodeAsNormalMap field value."""
        member = self.get_member("DecodeAsNormalMap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @decode_as_normal_map.setter
    def decode_as_normal_map(self, value: primitives.Bool) -> None:
        """Set the DecodeAsNormalMap field value."""
        member = self.get_member("DecodeAsNormalMap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DecodeAsNormalMap", fields.FieldBool(value=value)
            )

    @property
    def use_billboard_geometry(self) -> primitives.Bool | None:
        """The UseBillboardGeometry field value."""
        member = self.get_member("UseBillboardGeometry")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_billboard_geometry.setter
    def use_billboard_geometry(self, value: primitives.Bool) -> None:
        """Set the UseBillboardGeometry field value."""
        member = self.get_member("UseBillboardGeometry")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseBillboardGeometry", fields.FieldBool(value=value)
            )

    @property
    def use_per_billboard_scale(self) -> primitives.Bool | None:
        """The UsePerBillboardScale field value."""
        member = self.get_member("UsePerBillboardScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_per_billboard_scale.setter
    def use_per_billboard_scale(self, value: primitives.Bool) -> None:
        """Set the UsePerBillboardScale field value."""
        member = self.get_member("UsePerBillboardScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsePerBillboardScale", fields.FieldBool(value=value)
            )

    @property
    def use_per_billboard_rotation(self) -> primitives.Bool | None:
        """The UsePerBillboardRotation field value."""
        member = self.get_member("UsePerBillboardRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_per_billboard_rotation.setter
    def use_per_billboard_rotation(self, value: primitives.Bool) -> None:
        """Set the UsePerBillboardRotation field value."""
        member = self.get_member("UsePerBillboardRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsePerBillboardRotation", fields.FieldBool(value=value)
            )

    @property
    def use_per_billboard_uv(self) -> primitives.Bool | None:
        """The UsePerBillboardUV field value."""
        member = self.get_member("UsePerBillboardUV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_per_billboard_uv.setter
    def use_per_billboard_uv(self, value: primitives.Bool) -> None:
        """Set the UsePerBillboardUV field value."""
        member = self.get_member("UsePerBillboardUV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsePerBillboardUV", fields.FieldBool(value=value)
            )

    @property
    def billboard_size(self) -> primitives.Float2 | None:
        """The BillboardSize field value."""
        member = self.get_member("BillboardSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @billboard_size.setter
    def billboard_size(self, value: primitives.Float2) -> None:
        """Set the BillboardSize field value."""
        member = self.get_member("BillboardSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BillboardSize", fields.FieldFloat2(value=value)
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
    def unlit(self) -> str | None:
        """Target ID of the _unlit reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_unlit")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unlit.setter
    def unlit(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _unlit reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_unlit")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unlit",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def unlit_billboard(self) -> str | None:
        """Target ID of the _unlitBillboard reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_unlitBillboard")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unlit_billboard.setter
    def unlit_billboard(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _unlitBillboard reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_unlitBillboard")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unlitBillboard",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

