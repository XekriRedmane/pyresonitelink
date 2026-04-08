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
    """Wrapper for [FrooxEngine]FrooxEngine.BooleanUserOverrideGather.

    Category: Transform/Drivers
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
        """The Default field value."""
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
        """The CreateOverrideOnWrite field value."""
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
        """The PersistentOverrides field value."""
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
        """Target ID of the Target reference (targets IField[primitives.Bool])."""
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
        """The Any field value."""
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
        """The All field value."""
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
        """The None field value."""
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
        """The TrueCount field value."""
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
        """The FalseCount field value."""
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
        """The ExcludeHeadless field value."""
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

