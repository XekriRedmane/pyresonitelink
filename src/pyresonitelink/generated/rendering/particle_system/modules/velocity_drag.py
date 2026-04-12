"""Generated component: VelocityDrag."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VelocityDrag(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The VelocityDrag component makes particles in a particle system slow down towards 0 Velocity when not acted upon as if moving through a substance.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.VelocityDrag"

    def __init__(self, drag: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            drag: Initial value for Drag.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if drag is not None:
            self.drag = drag

    @property
    def drag(self) -> primitives.Float | None:
        """How much to slow down particles to 0 velocity."""
        member = self.get_member("Drag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drag.setter
    def drag(self, value: primitives.Float) -> None:
        """Set the Drag field value."""
        member = self.get_member("Drag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Drag", fields.FieldFloat(value=value)
            )

