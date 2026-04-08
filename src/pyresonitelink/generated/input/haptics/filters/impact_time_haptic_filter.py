"""Generated component: ImpactTimeHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ImpactTimeHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ImpactTimeHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ImpactTimeHapticFilter"

    def __init__(self, use_global_time: primitives.Bool | None = None, start_time: primitives.Float | None = None, end_time: primitives.Float | None = None, start_intensity: primitives.Float | None = None, end_intensity: primitives.Float | None = None, power: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_global_time: Initial value for UseGlobalTime.
            start_time: Initial value for StartTime.
            end_time: Initial value for EndTime.
            start_intensity: Initial value for StartIntensity.
            end_intensity: Initial value for EndIntensity.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_global_time is not None:
            self.use_global_time = use_global_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if start_intensity is not None:
            self.start_intensity = start_intensity
        if end_intensity is not None:
            self.end_intensity = end_intensity
        if power is not None:
            self.power = power

    @property
    def use_global_time(self) -> primitives.Bool | None:
        """The UseGlobalTime field value."""
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
    def start_time(self) -> primitives.Float | None:
        """The StartTime field value."""
        member = self.get_member("StartTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_time.setter
    def start_time(self, value: primitives.Float) -> None:
        """Set the StartTime field value."""
        member = self.get_member("StartTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartTime", fields.FieldFloat(value=value)
            )

    @property
    def end_time(self) -> primitives.Float | None:
        """The EndTime field value."""
        member = self.get_member("EndTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_time.setter
    def end_time(self, value: primitives.Float) -> None:
        """Set the EndTime field value."""
        member = self.get_member("EndTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndTime", fields.FieldFloat(value=value)
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

