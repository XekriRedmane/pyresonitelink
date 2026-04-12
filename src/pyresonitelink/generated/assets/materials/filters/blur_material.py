"""Generated component: BlurMaterial."""

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


class BlurMaterial(GeneratedComponent, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """The BlurMaterial Component is used to blur objects rendered behind it, by first rendering everything behind it using z-test and then grabbing the pixels, then creating spread transparent ghost images of the original pixels to give the illusion of blur.

    Category: Assets/Materials/Filters

    Used to make drunk effects, privacy glass, or magic effects.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BlurMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, rect: primitives.Rect | None = None, rect_clip: primitives.Bool | None = None, color_mask: ColorMask | str | None = None, stencil_comparison: StencilComparison | str | None = None, stencil_operation: StencilOperation | str | None = None, stencil_id: primitives.Byte | None = None, stencil_write_mask: primitives.Byte | None = None, stencil_read_mask: primitives.Byte | None = None, render_queue: primitives.Int | None = None, iterations: primitives.Int | None = None, spread: primitives.Float2 | None = None, spread_magnitude_texture: str | IAssetProvider[ITexture2D] | None = None, use_poisson_disc: primitives.Bool | None = None, depth_fade_divisor: primitives.Float | None = None, spread_texture_scale: primitives.Float2 | None = None, spread_texture_offset: primitives.Float2 | None = None, refract: primitives.Bool | None = None, refraction_strength: primitives.Float | None = None, normal_map: str | IAssetProvider[ITexture2D] | None = None, normal_texture_scale: primitives.Float2 | None = None, normal_texture_offset: primitives.Float2 | None = None, per_object: primitives.Bool | None = None, blend_mode: BlendMode | str | None = None, sidedness: Sidedness | str | None = None, zwrite: ZWrite | str | None = None, ztest: ZTest | str | None = None, global_: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
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
            iterations: Initial value for Iterations.
            spread: Initial value for Spread.
            spread_magnitude_texture: Initial value for SpreadMagnitudeTexture.
            use_poisson_disc: Initial value for UsePoissonDisc.
            depth_fade_divisor: Initial value for DepthFadeDivisor.
            spread_texture_scale: Initial value for SpreadTextureScale.
            spread_texture_offset: Initial value for SpreadTextureOffset.
            refract: Initial value for Refract.
            refraction_strength: Initial value for RefractionStrength.
            normal_map: Initial value for NormalMap.
            normal_texture_scale: Initial value for NormalTextureScale.
            normal_texture_offset: Initial value for NormalTextureOffset.
            per_object: Initial value for PerObject.
            blend_mode: Initial value for BlendMode.
            sidedness: Initial value for Sidedness.
            zwrite: Initial value for ZWrite.
            ztest: Initial value for ZTest.
            global_: Initial value for _global.
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
        if iterations is not None:
            self.iterations = iterations
        if spread is not None:
            self.spread = spread
        if spread_magnitude_texture is not None:
            self.spread_magnitude_texture = spread_magnitude_texture
        if use_poisson_disc is not None:
            self.use_poisson_disc = use_poisson_disc
        if depth_fade_divisor is not None:
            self.depth_fade_divisor = depth_fade_divisor
        if spread_texture_scale is not None:
            self.spread_texture_scale = spread_texture_scale
        if spread_texture_offset is not None:
            self.spread_texture_offset = spread_texture_offset
        if refract is not None:
            self.refract = refract
        if refraction_strength is not None:
            self.refraction_strength = refraction_strength
        if normal_map is not None:
            self.normal_map = normal_map
        if normal_texture_scale is not None:
            self.normal_texture_scale = normal_texture_scale
        if normal_texture_offset is not None:
            self.normal_texture_offset = normal_texture_offset
        if per_object is not None:
            self.per_object = per_object
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
    def iterations(self) -> primitives.Int | None:
        """The Iterations field value."""
        member = self.get_member("Iterations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @iterations.setter
    def iterations(self, value: primitives.Int) -> None:
        """Set the Iterations field value."""
        member = self.get_member("Iterations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Iterations", fields.FieldInt(value=value)
            )

    @property
    def spread(self) -> primitives.Float2 | None:
        """The Spread field value."""
        member = self.get_member("Spread")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spread.setter
    def spread(self, value: primitives.Float2) -> None:
        """Set the Spread field value."""
        member = self.get_member("Spread")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spread", fields.FieldFloat2(value=value)
            )

    @property
    def spread_magnitude_texture(self) -> str | None:
        """Target ID of the SpreadMagnitudeTexture reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("SpreadMagnitudeTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spread_magnitude_texture.setter
    def spread_magnitude_texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the SpreadMagnitudeTexture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SpreadMagnitudeTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpreadMagnitudeTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def use_poisson_disc(self) -> primitives.Bool | None:
        """The UsePoissonDisc field value."""
        member = self.get_member("UsePoissonDisc")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_poisson_disc.setter
    def use_poisson_disc(self, value: primitives.Bool) -> None:
        """Set the UsePoissonDisc field value."""
        member = self.get_member("UsePoissonDisc")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsePoissonDisc", fields.FieldBool(value=value)
            )

    @property
    def depth_fade_divisor(self) -> primitives.Float | None:
        """The DepthFadeDivisor field value."""
        member = self.get_member("DepthFadeDivisor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth_fade_divisor.setter
    def depth_fade_divisor(self, value: primitives.Float) -> None:
        """Set the DepthFadeDivisor field value."""
        member = self.get_member("DepthFadeDivisor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DepthFadeDivisor", fields.FieldFloat(value=value)
            )

    @property
    def spread_texture_scale(self) -> primitives.Float2 | None:
        """The SpreadTextureScale field value."""
        member = self.get_member("SpreadTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spread_texture_scale.setter
    def spread_texture_scale(self, value: primitives.Float2) -> None:
        """Set the SpreadTextureScale field value."""
        member = self.get_member("SpreadTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpreadTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def spread_texture_offset(self) -> primitives.Float2 | None:
        """The SpreadTextureOffset field value."""
        member = self.get_member("SpreadTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spread_texture_offset.setter
    def spread_texture_offset(self, value: primitives.Float2) -> None:
        """Set the SpreadTextureOffset field value."""
        member = self.get_member("SpreadTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpreadTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def refract(self) -> primitives.Bool | None:
        """The Refract field value."""
        member = self.get_member("Refract")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @refract.setter
    def refract(self, value: primitives.Bool) -> None:
        """Set the Refract field value."""
        member = self.get_member("Refract")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Refract", fields.FieldBool(value=value)
            )

    @property
    def refraction_strength(self) -> primitives.Float | None:
        """The RefractionStrength field value."""
        member = self.get_member("RefractionStrength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @refraction_strength.setter
    def refraction_strength(self, value: primitives.Float) -> None:
        """Set the RefractionStrength field value."""
        member = self.get_member("RefractionStrength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RefractionStrength", fields.FieldFloat(value=value)
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
    def normal_texture_scale(self) -> primitives.Float2 | None:
        """The NormalTextureScale field value."""
        member = self.get_member("NormalTextureScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_texture_scale.setter
    def normal_texture_scale(self, value: primitives.Float2) -> None:
        """Set the NormalTextureScale field value."""
        member = self.get_member("NormalTextureScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalTextureScale", fields.FieldFloat2(value=value)
            )

    @property
    def normal_texture_offset(self) -> primitives.Float2 | None:
        """The NormalTextureOffset field value."""
        member = self.get_member("NormalTextureOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_texture_offset.setter
    def normal_texture_offset(self, value: primitives.Float2) -> None:
        """Set the NormalTextureOffset field value."""
        member = self.get_member("NormalTextureOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalTextureOffset", fields.FieldFloat2(value=value)
            )

    @property
    def per_object(self) -> primitives.Bool | None:
        """The PerObject field value."""
        member = self.get_member("PerObject")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @per_object.setter
    def per_object(self, value: primitives.Bool) -> None:
        """Set the PerObject field value."""
        member = self.get_member("PerObject")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerObject", fields.FieldBool(value=value)
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
    def per_object(self) -> str | None:
        """Target ID of the _perObject reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_perObject")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @per_object.setter
    def per_object(self, target: str | IAssetProvider[Shader] | None) -> None:
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

