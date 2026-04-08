"""Generated component: RadialDistanceHapticFilter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadialDistanceHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RadialDistanceHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadialDistanceHapticFilter"

    def __init__(self, start_radius: np.float32 | None = None, end_radius: np.float32 | None = None, start_intensity: np.float32 | None = None, end_intensity: np.float32 | None = None, power: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start_radius: Initial value for StartRadius.
            end_radius: Initial value for EndRadius.
            start_intensity: Initial value for StartIntensity.
            end_intensity: Initial value for EndIntensity.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start_radius is not None:
            self.start_radius = start_radius
        if end_radius is not None:
            self.end_radius = end_radius
        if start_intensity is not None:
            self.start_intensity = start_intensity
        if end_intensity is not None:
            self.end_intensity = end_intensity
        if power is not None:
            self.power = power

    @property
    def start_radius(self) -> np.float32 | None:
        """The StartRadius field value."""
        member = self.get_member("StartRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_radius.setter
    def start_radius(self, value: np.float32) -> None:
        """Set the StartRadius field value."""
        member = self.get_member("StartRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartRadius", fields.FieldFloat(value=value)
            )

    @property
    def end_radius(self) -> np.float32 | None:
        """The EndRadius field value."""
        member = self.get_member("EndRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_radius.setter
    def end_radius(self, value: np.float32) -> None:
        """Set the EndRadius field value."""
        member = self.get_member("EndRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndRadius", fields.FieldFloat(value=value)
            )

    @property
    def start_intensity(self) -> np.float32 | None:
        """The StartIntensity field value."""
        member = self.get_member("StartIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_intensity.setter
    def start_intensity(self, value: np.float32) -> None:
        """Set the StartIntensity field value."""
        member = self.get_member("StartIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartIntensity", fields.FieldFloat(value=value)
            )

    @property
    def end_intensity(self) -> np.float32 | None:
        """The EndIntensity field value."""
        member = self.get_member("EndIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_intensity.setter
    def end_intensity(self, value: np.float32) -> None:
        """Set the EndIntensity field value."""
        member = self.get_member("EndIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndIntensity", fields.FieldFloat(value=value)
            )

    @property
    def power(self) -> np.float32 | None:
        """The Power field value."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: np.float32) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

