"""Generated component: NumericUserOverrideGather."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NumericUserOverrideGather(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The NumericOverrideGather component acts the same as a ValueUserOverride`1 with the key difference being it can get the average, minimum, maximum, and sum of all the values users picked that are still in the session.

    Category: Transform/Drivers

    Can be used to check if all users are using the same setting (like
    saying they're ready for a game round to start) or check the average of
    what people say the number of jellybeans in a jar is (so that someone
    can guess the average and get the closest to the answer)

    Parameterize with a value type::

        NumericUserOverrideGather[primitives.Float]
        NumericUserOverrideGather[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NumericUserOverrideGather<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.NumericUserOverrideGather<>"

    def __init__(self, default: T | None = None, create_override_on_write: primitives.Bool | None = None, persistent_overrides: primitives.Bool | None = None, clear_on_user_leave: primitives.Bool | None = None, target: str | IField[T] | None = None, min: T | None = None, max: T | None = None, sum: T | None = None, average: T | None = None, exclude_headless: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default: Initial value for Default.
            create_override_on_write: Initial value for CreateOverrideOnWrite.
            persistent_overrides: Initial value for PersistentOverrides.
            clear_on_user_leave: Initial value for ClearOnUserLeave.
            target: Initial value for Target.
            min: Initial value for Min.
            max: Initial value for Max.
            sum: Initial value for Sum.
            average: Initial value for Average.
            exclude_headless: Initial value for ExcludeHeadless.
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
        if min is not None:
            self.min = min
        if max is not None:
            self.max = max
        if sum is not None:
            self.sum = sum
        if average is not None:
            self.average = average
        if exclude_headless is not None:
            self.exclude_headless = exclude_headless

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
        """Whether changes to ``Target`` creates a new override or updates the overrides value for that user."""
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
        """Whether the ``_overrides`` list contents are saved when this component is saved."""
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
        """The field to drive with different values for each user's local machine using the ``_overrides`` list."""
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
    def min(self) -> T | None:
        """The Min field value (type depends on type parameter)."""
        member = self.get_member("Min")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min.setter
    def min(self, value: T) -> None:
        """Set the Min field value."""
        member = self.get_member("Min")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Min", self._type_info.field_class(value=value)
            )

    @property
    def max(self) -> T | None:
        """The Max field value (type depends on type parameter)."""
        member = self.get_member("Max")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max.setter
    def max(self, value: T) -> None:
        """Set the Max field value."""
        member = self.get_member("Max")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Max", self._type_info.field_class(value=value)
            )

    @property
    def sum(self) -> T | None:
        """The Sum field value (type depends on type parameter)."""
        member = self.get_member("Sum")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sum.setter
    def sum(self, value: T) -> None:
        """Set the Sum field value."""
        member = self.get_member("Sum")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Sum", self._type_info.field_class(value=value)
            )

    @property
    def average(self) -> T | None:
        """The Average field value (type depends on type parameter)."""
        member = self.get_member("Average")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average.setter
    def average(self, value: T) -> None:
        """Set the Average field value."""
        member = self.get_member("Average")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None and self._type_info.field_class is not None:
            self.set_member(
                "Average", self._type_info.field_class(value=value)
            )

    @property
    def exclude_headless(self) -> primitives.Bool | None:
        """Whether headless client values should be excluded from calculations."""
        member = self.get_member("ExcludeHeadless")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_headless.setter
    def exclude_headless(self, value: primitives.Bool) -> None:
        """Set the ExcludeHeadless field value."""
        member = self.get_member("ExcludeHeadless")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeHeadless", fields.FieldBool(value=value)
            )

