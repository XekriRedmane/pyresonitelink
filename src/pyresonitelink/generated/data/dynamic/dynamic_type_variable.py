"""Generated component: DynamicTypeVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idynamic_variable import IDynamicVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicTypeVariable(GeneratedComponent, IDynamicVariable, IComponent, IWorldEventReceiver):
    """The DynamicTypeVariable Component is used to define a Type as the value of a dynamic variable.

    Category: Data/Dynamic

    For more info on Dynamic Variables and how they work including this type
    of component, see Dynamic Variables.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicTypeVariable"

    def __init__(self, variable_name: primitives.String | None = None, value: Type | str | None = None, override_on_link: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            value: Initial value for Value.
            override_on_link: Initial value for OverrideOnLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if value is not None:
            self.value = value
        if override_on_link is not None:
            self.override_on_link = override_on_link

    @property
    def variable_name(self) -> primitives.String | None:
        """The name of the variable."""
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
    def value(self) -> Type | None:
        """The value of the dynamic variable that keeps in sync with the variable's valye."""
        member = self.get_member("Value")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @value.setter
    def value(self, value: Type | str) -> None:
        """Set Value. The value of the dynamic variable that keeps in sync with the variable's valye."""
        member = self.get_member("Value")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Value",
                members.FieldEnum(value=str(value)),
            )

    @property
    def override_on_link(self) -> primitives.Bool | None:
        """Whether to write the current value of the dynamic variable in a space when it connects to it with the one this component is storing."""
        member = self.get_member("OverrideOnLink")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_on_link.setter
    def override_on_link(self, value: primitives.Bool) -> None:
        """Set the OverrideOnLink field value."""
        member = self.get_member("OverrideOnLink")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideOnLink", fields.FieldBool(value=value)
            )

