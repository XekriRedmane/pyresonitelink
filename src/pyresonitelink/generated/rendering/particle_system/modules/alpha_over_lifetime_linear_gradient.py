"""Generated component: AlphaOverLifetimeLinearGradient."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AlphaOverLifetimeLinearGradient(GeneratedComponent, ICustomInspector, IParticleSystemModule, IWorldEventReceiver):
    """The AlphaOverLifetimeLinearGradient component implements the older alpha over lifetime system that came from Unity. It allows for particles to change alpha depending on how long they have existed for.

A more modern alternative to this with actual editablilty is the ColorOverLifetimeTexture component.

This component is part of the Photon Dust system made by Frooxius.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.AlphaOverLifetimeLinearGradient"

    @property
    def alpha_over_lifetime(self) -> members.Member | None:
        """The Linear Gradient of alpha values to use over lifetime."""
        member = self.get_member("AlphaOverLifetime")
        if isinstance(member, members.Member):
            return member
        return None

    @alpha_over_lifetime.setter
    def alpha_over_lifetime(self, value: members.Member) -> None:
        """Set AlphaOverLifetime. The Linear Gradient of alpha values to use over lifetime."""
        self.set_member("AlphaOverLifetime", value)

