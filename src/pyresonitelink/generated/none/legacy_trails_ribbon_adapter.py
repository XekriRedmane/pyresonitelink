"""Generated component: LegacyTrailsRibbonAdapter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.legacy_particle_trail_mode import LegacyParticleTrailMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.trail_particle_inheritance import TrailParticleInheritance
from pyresonitelink.generated._types.root_space import RootSpace
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyTrailsRibbonAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Legacy Trails Ribbon Adapter component is used to convert legacy content from the old particle system driven by Unity to Photon Dust.

    Used in legacy content. do not use in new content.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.LegacyTrailsRibbonAdapter"

    def __init__(self, trails_mode: LegacyParticleTrailMode | str | None = None, particle_size_affects_trail_width: primitives.Bool | None = None, inherit_trail_color_from_particle: primitives.Bool | None = None, trail_world_space: primitives.Bool | None = None, trails_module: str | IField[primitives.Bool] | None = None, ribbon_module: str | IField[primitives.Bool] | None = None, ribbon_use_particle_size: str | IField[primitives.Bool] | None = None, ribbon_use_particle_color: str | IField[primitives.Bool] | None = None, trail_size_inheritance: str | IField[TrailParticleInheritance] | None = None, trail_color_inheritance: str | IField[TrailParticleInheritance] | None = None, trails_space: str | RootSpace | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            trails_mode: Initial value for TrailsMode.
            particle_size_affects_trail_width: Initial value for ParticleSizeAffectsTrailWidth.
            inherit_trail_color_from_particle: Initial value for InheritTrailColorFromParticle.
            trail_world_space: Initial value for TrailWorldSpace.
            trails_module: Initial value for TrailsModule.
            ribbon_module: Initial value for RibbonModule.
            ribbon_use_particle_size: Initial value for RibbonUseParticleSize.
            ribbon_use_particle_color: Initial value for RibbonUseParticleColor.
            trail_size_inheritance: Initial value for TrailSizeInheritance.
            trail_color_inheritance: Initial value for TrailColorInheritance.
            trails_space: Initial value for TrailsSpace.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if trails_mode is not None:
            self.trails_mode = trails_mode
        if particle_size_affects_trail_width is not None:
            self.particle_size_affects_trail_width = particle_size_affects_trail_width
        if inherit_trail_color_from_particle is not None:
            self.inherit_trail_color_from_particle = inherit_trail_color_from_particle
        if trail_world_space is not None:
            self.trail_world_space = trail_world_space
        if trails_module is not None:
            self.trails_module = trails_module
        if ribbon_module is not None:
            self.ribbon_module = ribbon_module
        if ribbon_use_particle_size is not None:
            self.ribbon_use_particle_size = ribbon_use_particle_size
        if ribbon_use_particle_color is not None:
            self.ribbon_use_particle_color = ribbon_use_particle_color
        if trail_size_inheritance is not None:
            self.trail_size_inheritance = trail_size_inheritance
        if trail_color_inheritance is not None:
            self.trail_color_inheritance = trail_color_inheritance
        if trails_space is not None:
            self.trails_space = trails_space

    @property
    def trails_mode(self) -> LegacyParticleTrailMode | None:
        """The enum used to control the conversion from legacy trails to Photon Dust."""
        member = self.get_member("TrailsMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LegacyParticleTrailMode(member.value)
        return None

    @trails_mode.setter
    def trails_mode(self, value: LegacyParticleTrailMode | str) -> None:
        """Set TrailsMode. The enum used to control the conversion from legacy trails to Photon Dust."""
        member = self.get_member("TrailsMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TrailsMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def particle_size_affects_trail_width(self) -> primitives.Bool | None:
        """Whether the particle size should affect the trail width."""
        member = self.get_member("ParticleSizeAffectsTrailWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @particle_size_affects_trail_width.setter
    def particle_size_affects_trail_width(self, value: primitives.Bool) -> None:
        """Set the ParticleSizeAffectsTrailWidth field value."""
        member = self.get_member("ParticleSizeAffectsTrailWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParticleSizeAffectsTrailWidth", fields.FieldBool(value=value)
            )

    @property
    def inherit_trail_color_from_particle(self) -> primitives.Bool | None:
        """Whether the trail should inherit color from the particle it is following."""
        member = self.get_member("InheritTrailColorFromParticle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inherit_trail_color_from_particle.setter
    def inherit_trail_color_from_particle(self, value: primitives.Bool) -> None:
        """Set the InheritTrailColorFromParticle field value."""
        member = self.get_member("InheritTrailColorFromParticle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InheritTrailColorFromParticle", fields.FieldBool(value=value)
            )

    @property
    def trail_world_space(self) -> primitives.Bool | None:
        """Whether the trail is in world or local space."""
        member = self.get_member("TrailWorldSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trail_world_space.setter
    def trail_world_space(self, value: primitives.Bool) -> None:
        """Set the TrailWorldSpace field value."""
        member = self.get_member("TrailWorldSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailWorldSpace", fields.FieldBool(value=value)
            )

    @property
    def trails_module(self) -> str | None:
        """The enabled field on a trails module to drive."""
        member = self.get_member("TrailsModule")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trails_module.setter
    def trails_module(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the TrailsModule reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TrailsModule")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrailsModule",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def ribbon_module(self) -> str | None:
        """The enabled field on a ribbons module to drive."""
        member = self.get_member("RibbonModule")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ribbon_module.setter
    def ribbon_module(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the RibbonModule reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RibbonModule")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RibbonModule",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def ribbon_use_particle_size(self) -> str | None:
        """The use particle size field to drive on a ribbons module."""
        member = self.get_member("RibbonUseParticleSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ribbon_use_particle_size.setter
    def ribbon_use_particle_size(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the RibbonUseParticleSize reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RibbonUseParticleSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RibbonUseParticleSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def ribbon_use_particle_color(self) -> str | None:
        """The use particle color field to drive on a ribbons module."""
        member = self.get_member("RibbonUseParticleColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ribbon_use_particle_color.setter
    def ribbon_use_particle_color(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the RibbonUseParticleColor reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RibbonUseParticleColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RibbonUseParticleColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def trail_size_inheritance(self) -> str | None:
        """The use particle size field to drive on a trails module."""
        member = self.get_member("TrailSizeInheritance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trail_size_inheritance.setter
    def trail_size_inheritance(self, target: str | IField[TrailParticleInheritance] | None) -> None:
        """Set the TrailSizeInheritance reference by target ID or IField[TrailParticleInheritance] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TrailSizeInheritance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrailSizeInheritance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.TrailParticleInheritance>'),
            )

    @property
    def trail_color_inheritance(self) -> str | None:
        """The use particle color field to drive on a trails module."""
        member = self.get_member("TrailColorInheritance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trail_color_inheritance.setter
    def trail_color_inheritance(self, target: str | IField[TrailParticleInheritance] | None) -> None:
        """Set the TrailColorInheritance reference by target ID or IField[TrailParticleInheritance] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TrailColorInheritance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrailColorInheritance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[PhotonDust]PhotonDust.TrailParticleInheritance>'),
            )

    @property
    def trails_space(self) -> str | None:
        """The trails space field to drive on a trails module."""
        member = self.get_member("TrailsSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @trails_space.setter
    def trails_space(self, target: str | RootSpace | None) -> None:
        """Set the TrailsSpace reference by target ID or RootSpace instance."""
        target_id: str | None = target.id if isinstance(target, RootSpace) else target  # type: ignore[assignment]
        member = self.get_member("TrailsSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TrailsSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RootSpace'),
            )

