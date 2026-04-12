"""Generated component: SineHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SineHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SineHapticFilter component is used to make haptics triggered by Components on the same slot change in intensity over time like its riding waves.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics/Filters

    Attach to a slot with a HapticVolume and a collider. This component will
    then start working.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SineHapticFilter"

    def __init__(self, use_global_time: primitives.Bool | None = None, distance_scale: primitives.Float | None = None, axis_scale: primitives.Float3 | None = None, min_intensity: primitives.Float | None = None, max_intensity: primitives.Float | None = None, frequency: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
    def use_global_time(self) -> primitives.Bool | None:
        """Whether to use the global time or the initial local time for initial time when touched."""
        member = self.get_member("UseGlobalTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_global_time.setter
    def use_global_time(self, value: primitives.Bool) -> None:
        """Set the UseGlobalTime field value."""
        member = self.get_member("UseGlobalTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseGlobalTime", fields.FieldBool(value=value)
            )

    @property
    def distance_scale(self) -> primitives.Float | None:
        """An optional value on how to add to the offset in time for the waves of intensity based on distance of the haptic device from the slot this component is on."""
        member = self.get_member("DistanceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_scale.setter
    def distance_scale(self, value: primitives.Float) -> None:
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
        """An optional value on how to add to the offset in time for the waves of intensity based on how close it is to a line direction in local space."""
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
    def min_intensity(self) -> primitives.Float | None:
        """The minimum haptics intensity this component will send."""
        member = self.get_member("MinIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_intensity.setter
    def min_intensity(self, value: primitives.Float) -> None:
        """Set the MinIntensity field value."""
        member = self.get_member("MinIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinIntensity", fields.FieldFloat(value=value)
            )

    @property
    def max_intensity(self) -> primitives.Float | None:
        """The maximum haptics intensity this component will send."""
        member = self.get_member("MaxIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_intensity.setter
    def max_intensity(self, value: primitives.Float) -> None:
        """Set the MaxIntensity field value."""
        member = self.get_member("MaxIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxIntensity", fields.FieldFloat(value=value)
            )

    @property
    def frequency(self) -> primitives.Float | None:
        """The speed at which the sinewave goes up and down over time."""
        member = self.get_member("Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frequency.setter
    def frequency(self, value: primitives.Float) -> None:
        """Set the Frequency field value."""
        member = self.get_member("Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Frequency", fields.FieldFloat(value=value)
            )

