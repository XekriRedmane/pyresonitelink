"""Generated component: CloudValueVariableDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CloudValueVariableDriver(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The CloudValueVariableDriver component drives the ``Target`` field of type T with the value of the specified cloud variable owned by the local user.

    Category: Cloud/Variables

    Upon being given a valid cloud variable ``Path``, the component will
    drive the value of the ``Target`` with the value of the cloud variable
    owned by the local user. If ``OverrideOwner`` is specified, the field
    will only be driven to the value for the user specified in
    ``OverrideOwner``. Otherwise, the field will take the value of the
    ``FallbackValue``.

    Parameterize with a value type::

        CloudValueVariableDriver[primitives.Float]
        CloudValueVariableDriver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloudValueVariableDriver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CloudValueVariableDriver<>"

    def __init__(self, path: primitives.String | None = None, target: str | IField[T] | None = None, is_linked_to_cloud: primitives.Bool | None = None, write_back: primitives.Bool | None = None, fallback_value: T | None = None, override_owner: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            target: Initial value for Target.
            is_linked_to_cloud: Initial value for IsLinkedToCloud.
            write_back: Initial value for WriteBack.
            fallback_value: Initial value for FallbackValue.
            override_owner: Initial value for OverrideOwner.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path
        if target is not None:
            self.target = target
        if is_linked_to_cloud is not None:
            self.is_linked_to_cloud = is_linked_to_cloud
        if write_back is not None:
            self.write_back = write_back
        if fallback_value is not None:
            self.fallback_value = fallback_value
        if override_owner is not None:
            self.override_owner = override_owner

    @property
    def path(self) -> primitives.String | None:
        """The path of the variable this component will read."""
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
    def target(self) -> str | None:
        """The target field to which the variable value will be written."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[T] | None) -> None:
        """Set the Target reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def is_linked_to_cloud(self) -> primitives.Bool | None:
        """(Read Only) Indicates whether this field was successfully bound to the target variable."""
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
    def write_back(self) -> primitives.Bool | None:
        """Updates the value in the cloud when the driven field is changed. See write backs."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
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
    def override_owner(self) -> primitives.String | None:
        """The UserID of the user that made a definition for the variable specified by ``Path`` or the local user if not specified."""
        member = self.get_member("OverrideOwner")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_owner.setter
    def override_owner(self, value: primitives.String) -> None:
        """Set the OverrideOwner field value."""
        member = self.get_member("OverrideOwner")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideOwner", fields.FieldString(value=value)
            )

