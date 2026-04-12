"""Generated component: AuthorityTimeBase."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AuthorityTimeBase(GeneratedComponent, IValue, IComponent, IWorldEventReceiver):
    """The AuthorityTimeBase component allows for fine-grained control over the world time with a certain speed and with respect to a given offset.

    Category: Utility

    The output of the component is the current world time (as a Double)
    multiplied by the ``BaseSpeed``, minus the ``_actualOffset``. The output
    of the component is accessed by sourcing the component itself. To write
    to the current time of the component, you write to said source. When
    writing to the component source, ``_actualOffset`` is automatically
    updated to reflect the correct time. When writing to ``BaseSpeed``,
    ``_actualOffset`` is automatically updated to keep the same time.
    Writing to ``_actualOffset`` does not affect any other fields.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AuthorityTimeBase"

    def __init__(self, base_speed: primitives.Float | None = None, actual_speed: primitives.Float | None = None, actual_offset: primitives.Double | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            base_speed: Initial value for BaseSpeed.
            actual_speed: Initial value for _actualSpeed.
            actual_offset: Initial value for _actualOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if base_speed is not None:
            self.base_speed = base_speed
        if actual_speed is not None:
            self.actual_speed = actual_speed
        if actual_offset is not None:
            self.actual_offset = actual_offset

    @property
    def base_speed(self) -> primitives.Float | None:
        """Speed of the time base."""
        member = self.get_member("BaseSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_speed.setter
    def base_speed(self, value: primitives.Float) -> None:
        """Set the BaseSpeed field value."""
        member = self.get_member("BaseSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseSpeed", fields.FieldFloat(value=value)
            )

    @property
    def actual_speed(self) -> primitives.Float | None:
        """Actual speed of the time base. Should not be written to or driven."""
        member = self.get_member("_actualSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_speed.setter
    def actual_speed(self, value: primitives.Float) -> None:
        """Set the _actualSpeed field value."""
        member = self.get_member("_actualSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_actualSpeed", fields.FieldFloat(value=value)
            )

    @property
    def actual_offset(self) -> primitives.Double | None:
        """Offset of the time base from the current world time. Can be written to or driven perfectly fine."""
        member = self.get_member("_actualOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_offset.setter
    def actual_offset(self, value: primitives.Double) -> None:
        """Set the _actualOffset field value."""
        member = self.get_member("_actualOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_actualOffset", fields.FieldDouble(value=value)
            )

