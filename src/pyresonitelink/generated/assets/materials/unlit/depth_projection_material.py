"""Generated component: DepthProjectionMaterial."""

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


class DepthProjectionMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DepthProjectionMaterial.

    Category: Assets/Materials/Unlit
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DepthProjectionMaterial"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, color: str | IAssetProvider[ITexture2D] | None = None, depth: str | IAssetProvider[ITexture2D] | None = None, color_texture_offset: primitives.Float2 | None = None, color_texture_scale: primitives.Float2 | None = None, depth_texture_offset: primitives.Float2 | None = None, depth_texture_scale: primitives.Float2 | None = None, depth_from: np.float32 | None = None, depth_to: np.float32 | None = None, field_of_view: primitives.Float2 | None = None, near_clip: np.float32 | None = None, far_clip: np.float32 | None = None, discard_threshold: np.float32 | None = None, discard_offset: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            color: Initial value for Color.
            depth: Initial value for Depth.
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
    def depth_encoding(self) -> members.FieldEnum | None:
        """The DepthEncoding member."""
        member = self.get_member("DepthEncoding")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @depth_encoding.setter
    def depth_encoding(self, value: members.FieldEnum) -> None:
        """Set the DepthEncoding member."""
        self.set_member("DepthEncoding", value)

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
    def depth_from(self) -> np.float32 | None:
        """The DepthFrom field value."""
        member = self.get_member("DepthFrom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_from.setter
    def depth_from(self, value: np.float32) -> None:
        """Set the DepthFrom field value."""
        member = self.get_member("DepthFrom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthFrom", fields.FieldFloat(value=value)
            )

    @property
    def depth_to(self) -> np.float32 | None:
        """The DepthTo field value."""
        member = self.get_member("DepthTo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_to.setter
    def depth_to(self, value: np.float32) -> None:
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
    def near_clip(self) -> np.float32 | None:
        """The NearClip field value."""
        member = self.get_member("NearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clip.setter
    def near_clip(self, value: np.float32) -> None:
        """Set the NearClip field value."""
        member = self.get_member("NearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClip", fields.FieldFloat(value=value)
            )

    @property
    def far_clip(self) -> np.float32 | None:
        """The FarClip field value."""
        member = self.get_member("FarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clip.setter
    def far_clip(self, value: np.float32) -> None:
        """Set the FarClip field value."""
        member = self.get_member("FarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClip", fields.FieldFloat(value=value)
            )

    @property
    def discard_threshold(self) -> np.float32 | None:
        """The DiscardThreshold field value."""
        member = self.get_member("DiscardThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @discard_threshold.setter
    def discard_threshold(self, value: np.float32) -> None:
        """Set the DiscardThreshold field value."""
        member = self.get_member("DiscardThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DiscardThreshold", fields.FieldFloat(value=value)
            )

    @property
    def discard_offset(self) -> np.float32 | None:
        """The DiscardOffset field value."""
        member = self.get_member("DiscardOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @discard_offset.setter
    def discard_offset(self, value: np.float32) -> None:
        """Set the DiscardOffset field value."""
        member = self.get_member("DiscardOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DiscardOffset", fields.FieldFloat(value=value)
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

