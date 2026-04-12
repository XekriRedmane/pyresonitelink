"""Generated component: ColorOverLifetimeLinearGradient."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorOverLifetimeLinearGradient(GeneratedComponent, ICustomInspector, IParticleSystemModule, IWorldEventReceiver):
    """The ColorOverLifetimeLinearGradient component implements the older color over lifetime system that came from Unity. It allows for particles to change color depending on how long they have existed for.

This component is part of the Photon Dust system made by Frooxius.

A more modern alternative to this with actual editablilty is the ColorOverLifetimeTexture component.

    Category: Rendering/Particle System/Modules

    Attach to a slot, add to the list of modules in a ParticleSystem, and
    adjust the values to make the desired effect from this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorOverLifetimeLinearGradient"

    @property
    def color_over_lifetime(self) -> members.Member | None:
        """A Linear Gradient of colors and points to use to give particles color over lifetime."""
        member = self.get_member("ColorOverLifetime")
        if isinstance(member, members.Member):
            return member
        return None

    @color_over_lifetime.setter
    def color_over_lifetime(self, value: members.Member) -> None:
        """Set ColorOverLifetime. A Linear Gradient of colors and points to use to give particles color over lifetime."""
        self.set_member("ColorOverLifetime", value)

