"""Generated component: WireframeMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.icommon_material import ICommonMaterial
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WireframeMaterial(GeneratedComponent, ICommonMaterial, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WireframeMaterial.

    Category: Assets/Materials/Unlit
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WireframeMaterial"

    def __init__(self, high_priority_integration: bool | None = None, thickness: np.float32 | None = None, screen_space: bool | None = None, line_color: primitives.ColorX | None = None, fill_color: primitives.ColorX | None = None, inner_line_color: primitives.ColorX | None = None, inner_fill_color: primitives.ColorX | None = None, use_fresnel: bool | None = None, line_far_color: primitives.ColorX | None = None, fill_far_color: primitives.ColorX | None = None, inner_line_far_color: primitives.ColorX | None = None, inner_fill_far_color: primitives.ColorX | None = None, exp: np.float32 | None = None, texture: str | IAssetProvider[ITexture2D] | None = None, double_sided: bool | None = None, offset_factor: np.float32 | None = None, offset_units: np.float32 | None = None, render_queue: np.int32 | None = None, regular: str | IAssetProvider[Shader] | None = None, regular_double_sided: str | IAssetProvider[Shader] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            thickness: Initial value for Thickness.
            screen_space: Initial value for ScreenSpace.
            line_color: Initial value for LineColor.
            fill_color: Initial value for FillColor.
            inner_line_color: Initial value for InnerLineColor.
            inner_fill_color: Initial value for InnerFillColor.
            use_fresnel: Initial value for UseFresnel.
            line_far_color: Initial value for LineFarColor.
            fill_far_color: Initial value for FillFarColor.
            inner_line_far_color: Initial value for InnerLineFarColor.
            inner_fill_far_color: Initial value for InnerFillFarColor.
            exp: Initial value for Exp.
            texture: Initial value for Texture.
            double_sided: Initial value for DoubleSided.
            offset_factor: Initial value for OffsetFactor.
            offset_units: Initial value for OffsetUnits.
            render_queue: Initial value for RenderQueue.
            regular: Initial value for _regular.
            regular_double_sided: Initial value for _regularDoubleSided.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if thickness is not None:
            self.thickness = thickness
        if screen_space is not None:
            self.screen_space = screen_space
        if line_color is not None:
            self.line_color = line_color
        if fill_color is not None:
            self.fill_color = fill_color
        if inner_line_color is not None:
            self.inner_line_color = inner_line_color
        if inner_fill_color is not None:
            self.inner_fill_color = inner_fill_color
        if use_fresnel is not None:
            self.use_fresnel = use_fresnel
        if line_far_color is not None:
            self.line_far_color = line_far_color
        if fill_far_color is not None:
            self.fill_far_color = fill_far_color
        if inner_line_far_color is not None:
            self.inner_line_far_color = inner_line_far_color
        if inner_fill_far_color is not None:
            self.inner_fill_far_color = inner_fill_far_color
        if exp is not None:
            self.exp = exp
        if texture is not None:
            self.texture = texture
        if double_sided is not None:
            self.double_sided = double_sided
        if offset_factor is not None:
            self.offset_factor = offset_factor
        if offset_units is not None:
            self.offset_units = offset_units
        if render_queue is not None:
            self.render_queue = render_queue
        if regular is not None:
            self.regular = regular
        if regular_double_sided is not None:
            self.regular_double_sided = regular_double_sided

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
    def thickness(self) -> np.float32 | None:
        """The Thickness field value."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: np.float32) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def screen_space(self) -> bool | None:
        """The ScreenSpace field value."""
        member = self.get_member("ScreenSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_space.setter
    def screen_space(self, value: bool) -> None:
        """Set the ScreenSpace field value."""
        member = self.get_member("ScreenSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenSpace", fields.FieldBool(value=value)
            )

    @property
    def line_color(self) -> primitives.ColorX | None:
        """The LineColor field value."""
        member = self.get_member("LineColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_color.setter
    def line_color(self, value: primitives.ColorX) -> None:
        """Set the LineColor field value."""
        member = self.get_member("LineColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LineColor", fields.FieldColorX(value=value)
            )

    @property
    def fill_color(self) -> primitives.ColorX | None:
        """The FillColor field value."""
        member = self.get_member("FillColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_color.setter
    def fill_color(self, value: primitives.ColorX) -> None:
        """Set the FillColor field value."""
        member = self.get_member("FillColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillColor", fields.FieldColorX(value=value)
            )

    @property
    def inner_line_color(self) -> primitives.ColorX | None:
        """The InnerLineColor field value."""
        member = self.get_member("InnerLineColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_line_color.setter
    def inner_line_color(self, value: primitives.ColorX) -> None:
        """Set the InnerLineColor field value."""
        member = self.get_member("InnerLineColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerLineColor", fields.FieldColorX(value=value)
            )

    @property
    def inner_fill_color(self) -> primitives.ColorX | None:
        """The InnerFillColor field value."""
        member = self.get_member("InnerFillColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_fill_color.setter
    def inner_fill_color(self, value: primitives.ColorX) -> None:
        """Set the InnerFillColor field value."""
        member = self.get_member("InnerFillColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerFillColor", fields.FieldColorX(value=value)
            )

    @property
    def use_fresnel(self) -> bool | None:
        """The UseFresnel field value."""
        member = self.get_member("UseFresnel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_fresnel.setter
    def use_fresnel(self, value: bool) -> None:
        """Set the UseFresnel field value."""
        member = self.get_member("UseFresnel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFresnel", fields.FieldBool(value=value)
            )

    @property
    def line_far_color(self) -> primitives.ColorX | None:
        """The LineFarColor field value."""
        member = self.get_member("LineFarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @line_far_color.setter
    def line_far_color(self, value: primitives.ColorX) -> None:
        """Set the LineFarColor field value."""
        member = self.get_member("LineFarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LineFarColor", fields.FieldColorX(value=value)
            )

    @property
    def fill_far_color(self) -> primitives.ColorX | None:
        """The FillFarColor field value."""
        member = self.get_member("FillFarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fill_far_color.setter
    def fill_far_color(self, value: primitives.ColorX) -> None:
        """Set the FillFarColor field value."""
        member = self.get_member("FillFarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FillFarColor", fields.FieldColorX(value=value)
            )

    @property
    def inner_line_far_color(self) -> primitives.ColorX | None:
        """The InnerLineFarColor field value."""
        member = self.get_member("InnerLineFarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_line_far_color.setter
    def inner_line_far_color(self, value: primitives.ColorX) -> None:
        """Set the InnerLineFarColor field value."""
        member = self.get_member("InnerLineFarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerLineFarColor", fields.FieldColorX(value=value)
            )

    @property
    def inner_fill_far_color(self) -> primitives.ColorX | None:
        """The InnerFillFarColor field value."""
        member = self.get_member("InnerFillFarColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inner_fill_far_color.setter
    def inner_fill_far_color(self, value: primitives.ColorX) -> None:
        """Set the InnerFillFarColor field value."""
        member = self.get_member("InnerFillFarColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InnerFillFarColor", fields.FieldColorX(value=value)
            )

    @property
    def exp(self) -> np.float32 | None:
        """The Exp field value."""
        member = self.get_member("Exp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exp.setter
    def exp(self, value: np.float32) -> None:
        """Set the Exp field value."""
        member = self.get_member("Exp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exp", fields.FieldFloat(value=value)
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
    def double_sided(self) -> bool | None:
        """The DoubleSided field value."""
        member = self.get_member("DoubleSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @double_sided.setter
    def double_sided(self, value: bool) -> None:
        """Set the DoubleSided field value."""
        member = self.get_member("DoubleSided")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoubleSided", fields.FieldBool(value=value)
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

    @property
    def regular(self) -> str | None:
        """Target ID of the _regular reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_regular")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @regular.setter
    def regular(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _regular reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_regular")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_regular",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def regular_double_sided(self) -> str | None:
        """Target ID of the _regularDoubleSided reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_regularDoubleSided")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @regular_double_sided.setter
    def regular_double_sided(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _regularDoubleSided reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_regularDoubleSided")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_regularDoubleSided",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

