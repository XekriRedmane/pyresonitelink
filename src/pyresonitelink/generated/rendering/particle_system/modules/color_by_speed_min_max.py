"""Generated component: ColorBySpeedMinMax."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iparticle_system_module import IParticleSystemModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorBySpeedMinMax(GeneratedComponent, IParticleSystemModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PhotonDust.ColorBySpeedMinMax.

    Category: Rendering/Particle System/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotonDust.ColorBySpeedMinMax"

    def __init__(self, min_speed: np.float32 | None = None, max_speed: np.float32 | None = None, min_color: primitives.ColorX | None = None, max_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_speed: Initial value for MinSpeed.
            max_speed: Initial value for MaxSpeed.
            min_color: Initial value for MinColor.
            max_color: Initial value for MaxColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_speed is not None:
            self.min_speed = min_speed
        if max_speed is not None:
            self.max_speed = max_speed
        if min_color is not None:
            self.min_color = min_color
        if max_color is not None:
            self.max_color = max_color

    @property
    def min_speed(self) -> np.float32 | None:
        """The MinSpeed field value."""
        member = self.get_member("MinSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_speed.setter
    def min_speed(self, value: np.float32) -> None:
        """Set the MinSpeed field value."""
        member = self.get_member("MinSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSpeed", fields.FieldFloat(value=value)
            )

    @property
    def max_speed(self) -> np.float32 | None:
        """The MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_speed.setter
    def max_speed(self, value: np.float32) -> None:
        """Set the MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSpeed", fields.FieldFloat(value=value)
            )

    @property
    def min_color(self) -> primitives.ColorX | None:
        """The MinColor field value."""
        member = self.get_member("MinColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_color.setter
    def min_color(self, value: primitives.ColorX) -> None:
        """Set the MinColor field value."""
        member = self.get_member("MinColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinColor", fields.FieldColorX(value=value)
            )

    @property
    def max_color(self) -> primitives.ColorX | None:
        """The MaxColor field value."""
        member = self.get_member("MaxColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_color.setter
    def max_color(self, value: primitives.ColorX) -> None:
        """Set the MaxColor field value."""
        member = self.get_member("MaxColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxColor", fields.FieldColorX(value=value)
            )

