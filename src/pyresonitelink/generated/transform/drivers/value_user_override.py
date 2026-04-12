"""Generated component: ValueUserOverride."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueUserOverride(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ValueUserOverride Component allows storing "override" values for each user listed under ``_overrides`` and driving the ``Target`` field with them.
}}

    Category: Transform/Drivers

    **Behavior**: The ``_overrides`` bag contains a list of users and their associated values - whenever the local user matches a user entry in the bag, the associated value is driven to ``Target``. Otherwise, ``Target`` is driven to the value in ``Default``.

``CreateOverrideOnWrite`` allows for new users and values to be added to the bag when the driven value in ``Target`` is directly or indirectly changed by that user. If it is not enabled, the value in ``Target`` is not changeable unless the override is added or changed manually from the inspector panel.

Attempting to write to or otherwise cause a discrete entry to a driven field is known as Hooking it. Any Hook to the ``Target`` value is intercepted by the ValueUserOverride Component and will change the modifying user's entry in the ``_overrides`` bag. If there is no entry for the user and if ``CreateOverrideOnWrite`` is enabled, it will create an entry using the set value.

    **Related Components**: * BooleanUserOverrideGather
* NumericUserOverrideGather

    Parameterize with a value type::

        ValueUserOverride[primitives.Float]
        ValueUserOverride[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueUserOverride<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ValueUserOverride<>"

    def __init__(self, default: T | None = None, create_override_on_write: primitives.Bool | None = None, persistent_overrides: primitives.Bool | None = None, clear_on_user_leave: primitives.Bool | None = None, target: str | IField[T] | None = None, *, component: workers.Component | None = None) -> None:
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
    def create_override_on_write(self) -> primitives.Bool | None:
        """Creates an entry in ``_overrides`` when ``Target`` is written back."""
        member = self.get_member("CreateOverrideOnWrite")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @create_override_on_write.setter
    def create_override_on_write(self, value: primitives.Bool) -> None:
        """Set the CreateOverrideOnWrite field value."""
        member = self.get_member("CreateOverrideOnWrite")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreateOverrideOnWrite", fields.FieldBool(value=value)
            )

    @property
    def persistent_overrides(self) -> primitives.Bool | None:
        """Values in ``_overrides`` are stored with the object when it is saved."""
        member = self.get_member("PersistentOverrides")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @persistent_overrides.setter
    def persistent_overrides(self, value: primitives.Bool) -> None:
        """Set the PersistentOverrides field value."""
        member = self.get_member("PersistentOverrides")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PersistentOverrides", fields.FieldBool(value=value)
            )

    @property
    def clear_on_user_leave(self) -> primitives.Bool | None:
        """The ClearOnUserLeave field value."""
        member = self.get_member("ClearOnUserLeave")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clear_on_user_leave.setter
    def clear_on_user_leave(self, value: primitives.Bool) -> None:
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
        """Target field of the specified type, that gets driven to the override value."""
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

