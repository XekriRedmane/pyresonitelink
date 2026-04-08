"""Generated component: CloudValueVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CloudValueVariable(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CloudValueVariable<>.

    Category: Cloud/Variables

    Parameterize with a value type::

        CloudValueVariable[primitives.Float]
        CloudValueVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloudValueVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CloudValueVariable<>"

    def __init__(self, path: primitives.String | None = None, is_linked_to_cloud: primitives.Bool | None = None, variable_owner_id: primitives.String | None = None, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            is_linked_to_cloud: Initial value for IsLinkedToCloud.
            variable_owner_id: Initial value for VariableOwnerId.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path
        if is_linked_to_cloud is not None:
            self.is_linked_to_cloud = is_linked_to_cloud
        if variable_owner_id is not None:
            self.variable_owner_id = variable_owner_id
        if value is not None:
            self.value = value

    @property
    def path(self) -> primitives.String | None:
        """The Path field value."""
        member = self.get_member("Path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
        """Set the Path field value."""
        member = self.get_member("Path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Path", fields.FieldString(value=value)
            )

    @property
    def is_linked_to_cloud(self) -> primitives.Bool | None:
        """The IsLinkedToCloud field value."""
        member = self.get_member("IsLinkedToCloud")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_linked_to_cloud.setter
    def is_linked_to_cloud(self, value: primitives.Bool) -> None:
        """Set the IsLinkedToCloud field value."""
        member = self.get_member("IsLinkedToCloud")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLinkedToCloud", fields.FieldBool(value=value)
            )

    @property
    def variable_owner_id(self) -> primitives.String | None:
        """The VariableOwnerId field value."""
        member = self.get_member("VariableOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_owner_id.setter
    def variable_owner_id(self, value: primitives.String) -> None:
        """Set the VariableOwnerId field value."""
        member = self.get_member("VariableOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableOwnerId", fields.FieldString(value=value)
            )

    @property
    def change_handling(self) -> members.FieldEnum | None:
        """The ChangeHandling member."""
        member = self.get_member("ChangeHandling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @change_handling.setter
    def change_handling(self, value: members.FieldEnum) -> None:
        """Set the ChangeHandling member."""
        self.set_member("ChangeHandling", value)

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

