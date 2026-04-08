"""Generated component: ParticleDeathSubEmitter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleDeathSubEmitter(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ParticleDeathSubEmitter.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ParticleDeathSubEmitter"

    def __init__(self, emit_min: np.int32 | None = None, emit_max: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            emit_min: Initial value for EmitMin.
            emit_max: Initial value for EmitMax.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if emit_min is not None:
            self.emit_min = emit_min
        if emit_max is not None:
            self.emit_max = emit_max

    @property
    def emit_min(self) -> np.int32 | None:
        """The EmitMin field value."""
        member = self.get_member("EmitMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emit_min.setter
    def emit_min(self, value: np.int32) -> None:
        """Set the EmitMin field value."""
        member = self.get_member("EmitMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmitMin", fields.FieldInt(value=value)
            )

    @property
    def emit_max(self) -> np.int32 | None:
        """The EmitMax field value."""
        member = self.get_member("EmitMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @emit_max.setter
    def emit_max(self, value: np.int32) -> None:
        """Set the EmitMax field value."""
        member = self.get_member("EmitMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EmitMax", fields.FieldInt(value=value)
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

