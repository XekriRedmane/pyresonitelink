"""Generated component: ParticleLifetimeSubEmitter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleLifetimeSubEmitter(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleLifetimeSubEmitter.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleLifetimeSubEmitter"

    def __init__(self, rate: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rate: Initial value for Rate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rate is not None:
            self.rate = rate

    @property
    def rate(self) -> np.float32 | None:
        """The Rate field value."""
        member = self.get_member("Rate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate.setter
    def rate(self, value: np.float32) -> None:
        """Set the Rate field value."""
        member = self.get_member("Rate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rate", fields.FieldFloat(value=value)
            )

    @property
    def parameters(self) -> members.SyncObject | None:
        """The Parameters member."""
        member = self.get_member("Parameters")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @parameters.setter
    def parameters(self, value: members.SyncObject) -> None:
        """Set the Parameters member."""
        self.set_member("Parameters", value)

