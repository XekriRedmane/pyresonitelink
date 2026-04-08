"""Generated component: SineHapticFilter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SineHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SineHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SineHapticFilter"

    def __init__(self, use_global_time: bool | None = None, distance_scale: np.float32 | None = None, axis_scale: primitives.Float3 | None = None, min_intensity: np.float32 | None = None, max_intensity: np.float32 | None = None, frequency: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_global_time: Initial value for UseGlobalTime.
            distance_scale: Initial value for DistanceScale.
            axis_scale: Initial value for AxisScale.
            min_intensity: Initial value for MinIntensity.
            max_intensity: Initial value for MaxIntensity.
            frequency: Initial value for Frequency.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_global_time is not None:
            self.use_global_time = use_global_time
        if distance_scale is not None:
            self.distance_scale = distance_scale
        if axis_scale is not None:
            self.axis_scale = axis_scale
        if min_intensity is not None:
            self.min_intensity = min_intensity
        if max_intensity is not None:
            self.max_intensity = max_intensity
        if frequency is not None:
            self.frequency = frequency

    @property
    def use_global_time(self) -> bool | None:
        """The UseGlobalTime field value."""
        member = self.get_member("UseGlobalTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_global_time.setter
    def use_global_time(self, value: bool) -> None:
        """Set the UseGlobalTime field value."""
        member = self.get_member("UseGlobalTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseGlobalTime", fields.FieldBool(value=value)
            )

    @property
    def distance_scale(self) -> np.float32 | None:
        """The DistanceScale field value."""
        member = self.get_member("DistanceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_scale.setter
    def distance_scale(self, value: np.float32) -> None:
        """Set the DistanceScale field value."""
        member = self.get_member("DistanceScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistanceScale", fields.FieldNullableFloat(value=value)
            )

    @property
    def axis_scale(self) -> primitives.Float3 | None:
        """The AxisScale field value."""
        member = self.get_member("AxisScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis_scale.setter
    def axis_scale(self, value: primitives.Float3) -> None:
        """Set the AxisScale field value."""
        member = self.get_member("AxisScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AxisScale", fields.FieldNullableFloat3(value=value)
            )

    @property
    def min_intensity(self) -> np.float32 | None:
        """The MinIntensity field value."""
        member = self.get_member("MinIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_intensity.setter
    def min_intensity(self, value: np.float32) -> None:
        """Set the MinIntensity field value."""
        member = self.get_member("MinIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinIntensity", fields.FieldFloat(value=value)
            )

    @property
    def max_intensity(self) -> np.float32 | None:
        """The MaxIntensity field value."""
        member = self.get_member("MaxIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_intensity.setter
    def max_intensity(self, value: np.float32) -> None:
        """Set the MaxIntensity field value."""
        member = self.get_member("MaxIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxIntensity", fields.FieldFloat(value=value)
            )

    @property
    def frequency(self) -> np.float32 | None:
        """The Frequency field value."""
        member = self.get_member("Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frequency.setter
    def frequency(self, value: np.float32) -> None:
        """Set the Frequency field value."""
        member = self.get_member("Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Frequency", fields.FieldFloat(value=value)
            )

