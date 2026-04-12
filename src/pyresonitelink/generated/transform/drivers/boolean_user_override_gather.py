"""Generated component: BooleanUserOverrideGather."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanUserOverrideGather(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The BooleanUserOverrideGather Component allows storing Boolean "override" values for each user listed under ``_overrides`` and driving the ``Target`` field. The behavior is similar to ValueUserOverride&lt;Bool&gt;, except this component also reports aggregate information about the overrides.

}}

    Category: Transform/Drivers

    Note that the reporting fields (Any, All, None, TrueCount and
    FalseCount) count only the values for users in the sessions (including
    away users and headless servers), but not all the values in the
    ``_overrides`` list.

    **Behavior**: The ``_overrides`` bag contains a list of users and their associated Boolean values - whenever the local user matches a user entry in the bag, the associated value is driven to ``Target``. Otherwise, ``Target`` is driven to the value in ``Default``.

``CreateOverrideOnWrite`` allows for new users and values to be added to the bag when the driven value in ``Target`` is directly or indirectly changed by that user. If it is not enabled, the value in ``Target`` is not changeable unless the override is added or changed manually from the inspector panel.

Attempting to write to or otherwise cause a discrete entry to a driven field is known as Hooking it. Any Hook to the ``Target`` value is intercepted by the BooleanUserOverrideGather Component and will change the modifying user's entry in the ``_overrides`` bag. If there is no entry for the user and if ``CreateOverrideOnWrite`` is enabled, it will create an entry using the set value.

    **Related Components**: * ValueUserOverride
* NumericUserOverrideGather
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanUserOverrideGather"

    def __init__(self, default: primitives.Bool | None = None, create_override_on_write: primitives.Bool | None = None, persistent_overrides: primitives.Bool | None = None, clear_on_user_leave: primitives.Bool | None = None, target: str | IField[primitives.Bool] | None = None, any: primitives.Bool | None = None, all: primitives.Bool | None = None, none: primitives.Bool | None = None, true_count: primitives.Int | None = None, false_count: primitives.Int | None = None, exclude_headless: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default: Initial value for Default.
            create_override_on_write: Initial value for CreateOverrideOnWrite.
            persistent_overrides: Initial value for PersistentOverrides.
            clear_on_user_leave: Initial value for ClearOnUserLeave.
            target: Initial value for Target.
            any: Initial value for Any.
            all: Initial value for All.
            none: Initial value for None.
            true_count: Initial value for TrueCount.
            false_count: Initial value for FalseCount.
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
        if any is not None:
            self.any = any
        if all is not None:
            self.all = all
        if none is not None:
            self.none = none
        if true_count is not None:
            self.true_count = true_count
        if false_count is not None:
            self.false_count = false_count
        if exclude_headless is not None:
            self.exclude_headless = exclude_headless

    @property
    def default(self) -> primitives.Bool | None:
        """The default value given to ``Target`` if no suitable override exists in ``_overrides``."""
        member = self.get_member("Default")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default.setter
    def default(self, value: primitives.Bool) -> None:
        """Set the Default field value."""
        member = self.get_member("Default")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Default", fields.FieldBool(value=value)
            )

    @property
    def create_override_on_write(self) -> primitives.Bool | None:
        """Whether an entry in ``_overrides`` should be created when ``Target`` is written back."""
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
        """Whether values in ``_overrides`` should persist when the component is saved."""
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
        """Reference to the field that gets driven to the override value."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def any(self) -> primitives.Bool | None:
        """Reports ``true`` when any user in the session would have their override be ``true`` (either from the default value or an override)."""
        member = self.get_member("Any")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @any.setter
    def any(self, value: primitives.Bool) -> None:
        """Set the Any field value."""
        member = self.get_member("Any")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Any", fields.FieldBool(value=value)
            )

    @property
    def all(self) -> primitives.Bool | None:
        """Reports ``true`` when all users in the session would have their override be ``true`` (either from the default value or an override)."""
        member = self.get_member("All")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @all.setter
    def all(self, value: primitives.Bool) -> None:
        """Set the All field value."""
        member = self.get_member("All")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "All", fields.FieldBool(value=value)
            )

    @property
    def none(self) -> primitives.Bool | None:
        """Reports ``true`` when none of the users in the session would have their override be ``true`` (either from the default value or an override)."""
        member = self.get_member("None")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @none.setter
    def none(self, value: primitives.Bool) -> None:
        """Set the None field value."""
        member = self.get_member("None")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "None", fields.FieldBool(value=value)
            )

    @property
    def true_count(self) -> primitives.Int | None:
        """Reports the total count of ``true`` values for all users in the session."""
        member = self.get_member("TrueCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @true_count.setter
    def true_count(self, value: primitives.Int) -> None:
        """Set the TrueCount field value."""
        member = self.get_member("TrueCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TrueCount", fields.FieldInt(value=value)
            )

    @property
    def false_count(self) -> primitives.Int | None:
        """Reports the total count of ``false`` values for all users in the session."""
        member = self.get_member("FalseCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @false_count.setter
    def false_count(self, value: primitives.Int) -> None:
        """Set the FalseCount field value."""
        member = self.get_member("FalseCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FalseCount", fields.FieldInt(value=value)
            )

    @property
    def exclude_headless(self) -> primitives.Bool | None:
        """Whether to exclude a headless user when doing aggregates and overrides."""
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

