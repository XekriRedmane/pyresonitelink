"""Generated component: SimplexNoiseHapticFilter."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimplexNoiseHapticFilter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.SimplexNoiseHapticFilter.

    Category: Input/Haptics/Filters
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimplexNoiseHapticFilter"

    def __init__(self, noise_scale: primitives.Float3 | None = None, noise_offset: primitives.Float3 | None = None, min_value: primitives.Float | None = None, max_value: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            noise_scale: Initial value for NoiseScale.
            noise_offset: Initial value for NoiseOffset.
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if noise_scale is not None:
            self.noise_scale = noise_scale
        if noise_offset is not None:
            self.noise_offset = noise_offset
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value

    @property
    def noise_scale(self) -> primitives.Float3 | None:
        """The NoiseScale field value."""
        member = self.get_member("NoiseScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_scale.setter
    def noise_scale(self, value: primitives.Float3) -> None:
        """Set the NoiseScale field value."""
        member = self.get_member("NoiseScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseScale", fields.FieldFloat3(value=value)
            )

    @property
    def noise_offset(self) -> primitives.Float3 | None:
        """The NoiseOffset field value."""
        member = self.get_member("NoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @noise_offset.setter
    def noise_offset(self, value: primitives.Float3) -> None:
        """Set the NoiseOffset field value."""
        member = self.get_member("NoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoiseOffset", fields.FieldFloat3(value=value)
            )

    @property
    def min_value(self) -> primitives.Float | None:
        """The MinValue field value."""
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
        """The MaxValue field value."""
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

