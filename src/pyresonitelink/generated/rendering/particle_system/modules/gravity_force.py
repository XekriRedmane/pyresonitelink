"""Generated component: GravityForce."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GravityForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The GravityForce component acts as a global force for particles that makes them fall either up or down along the Up axis.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.GravityForce"

    def __init__(self, gravity: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            gravity: Initial value for Gravity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if gravity is not None:
            self.gravity = gravity

    @property
    def gravity(self) -> primitives.Float | None:
        """The force to apply. Negative values are down and positive values are up."""
        member = self.get_member("Gravity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gravity.setter
    def gravity(self, value: primitives.Float) -> None:
        """Set the Gravity field value."""
        member = self.get_member("Gravity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gravity", fields.FieldFloat(value=value)
            )

    @property
    def override_force_space(self) -> members.SyncObject | None:
        """The space to calculate gravity force in. Is converted into the particle system's space."""
        member = self.get_member("OverrideForceSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @override_force_space.setter
    def override_force_space(self, value: members.SyncObject) -> None:
        """Set OverrideForceSpace. The space to calculate gravity force in. Is converted into the particle system's space."""
        self.set_member("OverrideForceSpace", value)

