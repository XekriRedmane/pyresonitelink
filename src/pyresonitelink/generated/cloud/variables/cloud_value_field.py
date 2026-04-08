"""Generated component: CloudValueField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CloudValueField(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CloudValueField<>.

    Category: Cloud/Variables

    Parameterize with a value type::

        CloudValueField[np.float32]
        CloudValueField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CloudValueField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.CloudValueField<>"

    def __init__(self, path: str | None = None, is_linked_to_cloud: bool | None = None, variable_owner_id: str | None = None, target: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            is_linked_to_cloud: Initial value for IsLinkedToCloud.
            variable_owner_id: Initial value for VariableOwnerId.
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
        if target is not None:
            self.target = target

    @property
    def path(self) -> str | None:
        """The Path field value."""
        member = self.get_member("Path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: str) -> None:
        """Set the Path field value."""
        member = self.get_member("Path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Path", fields.FieldString(value=value)
            )

    @property
    def is_linked_to_cloud(self) -> bool | None:
        """The IsLinkedToCloud field value."""
        member = self.get_member("IsLinkedToCloud")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_linked_to_cloud.setter
    def is_linked_to_cloud(self, value: bool) -> None:
        """Set the IsLinkedToCloud field value."""
        member = self.get_member("IsLinkedToCloud")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLinkedToCloud", fields.FieldBool(value=value)
            )

    @property
    def variable_owner_id(self) -> str | None:
        """The VariableOwnerId field value."""
        member = self.get_member("VariableOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_owner_id.setter
    def variable_owner_id(self, value: str) -> None:
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
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[T])."""
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

