"""Generated component: HoverDynamicValueSet."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iui_hoverable import IUIHoverable
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HoverDynamicValueSet(GenericComponent[T], IUIHoverable, IUIComputeComponent, IWorldEventReceiver):
    """The HoverDynamicValueSet component listens for a user's hover event on a UIX element and sets a value.

}}

    Category: UIX/Interaction

    Parameterize with a value type::

        HoverDynamicValueSet[primitives.Float]
        HoverDynamicValueSet[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.HoverDynamicValueSet<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.HoverDynamicValueSet<>"

    def __init__(self, variable_name: primitives.String | None = None, value_on_begin_hover: T | None = None, value_on_end_hover: T | None = None, set_value_on_begin_hover: primitives.Bool | None = None, set_value_on_end_hover: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            value_on_begin_hover: Initial value for ValueOnBeginHover.
            value_on_end_hover: Initial value for ValueOnEndHover.
            set_value_on_begin_hover: Initial value for SetValueOnBeginHover.
            set_value_on_end_hover: Initial value for SetValueOnEndHover.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if value_on_begin_hover is not None:
            self.value_on_begin_hover = value_on_begin_hover
        if value_on_end_hover is not None:
            self.value_on_end_hover = value_on_end_hover
        if set_value_on_begin_hover is not None:
            self.set_value_on_begin_hover = set_value_on_begin_hover
        if set_value_on_end_hover is not None:
            self.set_value_on_end_hover = set_value_on_end_hover

    @property
    def variable_name(self) -> primitives.String | None:
        """The dynamic variable name to find these values."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: primitives.String) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def value_on_begin_hover(self) -> T | None:
        """The ValueOnBeginHover field value (type depends on type parameter)."""
        member = self.get_member("ValueOnBeginHover")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_on_begin_hover.setter
    def value_on_begin_hover(self, value: T) -> None:
        """Set the ValueOnBeginHover field value."""
        member = self.get_member("ValueOnBeginHover")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "ValueOnBeginHover", self._type_info.field_class(value=value)
            )

    @property
    def value_on_end_hover(self) -> T | None:
        """The ValueOnEndHover field value (type depends on type parameter)."""
        member = self.get_member("ValueOnEndHover")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @value_on_end_hover.setter
    def value_on_end_hover(self, value: T) -> None:
        """Set the ValueOnEndHover field value."""
        member = self.get_member("ValueOnEndHover")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "ValueOnEndHover", self._type_info.field_class(value=value)
            )

    @property
    def set_value_on_begin_hover(self) -> primitives.Bool | None:
        """Sets the value when a hover event is detected."""
        member = self.get_member("SetValueOnBeginHover")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_value_on_begin_hover.setter
    def set_value_on_begin_hover(self, value: primitives.Bool) -> None:
        """Set the SetValueOnBeginHover field value."""
        member = self.get_member("SetValueOnBeginHover")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetValueOnBeginHover", fields.FieldBool(value=value)
            )

    @property
    def set_value_on_end_hover(self) -> primitives.Bool | None:
        """Sets the value when a hover event has ended."""
        member = self.get_member("SetValueOnEndHover")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_value_on_end_hover.setter
    def set_value_on_end_hover(self, value: primitives.Bool) -> None:
        """Set the SetValueOnEndHover field value."""
        member = self.get_member("SetValueOnEndHover")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetValueOnEndHover", fields.FieldBool(value=value)
            )

