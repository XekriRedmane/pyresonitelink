"""Generated component: DirectTagHapticSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idirect_haptic_source import IDirectHapticSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DirectTagHapticSource(GeneratedComponent, IDirectHapticSource, IComponent, IWorldEventReceiver):
    """The DirectTagHapticsSource component allows driving haptic sensations for a given haptic point directly, rather than using the haptic volume system.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics

    * works only with tagged haptic points. This component must have a
    matching Tag to a configured haptic device and must be present under the
    user to work * It doesn't prevent the haptic volumes from sending
    haptics - the effects are additive. If you want only this component to
    control the haptics, do not setup a corresponding tagged haptic point
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DirectTagHapticSource"

    def __init__(self, haptic_tag: primitives.String | None = None, force: primitives.Float | None = None, temperature: primitives.Float | None = None, pain: primitives.Float | None = None, vibration: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            haptic_tag: Initial value for HapticTag.
            force: Initial value for Force.
            temperature: Initial value for Temperature.
            pain: Initial value for Pain.
            vibration: Initial value for Vibration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if haptic_tag is not None:
            self.haptic_tag = haptic_tag
        if force is not None:
            self.force = force
        if temperature is not None:
            self.temperature = temperature
        if pain is not None:
            self.pain = pain
        if vibration is not None:
            self.vibration = vibration

    @property
    def haptic_tag(self) -> primitives.String | None:
        """The tag to influence."""
        member = self.get_member("HapticTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @haptic_tag.setter
    def haptic_tag(self, value: primitives.String) -> None:
        """Set the HapticTag field value."""
        member = self.get_member("HapticTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HapticTag", fields.FieldString(value=value)
            )

    @property
    def force(self) -> primitives.Float | None:
        """The force addition for haptics with the ``HapticTag`` tag."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: primitives.Float) -> None:
        """Set the Force field value."""
        member = self.get_member("Force")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Force", fields.FieldFloat(value=value)
            )

    @property
    def temperature(self) -> primitives.Float | None:
        """The temperature addition for haptics with the ``HapticTag`` tag."""
        member = self.get_member("Temperature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @temperature.setter
    def temperature(self, value: primitives.Float) -> None:
        """Set the Temperature field value."""
        member = self.get_member("Temperature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Temperature", fields.FieldFloat(value=value)
            )

    @property
    def pain(self) -> primitives.Float | None:
        """The pain addition for haptics with the ``HapticTag`` tag."""
        member = self.get_member("Pain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pain.setter
    def pain(self, value: primitives.Float) -> None:
        """Set the Pain field value."""
        member = self.get_member("Pain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pain", fields.FieldFloat(value=value)
            )

    @property
    def vibration(self) -> primitives.Float | None:
        """The vibration addition for haptics with the ``HapticTag`` tag."""
        member = self.get_member("Vibration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vibration.setter
    def vibration(self, value: primitives.Float) -> None:
        """Set the Vibration field value."""
        member = self.get_member("Vibration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vibration", fields.FieldFloat(value=value)
            )

