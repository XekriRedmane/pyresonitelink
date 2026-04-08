"""Generated component: ColorListInitializer."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorListInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorListInitializer.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorListInitializer"

    @property
    def colors(self) -> members.SyncList | None:
        """The Colors member."""
        member = self.get_member("Colors")
        if isinstance(member, members.SyncList):
            return member
        return None

    @colors.setter
    def colors(self, value: members.SyncList) -> None:
        """Set the Colors member."""
        self.set_member("Colors", value)

