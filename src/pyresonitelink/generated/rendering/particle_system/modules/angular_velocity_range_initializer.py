"""Generated component: AngularVelocityRangeInitializer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AngularVelocityRangeInitializer(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.AngularVelocityRangeInitializer.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.AngularVelocityRangeInitializer"

    def __init__(self, min_value: np.float32 | None = None, max_value: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def min_value(self) -> np.float32 | None:
        """The MinValue field value."""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: np.float32) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldFloat(value=value)
            )

    @property
    def max_value(self) -> np.float32 | None:
        """The MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: np.float32) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldFloat(value=value)
            )

