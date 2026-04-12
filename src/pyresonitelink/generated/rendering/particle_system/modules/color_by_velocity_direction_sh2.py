"""Generated component: ColorByVelocityDirectionSH2."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.spherical_harmonics_l2 import SphericalHarmonicsL2
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorByVelocityDirectionSH2(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Color By Velocity Direction SH2 component samples a ColorX spherical harmonic based on the velocity vector of a particle in it's simulation space. that sampled color becomes the particle's color.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorByVelocityDirectionSH2"

    def __init__(self, sh: SphericalHarmonicsL2 | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sh: Initial value for SH.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sh is not None:
            self.sh = sh

    @property
    def sh(self) -> SphericalHarmonicsL2 | None:
        """The spherical harmonic to sample."""
        member = self.get_member("SH")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SphericalHarmonicsL2(member.value)
        return None

    @sh.setter
    def sh(self, value: SphericalHarmonicsL2 | str) -> None:
        """Set SH. The spherical harmonic to sample."""
        member = self.get_member("SH")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SH",
                members.FieldEnum(value=str(value)),
            )

