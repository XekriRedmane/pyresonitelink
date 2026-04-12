"""Generated component: MigrationListUI."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MigrationListUI(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The MigrationListUI component is used to list previous and current migration tasks.

    Used internally in the migration screen.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MigrationListUI"

    def __init__(self, selected_task_id: primitives.String | None = None, list_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selected_task_id: Initial value for SelectedTaskId.
            list_root: Initial value for _listRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selected_task_id is not None:
            self.selected_task_id = selected_task_id
        if list_root is not None:
            self.list_root = list_root

    @property
    def selected_task_id(self) -> primitives.String | None:
        """The task that the user has selected."""
        member = self.get_member("SelectedTaskId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_task_id.setter
    def selected_task_id(self, value: primitives.String) -> None:
        """Set the SelectedTaskId field value."""
        member = self.get_member("SelectedTaskId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedTaskId", fields.FieldString(value=value)
            )

    @property
    def list_root(self) -> str | None:
        """The place to list migrations."""
        member = self.get_member("_listRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @list_root.setter
    def list_root(self, target: str | Slot | None) -> None:
        """Set the _listRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_listRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_listRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

