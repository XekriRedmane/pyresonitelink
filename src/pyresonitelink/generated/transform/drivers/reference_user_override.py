"""Generated component: ReferenceUserOverride."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceUserOverride(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReferenceUserOverride<>.

    Category: Transform/Drivers

    Parameterize with a value type::

        ReferenceUserOverride[primitives.Float]
        ReferenceUserOverride[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceUserOverride<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceUserOverride<>"

    def __init__(self, target: str | SyncRef[T] | None = None, default: str | T | None = None, create_override_on_write: primitives.Bool | None = None, persistent_overrides: primitives.Bool | None = None, clear_on_user_leave: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            default: Initial value for Default.
            create_override_on_write: Initial value for CreateOverrideOnWrite.
            persistent_overrides: Initial value for PersistentOverrides.
            clear_on_user_leave: Initial value for ClearOnUserLeave.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if default is not None:
            self.default = default
        if create_override_on_write is not None:
            self.create_override_on_write = create_override_on_write
        if persistent_overrides is not None:
            self.persistent_overrides = persistent_overrides
        if clear_on_user_leave is not None:
            self.clear_on_user_leave = clear_on_user_leave

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncRef[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncRef[T] | None) -> None:
        """Set the Target reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def default(self) -> str | None:
        """Target ID of the Default reference (targets T)."""
        member = self.get_member("Default")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default.setter
    def default(self, target: str | T | None) -> None:
        """Set the Default reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("Default")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Default",
                members.Reference(targetId=target_id, targetType='T'),
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

