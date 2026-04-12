"""Generated component: UndoManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UndoManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The UndoManager component keeps track of all user's actions in the world, allowing users to Undo or revert back to a previous step or action. Undoing can be controlled in ProtoFlux within the Undo Category, where users create undo batches and steps that this component can utilize. Undoing can be disabled by setting max steps to ``0``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.UndoManager"

    def __init__(self, max_undo_steps: primitives.Int | None = None, unsaved_changes: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_undo_steps: Initial value for MaxUndoSteps.
            unsaved_changes: Initial value for UnsavedChanges.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_undo_steps is not None:
            self.max_undo_steps = max_undo_steps
        if unsaved_changes is not None:
            self.unsaved_changes = unsaved_changes

    @property
    def max_undo_steps(self) -> primitives.Int | None:
        """The maximum memory for Undoable actions per user for the current world."""
        member = self.get_member("MaxUndoSteps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_undo_steps.setter
    def max_undo_steps(self, value: primitives.Int) -> None:
        """Set the MaxUndoSteps field value."""
        member = self.get_member("MaxUndoSteps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxUndoSteps", fields.FieldInt(value=value)
            )

    @property
    def unsaved_changes(self) -> primitives.Bool | None:
        """Whether the user has done anything that makes an undo step, which tells the world it has unsaved changes."""
        member = self.get_member("UnsavedChanges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unsaved_changes.setter
    def unsaved_changes(self, value: primitives.Bool) -> None:
        """Set the UnsavedChanges field value."""
        member = self.get_member("UnsavedChanges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnsavedChanges", fields.FieldBool(value=value)
            )

