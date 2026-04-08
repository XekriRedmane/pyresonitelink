"""Generated component: ValueUserOverride."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueUserOverride(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueUserOverride<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        ValueUserOverride[np.float32]
        ValueUserOverride[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueUserOverride<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueUserOverride<>"

    def __init__(self, default: T | None = None, create_override_on_write: bool | None = None, persistent_overrides: bool | None = None, clear_on_user_leave: bool | None = None, target: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default: Initial value for Default.
            create_override_on_write: Initial value for CreateOverrideOnWrite.
            persistent_overrides: Initial value for PersistentOverrides.
            clear_on_user_leave: Initial value for ClearOnUserLeave.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default is not None:
            self.default = default
        if create_override_on_write is not None:
            self.create_override_on_write = create_override_on_write
        if persistent_overrides is not None:
            self.persistent_overrides = persistent_overrides
        if clear_on_user_leave is not None:
            self.clear_on_user_leave = clear_on_user_leave
        if target is not None:
            self.target = target

    @property
    def default(self) -> T | None:
        """The Default field value (type depends on type parameter)."""
        member = self.get_member("Default")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default.setter
    def default(self, value: T) -> None:
        """Set the Default field value."""
        member = self.get_member("Default")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Default", self._type_info.field_class(value=value)
            )

    @property
    def create_override_on_write(self) -> bool | None:
        """The CreateOverrideOnWrite field value."""
        member = self.get_member("CreateOverrideOnWrite")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @create_override_on_write.setter
    def create_override_on_write(self, value: bool) -> None:
        """Set the CreateOverrideOnWrite field value."""
        member = self.get_member("CreateOverrideOnWrite")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreateOverrideOnWrite", fields.FieldBool(value=value)
            )

    @property
    def persistent_overrides(self) -> bool | None:
        """The PersistentOverrides field value."""
        member = self.get_member("PersistentOverrides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @persistent_overrides.setter
    def persistent_overrides(self, value: bool) -> None:
        """Set the PersistentOverrides field value."""
        member = self.get_member("PersistentOverrides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PersistentOverrides", fields.FieldBool(value=value)
            )

    @property
    def clear_on_user_leave(self) -> bool | None:
        """The ClearOnUserLeave field value."""
        member = self.get_member("ClearOnUserLeave")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clear_on_user_leave.setter
    def clear_on_user_leave(self, value: bool) -> None:
        """Set the ClearOnUserLeave field value."""
        member = self.get_member("ClearOnUserLeave")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClearOnUserLeave", fields.FieldBool(value=value)
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

