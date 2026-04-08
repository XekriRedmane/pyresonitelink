"""Generated component: OrientByVelocity."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OrientByVelocity(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.OrientByVelocity.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.OrientByVelocity"

    def __init__(self, up: primitives.Float3 | None = None, minimum_velocity: np.float32 | None = None, velocity_transition_range: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            up: Initial value for Up.
            minimum_velocity: Initial value for MinimumVelocity.
            velocity_transition_range: Initial value for VelocityTransitionRange.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if up is not None:
            self.up = up
        if minimum_velocity is not None:
            self.minimum_velocity = minimum_velocity
        if velocity_transition_range is not None:
            self.velocity_transition_range = velocity_transition_range

    @property
    def up(self) -> primitives.Float3 | None:
        """The Up field value."""
        member = self.get_member("Up")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @up.setter
    def up(self, value: primitives.Float3) -> None:
        """Set the Up field value."""
        member = self.get_member("Up")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Up", fields.FieldFloat3(value=value)
            )

    @property
    def minimum_velocity(self) -> np.float32 | None:
        """The MinimumVelocity field value."""
        member = self.get_member("MinimumVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_velocity.setter
    def minimum_velocity(self, value: np.float32) -> None:
        """Set the MinimumVelocity field value."""
        member = self.get_member("MinimumVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumVelocity", fields.FieldFloat(value=value)
            )

    @property
    def velocity_transition_range(self) -> np.float32 | None:
        """The VelocityTransitionRange field value."""
        member = self.get_member("VelocityTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity_transition_range.setter
    def velocity_transition_range(self, value: np.float32) -> None:
        """Set the VelocityTransitionRange field value."""
        member = self.get_member("VelocityTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VelocityTransitionRange", fields.FieldFloat(value=value)
            )

