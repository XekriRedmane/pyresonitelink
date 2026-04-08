"""Generated component: ChannelMatrixMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.i_uix_material import IUIX_Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ChannelMatrixMaterial(GeneratedComponent, IUIX_Material, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ChannelMatrixMaterial.

    Category: Assets/Materials/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ChannelMatrixMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, rect: primitives.Rect | None = None, rect_clip: primitives.Bool | None = None, stencil_id: primitives.Byte | None = None, stencil_write_mask: primitives.Byte | None = None, stencil_read_mask: primitives.Byte | None = None, render_queue: primitives.Int | None = None, shader: str | IAssetProvider[Shader] | None = None, red_from_red: primitives.Float | None = None, red_from_green: primitives.Float | None = None, red_from_blue: primitives.Float | None = None, red_offset: primitives.Float | None = None, green_from_red: primitives.Float | None = None, green_from_green: primitives.Float | None = None, green_from_blue: primitives.Float | None = None, green_offset: primitives.Float | None = None, blue_from_red: primitives.Float | None = None, blue_from_green: primitives.Float | None = None, blue_from_blue: primitives.Float | None = None, blue_offset: primitives.Float | None = None, clamp_red_min: primitives.Float | None = None, clamp_green_min: primitives.Float | None = None, clamp_blue_min: primitives.Float | None = None, clamp_red_max: primitives.Float | None = None, clamp_green_max: primitives.Float | None = None, clamp_blue_max: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
            red_from_red: Initial value for RedFromRed.
            red_from_green: Initial value for RedFromGreen.
            red_from_blue: Initial value for RedFromBlue.
            red_offset: Initial value for RedOffset.
            green_from_red: Initial value for GreenFromRed.
            green_from_green: Initial value for GreenFromGreen.
            green_from_blue: Initial value for GreenFromBlue.
            green_offset: Initial value for GreenOffset.
            blue_from_red: Initial value for BlueFromRed.
            blue_from_green: Initial value for BlueFromGreen.
            blue_from_blue: Initial value for BlueFromBlue.
            blue_offset: Initial value for BlueOffset.
            clamp_red_min: Initial value for ClampRedMin.
            clamp_green_min: Initial value for ClampGreenMin.
            clamp_blue_min: Initial value for ClampBlueMin.
            clamp_red_max: Initial value for ClampRedMax.
            clamp_green_max: Initial value for ClampGreenMax.
            clamp_blue_max: Initial value for ClampBlueMax.
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
        if red_from_red is not None:
            self.red_from_red = red_from_red
        if red_from_green is not None:
            self.red_from_green = red_from_green
        if red_from_blue is not None:
            self.red_from_blue = red_from_blue
        if red_offset is not None:
            self.red_offset = red_offset
        if green_from_red is not None:
            self.green_from_red = green_from_red
        if green_from_green is not None:
            self.green_from_green = green_from_green
        if green_from_blue is not None:
            self.green_from_blue = green_from_blue
        if green_offset is not None:
            self.green_offset = green_offset
        if blue_from_red is not None:
            self.blue_from_red = blue_from_red
        if blue_from_green is not None:
            self.blue_from_green = blue_from_green
        if blue_from_blue is not None:
            self.blue_from_blue = blue_from_blue
        if blue_offset is not None:
            self.blue_offset = blue_offset
        if clamp_red_min is not None:
            self.clamp_red_min = clamp_red_min
        if clamp_green_min is not None:
            self.clamp_green_min = clamp_green_min
        if clamp_blue_min is not None:
            self.clamp_blue_min = clamp_blue_min
        if clamp_red_max is not None:
            self.clamp_red_max = clamp_red_max
        if clamp_green_max is not None:
            self.clamp_green_max = clamp_green_max
        if clamp_blue_max is not None:
            self.clamp_blue_max = clamp_blue_max

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
    def red_from_red(self) -> primitives.Float | None:
        """The RedFromRed field value."""
        member = self.get_member("RedFromRed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @red_from_red.setter
    def red_from_red(self, value: primitives.Float) -> None:
        """Set the RedFromRed field value."""
        member = self.get_member("RedFromRed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RedFromRed", fields.FieldFloat(value=value)
            )

    @property
    def red_from_green(self) -> primitives.Float | None:
        """The RedFromGreen field value."""
        member = self.get_member("RedFromGreen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @red_from_green.setter
    def red_from_green(self, value: primitives.Float) -> None:
        """Set the RedFromGreen field value."""
        member = self.get_member("RedFromGreen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RedFromGreen", fields.FieldFloat(value=value)
            )

    @property
    def red_from_blue(self) -> primitives.Float | None:
        """The RedFromBlue field value."""
        member = self.get_member("RedFromBlue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @red_from_blue.setter
    def red_from_blue(self, value: primitives.Float) -> None:
        """Set the RedFromBlue field value."""
        member = self.get_member("RedFromBlue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RedFromBlue", fields.FieldFloat(value=value)
            )

    @property
    def red_offset(self) -> primitives.Float | None:
        """The RedOffset field value."""
        member = self.get_member("RedOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @red_offset.setter
    def red_offset(self, value: primitives.Float) -> None:
        """Set the RedOffset field value."""
        member = self.get_member("RedOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RedOffset", fields.FieldFloat(value=value)
            )

    @property
    def green_from_red(self) -> primitives.Float | None:
        """The GreenFromRed field value."""
        member = self.get_member("GreenFromRed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @green_from_red.setter
    def green_from_red(self, value: primitives.Float) -> None:
        """Set the GreenFromRed field value."""
        member = self.get_member("GreenFromRed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GreenFromRed", fields.FieldFloat(value=value)
            )

    @property
    def green_from_green(self) -> primitives.Float | None:
        """The GreenFromGreen field value."""
        member = self.get_member("GreenFromGreen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @green_from_green.setter
    def green_from_green(self, value: primitives.Float) -> None:
        """Set the GreenFromGreen field value."""
        member = self.get_member("GreenFromGreen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GreenFromGreen", fields.FieldFloat(value=value)
            )

    @property
    def green_from_blue(self) -> primitives.Float | None:
        """The GreenFromBlue field value."""
        member = self.get_member("GreenFromBlue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @green_from_blue.setter
    def green_from_blue(self, value: primitives.Float) -> None:
        """Set the GreenFromBlue field value."""
        member = self.get_member("GreenFromBlue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GreenFromBlue", fields.FieldFloat(value=value)
            )

    @property
    def green_offset(self) -> primitives.Float | None:
        """The GreenOffset field value."""
        member = self.get_member("GreenOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @green_offset.setter
    def green_offset(self, value: primitives.Float) -> None:
        """Set the GreenOffset field value."""
        member = self.get_member("GreenOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GreenOffset", fields.FieldFloat(value=value)
            )

    @property
    def blue_from_red(self) -> primitives.Float | None:
        """The BlueFromRed field value."""
        member = self.get_member("BlueFromRed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blue_from_red.setter
    def blue_from_red(self, value: primitives.Float) -> None:
        """Set the BlueFromRed field value."""
        member = self.get_member("BlueFromRed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlueFromRed", fields.FieldFloat(value=value)
            )

    @property
    def blue_from_green(self) -> primitives.Float | None:
        """The BlueFromGreen field value."""
        member = self.get_member("BlueFromGreen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blue_from_green.setter
    def blue_from_green(self, value: primitives.Float) -> None:
        """Set the BlueFromGreen field value."""
        member = self.get_member("BlueFromGreen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlueFromGreen", fields.FieldFloat(value=value)
            )

    @property
    def blue_from_blue(self) -> primitives.Float | None:
        """The BlueFromBlue field value."""
        member = self.get_member("BlueFromBlue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blue_from_blue.setter
    def blue_from_blue(self, value: primitives.Float) -> None:
        """Set the BlueFromBlue field value."""
        member = self.get_member("BlueFromBlue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlueFromBlue", fields.FieldFloat(value=value)
            )

    @property
    def blue_offset(self) -> primitives.Float | None:
        """The BlueOffset field value."""
        member = self.get_member("BlueOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blue_offset.setter
    def blue_offset(self, value: primitives.Float) -> None:
        """Set the BlueOffset field value."""
        member = self.get_member("BlueOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlueOffset", fields.FieldFloat(value=value)
            )

    @property
    def clamp_red_min(self) -> primitives.Float | None:
        """The ClampRedMin field value."""
        member = self.get_member("ClampRedMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp_red_min.setter
    def clamp_red_min(self, value: primitives.Float) -> None:
        """Set the ClampRedMin field value."""
        member = self.get_member("ClampRedMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClampRedMin", fields.FieldFloat(value=value)
            )

    @property
    def clamp_green_min(self) -> primitives.Float | None:
        """The ClampGreenMin field value."""
        member = self.get_member("ClampGreenMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp_green_min.setter
    def clamp_green_min(self, value: primitives.Float) -> None:
        """Set the ClampGreenMin field value."""
        member = self.get_member("ClampGreenMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClampGreenMin", fields.FieldFloat(value=value)
            )

    @property
    def clamp_blue_min(self) -> primitives.Float | None:
        """The ClampBlueMin field value."""
        member = self.get_member("ClampBlueMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp_blue_min.setter
    def clamp_blue_min(self, value: primitives.Float) -> None:
        """Set the ClampBlueMin field value."""
        member = self.get_member("ClampBlueMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClampBlueMin", fields.FieldFloat(value=value)
            )

    @property
    def clamp_red_max(self) -> primitives.Float | None:
        """The ClampRedMax field value."""
        member = self.get_member("ClampRedMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp_red_max.setter
    def clamp_red_max(self, value: primitives.Float) -> None:
        """Set the ClampRedMax field value."""
        member = self.get_member("ClampRedMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClampRedMax", fields.FieldFloat(value=value)
            )

    @property
    def clamp_green_max(self) -> primitives.Float | None:
        """The ClampGreenMax field value."""
        member = self.get_member("ClampGreenMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp_green_max.setter
    def clamp_green_max(self, value: primitives.Float) -> None:
        """Set the ClampGreenMax field value."""
        member = self.get_member("ClampGreenMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClampGreenMax", fields.FieldFloat(value=value)
            )

    @property
    def clamp_blue_max(self) -> primitives.Float | None:
        """The ClampBlueMax field value."""
        member = self.get_member("ClampBlueMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clamp_blue_max.setter
    def clamp_blue_max(self, value: primitives.Float) -> None:
        """Set the ClampBlueMax field value."""
        member = self.get_member("ClampBlueMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClampBlueMax", fields.FieldFloat(value=value)
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

