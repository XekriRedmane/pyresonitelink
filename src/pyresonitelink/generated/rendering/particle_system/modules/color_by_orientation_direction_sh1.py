"""Generated component: ColorByOrientationDirectionSH1."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorByOrientationDirectionSH1(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorByOrientationDirectionSH1.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorByOrientationDirectionSH1"

    @property
    def sh(self) -> members.FieldEnum | None:
        """The SH member."""
        member = self.get_member("SH")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sh.setter
    def sh(self, value: members.FieldEnum) -> None:
        """Set the SH member."""
        self.set_member("SH", value)

