"""Generated component: ActiveUserCloudField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ActiveUserCloudField(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ActiveUserCloudField<>.

    Category: Cloud/Variables

    Parameterize with a value type::

        ActiveUserCloudField[np.float32]
        ActiveUserCloudField[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ActiveUserCloudField<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ActiveUserCloudField<>"

    def __init__(self, path: str | None = None, is_linked_to_cloud: bool | None = None, update_cloud_variable: bool | None = None, fallback_value: T | None = None, target: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            path: Initial value for Path.
            is_linked_to_cloud: Initial value for IsLinkedToCloud.
            update_cloud_variable: Initial value for UpdateCloudVariable.
            fallback_value: Initial value for FallbackValue.
            target: Initial value for Target.
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
    def update_cloud_variable(self) -> bool | None:
        """The UpdateCloudVariable field value."""
        member = self.get_member("UpdateCloudVariable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_cloud_variable.setter
    def update_cloud_variable(self, value: bool) -> None:
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

