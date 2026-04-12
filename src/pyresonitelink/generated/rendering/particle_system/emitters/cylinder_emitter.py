"""Generated component: CylinderEmitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.cylinder_emitter_direction import CylinderEmitterDirection
from pyresonitelink.generated._enums.cylinder_emitter_caps_direction import CylinderEmitterCapsDirection
from pyresonitelink.generated._enums.direction_transform_mode import DirectionTransformMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.iparticle_system_emitter import IParticleSystemEmitter


class CylinderEmitter(GeneratedComponent, IParticleSystemEmitter):
    """The CylinderEmitter component is used to emit particles in PhotonDust.

    Category: Rendering/Particle System/Emitters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.CylinderEmitter"

    def __init__(self, system: str | ParticleSystem | None = None, rate: primitives.Float | None = None, burst_on_activated_min: primitives.Float | None = None, burst_on_activated_max: primitives.Float | None = None, burst_on_start: primitives.Bool | None = None, radius: primitives.Float | None = None, height: primitives.Float | None = None, emit_from_shell: primitives.Bool | None = None, exclude_caps: primitives.Bool | None = None, direction_mode: CylinderEmitterDirection | str | None = None, caps_direction_mode: CylinderEmitterCapsDirection | str | None = None, random_direction_weight: primitives.Float | None = None, direction: primitives.Float3 | None = None, direction_transform_mode: DirectionTransformMode | str | None = None, direction_post_transform: primitives.Float3x3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            system: Initial value for System.
            rate: Initial value for Rate.
            burst_on_activated_min: Initial value for BurstOnActivatedMin.
            burst_on_activated_max: Initial value for BurstOnActivatedMax.
            burst_on_start: Initial value for BurstOnStart.
            radius: Initial value for Radius.
            height: Initial value for Height.
            emit_from_shell: Initial value for EmitFromShell.
            exclude_caps: Initial value for ExcludeCaps.
            direction_mode: Initial value for DirectionMode.
            caps_direction_mode: Initial value for CapsDirectionMode.
            random_direction_weight: Initial value for RandomDirectionWeight.
            direction: Initial value for Direction.
            direction_transform_mode: Initial value for DirectionTransformMode.
            direction_post_transform: Initial value for DirectionPostTransform.
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
        if radius is not None:
            self.radius = radius
        if height is not None:
            self.height = height
        if emit_from_shell is not None:
            self.emit_from_shell = emit_from_shell
        if exclude_caps is not None:
            self.exclude_caps = exclude_caps
        if direction_mode is not None:
            self.direction_mode = direction_mode
        if caps_direction_mode is not None:
            self.caps_direction_mode = caps_direction_mode
        if random_direction_weight is not None:
            self.random_direction_weight = random_direction_weight
        if direction is not None:
            self.direction = direction
        if direction_transform_mode is not None:
            self.direction_transform_mode = direction_transform_mode
        if direction_post_transform is not None:
            self.direction_post_transform = direction_post_transform

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
    def radius(self) -> primitives.Float | None:
        """The radius of the emitting cylinder shape"""
        member = self.get_member("Radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the Radius field value."""
        member = self.get_member("Radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Radius", fields.FieldFloat(value=value)
            )

    @property
    def height(self) -> primitives.Float | None:
        """The height of the emitting cylinder shape."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def emit_from_shell(self) -> primitives.Bool | None:
        """The EmitFromShell field value."""
        member = self.get_member("EmitFromShell")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emit_from_shell.setter
    def emit_from_shell(self, value: primitives.Bool) -> None:
        """Set the EmitFromShell field value."""
        member = self.get_member("EmitFromShell")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmitFromShell", fields.FieldBool(value=value)
            )

    @property
    def exclude_caps(self) -> primitives.Bool | None:
        """Whether to exclude the ends of the cylinder when emitting particles."""
        member = self.get_member("ExcludeCaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_caps.setter
    def exclude_caps(self, value: primitives.Bool) -> None:
        """Set the ExcludeCaps field value."""
        member = self.get_member("ExcludeCaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeCaps", fields.FieldBool(value=value)
            )

    @property
    def direction_mode(self) -> CylinderEmitterDirection | None:
        """How to emit particles from the cylinder."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CylinderEmitterDirection(member.value)
        return None

    @direction_mode.setter
    def direction_mode(self, value: CylinderEmitterDirection | str) -> None:
        """Set DirectionMode. How to emit particles from the cylinder."""
        member = self.get_member("DirectionMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DirectionMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def caps_direction_mode(self) -> CylinderEmitterCapsDirection | None:
        """how to emit particles from the cylinder caps."""
        member = self.get_member("CapsDirectionMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CylinderEmitterCapsDirection(member.value)
        return None

    @caps_direction_mode.setter
    def caps_direction_mode(self, value: CylinderEmitterCapsDirection | str) -> None:
        """Set CapsDirectionMode. how to emit particles from the cylinder caps."""
        member = self.get_member("CapsDirectionMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CapsDirectionMode",
                members.FieldEnum(value=str(value)),
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
    def direction_transform_mode(self) -> DirectionTransformMode | None:
        """How to handle the direction when emitting particles."""
        member = self.get_member("DirectionTransformMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return DirectionTransformMode(member.value)
        return None

    @direction_transform_mode.setter
    def direction_transform_mode(self, value: DirectionTransformMode | str) -> None:
        """Set DirectionTransformMode. How to handle the direction when emitting particles."""
        member = self.get_member("DirectionTransformMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DirectionTransformMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def direction_post_transform(self) -> primitives.Float3x3 | None:
        """The direction particles should be when spawned post transform using a matrix."""
        member = self.get_member("DirectionPostTransform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @direction_post_transform.setter
    def direction_post_transform(self, value: primitives.Float3x3) -> None:
        """Set the DirectionPostTransform field value."""
        member = self.get_member("DirectionPostTransform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DirectionPostTransform", fields.FieldFloat3x3(value=value)
            )

