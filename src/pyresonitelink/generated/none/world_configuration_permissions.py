"""Generated component: WorldConfigurationPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldConfigurationPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldConfigurationPermissions.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldConfigurationPermissions"

    def __init__(self, allow_changes: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_changes: Initial value for AllowChanges.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_changes is not None:
            self.allow_changes = allow_changes

    @property
    def allow_changes(self) -> bool | None:
        """The AllowChanges field value."""
        member = self.get_member("AllowChanges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_changes.setter
    def allow_changes(self, value: bool) -> None:
        """Set the AllowChanges field value."""
        member = self.get_member("AllowChanges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowChanges", fields.FieldBool(value=value)
            )

