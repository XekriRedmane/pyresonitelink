"""Generated component: BatchAction."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BatchAction(GeneratedComponent, IUndoable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.BatchAction.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.BatchAction"

    def __init__(self, description: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if description is not None:
            self.description = description

    @property
    def description(self) -> str | None:
        """The _description field value."""
        member = self.get_member("_description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: str) -> None:
        """Set the _description field value."""
        member = self.get_member("_description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_description", fields.FieldString(value=value)
            )

