"""Generated component: HapticVolume."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.sensation_class import SensationClass
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ihaptic_source import IHapticSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HapticVolume(GeneratedComponent, IHapticSource, IComponent, IWorldEventReceiver):
    """Haptic Volumes allows a user to feel haptics through a collider set to Haptic Trigger shared on the same slot.

Haptic Volumes can be paired with Haptic Filters placed on the same slot to give more precise control over a user's haptics. Each haptic filter is applied by multiplying each influence together, hence being multiplicative.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics

    When placed on a slot with a collider component, the collider's type
    automatically switches to haptic trigger.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HapticVolume"

    def __init__(self, sensation: SensationClass | str | None = None, intensity: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            sensation: Initial value for Sensation.
            intensity: Initial value for Intensity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if sensation is not None:
            self.sensation = sensation
        if intensity is not None:
            self.intensity = intensity

    @property
    def sensation(self) -> SensationClass | None:
        """The type of haptic you want to do, for controllers the haptic types are subtly different variations. Specifying this is useful for haptic suits that have more advanced haptic motors."""
        member = self.get_member("Sensation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SensationClass(member.value)
        return None

    @sensation.setter
    def sensation(self, value: SensationClass | str) -> None:
        """Set Sensation. The type of haptic you want to do, for controllers the haptic types are subtly different variations. Specifying this is useful for haptic suits that have more advanced haptic motors."""
        member = self.get_member("Sensation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Sensation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def intensity(self) -> primitives.Float | None:
        """The haptic intensity ranging from zero to one, zero being none one being max that the device allows."""
        member = self.get_member("Intensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intensity.setter
    def intensity(self, value: primitives.Float) -> None:
        """Set the Intensity field value."""
        member = self.get_member("Intensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Intensity", fields.FieldFloat(value=value)
            )

    @property
    def sensation_hints(self) -> members.SyncList | None:
        """Allows triggering specific predefined sensations with certain haptic devices. Only useful for OWO haptic vests currently."""
        member = self.get_member("SensationHints")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sensation_hints.setter
    def sensation_hints(self, value: members.SyncList) -> None:
        """Set SensationHints. Allows triggering specific predefined sensations with certain haptic devices. Only useful for OWO haptic vests currently."""
        self.set_member("SensationHints", value)

