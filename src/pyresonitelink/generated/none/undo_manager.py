"""Generated component: UndoManager."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UndoManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Undo.UndoManager.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.UndoManager"

    def __init__(self, max_undo_steps: np.int32 | None = None, unsaved_changes: bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def max_undo_steps(self) -> np.int32 | None:
        """The MaxUndoSteps field value."""
        member = self.get_member("MaxUndoSteps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_undo_steps.setter
    def max_undo_steps(self, value: np.int32) -> None:
        """Set the MaxUndoSteps field value."""
        member = self.get_member("MaxUndoSteps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxUndoSteps", fields.FieldInt(value=value)
            )

    @property
    def unsaved_changes(self) -> bool | None:
        """The UnsavedChanges field value."""
        member = self.get_member("UnsavedChanges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unsaved_changes.setter
    def unsaved_changes(self, value: bool) -> None:
        """Set the UnsavedChanges field value."""
        member = self.get_member("UnsavedChanges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnsavedChanges", fields.FieldBool(value=value)
            )

