"""Generated component: DynamicValueVariableReset."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicValueVariableReset(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicValueVariableReset<>.

    Category: Data/Dynamic

    Parameterize with a value type::

        DynamicValueVariableReset[np.float32]
        DynamicValueVariableReset[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicValueVariableReset<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.DynamicValueVariableReset<>"

    def __init__(self, variable_name: str | None = None, reset_on_load: bool | None = None, reset_on_duplicate: bool | None = None, reset_on_paste: bool | None = None, reset_value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            reset_on_load: Initial value for ResetOnLoad.
            reset_on_duplicate: Initial value for ResetOnDuplicate.
            reset_on_paste: Initial value for ResetOnPaste.
            reset_value: Initial value for ResetValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if reset_on_load is not None:
            self.reset_on_load = reset_on_load
        if reset_on_duplicate is not None:
            self.reset_on_duplicate = reset_on_duplicate
        if reset_on_paste is not None:
            self.reset_on_paste = reset_on_paste
        if reset_value is not None:
            self.reset_value = reset_value

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
    def reset_on_load(self) -> bool | None:
        """The ResetOnLoad field value."""
        member = self.get_member("ResetOnLoad")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_on_load.setter
    def reset_on_load(self, value: bool) -> None:
        """Set the ResetOnLoad field value."""
        member = self.get_member("ResetOnLoad")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetOnLoad", fields.FieldBool(value=value)
            )

    @property
    def reset_on_duplicate(self) -> bool | None:
        """The ResetOnDuplicate field value."""
        member = self.get_member("ResetOnDuplicate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_on_duplicate.setter
    def reset_on_duplicate(self, value: bool) -> None:
        """Set the ResetOnDuplicate field value."""
        member = self.get_member("ResetOnDuplicate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetOnDuplicate", fields.FieldBool(value=value)
            )

    @property
    def reset_on_paste(self) -> bool | None:
        """The ResetOnPaste field value."""
        member = self.get_member("ResetOnPaste")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_on_paste.setter
    def reset_on_paste(self, value: bool) -> None:
        """Set the ResetOnPaste field value."""
        member = self.get_member("ResetOnPaste")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetOnPaste", fields.FieldBool(value=value)
            )

    @property
    def reset_value(self) -> T | None:
        """The ResetValue field value (type depends on type parameter)."""
        member = self.get_member("ResetValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_value.setter
    def reset_value(self, value: T) -> None:
        """Set the ResetValue field value."""
        member = self.get_member("ResetValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None:
            self.set_member(
                "ResetValue", self._type_info.field_class(value=value)
            )

