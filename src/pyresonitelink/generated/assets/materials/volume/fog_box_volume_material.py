"""Generated component: FogBoxVolumeMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.color import Color
from pyresonitelink.generated._enums.saturation import Saturation
from pyresonitelink.generated._enums.accumulation import Accumulation
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FogBoxVolumeMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The FogBoxVolumeMaterial is a material used to create cube-shaped volumetric fog on a mesh, such as a Texture3D. Using this material on non-cube-like meshes may result in visual artifacts and/or denser fog in places where the corners of the cube would be.

    Category: Assets/Materials/Volume

    **Description**: The FogBoxVolumeMaterial is a material used to create cube-shaped volumetric fog on a mesh, such as a Texture3D. Using this material on non-cube-like meshes may result in visual artifacts and/or denser fog in places where the corners of the cube would be. 

Although only cube-shaped meshes are officially supported, users may use the LookAtUser component targeting the local User along with a spherical mesh to create an illusion of a sphere-shaped fog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FogBoxVolumeMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, base_color: primitives.ColorX | None = None, accumulation_color: primitives.ColorX | None = None, accumulation_color_bottom: primitives.ColorX | None = None, accumulation_color_top: primitives.ColorX | None = None, fog_start: primitives.Float | None = None, fog_end: primitives.Float | None = None, fog_density: primitives.Float | None = None, gamma_curve: primitives.Float | None = None, world_space: primitives.Bool | None = None, color_mode: Color | str | None = None, saturation_mode: Saturation | str | None = None, accumulation_mode: Accumulation | str | None = None, accumulation_rate: primitives.Float | None = None, blend_mode: BlendMode | str | None = None, render_queue: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
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
            color_mode: Initial value for ColorMode.
            saturation_mode: Initial value for SaturationMode.
            accumulation_mode: Initial value for AccumulationMode.
            accumulation_rate: Initial value for AccumulationRate.
            blend_mode: Initial value for BlendMode.
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
        if color_mode is not None:
            self.color_mode = color_mode
        if saturation_mode is not None:
            self.saturation_mode = saturation_mode
        if accumulation_mode is not None:
            self.accumulation_mode = accumulation_mode
        if accumulation_rate is not None:
            self.accumulation_rate = accumulation_rate
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if render_queue is not None:
            self.render_queue = render_queue

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
    def fog_start(self) -> primitives.Float | None:
        """The FogStart field value."""
        member = self.get_member("FogStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fog_start.setter
    def fog_start(self, value: primitives.Float) -> None:
        """Set the FogStart field value."""
        member = self.get_member("FogStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FogStart", fields.FieldFloat(value=value)
            )

    @property
    def fog_end(self) -> primitives.Float | None:
        """The FogEnd field value."""
        member = self.get_member("FogEnd")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fog_end.setter
    def fog_end(self, value: primitives.Float) -> None:
        """Set the FogEnd field value."""
        member = self.get_member("FogEnd")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FogEnd", fields.FieldFloat(value=value)
            )

    @property
    def fog_density(self) -> primitives.Float | None:
        """The FogDensity field value."""
        member = self.get_member("FogDensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fog_density.setter
    def fog_density(self, value: primitives.Float) -> None:
        """Set the FogDensity field value."""
        member = self.get_member("FogDensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FogDensity", fields.FieldFloat(value=value)
            )

    @property
    def gamma_curve(self) -> primitives.Float | None:
        """The GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gamma_curve.setter
    def gamma_curve(self, value: primitives.Float) -> None:
        """Set the GammaCurve field value."""
        member = self.get_member("GammaCurve")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GammaCurve", fields.FieldFloat(value=value)
            )

    @property
    def world_space(self) -> primitives.Bool | None:
        """The WorldSpace field value."""
        member = self.get_member("WorldSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @world_space.setter
    def world_space(self, value: primitives.Bool) -> None:
        """Set the WorldSpace field value."""
        member = self.get_member("WorldSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorldSpace", fields.FieldBool(value=value)
            )

    @property
    def color_mode(self) -> Color | None:
        """The ColorMode enum value."""
        member = self.get_member("ColorMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Color(member.value)
        return None

    @color_mode.setter
    def color_mode(self, value: Color | str) -> None:
        """Set the ColorMode enum value."""
        member = self.get_member("ColorMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ColorMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def saturation_mode(self) -> Saturation | None:
        """The SaturationMode enum value."""
        member = self.get_member("SaturationMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Saturation(member.value)
        return None

    @saturation_mode.setter
    def saturation_mode(self, value: Saturation | str) -> None:
        """Set the SaturationMode enum value."""
        member = self.get_member("SaturationMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SaturationMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def accumulation_mode(self) -> Accumulation | None:
        """The AccumulationMode enum value."""
        member = self.get_member("AccumulationMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Accumulation(member.value)
        return None

    @accumulation_mode.setter
    def accumulation_mode(self, value: Accumulation | str) -> None:
        """Set the AccumulationMode enum value."""
        member = self.get_member("AccumulationMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AccumulationMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def accumulation_rate(self) -> primitives.Float | None:
        """The AccumulationRate field value."""
        member = self.get_member("AccumulationRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulation_rate.setter
    def accumulation_rate(self, value: primitives.Float) -> None:
        """Set the AccumulationRate field value."""
        member = self.get_member("AccumulationRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulationRate", fields.FieldFloat(value=value)
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

