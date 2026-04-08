"""Generated component: DynamicVariableStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.idynamic_variable import IDynamicVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicVariableStatus(GenericComponent[T], IDynamicVariable[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicVariableStatus<>.

    Category: Data/Dynamic

    Parameterize with a value type::

        DynamicVariableStatus[primitives.Float]
        DynamicVariableStatus[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicVariableStatus<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DynamicVariableStatus<>"

    def __init__(self, variable_name: primitives.String | None = None, is_linked_to_space: primitives.Bool | None = None, variable_exists: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            is_linked_to_space: Initial value for IsLinkedToSpace.
            variable_exists: Initial value for VariableExists.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if is_linked_to_space is not None:
            self.is_linked_to_space = is_linked_to_space
        if variable_exists is not None:
            self.variable_exists = variable_exists

    @property
    def variable_name(self) -> primitives.String | None:
        """The VariableName field value."""
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
    def is_linked_to_space(self) -> primitives.Bool | None:
        """The IsLinkedToSpace field value."""
        member = self.get_member("IsLinkedToSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_linked_to_space.setter
    def is_linked_to_space(self, value: primitives.Bool) -> None:
        """Set the IsLinkedToSpace field value."""
        member = self.get_member("IsLinkedToSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLinkedToSpace", fields.FieldBool(value=value)
            )

    @property
    def variable_exists(self) -> primitives.Bool | None:
        """The VariableExists field value."""
        member = self.get_member("VariableExists")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_exists.setter
    def variable_exists(self, value: primitives.Bool) -> None:
        """Set the VariableExists field value."""
        member = self.get_member("VariableExists")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableExists", fields.FieldBool(value=value)
            )

