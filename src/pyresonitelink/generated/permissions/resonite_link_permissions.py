"""Generated component: ResoniteLinkPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ResoniteLinkPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ResoniteLinkPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ResoniteLinkPermissions"

    def __init__(self, allow_read_access: bool | None = None, allow_write_access: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_read_access: Initial value for AllowReadAccess.
            allow_write_access: Initial value for AllowWriteAccess.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_read_access is not None:
            self.allow_read_access = allow_read_access
        if allow_write_access is not None:
            self.allow_write_access = allow_write_access

    @property
    def allow_read_access(self) -> bool | None:
        """The AllowReadAccess field value."""
        member = self.get_member("AllowReadAccess")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_read_access.setter
    def allow_read_access(self, value: bool) -> None:
        """Set the AllowReadAccess field value."""
        member = self.get_member("AllowReadAccess")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowReadAccess", fields.FieldBool(value=value)
            )

    @property
    def allow_write_access(self) -> bool | None:
        """The AllowWriteAccess field value."""
        member = self.get_member("AllowWriteAccess")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_write_access.setter
    def allow_write_access(self, value: bool) -> None:
        """Set the AllowWriteAccess field value."""
        member = self.get_member("AllowWriteAccess")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowWriteAccess", fields.FieldBool(value=value)
            )

