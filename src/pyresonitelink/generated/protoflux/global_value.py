"""Generated component: GlobalValue."""

from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GlobalValue(GenericComponent[T], IGlobalValueProxy[T], IComponent, IWorldEventReceiver):
    """The GlobalValue&lt;T&gt; component is used by ProtoFlux to define a global of a FrooxEngine value type.

    Category: ProtoFlux

    When not using ProtoFlux, this component has no use over more idiomatic
    components such as a ValueField. When using ProtoFlux, the underlying
    value can be changed and any node that accepts a global input that
    references the component will update during execution. This can allow
    one to dynamically change things like dynamic impulse receiver tags.
    This component can also simply be used for static global values that
    need to be referenced in a lot of places for when the overhead of
    dynamic variables is undesirable. When combined with the Global To
    Output node, this component also provides more UX than sourcing a
    ValueField by being able to see the underlying value directly.

    Parameterize with a value type::

        GlobalValue[primitives.Float]
        GlobalValue[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalValue<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ProtoFlux.GlobalValue<>"

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

