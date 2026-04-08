"""Generated component: AlphaOverLifetimeLinearGradient."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AlphaOverLifetimeLinearGradient(GeneratedComponent, ICustomInspector, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.AlphaOverLifetimeLinearGradient.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.AlphaOverLifetimeLinearGradient"

    @property
    def alpha_over_lifetime(self) -> members.Member | None:
        """The AlphaOverLifetime member."""
        member = self.get_member("AlphaOverLifetime")
        if isinstance(member, members.Member):
            return member
        return None

    @alpha_over_lifetime.setter
    def alpha_over_lifetime(self, value: members.Member) -> None:
        """Set the AlphaOverLifetime member."""
        self.set_member("AlphaOverLifetime", value)

