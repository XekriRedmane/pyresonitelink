"""Generated component: SkinnedMeshEmitter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.skinned_mesh_renderer import SkinnedMeshRenderer
from pyresonitelink.generated._types.iparticle_system_emitter import IParticleSystemEmitter


class SkinnedMeshEmitter(GeneratedComponent, IParticleSystemEmitter):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.SkinnedMeshEmitter.

    Category: Rendering/Particle System/Emitters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.SkinnedMeshEmitter"

    def __init__(self, system: str | ParticleSystem | None = None, rate: np.float32 | None = None, burst_on_activated_min: np.float32 | None = None, burst_on_activated_max: np.float32 | None = None, burst_on_start: bool | None = None, use_vertex_colors: bool | None = None, uniform_distribution: bool | None = None, direction: primitives.Float3 | None = None, random_direction_weight: np.float32 | None = None, color_texture: str | IAssetProvider[Texture2D] | None = None, uv_offset: primitives.Float2 | None = None, uv_scale: primitives.Float2 | None = None, skin: str | SkinnedMeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            system: Initial value for System.
            rate: Initial value for Rate.
            burst_on_activated_min: Initial value for BurstOnActivatedMin.
            burst_on_activated_max: Initial value for BurstOnActivatedMax.
            burst_on_start: Initial value for BurstOnStart.
            use_vertex_colors: Initial value for UseVertexColors.
            uniform_distribution: Initial value for UniformDistribution.
            direction: Initial value for Direction.
            random_direction_weight: Initial value for RandomDirectionWeight.
            color_texture: Initial value for ColorTexture.
            uv_offset: Initial value for UVOffset.
            uv_scale: Initial value for UVScale.
            skin: Initial value for Skin.
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
        if use_vertex_colors is not None:
            self.use_vertex_colors = use_vertex_colors
        if uniform_distribution is not None:
            self.uniform_distribution = uniform_distribution
        if direction is not None:
            self.direction = direction
        if random_direction_weight is not None:
            self.random_direction_weight = random_direction_weight
        if color_texture is not None:
            self.color_texture = color_texture
        if uv_offset is not None:
            self.uv_offset = uv_offset
        if uv_scale is not None:
            self.uv_scale = uv_scale
        if skin is not None:
            self.skin = skin

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
    def rate(self) -> np.float32 | None:
        """The Rate field value."""
        member = self.get_member("Rate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate.setter
    def rate(self, value: np.float32) -> None:
        """Set the Rate field value."""
        member = self.get_member("Rate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rate", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_activated_min(self) -> np.float32 | None:
        """The BurstOnActivatedMin field value."""
        member = self.get_member("BurstOnActivatedMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_activated_min.setter
    def burst_on_activated_min(self, value: np.float32) -> None:
        """Set the BurstOnActivatedMin field value."""
        member = self.get_member("BurstOnActivatedMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnActivatedMin", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_activated_max(self) -> np.float32 | None:
        """The BurstOnActivatedMax field value."""
        member = self.get_member("BurstOnActivatedMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_activated_max.setter
    def burst_on_activated_max(self, value: np.float32) -> None:
        """Set the BurstOnActivatedMax field value."""
        member = self.get_member("BurstOnActivatedMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnActivatedMax", fields.FieldFloat(value=value)
            )

    @property
    def burst_on_start(self) -> bool | None:
        """The BurstOnStart field value."""
        member = self.get_member("BurstOnStart")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @burst_on_start.setter
    def burst_on_start(self, value: bool) -> None:
        """Set the BurstOnStart field value."""
        member = self.get_member("BurstOnStart")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BurstOnStart", fields.FieldBool(value=value)
            )

    @property
    def emit_from(self) -> members.FieldEnum | None:
        """The EmitFrom member."""
        member = self.get_member("EmitFrom")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @emit_from.setter
    def emit_from(self, value: members.FieldEnum) -> None:
        """Set the EmitFrom member."""
        self.set_member("EmitFrom", value)

    @property
    def use_vertex_colors(self) -> bool | None:
        """The UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_vertex_colors.setter
    def use_vertex_colors(self, value: bool) -> None:
        """Set the UseVertexColors field value."""
        member = self.get_member("UseVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseVertexColors", fields.FieldBool(value=value)
            )

    @property
    def uniform_distribution(self) -> bool | None:
        """The UniformDistribution field value."""
        member = self.get_member("UniformDistribution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uniform_distribution.setter
    def uniform_distribution(self, value: bool) -> None:
        """Set the UniformDistribution field value."""
        member = self.get_member("UniformDistribution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UniformDistribution", fields.FieldBool(value=value)
            )

    @property
    def direction_mode(self) -> members.FieldEnum | None:
        """The DirectionMode member."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @direction_mode.setter
    def direction_mode(self, value: members.FieldEnum) -> None:
        """Set the DirectionMode member."""
        self.set_member("DirectionMode", value)

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
    def random_direction_weight(self) -> np.float32 | None:
        """The RandomDirectionWeight field value."""
        member = self.get_member("RandomDirectionWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @random_direction_weight.setter
    def random_direction_weight(self, value: np.float32) -> None:
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
        """Target ID of the ColorTexture reference (targets IAssetProvider[Texture2D])."""
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
    def wrap_mode(self) -> members.FieldEnum | None:
        """The WrapMode member."""
        member = self.get_member("WrapMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @wrap_mode.setter
    def wrap_mode(self, value: members.FieldEnum) -> None:
        """Set the WrapMode member."""
        self.set_member("WrapMode", value)

    @property
    def uv_offset(self) -> primitives.Float2 | None:
        """The UVOffset field value."""
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
        """The UVScale field value."""
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
        """The ClipRect member."""
        member = self.get_member("ClipRect")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @clip_rect.setter
    def clip_rect(self, value: members.FieldEnum) -> None:
        """Set the ClipRect member."""
        self.set_member("ClipRect", value)

    @property
    def skin(self) -> str | None:
        """Target ID of the Skin reference (targets SkinnedMeshRenderer)."""
        member = self.get_member("Skin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @skin.setter
    def skin(self, target: str | SkinnedMeshRenderer | None) -> None:
        """Set the Skin reference by target ID or SkinnedMeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, SkinnedMeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Skin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Skin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SkinnedMeshRenderer'),
            )

