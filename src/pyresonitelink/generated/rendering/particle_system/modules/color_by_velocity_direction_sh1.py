"""Generated component: ColorByVelocityDirectionSH1."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorByVelocityDirectionSH1(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """The Color By Velocity Direction SH1 component samples a ColorX spherical harmonic based on the velocity vector of a particle in it's simulation space. that sampled color becomes the particle's color.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorByVelocityDirectionSH1"

    def __init__(self, sh: primitives.SphericalHarmonicsL1 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sh: Initial value for SH.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sh is not None:
            self.sh = sh

    @property
    def sh(self) -> primitives.SphericalHarmonicsL1 | None:
        """The spherical harmonic to sample."""
        member = self.get_member("SH")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sh.setter
    def sh(self, value: primitives.SphericalHarmonicsL1) -> None:
        """Set the SH field value."""
        member = self.get_member("SH")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SH", fields.FieldSphericalHarmonicsL1(value=value)
            )

