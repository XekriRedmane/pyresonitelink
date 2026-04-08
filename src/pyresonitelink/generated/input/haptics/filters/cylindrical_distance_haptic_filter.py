"""Generated component: CylindricalDistanceHapticFilter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CylindricalDistanceHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CylindricalDistanceHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CylindricalDistanceHapticFilter"

    def __init__(self, start_radius: np.float32 | None = None, end_radius: np.float32 | None = None, start_radius_intensity: np.float32 | None = None, end_radius_intensity: np.float32 | None = None, radius_power: np.float32 | None = None, start_axis_offset: np.float32 | None = None, end_axis_offset: np.float32 | None = None, start_axis_intensity: np.float32 | None = None, end_axis_intensity: np.float32 | None = None, axis_power: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            start_radius: Initial value for StartRadius.
            end_radius: Initial value for EndRadius.
            start_radius_intensity: Initial value for StartRadiusIntensity.
            end_radius_intensity: Initial value for EndRadiusIntensity.
            radius_power: Initial value for RadiusPower.
            start_axis_offset: Initial value for StartAxisOffset.
            end_axis_offset: Initial value for EndAxisOffset.
            start_axis_intensity: Initial value for StartAxisIntensity.
            end_axis_intensity: Initial value for EndAxisIntensity.
            axis_power: Initial value for AxisPower.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if start_radius is not None:
            self.start_radius = start_radius
        if end_radius is not None:
            self.end_radius = end_radius
        if start_radius_intensity is not None:
            self.start_radius_intensity = start_radius_intensity
        if end_radius_intensity is not None:
            self.end_radius_intensity = end_radius_intensity
        if radius_power is not None:
            self.radius_power = radius_power
        if start_axis_offset is not None:
            self.start_axis_offset = start_axis_offset
        if end_axis_offset is not None:
            self.end_axis_offset = end_axis_offset
        if start_axis_intensity is not None:
            self.start_axis_intensity = start_axis_intensity
        if end_axis_intensity is not None:
            self.end_axis_intensity = end_axis_intensity
        if axis_power is not None:
            self.axis_power = axis_power

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
    def start_radius_intensity(self) -> np.float32 | None:
        """The StartRadiusIntensity field value."""
        member = self.get_member("StartRadiusIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_radius_intensity.setter
    def start_radius_intensity(self, value: np.float32) -> None:
        """Set the StartRadiusIntensity field value."""
        member = self.get_member("StartRadiusIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartRadiusIntensity", fields.FieldFloat(value=value)
            )

    @property
    def end_radius_intensity(self) -> np.float32 | None:
        """The EndRadiusIntensity field value."""
        member = self.get_member("EndRadiusIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_radius_intensity.setter
    def end_radius_intensity(self, value: np.float32) -> None:
        """Set the EndRadiusIntensity field value."""
        member = self.get_member("EndRadiusIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndRadiusIntensity", fields.FieldFloat(value=value)
            )

    @property
    def radius_power(self) -> np.float32 | None:
        """The RadiusPower field value."""
        member = self.get_member("RadiusPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius_power.setter
    def radius_power(self, value: np.float32) -> None:
        """Set the RadiusPower field value."""
        member = self.get_member("RadiusPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadiusPower", fields.FieldFloat(value=value)
            )

    @property
    def start_axis_offset(self) -> np.float32 | None:
        """The StartAxisOffset field value."""
        member = self.get_member("StartAxisOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_axis_offset.setter
    def start_axis_offset(self, value: np.float32) -> None:
        """Set the StartAxisOffset field value."""
        member = self.get_member("StartAxisOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartAxisOffset", fields.FieldFloat(value=value)
            )

    @property
    def end_axis_offset(self) -> np.float32 | None:
        """The EndAxisOffset field value."""
        member = self.get_member("EndAxisOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_axis_offset.setter
    def end_axis_offset(self, value: np.float32) -> None:
        """Set the EndAxisOffset field value."""
        member = self.get_member("EndAxisOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndAxisOffset", fields.FieldFloat(value=value)
            )

    @property
    def start_axis_intensity(self) -> np.float32 | None:
        """The StartAxisIntensity field value."""
        member = self.get_member("StartAxisIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_axis_intensity.setter
    def start_axis_intensity(self, value: np.float32) -> None:
        """Set the StartAxisIntensity field value."""
        member = self.get_member("StartAxisIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartAxisIntensity", fields.FieldFloat(value=value)
            )

    @property
    def end_axis_intensity(self) -> np.float32 | None:
        """The EndAxisIntensity field value."""
        member = self.get_member("EndAxisIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_axis_intensity.setter
    def end_axis_intensity(self, value: np.float32) -> None:
        """Set the EndAxisIntensity field value."""
        member = self.get_member("EndAxisIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndAxisIntensity", fields.FieldFloat(value=value)
            )

    @property
    def axis_power(self) -> np.float32 | None:
        """The AxisPower field value."""
        member = self.get_member("AxisPower")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis_power.setter
    def axis_power(self, value: np.float32) -> None:
        """Set the AxisPower field value."""
        member = self.get_member("AxisPower")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AxisPower", fields.FieldFloat(value=value)
            )

