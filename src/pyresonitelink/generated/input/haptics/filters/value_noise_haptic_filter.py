"""Generated component: ValueNoiseHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueNoiseHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ValueNoiseHapticFilter component makes a random intensity value every update to a device touching a HapticVolume.

This works as part of the game's robust Haptics system.

    Category: Input/Haptics/Filters

    Attach to a slot with a valid and working HapticVolume to add to the
    list of multiplicative haptic filters.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueNoiseHapticFilter"

    def __init__(self, min_value: primitives.Float | None = None, max_value: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def min_value(self) -> primitives.Float | None:
        """The minimum haptic intensity to output in a game tick."""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: primitives.Float) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldFloat(value=value)
            )

    @property
    def max_value(self) -> primitives.Float | None:
        """The maximum haptic intensity to output in a game tick."""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: primitives.Float) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldFloat(value=value)
            )

