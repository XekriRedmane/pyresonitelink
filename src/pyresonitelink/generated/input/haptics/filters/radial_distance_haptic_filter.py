"""Generated component: RadialDistanceHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadialDistanceHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The RadialDistanceHapticFilter controls haptic areas on the same slot so that haptics within their range are influenced differently depending on how far away they are from the slot center in local space. The start and end intensities when mapped to the haptic devices Distance from the slot, the power is unclamped.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics/Filters

    Attach to a slot with a HapticVolume for the simplest use case. Bringing
    a user's VR controllers closer or further away changes that device's
    haptics intensity.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadialDistanceHapticFilter"

    def __init__(self, start_radius: primitives.Float | None = None, end_radius: primitives.Float | None = None, start_intensity: primitives.Float | None = None, end_intensity: primitives.Float | None = None, power: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
    def start_radius(self) -> primitives.Float | None:
        """The starting radius point (Usually 0 distance). When the haptic device point is this Distance away from the slot this component is on in local space, the haptic gets a signal of ``Power``*``StartIntensity``"""
        member = self.get_member("StartRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_radius.setter
    def start_radius(self, value: primitives.Float) -> None:
        """Set the StartRadius field value."""
        member = self.get_member("StartRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartRadius", fields.FieldFloat(value=value)
            )

    @property
    def end_radius(self) -> primitives.Float | None:
        """The ending radius point (Usually 0 distance). When the haptic device point is this Distance away from the slot this component is on in local space, the haptic gets a signal of ``Power``*``StartIntensity``."""
        member = self.get_member("EndRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_radius.setter
    def end_radius(self, value: primitives.Float) -> None:
        """Set the EndRadius field value."""
        member = self.get_member("EndRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndRadius", fields.FieldFloat(value=value)
            )

    @property
    def start_intensity(self) -> primitives.Float | None:
        """The intensity*``Power`` for the haptic device when it is ``StartRadius`` from the slot this component is on."""
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
        """The intensity*``Power`` for the haptic device when it is ``EndRadius`` from the slot this component is on."""
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
        """How much to amplify the intensity for the haptic device."""
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

