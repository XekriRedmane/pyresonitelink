"""Generated component: ParticleSystemMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.particle_system import ParticleSystem
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleSystemMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleSystemMetadata.

    Category: Rendering/Particle System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleSystemMetadata"

    def __init__(self, system: str | ParticleSystem | None = None, particle_count: primitives.Int | None = None, particles_fps: primitives.Float | None = None, last_simulation_time: primitives.Float | None = None, last_submission_time: primitives.Float | None = None, render_data_reallocation_count: primitives.Int | None = None, trail_count: primitives.Int | None = None, trail_capacity: primitives.Int | None = None, trail_point_capacity: primitives.Int | None = None, trails_data_reallocation_count: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            system: Initial value for System.
            particle_count: Initial value for ParticleCount.
            particles_fps: Initial value for ParticlesFPS.
            last_simulation_time: Initial value for LastSimulationTime.
            last_submission_time: Initial value for LastSubmissionTime.
            render_data_reallocation_count: Initial value for RenderDataReallocationCount.
            trail_count: Initial value for TrailCount.
            trail_capacity: Initial value for TrailCapacity.
            trail_point_capacity: Initial value for TrailPointCapacity.
            trails_data_reallocation_count: Initial value for TrailsDataReallocationCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if system is not None:
            self.system = system
        if particle_count is not None:
            self.particle_count = particle_count
        if particles_fps is not None:
            self.particles_fps = particles_fps
        if last_simulation_time is not None:
            self.last_simulation_time = last_simulation_time
        if last_submission_time is not None:
            self.last_submission_time = last_submission_time
        if render_data_reallocation_count is not None:
            self.render_data_reallocation_count = render_data_reallocation_count
        if trail_count is not None:
            self.trail_count = trail_count
        if trail_capacity is not None:
            self.trail_capacity = trail_capacity
        if trail_point_capacity is not None:
            self.trail_point_capacity = trail_point_capacity
        if trails_data_reallocation_count is not None:
            self.trails_data_reallocation_count = trails_data_reallocation_count

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
    def particle_count(self) -> primitives.Int | None:
        """The ParticleCount field value."""
        member = self.get_member("ParticleCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @particle_count.setter
    def particle_count(self, value: primitives.Int) -> None:
        """Set the ParticleCount field value."""
        member = self.get_member("ParticleCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParticleCount", fields.FieldInt(value=value)
            )

    @property
    def particles_fps(self) -> primitives.Float | None:
        """The ParticlesFPS field value."""
        member = self.get_member("ParticlesFPS")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @particles_fps.setter
    def particles_fps(self, value: primitives.Float) -> None:
        """Set the ParticlesFPS field value."""
        member = self.get_member("ParticlesFPS")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ParticlesFPS", fields.FieldFloat(value=value)
            )

    @property
    def last_simulation_time(self) -> primitives.Float | None:
        """The LastSimulationTime field value."""
        member = self.get_member("LastSimulationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_simulation_time.setter
    def last_simulation_time(self, value: primitives.Float) -> None:
        """Set the LastSimulationTime field value."""
        member = self.get_member("LastSimulationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastSimulationTime", fields.FieldFloat(value=value)
            )

    @property
    def last_submission_time(self) -> primitives.Float | None:
        """The LastSubmissionTime field value."""
        member = self.get_member("LastSubmissionTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_submission_time.setter
    def last_submission_time(self, value: primitives.Float) -> None:
        """Set the LastSubmissionTime field value."""
        member = self.get_member("LastSubmissionTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastSubmissionTime", fields.FieldFloat(value=value)
            )

    @property
    def render_data_reallocation_count(self) -> primitives.Int | None:
        """The RenderDataReallocationCount field value."""
        member = self.get_member("RenderDataReallocationCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_data_reallocation_count.setter
    def render_data_reallocation_count(self, value: primitives.Int) -> None:
        """Set the RenderDataReallocationCount field value."""
        member = self.get_member("RenderDataReallocationCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderDataReallocationCount", fields.FieldInt(value=value)
            )

    @property
    def trail_count(self) -> primitives.Int | None:
        """The TrailCount field value."""
        member = self.get_member("TrailCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trail_count.setter
    def trail_count(self, value: primitives.Int) -> None:
        """Set the TrailCount field value."""
        member = self.get_member("TrailCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailCount", fields.FieldInt(value=value)
            )

    @property
    def trail_capacity(self) -> primitives.Int | None:
        """The TrailCapacity field value."""
        member = self.get_member("TrailCapacity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trail_capacity.setter
    def trail_capacity(self, value: primitives.Int) -> None:
        """Set the TrailCapacity field value."""
        member = self.get_member("TrailCapacity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailCapacity", fields.FieldInt(value=value)
            )

    @property
    def trail_point_capacity(self) -> primitives.Int | None:
        """The TrailPointCapacity field value."""
        member = self.get_member("TrailPointCapacity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trail_point_capacity.setter
    def trail_point_capacity(self, value: primitives.Int) -> None:
        """Set the TrailPointCapacity field value."""
        member = self.get_member("TrailPointCapacity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailPointCapacity", fields.FieldInt(value=value)
            )

    @property
    def trails_data_reallocation_count(self) -> primitives.Int | None:
        """The TrailsDataReallocationCount field value."""
        member = self.get_member("TrailsDataReallocationCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @trails_data_reallocation_count.setter
    def trails_data_reallocation_count(self, value: primitives.Int) -> None:
        """Set the TrailsDataReallocationCount field value."""
        member = self.get_member("TrailsDataReallocationCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrailsDataReallocationCount", fields.FieldInt(value=value)
            )

