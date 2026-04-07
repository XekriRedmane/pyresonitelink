"""Generated component: ValueField."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T


class ValueField(GenericComponent[T]):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueField<>.

    Category: Data

    Parameterize with a value type::

        ValueField[np.float32]
        ValueField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueField<>"

    def __init__(self, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize, optionally setting Value.

        Args:
            value: Initial value for the Value field.
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
        elif self._type_info is not None:
            self.set_member(
                "Value", self._type_info.field_class(value=value)
            )

