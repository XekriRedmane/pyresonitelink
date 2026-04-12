"""Generated component: CloudValueField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.cloud_variable_change_mode import CloudVariableChangeMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CloudValueField(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The CloudValueField component links a field of type T to a cloud variable.

For more info on how Cloud Variables work in general, see Cloud Variables.

    Category: Cloud/Variables

    Put this component on a slot, and give it a valid cloud variable
    ``Path`` and ``VariableOwnerId``. When given a ``Target``, the contents
    of the field given to ``Target`` will auto update with the cloud
    variable value. Depending on the value of ``ChangeHandling`` and
    ``VariableOwnerId``, the cloud variable may be updated through this
    component as well. This updates as fast as reading/writing cloud
    variables permits. All the restrictions that apply to cloud variables
    apply to this component, including permissions and world contexts.

    Parameterize with a value type::

        CloudValueField[primitives.Float]
        CloudValueField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloudValueField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CloudValueField<>"

    def __init__(self, path: primitives.String | None = None, is_linked_to_cloud: primitives.Bool | None = None, variable_owner_id: primitives.String | None = None, change_handling: CloudVariableChangeMode | str | None = None, target: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            is_linked_to_cloud: Initial value for IsLinkedToCloud.
            variable_owner_id: Initial value for VariableOwnerId.
            change_handling: Initial value for ChangeHandling.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if path is not None:
            self.path = path
        if is_linked_to_cloud is not None:
            self.is_linked_to_cloud = is_linked_to_cloud
        if variable_owner_id is not None:
            self.variable_owner_id = variable_owner_id
        if change_handling is not None:
            self.change_handling = change_handling
        if target is not None:
            self.target = target

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
    def variable_owner_id(self) -> primitives.String | None:
        """The UserID of the user that made a definition for the variable specified by ``Path``"""
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
    def change_handling(self) -> CloudVariableChangeMode | None:
        """See Cloud Variable Change Mode."""
        member = self.get_member("ChangeHandling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CloudVariableChangeMode(member.value)
        return None

    @change_handling.setter
    def change_handling(self, value: CloudVariableChangeMode | str) -> None:
        """Set ChangeHandling. See Cloud Variable Change Mode."""
        member = self.get_member("ChangeHandling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ChangeHandling",
                members.FieldEnum(value=str(value)),
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

