"""Generated component: ParticleLightsModule."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleLightsModule(GeneratedComponent, IParticleSystemModule, IParticleRenderer, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleLightsModule.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleLightsModule"

    def __init__(self, template_light: str | Light | None = None, lights_ratio: primitives.Float | None = None, max_lights: primitives.Int | None = None, multiply_color_by_particle: primitives.Bool | None = None, multiply_intensity_by_alpha: primitives.Bool | None = None, multiply_range_by_size: primitives.Bool | None = None, range_multiplier: primitives.Float | None = None, intensity_multiplier: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            template_light: Initial value for TemplateLight.
            lights_ratio: Initial value for LightsRatio.
            max_lights: Initial value for MaxLights.
            multiply_color_by_particle: Initial value for MultiplyColorByParticle.
            multiply_intensity_by_alpha: Initial value for MultiplyIntensityByAlpha.
            multiply_range_by_size: Initial value for MultiplyRangeBySize.
            range_multiplier: Initial value for RangeMultiplier.
            intensity_multiplier: Initial value for IntensityMultiplier.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if template_light is not None:
            self.template_light = template_light
        if lights_ratio is not None:
            self.lights_ratio = lights_ratio
        if max_lights is not None:
            self.max_lights = max_lights
        if multiply_color_by_particle is not None:
            self.multiply_color_by_particle = multiply_color_by_particle
        if multiply_intensity_by_alpha is not None:
            self.multiply_intensity_by_alpha = multiply_intensity_by_alpha
        if multiply_range_by_size is not None:
            self.multiply_range_by_size = multiply_range_by_size
        if range_multiplier is not None:
            self.range_multiplier = range_multiplier
        if intensity_multiplier is not None:
            self.intensity_multiplier = intensity_multiplier

    @property
    def template_light(self) -> str | None:
        """Target ID of the TemplateLight reference (targets Light)."""
        member = self.get_member("TemplateLight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template_light.setter
    def template_light(self, target: str | Light | None) -> None:
        """Set the TemplateLight reference by target ID or Light instance."""
        target_id: str | None = target.id if isinstance(target, Light) else target  # type: ignore[assignment]
        member = self.get_member("TemplateLight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TemplateLight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Light'),
            )

    @property
    def lights_ratio(self) -> primitives.Float | None:
        """The LightsRatio field value."""
        member = self.get_member("LightsRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lights_ratio.setter
    def lights_ratio(self, value: primitives.Float) -> None:
        """Set the LightsRatio field value."""
        member = self.get_member("LightsRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LightsRatio", fields.FieldFloat(value=value)
            )

    @property
    def distribution(self) -> members.FieldEnum | None:
        """The Distribution member."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @distribution.setter
    def distribution(self, value: members.FieldEnum) -> None:
        """Set the Distribution member."""
        self.set_member("Distribution", value)

    @property
    def max_lights(self) -> primitives.Int | None:
        """The MaxLights field value."""
        member = self.get_member("MaxLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_lights.setter
    def max_lights(self, value: primitives.Int) -> None:
        """Set the MaxLights field value."""
        member = self.get_member("MaxLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxLights", fields.FieldInt(value=value)
            )

    @property
    def multiply_color_by_particle(self) -> primitives.Bool | None:
        """The MultiplyColorByParticle field value."""
        member = self.get_member("MultiplyColorByParticle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiply_color_by_particle.setter
    def multiply_color_by_particle(self, value: primitives.Bool) -> None:
        """Set the MultiplyColorByParticle field value."""
        member = self.get_member("MultiplyColorByParticle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiplyColorByParticle", fields.FieldBool(value=value)
            )

    @property
    def multiply_intensity_by_alpha(self) -> primitives.Bool | None:
        """The MultiplyIntensityByAlpha field value."""
        member = self.get_member("MultiplyIntensityByAlpha")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiply_intensity_by_alpha.setter
    def multiply_intensity_by_alpha(self, value: primitives.Bool) -> None:
        """Set the MultiplyIntensityByAlpha field value."""
        member = self.get_member("MultiplyIntensityByAlpha")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiplyIntensityByAlpha", fields.FieldBool(value=value)
            )

    @property
    def multiply_range_by_size(self) -> primitives.Bool | None:
        """The MultiplyRangeBySize field value."""
        member = self.get_member("MultiplyRangeBySize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiply_range_by_size.setter
    def multiply_range_by_size(self, value: primitives.Bool) -> None:
        """Set the MultiplyRangeBySize field value."""
        member = self.get_member("MultiplyRangeBySize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MultiplyRangeBySize", fields.FieldBool(value=value)
            )

    @property
    def angle_multiplier(self) -> members.FieldEnum | None:
        """The AngleMultiplier member."""
        member = self.get_member("AngleMultiplier")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @angle_multiplier.setter
    def angle_multiplier(self, value: members.FieldEnum) -> None:
        """Set the AngleMultiplier member."""
        self.set_member("AngleMultiplier", value)

    @property
    def range_multiplier(self) -> primitives.Float | None:
        """The RangeMultiplier field value."""
        member = self.get_member("RangeMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_multiplier.setter
    def range_multiplier(self, value: primitives.Float) -> None:
        """Set the RangeMultiplier field value."""
        member = self.get_member("RangeMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RangeMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def intensity_multiplier(self) -> primitives.Float | None:
        """The IntensityMultiplier field value."""
        member = self.get_member("IntensityMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intensity_multiplier.setter
    def intensity_multiplier(self, value: primitives.Float) -> None:
        """Set the IntensityMultiplier field value."""
        member = self.get_member("IntensityMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IntensityMultiplier", fields.FieldFloat(value=value)
            )

