"""Generated component: LUT_Material."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LUT_Material(GeneratedComponent, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LUT_Material.

    Category: Assets/Materials/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LUT_Material"

    def __init__(self, high_priority_integration: bool | None = None, rect: primitives.Rect | None = None, rect_clip: bool | None = None, stencil_id: np.uint8 | None = None, stencil_write_mask: np.uint8 | None = None, stencil_read_mask: np.uint8 | None = None, render_queue: np.int32 | None = None, shader: str | IAssetProvider[Shader] | None = None, lut: str | IAssetProvider[Texture3D] | None = None, secondary_lut: str | IAssetProvider[Texture3D] | None = None, use_s_rgb: bool | None = None, lerp: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            rect: Initial value for Rect.
            rect_clip: Initial value for RectClip.
            stencil_id: Initial value for StencilID.
            stencil_write_mask: Initial value for StencilWriteMask.
            stencil_read_mask: Initial value for StencilReadMask.
            render_queue: Initial value for RenderQueue.
            shader: Initial value for _shader.
            lut: Initial value for LUT.
            secondary_lut: Initial value for SecondaryLUT.
            use_s_rgb: Initial value for UseSRGB.
            lerp: Initial value for Lerp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if rect is not None:
            self.rect = rect
        if rect_clip is not None:
            self.rect_clip = rect_clip
        if stencil_id is not None:
            self.stencil_id = stencil_id
        if stencil_write_mask is not None:
            self.stencil_write_mask = stencil_write_mask
        if stencil_read_mask is not None:
            self.stencil_read_mask = stencil_read_mask
        if render_queue is not None:
            self.render_queue = render_queue
        if shader is not None:
            self.shader = shader
        if lut is not None:
            self.lut = lut
        if secondary_lut is not None:
            self.secondary_lut = secondary_lut
        if use_s_rgb is not None:
            self.use_s_rgb = use_s_rgb
        if lerp is not None:
            self.lerp = lerp

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
    def lut(self) -> str | None:
        """Target ID of the LUT reference (targets IAssetProvider[Texture3D])."""
        member = self.get_member("LUT")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lut.setter
    def lut(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the LUT reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("LUT")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LUT",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

    @property
    def secondary_lut(self) -> str | None:
        """Target ID of the SecondaryLUT reference (targets IAssetProvider[Texture3D])."""
        member = self.get_member("SecondaryLUT")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_lut.setter
    def secondary_lut(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the SecondaryLUT reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryLUT")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryLUT",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

    @property
    def use_s_rgb(self) -> bool | None:
        """The UseSRGB field value."""
        member = self.get_member("UseSRGB")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_s_rgb.setter
    def use_s_rgb(self, value: bool) -> None:
        """Set the UseSRGB field value."""
        member = self.get_member("UseSRGB")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSRGB", fields.FieldBool(value=value)
            )

    @property
    def lerp(self) -> np.float32 | None:
        """The Lerp field value."""
        member = self.get_member("Lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: np.float32) -> None:
        """Set the Lerp field value."""
        member = self.get_member("Lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Lerp", fields.FieldFloat(value=value)
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

