"""Generated component: ActiveUserCloudValueVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ActiveUserCloudValueVariable(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ActiveUserCloudValueVariable<>.

    Category: Cloud/Variables

    Parameterize with a value type::

        ActiveUserCloudValueVariable[primitives.Float]
        ActiveUserCloudValueVariable[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ActiveUserCloudValueVariable<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ActiveUserCloudValueVariable<>"

    def __init__(self, path: primitives.String | None = None, is_linked_to_cloud: primitives.Bool | None = None, update_cloud_variable: primitives.Bool | None = None, fallback_value: T | None = None, value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            is_linked_to_cloud: Initial value for IsLinkedToCloud.
            update_cloud_variable: Initial value for UpdateCloudVariable.
            fallback_value: Initial value for FallbackValue.
            value: Initial value for Value.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path
        if is_linked_to_cloud is not None:
            self.is_linked_to_cloud = is_linked_to_cloud
        if update_cloud_variable is not None:
            self.update_cloud_variable = update_cloud_variable
        if fallback_value is not None:
            self.fallback_value = fallback_value
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
    def update_cloud_variable(self) -> primitives.Bool | None:
        """The UpdateCloudVariable field value."""
        member = self.get_member("UpdateCloudVariable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_cloud_variable.setter
    def update_cloud_variable(self, value: primitives.Bool) -> None:
        """Set the UpdateCloudVariable field value."""
        member = self.get_member("UpdateCloudVariable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateCloudVariable", fields.FieldBool(value=value)
            )

    @property
    def fallback_value(self) -> T | None:
        """The FallbackValue field value (type depends on type parameter)."""
        member = self.get_member("FallbackValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fallback_value.setter
    def fallback_value(self, value: T) -> None:
        """Set the FallbackValue field value."""
        member = self.get_member("FallbackValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "FallbackValue", self._type_info.field_class(value=value)
            )

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

