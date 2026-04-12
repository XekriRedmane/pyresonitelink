"""Generated component: MeshEmitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.mesh_emission_source import MeshEmissionSource
from pyresonitelink.generated._enums.mesh_emitter_direction import MeshEmitterDirection
from pyresonitelink.generated._enums.wrap_mode import WrapMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.iparticle_system_emitter import IParticleSystemEmitter


class MeshEmitter(GeneratedComponent, IParticleSystemEmitter):
    """The MeshEmitter component allows for emitting particles from a mesh.

This is part of the Photon Dust system by Frooxius

    Category: Rendering/Particle System/Emitters

    **Related Components**: * SkinnedMeshEmitter
* Photon Dust
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.MeshEmitter"

    def __init__(self, system: str | ParticleSystem | None = None, rate: primitives.Float | None = None, burst_on_activated_min: primitives.Float | None = None, burst_on_activated_max: primitives.Float | None = None, burst_on_start: primitives.Bool | None = None, emit_from: MeshEmissionSource | str | None = None, use_vertex_colors: primitives.Bool | None = None, uniform_distribution: primitives.Bool | None = None, direction_mode: MeshEmitterDirection | str | None = None, direction: primitives.Float3 | None = None, random_direction_weight: primitives.Float | None = None, color_texture: str | IAssetProvider[Texture2D] | None = None, wrap_mode: WrapMode | str | None = None, uv_offset: primitives.Float2 | None = None, uv_scale: primitives.Float2 | None = None, mesh: str | IAssetProvider[Mesh] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            system: Initial value for System.
            rate: Initial value for Rate.
            burst_on_activated_min: Initial value for BurstOnActivatedMin.
            burst_on_activated_max: Initial value for BurstOnActivatedMax.
            burst_on_start: Initial value for BurstOnStart.
            emit_from: Initial value for EmitFrom.
            use_vertex_colors: Initial value for UseVertexColors.
            uniform_distribution: Initial value for UniformDistribution.
            direction_mode: Initial value for DirectionMode.
            direction: Initial value for Direction.
            random_direction_weight: Initial value for RandomDirectionWeight.
            color_texture: Initial value for ColorTexture.
            wrap_mode: Initial value for WrapMode.
            uv_offset: Initial value for UVOffset.
            uv_scale: Initial value for UVScale.
            mesh: Initial value for Mesh.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if system is not None:
            self.system = system
        if rate is not None:
            self.rate = rate
        if burst_on_activated_min is not None:
            self.burst_on_activated_min = burst_on_activated_min
        if burst_on_activated_max is not None:
            self.burst_on_activated_max = burst_on_activated_max
        if burst_on_start is not None:
            self.burst_on_start = burst_on_start
        if emit_from is not None:
            self.emit_from = emit_from
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if uniform_distribution is not None:
            self.uniform_distribution = uniform_distribution
        if direction_mode is not None:
            self.direction_mode = direction_mode
        if direction is not None:
            self.direction = direction
        if random_direction_weight is not None:
            self.random_direction_weight = random_direction_weight
        if color_texture is not None:
            self.color_texture = color_texture
        if wrap_mode is not None:
            self.wrap_mode = wrap_mode
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if mesh is not None:
            self.mesh = mesh

    @property
    def system(self) -> str | None:
        """Target ID of the System reference (targets ParticleSystem)."""
        member = self.get_member("System")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @system.setter
    def system(self, target: str | ParticleSystem | None) -> None:
        """Set the System reference by target ID or ParticleSystem instance."""
        target_id: str | None = target.id if isinstance(target, ParticleSystem) else target  # type: ignore[assignment]
        member = self.get_member("System")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "System",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleSystem'),
            )

    @property
    def rate(self) -> primitives.Float | None:
        """The Rate field value."""
        member = self.get_member("Rate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate.setter
    def rate(self, value: primitives.Float) -> None:
        """Set the Rate field value."""
        member = self.get_member("Rate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rate", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_activated_min(self) -> primitives.Float | None:
        """The BurstOnActivatedMin field value."""
        member = self.get_member("BurstOnActivatedMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_activated_min.setter
    def burst_on_activated_min(self, value: primitives.Float) -> None:
        """Set the BurstOnActivatedMin field value."""
        member = self.get_member("BurstOnActivatedMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnActivatedMin", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_activated_max(self) -> primitives.Float | None:
        """The BurstOnActivatedMax field value."""
        member = self.get_member("BurstOnActivatedMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_activated_max.setter
    def burst_on_activated_max(self, value: primitives.Float) -> None:
        """Set the BurstOnActivatedMax field value."""
        member = self.get_member("BurstOnActivatedMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnActivatedMax", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_start(self) -> primitives.Bool | None:
        """The BurstOnStart field value."""
        member = self.get_member("BurstOnStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_start.setter
    def burst_on_start(self, value: primitives.Bool) -> None:
        """Set the BurstOnStart field value."""
        member = self.get_member("BurstOnStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnStart", fields.FieldBool(value=value)
            )

    @property
    def emit_from(self) -> MeshEmissionSource | None:
        """What parts of the mesh to emit from for the specified mesh."""
        member = self.get_member("EmitFrom")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MeshEmissionSource(member.value)
        return None

    @emit_from.setter
    def emit_from(self, value: MeshEmissionSource | str) -> None:
        """Set EmitFrom. What parts of the mesh to emit from for the specified mesh."""
        member = self.get_member("EmitFrom")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "EmitFrom",
                members.FieldEnum(value=str(value)),
            )

    @property
    def use_vertex_colors(self) -> primitives.Bool | None:
        """Whether or not to use interpolated vertex colors of the mesh this is emitting from."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: primitives.Bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def uniform_distribution(self) -> primitives.Bool | None:
        """The UniformDistribution field value."""
        member = self.get_member("UniformDistribution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uniform_distribution.setter
    def uniform_distribution(self, value: primitives.Bool) -> None:
        """Set the UniformDistribution field value."""
        member = self.get_member("UniformDistribution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UniformDistribution", fields.FieldBool(value=value)
            )

    @property
    def direction_mode(self) -> MeshEmitterDirection | None:
        """How to determine the emission direction of particles emitted from this mesh."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MeshEmitterDirection(member.value)
        return None

    @direction_mode.setter
    def direction_mode(self, value: MeshEmitterDirection | str) -> None:
        """Set DirectionMode. How to determine the emission direction of particles emitted from this mesh."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DirectionMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def direction(self) -> primitives.Float3 | None:
        """The Direction field value."""
        member = self.get_member("Direction")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction.setter
    def direction(self, value: primitives.Float3) -> None:
        """Set the Direction field value."""
        member = self.get_member("Direction")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Direction", fields.FieldFloat3(value=value)
            )

    @property
    def random_direction_weight(self) -> primitives.Float | None:
        """The RandomDirectionWeight field value."""
        member = self.get_member("RandomDirectionWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @random_direction_weight.setter
    def random_direction_weight(self, value: primitives.Float) -> None:
        """Set the RandomDirectionWeight field value."""
        member = self.get_member("RandomDirectionWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RandomDirectionWeight", fields.FieldFloat(value=value)
            )

    @property
    def color_texture(self) -> str | None:
        """The texture to sample from for the particle starting color, which is sampled from the texture via the uv coordinate of the mesh surface the particle was emitted from."""
        member = self.get_member("ColorTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_texture.setter
    def color_texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the ColorTexture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ColorTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColorTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def wrap_mode(self) -> WrapMode | None:
        """How to wrap the texture sampling for the particle color when the uvs are beyond a 0 to 1 range."""
        member = self.get_member("WrapMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WrapMode(member.value)
        return None

    @wrap_mode.setter
    def wrap_mode(self, value: WrapMode | str) -> None:
        """Set WrapMode. How to wrap the texture sampling for the particle color when the uvs are beyond a 0 to 1 range."""
        member = self.get_member("WrapMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def uv_offset(self) -> primitives.Float2 | None:
        """How much to offset the UVs before sampling for particle color."""
        member = self.get_member("UVOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_offset.setter
    def uv_offset(self, value: primitives.Float2) -> None:
        """Set the UVOffset field value."""
        member = self.get_member("UVOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVOffset", fields.FieldFloat2(value=value)
            )

    @property
    def uv_scale(self) -> primitives.Float2 | None:
        """How much to scale up/down the UVs before sampling for particle color."""
        member = self.get_member("UVScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uv_scale.setter
    def uv_scale(self, value: primitives.Float2) -> None:
        """Set the UVScale field value."""
        member = self.get_member("UVScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UVScale", fields.FieldFloat2(value=value)
            )

    @property
    def clip_rect(self) -> members.FieldEnum | None:
        """Particles will only emit if the mesh surface uv is within this clip rectangle."""
        member = self.get_member("ClipRect")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @clip_rect.setter
    def clip_rect(self, value: members.FieldEnum) -> None:
        """Set ClipRect. Particles will only emit if the mesh surface uv is within this clip rectangle."""
        self.set_member("ClipRect", value)

    @property
    def mesh(self) -> str | None:
        """The mesh to use for particle emission."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | IAssetProvider[Mesh] | None) -> None:
        """Set the Mesh reference by target ID or IAssetProvider[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>'),
            )

