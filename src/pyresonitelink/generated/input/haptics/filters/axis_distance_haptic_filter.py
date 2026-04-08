"""Generated component: AxisDistanceHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisDistanceHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AxisDistanceHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisDistanceHapticFilter"

    def __init__(self, axis: primitives.Float3 | None = None, start_distance: primitives.Float | None = None, end_distance: primitives.Float | None = None, start_intensity: primitives.Float | None = None, end_intensity: primitives.Float | None = None, power: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            axis: Initial value for Axis.
            start_distance: Initial value for StartDistance.
            end_distance: Initial value for EndDistance.
            start_intensity: Initial value for StartIntensity.
            end_intensity: Initial value for EndIntensity.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if axis is not None:
            self.axis = axis
        if start_distance is not None:
            self.start_distance = start_distance
        if end_distance is not None:
            self.end_distance = end_distance
        if start_intensity is not None:
            self.start_intensity = start_intensity
        if end_intensity is not None:
            self.end_intensity = end_intensity
        if power is not None:
            self.power = power

    @property
    def axis(self) -> primitives.Float3 | None:
        """The Axis field value."""
        member = self.get_member("Axis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis.setter
    def axis(self, value: primitives.Float3) -> None:
        """Set the Axis field value."""
        member = self.get_member("Axis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Axis", fields.FieldFloat3(value=value)
            )

    @property
    def start_distance(self) -> primitives.Float | None:
        """The StartDistance field value."""
        member = self.get_member("StartDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_distance.setter
    def start_distance(self, value: primitives.Float) -> None:
        """Set the StartDistance field value."""
        member = self.get_member("StartDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartDistance", fields.FieldFloat(value=value)
            )

    @property
    def end_distance(self) -> primitives.Float | None:
        """The EndDistance field value."""
        member = self.get_member("EndDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_distance.setter
    def end_distance(self, value: primitives.Float) -> None:
        """Set the EndDistance field value."""
        member = self.get_member("EndDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndDistance", fields.FieldFloat(value=value)
            )

    @property
    def start_intensity(self) -> primitives.Float | None:
        """The StartIntensity field value."""
        member = self.get_member("StartIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_intensity.setter
    def start_intensity(self, value: primitives.Float) -> None:
        """Set the StartIntensity field value."""
        member = self.get_member("StartIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartIntensity", fields.FieldFloat(value=value)
            )

    @property
    def end_intensity(self) -> primitives.Float | None:
        """The EndIntensity field value."""
        member = self.get_member("EndIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_intensity.setter
    def end_intensity(self, value: primitives.Float) -> None:
        """Set the EndIntensity field value."""
        member = self.get_member("EndIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndIntensity", fields.FieldFloat(value=value)
            )

    @property
    def power(self) -> primitives.Float | None:
        """The Power field value."""
        member = self.get_member("Power")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @power.setter
    def power(self, value: primitives.Float) -> None:
        """Set the Power field value."""
        member = self.get_member("Power")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Power", fields.FieldFloat(value=value)
            )

