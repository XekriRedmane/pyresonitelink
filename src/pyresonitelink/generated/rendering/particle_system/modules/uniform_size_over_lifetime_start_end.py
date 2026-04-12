"""Generated component: UniformSizeOverLifetimeStartEnd."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UniformSizeOverLifetimeStartEnd(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The UniformSizeOverLifetimeStartEnd component makes particles in a particle system start with a size and lerp towards an end size over their lifetime.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.UniformSizeOverLifetimeStartEnd"

    def __init__(self, start_size: primitives.Float | None = None, end_size: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start_size: Initial value for StartSize.
            end_size: Initial value for EndSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start_size is not None:
            self.start_size = start_size
        if end_size is not None:
            self.end_size = end_size

    @property
    def start_size(self) -> primitives.Float | None:
        """The size that particles have when starting or being born."""
        member = self.get_member("StartSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_size.setter
    def start_size(self, value: primitives.Float) -> None:
        """Set the StartSize field value."""
        member = self.get_member("StartSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartSize", fields.FieldFloat(value=value)
            )

    @property
    def end_size(self) -> primitives.Float | None:
        """The size that particles go towards as their lifetime decreases."""
        member = self.get_member("EndSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_size.setter
    def end_size(self, value: primitives.Float) -> None:
        """Set the EndSize field value."""
        member = self.get_member("EndSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndSize", fields.FieldFloat(value=value)
            )

