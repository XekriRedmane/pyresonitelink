"""Generated component: AxisDistanceHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisDistanceHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AxisDistanceHapticFilter multiplicatively changes the intensity of a HapticVolume depending on the dot product from the vector of the device's position in local space to this component and ``Axis``. Essentially the smaller the angle between the device local position from 0 direction and the ``Axis`` direction the smaller the distance.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics/Filters

    Attach to a slot with a valid and working HapticVolume to add to the
    list of multiplicative haptic filters.
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
        """The axis to check distance from."""
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
        """The starting distance to map to ``StartIntensity`` for the intensity distance range."""
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
        """The ending distance to map to ``EndIntensity`` for the intensity distance range."""
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
        """When at ``StartDistance`` map the device intensity to this."""
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
        """When at ``EndDistance`` map the device intensity to this."""
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
        """How much to amplify the haptics effect in general."""
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

