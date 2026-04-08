"""Generated component: ParticleEmitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.iparticle_system_subsystem import IParticleSystemSubsystem
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleEmitter(GeneratedComponent, IParticleSystemSubsystem, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleEmitter.

    Category: Rendering/Particle System/Emitters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleEmitter"

    def __init__(self, system: str | ParticleSystem | None = None, rate: primitives.Float | None = None, burst_on_activated_min: primitives.Float | None = None, burst_on_activated_max: primitives.Float | None = None, burst_on_start: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            system: Initial value for System.
            rate: Initial value for Rate.
            burst_on_activated_min: Initial value for BurstOnActivatedMin.
            burst_on_activated_max: Initial value for BurstOnActivatedMax.
            burst_on_start: Initial value for BurstOnStart.
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

