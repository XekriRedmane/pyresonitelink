"""Generated component: FogBoxVolumeMaterial."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FogBoxVolumeMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FogBoxVolumeMaterial.

    Category: Assets/Materials/Volume
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FogBoxVolumeMaterial"

    def __init__(self, high_priority_integration: bool | None = None, shader: str | IAssetProvider[Shader] | None = None, base_color: primitives.ColorX | None = None, accumulation_color: primitives.ColorX | None = None, accumulation_color_bottom: primitives.ColorX | None = None, accumulation_color_top: primitives.ColorX | None = None, fog_start: np.float32 | None = None, fog_end: np.float32 | None = None, fog_density: np.float32 | None = None, gamma_curve: np.float32 | None = None, world_space: bool | None = None, accumulation_rate: np.float32 | None = None, render_queue: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            base_color: Initial value for BaseColor.
            accumulation_color: Initial value for AccumulationColor.
            accumulation_color_bottom: Initial value for AccumulationColorBottom.
            accumulation_color_top: Initial value for AccumulationColorTop.
            fog_start: Initial value for FogStart.
            fog_end: Initial value for FogEnd.
            fog_density: Initial value for FogDensity.
            gamma_curve: Initial value for GammaCurve.
            world_space: Initial value for WorldSpace.
            accumulation_rate: Initial value for AccumulationRate.
            render_queue: Initial value for RenderQueue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if base_color is not None:
            self.base_color = base_color
        if accumulation_color is not None:
            self.accumulation_color = accumulation_color
        if accumulation_color_bottom is not None:
            self.accumulation_color_bottom = accumulation_color_bottom
        if accumulation_color_top is not None:
            self.accumulation_color_top = accumulation_color_top
        if fog_start is not None:
            self.fog_start = fog_start
        if fog_end is not None:
            self.fog_end = fog_end
        if fog_density is not None:
            self.fog_density = fog_density
        if gamma_curve is not None:
            self.gamma_curve = gamma_curve
        if world_space is not None:
            self.world_space = world_space
        if accumulation_rate is not None:
            self.accumulation_rate = accumulation_rate
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
    def base_color(self) -> primitives.ColorX | None:
        """The BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_color.setter
    def base_color(self, value: primitives.ColorX) -> None:
        """Set the BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseColor", fields.FieldColorX(value=value)
            )

    @property
    def accumulation_color(self) -> primitives.ColorX | None:
        """The AccumulationColor field value."""
        member = self.get_member("AccumulationColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulation_color.setter
    def accumulation_color(self, value: primitives.ColorX) -> None:
        """Set the AccumulationColor field value."""
        member = self.get_member("AccumulationColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulationColor", fields.FieldColorX(value=value)
            )

    @property
    def accumulation_color_bottom(self) -> primitives.ColorX | None:
        """The AccumulationColorBottom field value."""
        member = self.get_member("AccumulationColorBottom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulation_color_bottom.setter
    def accumulation_color_bottom(self, value: primitives.ColorX) -> None:
        """Set the AccumulationColorBottom field value."""
        member = self.get_member("AccumulationColorBottom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulationColorBottom", fields.FieldColorX(value=value)
            )

    @property
    def accumulation_color_top(self) -> primitives.ColorX | None:
        """The AccumulationColorTop field value."""
        member = self.get_member("AccumulationColorTop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulation_color_top.setter
    def accumulation_color_top(self, value: primitives.ColorX) -> None:
        """Set the AccumulationColorTop field value."""
        member = self.get_member("AccumulationColorTop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulationColorTop", fields.FieldColorX(value=value)
            )

    @property
    def fog_start(self) -> np.float32 | None:
        """The FogStart field value."""
        member = self.get_member("FogStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fog_start.setter
    def fog_start(self, value: np.float32) -> None:
        """Set the FogStart field value."""
        member = self.get_member("FogStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FogStart", fields.FieldFloat(value=value)
            )

    @property
    def fog_end(self) -> np.float32 | None:
        """The FogEnd field value."""
        member = self.get_member("FogEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fog_end.setter
    def fog_end(self, value: np.float32) -> None:
        """Set the FogEnd field value."""
        member = self.get_member("FogEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FogEnd", fields.FieldFloat(value=value)
            )

    @property
    def fog_density(self) -> np.float32 | None:
        """The FogDensity field value."""
        member = self.get_member("FogDensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fog_density.setter
    def fog_density(self, value: np.float32) -> None:
        """Set the FogDensity field value."""
        member = self.get_member("FogDensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FogDensity", fields.FieldFloat(value=value)
            )

    @property
    def gamma_curve(self) -> np.float32 | None:
        """The GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gamma_curve.setter
    def gamma_curve(self, value: np.float32) -> None:
        """Set the GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GammaCurve", fields.FieldFloat(value=value)
            )

    @property
    def world_space(self) -> bool | None:
        """The WorldSpace field value."""
        member = self.get_member("WorldSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @world_space.setter
    def world_space(self, value: bool) -> None:
        """Set the WorldSpace field value."""
        member = self.get_member("WorldSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldSpace", fields.FieldBool(value=value)
            )

    @property
    def color_mode(self) -> members.FieldEnum | None:
        """The ColorMode member."""
        member = self.get_member("ColorMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @color_mode.setter
    def color_mode(self, value: members.FieldEnum) -> None:
        """Set the ColorMode member."""
        self.set_member("ColorMode", value)

    @property
    def saturation_mode(self) -> members.FieldEnum | None:
        """The SaturationMode member."""
        member = self.get_member("SaturationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @saturation_mode.setter
    def saturation_mode(self, value: members.FieldEnum) -> None:
        """Set the SaturationMode member."""
        self.set_member("SaturationMode", value)

    @property
    def accumulation_mode(self) -> members.FieldEnum | None:
        """The AccumulationMode member."""
        member = self.get_member("AccumulationMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @accumulation_mode.setter
    def accumulation_mode(self, value: members.FieldEnum) -> None:
        """Set the AccumulationMode member."""
        self.set_member("AccumulationMode", value)

    @property
    def accumulation_rate(self) -> np.float32 | None:
        """The AccumulationRate field value."""
        member = self.get_member("AccumulationRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulation_rate.setter
    def accumulation_rate(self, value: np.float32) -> None:
        """Set the AccumulationRate field value."""
        member = self.get_member("AccumulationRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulationRate", fields.FieldFloat(value=value)
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

