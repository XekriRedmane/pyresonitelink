"""Generated component: ValueProxySource."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueProxySource(GenericComponent[T], IUIGrabbable, IWorldEventReceiver):
    """The ValueProxySource component allows for the user to grab a value off from a UIX element. This requires a Button component to work.

}}

    Category: UIX/Interaction

    This is used to carry values to other UIX elements that are looking for
    it. Using this component along with the ValueReceiver and ValueField of
    a value type will allow the user to carry the value from source to
    receiver directly.

    Parameterize with a value type::

        ValueProxySource[primitives.Float]
        ValueProxySource[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueProxySource<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueProxySource<>"

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

