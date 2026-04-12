"""Generated component: DebugHapticPoint."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ihaptic_source import IHapticSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugHapticPoint(GeneratedComponent, IHapticSource, IComponent, IWorldEventReceiver):
    """The DebugHapticPoint component sends Force sensations to a haptic device as well as gets the name of the haptic device.

This works as part of the game's robust Haptics system.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugHapticPoint"

    def __init__(self, intensity: primitives.Float | None = None, index: primitives.Int | None = None, position: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            intensity: Initial value for Intensity.
            index: Initial value for Index.
            position: Initial value for Position.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if intensity is not None:
            self.intensity = intensity
        if index is not None:
            self.index = index
        if position is not None:
            self.position = position

    @property
    def intensity(self) -> primitives.Float | None:
        """Sends a sensation of force of this intensity to the Haptic device at ``Index``"""
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
    def index(self) -> primitives.Int | None:
        """The haptic device to send Intensity to and get a name for."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def position(self) -> primitives.String | None:
        """The name of the haptic device at ``Index``"""
        member = self.get_member("Position")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position.setter
    def position(self, value: primitives.String) -> None:
        """Set the Position field value."""
        member = self.get_member("Position")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Position", fields.FieldString(value=value)
            )

