"""Generated component: GravityForce."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GravityForce(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.GravityForce.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.GravityForce"

    def __init__(self, gravity: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            gravity: Initial value for Gravity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if gravity is not None:
            self.gravity = gravity

    @property
    def gravity(self) -> np.float32 | None:
        """The Gravity field value."""
        member = self.get_member("Gravity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gravity.setter
    def gravity(self, value: np.float32) -> None:
        """Set the Gravity field value."""
        member = self.get_member("Gravity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gravity", fields.FieldFloat(value=value)
            )

    @property
    def override_force_space(self) -> members.SyncObject | None:
        """The OverrideForceSpace member."""
        member = self.get_member("OverrideForceSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @override_force_space.setter
    def override_force_space(self, value: members.SyncObject) -> None:
        """Set the OverrideForceSpace member."""
        self.set_member("OverrideForceSpace", value)

