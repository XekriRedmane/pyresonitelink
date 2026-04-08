"""Generated component: UniformSizeSineMultiplier."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UniformSizeSineMultiplier(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.UniformSizeSineMultiplier.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.UniformSizeSineMultiplier"

    def __init__(self, speed: np.float32 | None = None, offset: np.float32 | None = None, min_multiplier: np.float32 | None = None, max_multiplier: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            speed: Initial value for Speed.
            offset: Initial value for Offset.
            min_multiplier: Initial value for MinMultiplier.
            max_multiplier: Initial value for MaxMultiplier.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if speed is not None:
            self.speed = speed
        if offset is not None:
            self.offset = offset
        if min_multiplier is not None:
            self.min_multiplier = min_multiplier
        if max_multiplier is not None:
            self.max_multiplier = max_multiplier

    @property
    def speed(self) -> np.float32 | None:
        """The Speed field value."""
        member = self.get_member("Speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: np.float32) -> None:
        """Set the Speed field value."""
        member = self.get_member("Speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Speed", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> np.float32 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: np.float32) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat(value=value)
            )

    @property
    def min_multiplier(self) -> np.float32 | None:
        """The MinMultiplier field value."""
        member = self.get_member("MinMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_multiplier.setter
    def min_multiplier(self, value: np.float32) -> None:
        """Set the MinMultiplier field value."""
        member = self.get_member("MinMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def max_multiplier(self) -> np.float32 | None:
        """The MaxMultiplier field value."""
        member = self.get_member("MaxMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_multiplier.setter
    def max_multiplier(self, value: np.float32) -> None:
        """Set the MaxMultiplier field value."""
        member = self.get_member("MaxMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxMultiplier", fields.FieldFloat(value=value)
            )

