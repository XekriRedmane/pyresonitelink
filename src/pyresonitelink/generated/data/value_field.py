"""Generated component: ValueField."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ivalue_source import IValueSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueField(GenericComponent[T], IValueSource[T], IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueField<>.

    Category: Data

    Parameterize with a value type::

        ValueField[primitives.Float]
        ValueField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueField<>"

    def __init__(self, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if value is not None:
            self.value = value

    @property
    def value(self) -> T | None:
        """The Value field value (type depends on type parameter)."""
        member = self.get_member("Value")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value.setter
    def value(self, value: T) -> None:
        """Set the Value field value."""
        member = self.get_member("Value")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Value", self._type_info.field_class(value=value)
            )

