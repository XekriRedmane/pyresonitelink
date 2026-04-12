"""Generated component: ColorListInitializer."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorListInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Color List Initializer component makes particles initialize their color in a particle system from a list of colors.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorListInitializer"

    @property
    def colors(self) -> members.SyncList | None:
        """A list of colors to use."""
        member = self.get_member("Colors")
        if isinstance(member, members.SyncList):
            return member
        return None

    @colors.setter
    def colors(self, value: members.SyncList) -> None:
        """Set Colors. A list of colors to use."""
        self.set_member("Colors", value)

