"""Generated component: DynamicField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.idynamic_variable import IDynamicVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicField(GenericComponent[T], IDynamicVariable[T], IComponent, IWorldEventReceiver):
    """The DynamicField binds the field pointed to by ``TargetField`` to the dynamic variable referred to by ``VariableName``. The field must be a value type.

    Category: Data/Dynamic

    This component works almost exactly like the DynamicValueVariable
    component, except that the value used for the dynamic variable is
    sourced from a separate field. This field will be automatically updated
    with the value of the dynamic variable, and writing to the field will
    write to the dynamic variable. This can be used to directly bind fields
    of separate components as a dynamic variable without having to use a
    DynamicValueVariableDriver or similar setup.

    Parameterize with a value type::

        DynamicField[primitives.Float]
        DynamicField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DynamicField<>"

    def __init__(self, variable_name: primitives.String | None = None, target_field: str | IField[T] | None = None, override_on_link: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            target_field: Initial value for TargetField.
            override_on_link: Initial value for OverrideOnLink.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if target_field is not None:
            self.target_field = target_field
        if override_on_link is not None:
            self.override_on_link = override_on_link

    @property
    def variable_name(self) -> primitives.String | None:
        """The name of the dynamic variable to be used"""
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
    def target_field(self) -> str | None:
        """The field that will be used as the dynamic variable's value."""
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_field.setter
    def target_field(self, target: str | IField[T] | None) -> None:
        """Set the TargetField reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def override_on_link(self) -> primitives.Bool | None:
        """If true, the value of the field will be written when this component is moved into a new space"""
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

