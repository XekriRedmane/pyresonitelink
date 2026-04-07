"""Generated component: DynamicTypeVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.idynamic_variable import IDynamicVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicTypeVariable(GeneratedComponent, IDynamicVariable, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicTypeVariable.

    Category: Data/Dynamic
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicTypeVariable"

    def __init__(self, variable_name: str | None = None, override_on_link: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            override_on_link: Initial value for OverrideOnLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if override_on_link is not None:
            self.override_on_link = override_on_link

    @property
    def variable_name(self) -> str | None:
        """The VariableName field value."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: str) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def value(self) -> members.Member | None:
        """The Value member."""
        member = self.get_member("Value")
        if isinstance(member, members.Member):
            return member
        return None

    @value.setter
    def value(self, value: members.Member) -> None:
        """Set the Value member."""
        self.set_member("Value", value)

    @property
    def override_on_link(self) -> bool | None:
        """The OverrideOnLink field value."""
        member = self.get_member("OverrideOnLink")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_on_link.setter
    def override_on_link(self, value: bool) -> None:
        """Set the OverrideOnLink field value."""
        member = self.get_member("OverrideOnLink")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideOnLink", fields.FieldBool(value=value)
            )

