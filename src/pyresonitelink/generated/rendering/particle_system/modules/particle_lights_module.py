"""Generated component: ParticleLightsModule."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.particle_follower_distribution import ParticleFollowerDistribution
from pyresonitelink.generated._enums.angle_multiplier import AngleMultiplier
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.light import Light
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleLightsModule(GeneratedComponent, IParticleSystemModule, IParticleRenderer, IWorldEventReceiver):
    """The ParticleLightsModule makes a particle system create lights every so often for emitted particles that follow the particle they're assigned to.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleLightsModule"

    def __init__(self, template_light: str | Light | None = None, lights_ratio: primitives.Float | None = None, distribution: ParticleFollowerDistribution | str | None = None, max_lights: primitives.Int | None = None, multiply_color_by_particle: primitives.Bool | None = None, multiply_intensity_by_alpha: primitives.Bool | None = None, multiply_range_by_size: primitives.Bool | None = None, angle_multiplier: AngleMultiplier | str | None = None, range_multiplier: primitives.Float | None = None, intensity_multiplier: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            template_light: Initial value for TemplateLight.
            lights_ratio: Initial value for LightsRatio.
            distribution: Initial value for Distribution.
            max_lights: Initial value for MaxLights.
            multiply_color_by_particle: Initial value for MultiplyColorByParticle.
            multiply_intensity_by_alpha: Initial value for MultiplyIntensityByAlpha.
            multiply_range_by_size: Initial value for MultiplyRangeBySize.
            angle_multiplier: Initial value for AngleMultiplier.
            range_multiplier: Initial value for RangeMultiplier.
            intensity_multiplier: Initial value for IntensityMultiplier.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if template_light is not None:
            self.template_light = template_light
        if lights_ratio is not None:
            self.lights_ratio = lights_ratio
        if distribution is not None:
            self.distribution = distribution
        if max_lights is not None:
            self.max_lights = max_lights
        if multiply_color_by_particle is not None:
            self.multiply_color_by_particle = multiply_color_by_particle
        if multiply_intensity_by_alpha is not None:
            self.multiply_intensity_by_alpha = multiply_intensity_by_alpha
        if multiply_range_by_size is not None:
            self.multiply_range_by_size = multiply_range_by_size
        if angle_multiplier is not None:
            self.angle_multiplier = angle_multiplier
        if range_multiplier is not None:
            self.range_multiplier = range_multiplier
        if intensity_multiplier is not None:
            self.intensity_multiplier = intensity_multiplier

    @property
    def template_light(self) -> str | None:
        """The light to use as a template."""
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
        """How many lights as a percentage there should be from a 0 to 1 range."""
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
    def distribution(self) -> ParticleFollowerDistribution | None:
        """How to distribute the lights among the particles being emitted."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ParticleFollowerDistribution(member.value)
        return None

    @distribution.setter
    def distribution(self, value: ParticleFollowerDistribution | str) -> None:
        """Set Distribution. How to distribute the lights among the particles being emitted."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Distribution",
                members.FieldEnum(value=str(value)),
            )

    @property
    def max_lights(self) -> primitives.Int | None:
        """The maximum number of lights that the particle system can have."""
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
        """Whether to multiply the color of the lights by the color of the particle it is attached to."""
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
        """Whether to multiply the intensity of the lights by the alpha channel of the color of the particle it is attached to."""
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
        """Whether to multiply the range of the light based on the size of the particle it is attached to."""
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
    def angle_multiplier(self) -> AngleMultiplier | None:
        """How to influence the angle of the light based on the angle of the particle it is following."""
        member = self.get_member("AngleMultiplier")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AngleMultiplier(member.value)
        return None

    @angle_multiplier.setter
    def angle_multiplier(self, value: AngleMultiplier | str) -> None:
        """Set AngleMultiplier. How to influence the angle of the light based on the angle of the particle it is following."""
        member = self.get_member("AngleMultiplier")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AngleMultiplier",
                members.FieldEnum(value=str(value)),
            )

    @property
    def range_multiplier(self) -> primitives.Float | None:
        """How much to amplify the range of the light."""
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
        """How much to amplify the intensity of the light."""
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

