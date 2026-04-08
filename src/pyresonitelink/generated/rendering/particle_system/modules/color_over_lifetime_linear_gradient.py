"""Generated component: ColorOverLifetimeLinearGradient."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorOverLifetimeLinearGradient(GeneratedComponent, ICustomInspector, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorOverLifetimeLinearGradient.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorOverLifetimeLinearGradient"

    @property
    def color_over_lifetime(self) -> members.Member | None:
        """The ColorOverLifetime member."""
        member = self.get_member("ColorOverLifetime")
        if isinstance(member, members.Member):
            return member
        return None

    @color_over_lifetime.setter
    def color_over_lifetime(self, value: members.Member) -> None:
        """Set the ColorOverLifetime member."""
        self.set_member("ColorOverLifetime", value)

