"""Generated component: ParticleRibbonsModule."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.trail_texture_mode import TrailTextureMode
from pyresonitelink.generated._enums.motion_vector_mode import MotionVectorMode
from pyresonitelink.generated._enums.particle_follower_distribution import ParticleFollowerDistribution
from pyresonitelink.generated._enums.uniform_size_mode import UniformSizeMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleRibbonsModule(GeneratedComponent, IParticleSystemModule, IParticleRenderer, IWorldEventReceiver):
    """The ParticleRibbonsModule component makes it to where a particle system will have ribbons that connect particles based on distance and other factors.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleRibbonsModule"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, texture_mode: TrailTextureMode | str | None = None, motion_vector_mode: MotionVectorMode | str | None = None, generate_lighting_data: primitives.Bool | None = None, ribbon_point_ratio: primitives.Float | None = None, distribution: ParticleFollowerDistribution | str | None = None, max_ribbon_points: primitives.Int | None = None, interweaved_ribbon_count: primitives.Int | None = None, use_particle_color: primitives.Bool | None = None, use_particle_size: primitives.Bool | None = None, shuffle_interweaved_ribbons: primitives.Bool | None = None, size_inheritance_mode: UniformSizeMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            texture_mode: Initial value for TextureMode.
            motion_vector_mode: Initial value for MotionVectorMode.
            generate_lighting_data: Initial value for GenerateLightingData.
            ribbon_point_ratio: Initial value for RibbonPointRatio.
            distribution: Initial value for Distribution.
            max_ribbon_points: Initial value for MaxRibbonPoints.
            interweaved_ribbon_count: Initial value for InterweavedRibbonCount.
            use_particle_color: Initial value for UseParticleColor.
            use_particle_size: Initial value for UseParticleSize.
            shuffle_interweaved_ribbons: Initial value for ShuffleInterweavedRibbons.
            size_inheritance_mode: Initial value for SizeInheritanceMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if texture_mode is not None:
            self.texture_mode = texture_mode
        if motion_vector_mode is not None:
            self.motion_vector_mode = motion_vector_mode
        if generate_lighting_data is not None:
            self.generate_lighting_data = generate_lighting_data
        if ribbon_point_ratio is not None:
            self.ribbon_point_ratio = ribbon_point_ratio
        if distribution is not None:
            self.distribution = distribution
        if max_ribbon_points is not None:
            self.max_ribbon_points = max_ribbon_points
        if interweaved_ribbon_count is not None:
            self.interweaved_ribbon_count = interweaved_ribbon_count
        if use_particle_color is not None:
            self.use_particle_color = use_particle_color
        if use_particle_size is not None:
            self.use_particle_size = use_particle_size
        if shuffle_interweaved_ribbons is not None:
            self.shuffle_interweaved_ribbons = shuffle_interweaved_ribbons
        if size_inheritance_mode is not None:
            self.size_inheritance_mode = size_inheritance_mode

    @property
    def material(self) -> str | None:
        """The material to give the ribbons"""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the Material reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def texture_mode(self) -> TrailTextureMode | None:
        """How to handle viewing the texture specified on the ribbons."""
        member = self.get_member("TextureMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TrailTextureMode(member.value)
        return None

    @texture_mode.setter
    def texture_mode(self, value: TrailTextureMode | str) -> None:
        """Set TextureMode. How to handle viewing the texture specified on the ribbons."""
        member = self.get_member("TextureMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TextureMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def motion_vector_mode(self) -> MotionVectorMode | None:
        """How to handle the rendering of ribbons in regards to motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MotionVectorMode(member.value)
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: MotionVectorMode | str) -> None:
        """Set MotionVectorMode. How to handle the rendering of ribbons in regards to motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MotionVectorMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def generate_lighting_data(self) -> primitives.Bool | None:
        """Whether to generate lighting data for the ribbons."""
        member = self.get_member("GenerateLightingData")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @generate_lighting_data.setter
    def generate_lighting_data(self, value: primitives.Bool) -> None:
        """Set the GenerateLightingData field value."""
        member = self.get_member("GenerateLightingData")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GenerateLightingData", fields.FieldBool(value=value)
            )

    @property
    def ribbon_point_ratio(self) -> primitives.Float | None:
        """How many of the particles should be ribbons."""
        member = self.get_member("RibbonPointRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ribbon_point_ratio.setter
    def ribbon_point_ratio(self, value: primitives.Float) -> None:
        """Set the RibbonPointRatio field value."""
        member = self.get_member("RibbonPointRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RibbonPointRatio", fields.FieldFloat(value=value)
            )

    @property
    def distribution(self) -> ParticleFollowerDistribution | None:
        """How to distribute the ribbon followers."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ParticleFollowerDistribution(member.value)
        return None

    @distribution.setter
    def distribution(self, value: ParticleFollowerDistribution | str) -> None:
        """Set Distribution. How to distribute the ribbon followers."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Distribution",
                members.FieldEnum(value=str(value)),
            )

    @property
    def max_ribbon_points(self) -> primitives.Int | None:
        """The max amount of ribbon points there should be."""
        member = self.get_member("MaxRibbonPoints")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_ribbon_points.setter
    def max_ribbon_points(self, value: primitives.Int) -> None:
        """Set the MaxRibbonPoints field value."""
        member = self.get_member("MaxRibbonPoints")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRibbonPoints", fields.FieldInt(value=value)
            )

    @property
    def interweaved_ribbon_count(self) -> primitives.Int | None:
        """The amount of long particle-interconnected ribbons there can be, essentially multiple ribbons rather than one ribbon line."""
        member = self.get_member("InterweavedRibbonCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interweaved_ribbon_count.setter
    def interweaved_ribbon_count(self, value: primitives.Int) -> None:
        """Set the InterweavedRibbonCount field value."""
        member = self.get_member("InterweavedRibbonCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterweavedRibbonCount", fields.FieldInt(value=value)
            )

    @property
    def use_particle_color(self) -> primitives.Bool | None:
        """Whether to use the color of particles the ribbons are following."""
        member = self.get_member("UseParticleColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_particle_color.setter
    def use_particle_color(self, value: primitives.Bool) -> None:
        """Set the UseParticleColor field value."""
        member = self.get_member("UseParticleColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseParticleColor", fields.FieldBool(value=value)
            )

    @property
    def use_particle_size(self) -> primitives.Bool | None:
        """Whether to use the size of particles the ribbons should follow."""
        member = self.get_member("UseParticleSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_particle_size.setter
    def use_particle_size(self, value: primitives.Bool) -> None:
        """Set the UseParticleSize field value."""
        member = self.get_member("UseParticleSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseParticleSize", fields.FieldBool(value=value)
            )

    @property
    def shuffle_interweaved_ribbons(self) -> primitives.Bool | None:
        """Randomly moves interweaved ribbon groups to new particles when they are generated."""
        member = self.get_member("ShuffleInterweavedRibbons")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shuffle_interweaved_ribbons.setter
    def shuffle_interweaved_ribbons(self, value: primitives.Bool) -> None:
        """Set the ShuffleInterweavedRibbons field value."""
        member = self.get_member("ShuffleInterweavedRibbons")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShuffleInterweavedRibbons", fields.FieldBool(value=value)
            )

    @property
    def size_inheritance_mode(self) -> UniformSizeMode | None:
        """How to inherit the size of the particles the ribbons are following."""
        member = self.get_member("SizeInheritanceMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UniformSizeMode(member.value)
        return None

    @size_inheritance_mode.setter
    def size_inheritance_mode(self, value: UniformSizeMode | str) -> None:
        """Set SizeInheritanceMode. How to inherit the size of the particles the ribbons are following."""
        member = self.get_member("SizeInheritanceMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SizeInheritanceMode",
                members.FieldEnum(value=str(value)),
            )

