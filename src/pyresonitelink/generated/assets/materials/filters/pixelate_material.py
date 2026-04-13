"""Generated component: PixelateMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.color_mask import ColorMask
from pyresonitelink.generated._enums.stencil_comparison import StencilComparison
from pyresonitelink.generated._enums.stencil_operation import StencilOperation
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.generated._enums.sidedness import Sidedness
from pyresonitelink.generated._enums.zwrite import ZWrite
from pyresonitelink.generated._enums.ztest import ZTest
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PixelateMaterial(GeneratedComponent, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """The Pixelate Material component point filters the colors behind it using a spaced out grid of points. It then uses the colors to make a new pixel grid which makes up the pixelated effect it generates.

    Category: Assets/Materials/Filters

    Attach to a slot and then insert into a SkinnedMeshRenderer or
    MeshRenderer with a mesh to view it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PixelateMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, rect: primitives.Rect | None = None, rect_clip: primitives.Bool | None = None, color_mask: ColorMask | str | None = None, stencil_comparison: StencilComparison | str | None = None, stencil_operation: StencilOperation | str | None = None, stencil_id: primitives.Byte | None = None, stencil_write_mask: primitives.Byte | None = None, stencil_read_mask: primitives.Byte | None = None, render_queue: primitives.Int | None = None, per_object_field: primitives.Bool | None = None, resolution: primitives.Float2 | None = None, resolution_magnitude_texture: str | IAssetProvider[ITexture2D] | None = None, resolution_texture_scale: primitives.Float2 | None = None, resolution_texture_offset: primitives.Float2 | None = None, blend_mode: BlendMode | str | None = None, sidedness: Sidedness | str | None = None, zwrite: ZWrite | str | None = None, ztest: ZTest | str | None = None, global_: str | IAssetProvider[Shader] | None = None, per_object_ref: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            rect: Initial value for Rect.
            rect_clip: Initial value for RectClip.
            color_mask: Initial value for ColorMask.
            stencil_comparison: Initial value for StencilComparison.
            stencil_operation: Initial value for StencilOperation.
            stencil_id: Initial value for StencilID.
            stencil_write_mask: Initial value for StencilWriteMask.
            stencil_read_mask: Initial value for StencilReadMask.
            render_queue: Initial value for RenderQueue.
            per_object_field: Initial value for PerObject.
            resolution: Initial value for Resolution.
            resolution_magnitude_texture: Initial value for ResolutionMagnitudeTexture.
            resolution_texture_scale: Initial value for ResolutionTextureScale.
            resolution_texture_offset: Initial value for ResolutionTextureOffset.
            blend_mode: Initial value for BlendMode.
            sidedness: Initial value for Sidedness.
            zwrite: Initial value for ZWrite.
            ztest: Initial value for ZTest.
            global_: Initial value for _global.
            per_object_ref: Initial value for _perObject.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if rect is not None:
            self.rect = rect
        if rect_clip is not None:
            self.rect_clip = rect_clip
        if color_mask is not None:
            self.color_mask = color_mask
        if stencil_comparison is not None:
            self.stencil_comparison = stencil_comparison
        if stencil_operation is not None:
            self.stencil_operation = stencil_operation
        if stencil_id is not None:
            self.stencil_id = stencil_id
        if stencil_write_mask is not None:
            self.stencil_write_mask = stencil_write_mask
        if stencil_read_mask is not None:
            self.stencil_read_mask = stencil_read_mask
        if render_queue is not None:
            self.render_queue = render_queue
        if per_object_field is not None:
            self.per_object_field = per_object_field
        if resolution is not None:
            self.resolution = resolution
        if resolution_magnitude_texture is not None:
            self.resolution_magnitude_texture = resolution_magnitude_texture
        if resolution_texture_scale is not None:
            self.resolution_texture_scale = resolution_texture_scale
        if resolution_texture_offset is not None:
            self.resolution_texture_offset = resolution_texture_offset
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if sidedness is not None:
            self.sidedness = sidedness
        if zwrite is not None:
            self.zwrite = zwrite
        if ztest is not None:
            self.ztest = ztest
        if global_ is not None:
            self.global_ = global_
        if per_object_ref is not None:
            self.per_object_ref = per_object_ref

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
    def rect_clip(self) -> primitives.Bool | None:
        """The RectClip field value."""
        member = self.get_member("RectClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rect_clip.setter
    def rect_clip(self, value: primitives.Bool) -> None:
        """Set the RectClip field value."""
        member = self.get_member("RectClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RectClip", fields.FieldBool(value=value)
            )

    @property
    def color_mask(self) -> ColorMask | None:
        """The ColorMask enum value."""
        member = self.get_member("ColorMask")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorMask(member.value)
        return None

    @color_mask.setter
    def color_mask(self, value: ColorMask | str) -> None:
        """Set the ColorMask enum value."""
        member = self.get_member("ColorMask")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ColorMask",
                members.FieldEnum(value=str(value)),
            )

    @property
    def stencil_comparison(self) -> StencilComparison | None:
        """The StencilComparison enum value."""
        member = self.get_member("StencilComparison")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StencilComparison(member.value)
        return None

    @stencil_comparison.setter
    def stencil_comparison(self, value: StencilComparison | str) -> None:
        """Set the StencilComparison enum value."""
        member = self.get_member("StencilComparison")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "StencilComparison",
                members.FieldEnum(value=str(value)),
            )

    @property
    def stencil_operation(self) -> StencilOperation | None:
        """The StencilOperation enum value."""
        member = self.get_member("StencilOperation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StencilOperation(member.value)
        return None

    @stencil_operation.setter
    def stencil_operation(self, value: StencilOperation | str) -> None:
        """Set the StencilOperation enum value."""
        member = self.get_member("StencilOperation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "StencilOperation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def stencil_id(self) -> primitives.Byte | None:
        """The StencilID field value."""
        member = self.get_member("StencilID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_id.setter
    def stencil_id(self, value: primitives.Byte) -> None:
        """Set the StencilID field value."""
        member = self.get_member("StencilID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilID", fields.FieldByte(value=value)
            )

    @property
    def stencil_write_mask(self) -> primitives.Byte | None:
        """The StencilWriteMask field value."""
        member = self.get_member("StencilWriteMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_write_mask.setter
    def stencil_write_mask(self, value: primitives.Byte) -> None:
        """Set the StencilWriteMask field value."""
        member = self.get_member("StencilWriteMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilWriteMask", fields.FieldByte(value=value)
            )

    @property
    def stencil_read_mask(self) -> primitives.Byte | None:
        """The StencilReadMask field value."""
        member = self.get_member("StencilReadMask")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stencil_read_mask.setter
    def stencil_read_mask(self, value: primitives.Byte) -> None:
        """Set the StencilReadMask field value."""
        member = self.get_member("StencilReadMask")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StencilReadMask", fields.FieldByte(value=value)
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
    def per_object_field(self) -> primitives.Bool | None:
        """The PerObject field value."""
        member = self.get_member("PerObject")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @per_object_field.setter
    def per_object_field(self, value: primitives.Bool) -> None:
        """Set the PerObject field value."""
        member = self.get_member("PerObject")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerObject", fields.FieldBool(value=value)
            )

    @property
    def resolution(self) -> primitives.Float2 | None:
        """The Resolution field value."""
        member = self.get_member("Resolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @resolution.setter
    def resolution(self, value: primitives.Float2) -> None:
        """Set the Resolution field value."""
        member = self.get_member("Resolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Resolution", fields.FieldFloat2(value=value)
            )

    @property
    def resolution_magnitude_texture(self) -> str | None:
        """Target ID of the ResolutionMagnitudeTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("ResolutionMagnitudeTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @resolution_magnitude_texture.setter
    def resolution_magnitude_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the ResolutionMagnitudeTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ResolutionMagnitudeTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ResolutionMagnitudeTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def resolution_texture_scale(self) -> primitives.Float2 | None:
        """The ResolutionTextureScale field value."""
        member = self.get_member("ResolutionTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @resolution_texture_scale.setter
    def resolution_texture_scale(self, value: primitives.Float2) -> None:
        """Set the ResolutionTextureScale field value."""
        member = self.get_member("ResolutionTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResolutionTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def resolution_texture_offset(self) -> primitives.Float2 | None:
        """The ResolutionTextureOffset field value."""
        member = self.get_member("ResolutionTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @resolution_texture_offset.setter
    def resolution_texture_offset(self, value: primitives.Float2) -> None:
        """Set the ResolutionTextureOffset field value."""
        member = self.get_member("ResolutionTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResolutionTextureOffset", fields.FieldFloat2(value=value)
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
    def global_(self) -> str | None:
        """Target ID of the _global reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_global")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @global_.setter
    def global_(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _global reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_global")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_global",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def per_object_ref(self) -> str | None:
        """Target ID of the _perObject reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_perObject")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @per_object_ref.setter
    def per_object_ref(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _perObject reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_perObject")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_perObject",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

