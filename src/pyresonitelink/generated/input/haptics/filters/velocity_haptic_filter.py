"""Generated component: VelocityHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VelocityHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VelocityHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VelocityHapticFilter"

    def __init__(self, velocity_smooth_time: primitives.Float | None = None, start_velocity: primitives.Float | None = None, end_velocity: primitives.Float | None = None, start_intensity: primitives.Float | None = None, end_intensity: primitives.Float | None = None, power: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            velocity_smooth_time: Initial value for VelocitySmoothTime.
            start_velocity: Initial value for StartVelocity.
            end_velocity: Initial value for EndVelocity.
            start_intensity: Initial value for StartIntensity.
            end_intensity: Initial value for EndIntensity.
            power: Initial value for Power.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if velocity_smooth_time is not None:
            self.velocity_smooth_time = velocity_smooth_time
        if start_velocity is not None:
            self.start_velocity = start_velocity
        if end_velocity is not None:
            self.end_velocity = end_velocity
        if start_intensity is not None:
            self.start_intensity = start_intensity
        if end_intensity is not None:
            self.end_intensity = end_intensity
        if power is not None:
            self.power = power

    @property
    def velocity_smooth_time(self) -> primitives.Float | None:
        """The VelocitySmoothTime field value."""
        member = self.get_member("VelocitySmoothTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity_smooth_time.setter
    def velocity_smooth_time(self, value: primitives.Float) -> None:
        """Set the VelocitySmoothTime field value."""
        member = self.get_member("VelocitySmoothTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VelocitySmoothTime", fields.FieldFloat(value=value)
            )

    @property
    def start_velocity(self) -> primitives.Float | None:
        """The StartVelocity field value."""
        member = self.get_member("StartVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_velocity.setter
    def start_velocity(self, value: primitives.Float) -> None:
        """Set the StartVelocity field value."""
        member = self.get_member("StartVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartVelocity", fields.FieldFloat(value=value)
            )

    @property
    def end_velocity(self) -> primitives.Float | None:
        """The EndVelocity field value."""
        member = self.get_member("EndVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_velocity.setter
    def end_velocity(self, value: primitives.Float) -> None:
        """Set the EndVelocity field value."""
        member = self.get_member("EndVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndVelocity", fields.FieldFloat(value=value)
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

