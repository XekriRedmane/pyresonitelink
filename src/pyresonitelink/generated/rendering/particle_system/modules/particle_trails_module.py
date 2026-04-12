"""Generated component: ParticleTrailsModule."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.trail_texture_mode import TrailTextureMode
from pyresonitelink.generated._enums.motion_vector_mode import MotionVectorMode
from pyresonitelink.generated._enums.particle_follower_distribution import ParticleFollowerDistribution
from pyresonitelink.generated._enums.trail_particle_inheritance import TrailParticleInheritance
from pyresonitelink.generated._enums.uniform_size_mode import UniformSizeMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iparticle_renderer import IParticleRenderer
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleTrailsModule(GeneratedComponent, IParticleSystemModule, IParticleRenderer, IWorldEventReceiver):
    """The ParticleTrailsModule component allows particles to have trails with different properties. This can be added multiple times for different trail types.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleTrailsModule"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, texture_mode: TrailTextureMode | str | None = None, motion_vector_mode: MotionVectorMode | str | None = None, generate_lighting_data: primitives.Bool | None = None, trails_ratio: primitives.Float | None = None, distribution: ParticleFollowerDistribution | str | None = None, max_trails: primitives.Int | None = None, min_vertex_distance: primitives.Float | None = None, trail_dies_with_particle: primitives.Bool | None = None, particle_color_inheritance: TrailParticleInheritance | str | None = None, particle_size_inheritance: TrailParticleInheritance | str | None = None, size_inheritance_mode: UniformSizeMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            texture_mode: Initial value for TextureMode.
            motion_vector_mode: Initial value for MotionVectorMode.
            generate_lighting_data: Initial value for GenerateLightingData.
            trails_ratio: Initial value for TrailsRatio.
            distribution: Initial value for Distribution.
            max_trails: Initial value for MaxTrails.
            min_vertex_distance: Initial value for MinVertexDistance.
            trail_dies_with_particle: Initial value for TrailDiesWithParticle.
            particle_color_inheritance: Initial value for ParticleColorInheritance.
            particle_size_inheritance: Initial value for ParticleSizeInheritance.
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
        if trails_ratio is not None:
            self.trails_ratio = trails_ratio
        if distribution is not None:
            self.distribution = distribution
        if max_trails is not None:
            self.max_trails = max_trails
        if min_vertex_distance is not None:
            self.min_vertex_distance = min_vertex_distance
        if trail_dies_with_particle is not None:
            self.trail_dies_with_particle = trail_dies_with_particle
        if particle_color_inheritance is not None:
            self.particle_color_inheritance = particle_color_inheritance
        if particle_size_inheritance is not None:
            self.particle_size_inheritance = particle_size_inheritance
        if size_inheritance_mode is not None:
            self.size_inheritance_mode = size_inheritance_mode

    @property
    def material(self) -> str | None:
        """The material the particle trails should have."""
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
        """How to handle the textures on trails."""
        member = self.get_member("TextureMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TrailTextureMode(member.value)
        return None

    @texture_mode.setter
    def texture_mode(self, value: TrailTextureMode | str) -> None:
        """Set TextureMode. How to handle the textures on trails."""
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
        """How to handle rendering the trails when it comes to motion vectors."""
        member = self.get_member("MotionVectorMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MotionVectorMode(member.value)
        return None

    @motion_vector_mode.setter
    def motion_vector_mode(self, value: MotionVectorMode | str) -> None:
        """Set MotionVectorMode. How to handle rendering the trails when it comes to motion vectors."""
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
        """Whether the trails have lighting data."""
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
    def trails_ratio(self) -> primitives.Float | None:
        """How many of the particles as a 01 percentage should have trails"""
        member = self.get_member("TrailsRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trails_ratio.setter
    def trails_ratio(self, value: primitives.Float) -> None:
        """Set the TrailsRatio field value."""
        member = self.get_member("TrailsRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailsRatio", fields.FieldFloat(value=value)
            )

    @property
    def distribution(self) -> ParticleFollowerDistribution | None:
        """How to distribute the followers for this module."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ParticleFollowerDistribution(member.value)
        return None

    @distribution.setter
    def distribution(self, value: ParticleFollowerDistribution | str) -> None:
        """Set Distribution. How to distribute the followers for this module."""
        member = self.get_member("Distribution")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Distribution",
                members.FieldEnum(value=str(value)),
            )

    @property
    def max_trails(self) -> primitives.Int | None:
        """The maximum amount of trails the system can have of this particular trail type."""
        member = self.get_member("MaxTrails")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_trails.setter
    def max_trails(self, value: primitives.Int) -> None:
        """Set the MaxTrails field value."""
        member = self.get_member("MaxTrails")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTrails", fields.FieldInt(value=value)
            )

    @property
    def simulation_space(self) -> members.SyncObject | None:
        """What Transform space to simulate the trails for this module in?"""
        member = self.get_member("SimulationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @simulation_space.setter
    def simulation_space(self, value: members.SyncObject) -> None:
        """Set SimulationSpace. What Transform space to simulate the trails for this module in?"""
        self.set_member("SimulationSpace", value)

    @property
    def min_vertex_distance(self) -> primitives.Float | None:
        """The minimum vertex distance between trail segments when generating trail geometry."""
        member = self.get_member("MinVertexDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_vertex_distance.setter
    def min_vertex_distance(self, value: primitives.Float) -> None:
        """Set the MinVertexDistance field value."""
        member = self.get_member("MinVertexDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinVertexDistance", fields.FieldFloat(value=value)
            )

    @property
    def trail_dies_with_particle(self) -> primitives.Bool | None:
        """Whether the trail disappears instantly when the particle dies or not."""
        member = self.get_member("TrailDiesWithParticle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trail_dies_with_particle.setter
    def trail_dies_with_particle(self, value: primitives.Bool) -> None:
        """Set the TrailDiesWithParticle field value."""
        member = self.get_member("TrailDiesWithParticle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailDiesWithParticle", fields.FieldBool(value=value)
            )

    @property
    def particle_color_inheritance(self) -> TrailParticleInheritance | None:
        """How the trail inherits the color of the particle it's following."""
        member = self.get_member("ParticleColorInheritance")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TrailParticleInheritance(member.value)
        return None

    @particle_color_inheritance.setter
    def particle_color_inheritance(self, value: TrailParticleInheritance | str) -> None:
        """Set ParticleColorInheritance. How the trail inherits the color of the particle it's following."""
        member = self.get_member("ParticleColorInheritance")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ParticleColorInheritance",
                members.FieldEnum(value=str(value)),
            )

    @property
    def particle_size_inheritance(self) -> TrailParticleInheritance | None:
        """How the trail inherits the size of the particle it's following."""
        member = self.get_member("ParticleSizeInheritance")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return TrailParticleInheritance(member.value)
        return None

    @particle_size_inheritance.setter
    def particle_size_inheritance(self, value: TrailParticleInheritance | str) -> None:
        """Set ParticleSizeInheritance. How the trail inherits the size of the particle it's following."""
        member = self.get_member("ParticleSizeInheritance")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ParticleSizeInheritance",
                members.FieldEnum(value=str(value)),
            )

    @property
    def size_inheritance_mode(self) -> UniformSizeMode | None:
        """How the size the trail inherited from the particle it's followinh should be applied."""
        member = self.get_member("SizeInheritanceMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UniformSizeMode(member.value)
        return None

    @size_inheritance_mode.setter
    def size_inheritance_mode(self, value: UniformSizeMode | str) -> None:
        """Set SizeInheritanceMode. How the size the trail inherited from the particle it's followinh should be applied."""
        member = self.get_member("SizeInheritanceMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SizeInheritanceMode",
                members.FieldEnum(value=str(value)),
            )

