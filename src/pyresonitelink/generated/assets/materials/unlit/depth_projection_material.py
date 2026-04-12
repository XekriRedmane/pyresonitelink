"""Generated component: DepthProjectionMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.depth_encoding import DepthEncoding
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.generated._enums.zwrite import ZWrite
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DepthProjectionMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The DepthProjectionMaterial is commonly used when importing depth videos and acts as a material that displaces vertices in 3D.

    Category: Assets/Materials/Unlit

    The material uses a file that has a greyscale video (representing depth
    at each pixel) and a normal color video in order to "overlay" the color
    info on top of the 3D distortion created by the greyscale input. There
    are texture2D slots for depth and color, meaning two separate files
    could be used given the DepthTextureOffset property is set to 0.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DepthProjectionMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, color: str | IAssetProvider[ITexture2D] | None = None, depth: str | IAssetProvider[ITexture2D] | None = None, depth_encoding: DepthEncoding | str | None = None, color_texture_offset: primitives.Float2 | None = None, color_texture_scale: primitives.Float2 | None = None, depth_texture_offset: primitives.Float2 | None = None, depth_texture_scale: primitives.Float2 | None = None, depth_from: primitives.Float | None = None, depth_to: primitives.Float | None = None, field_of_view: primitives.Float2 | None = None, near_clip: primitives.Float | None = None, far_clip: primitives.Float | None = None, discard_threshold: primitives.Float | None = None, discard_offset: primitives.Float | None = None, blend_mode: BlendMode | str | None = None, zwrite: ZWrite | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            color: Initial value for Color.
            depth: Initial value for Depth.
            depth_encoding: Initial value for DepthEncoding.
            color_texture_offset: Initial value for ColorTextureOffset.
            color_texture_scale: Initial value for ColorTextureScale.
            depth_texture_offset: Initial value for DepthTextureOffset.
            depth_texture_scale: Initial value for DepthTextureScale.
            depth_from: Initial value for DepthFrom.
            depth_to: Initial value for DepthTo.
            field_of_view: Initial value for FieldOfView.
            near_clip: Initial value for NearClip.
            far_clip: Initial value for FarClip.
            discard_threshold: Initial value for DiscardThreshold.
            discard_offset: Initial value for DiscardOffset.
            blend_mode: Initial value for BlendMode.
            zwrite: Initial value for ZWrite.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if color is not None:
            self.color = color
        if depth is not None:
            self.depth = depth
        if depth_encoding is not None:
            self.depth_encoding = depth_encoding
        if color_texture_offset is not None:
            self.color_texture_offset = color_texture_offset
        if color_texture_scale is not None:
            self.color_texture_scale = color_texture_scale
        if depth_texture_offset is not None:
            self.depth_texture_offset = depth_texture_offset
        if depth_texture_scale is not None:
            self.depth_texture_scale = depth_texture_scale
        if depth_from is not None:
            self.depth_from = depth_from
        if depth_to is not None:
            self.depth_to = depth_to
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if near_clip is not None:
            self.near_clip = near_clip
        if far_clip is not None:
            self.far_clip = far_clip
        if discard_threshold is not None:
            self.discard_threshold = discard_threshold
        if discard_offset is not None:
            self.discard_offset = discard_offset
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if zwrite is not None:
            self.zwrite = zwrite

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
    def color(self) -> str | None:
        """Target ID of the Color reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color.setter
    def color(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Color reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Color")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Color",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def depth(self) -> str | None:
        """Target ID of the Depth reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Depth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @depth.setter
    def depth(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Depth reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Depth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Depth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def depth_encoding(self) -> DepthEncoding | None:
        """The DepthEncoding enum value."""
        member = self.get_member("DepthEncoding")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return DepthEncoding(member.value)
        return None

    @depth_encoding.setter
    def depth_encoding(self, value: DepthEncoding | str) -> None:
        """Set the DepthEncoding enum value."""
        member = self.get_member("DepthEncoding")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DepthEncoding",
                members.FieldEnum(value=str(value)),
            )

    @property
    def color_texture_offset(self) -> primitives.Float2 | None:
        """The ColorTextureOffset field value."""
        member = self.get_member("ColorTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_texture_offset.setter
    def color_texture_offset(self, value: primitives.Float2) -> None:
        """Set the ColorTextureOffset field value."""
        member = self.get_member("ColorTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def color_texture_scale(self) -> primitives.Float2 | None:
        """The ColorTextureScale field value."""
        member = self.get_member("ColorTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color_texture_scale.setter
    def color_texture_scale(self, value: primitives.Float2) -> None:
        """Set the ColorTextureScale field value."""
        member = self.get_member("ColorTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ColorTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def depth_texture_offset(self) -> primitives.Float2 | None:
        """The DepthTextureOffset field value."""
        member = self.get_member("DepthTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_texture_offset.setter
    def depth_texture_offset(self, value: primitives.Float2) -> None:
        """Set the DepthTextureOffset field value."""
        member = self.get_member("DepthTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def depth_texture_scale(self) -> primitives.Float2 | None:
        """The DepthTextureScale field value."""
        member = self.get_member("DepthTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_texture_scale.setter
    def depth_texture_scale(self, value: primitives.Float2) -> None:
        """Set the DepthTextureScale field value."""
        member = self.get_member("DepthTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def depth_from(self) -> primitives.Float | None:
        """The DepthFrom field value."""
        member = self.get_member("DepthFrom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_from.setter
    def depth_from(self, value: primitives.Float) -> None:
        """Set the DepthFrom field value."""
        member = self.get_member("DepthFrom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthFrom", fields.FieldFloat(value=value)
            )

    @property
    def depth_to(self) -> primitives.Float | None:
        """The DepthTo field value."""
        member = self.get_member("DepthTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_to.setter
    def depth_to(self, value: primitives.Float) -> None:
        """Set the DepthTo field value."""
        member = self.get_member("DepthTo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthTo", fields.FieldFloat(value=value)
            )

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
    def near_clip(self) -> primitives.Float | None:
        """The NearClip field value."""
        member = self.get_member("NearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clip.setter
    def near_clip(self, value: primitives.Float) -> None:
        """Set the NearClip field value."""
        member = self.get_member("NearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClip", fields.FieldFloat(value=value)
            )

    @property
    def far_clip(self) -> primitives.Float | None:
        """The FarClip field value."""
        member = self.get_member("FarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clip.setter
    def far_clip(self, value: primitives.Float) -> None:
        """Set the FarClip field value."""
        member = self.get_member("FarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClip", fields.FieldFloat(value=value)
            )

    @property
    def discard_threshold(self) -> primitives.Float | None:
        """The DiscardThreshold field value."""
        member = self.get_member("DiscardThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @discard_threshold.setter
    def discard_threshold(self, value: primitives.Float) -> None:
        """Set the DiscardThreshold field value."""
        member = self.get_member("DiscardThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DiscardThreshold", fields.FieldFloat(value=value)
            )

    @property
    def discard_offset(self) -> primitives.Float | None:
        """The DiscardOffset field value."""
        member = self.get_member("DiscardOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @discard_offset.setter
    def discard_offset(self, value: primitives.Float) -> None:
        """Set the DiscardOffset field value."""
        member = self.get_member("DiscardOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DiscardOffset", fields.FieldFloat(value=value)
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

