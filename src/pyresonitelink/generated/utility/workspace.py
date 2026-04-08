"""Generated component: Workspace."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.imodified_event_receiver import IModifiedEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Workspace(GeneratedComponent, ICustomInspector, IModifiedEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Workspace.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Workspace"

    def __init__(self, override_owner_id: str | None = None, workspace_path: str | None = None, read_only: bool | None = None, autosave_delay: np.float32 | None = None, suspend_updates: bool | None = None, unsaved_changes: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            override_owner_id: Initial value for OverrideOwnerId.
            workspace_path: Initial value for WorkspacePath.
            read_only: Initial value for ReadOnly.
            autosave_delay: Initial value for AutosaveDelay.
            suspend_updates: Initial value for SuspendUpdates.
            unsaved_changes: Initial value for _unsavedChanges.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if override_owner_id is not None:
            self.override_owner_id = override_owner_id
        if workspace_path is not None:
            self.workspace_path = workspace_path
        if read_only is not None:
            self.read_only = read_only
        if autosave_delay is not None:
            self.autosave_delay = autosave_delay
        if suspend_updates is not None:
            self.suspend_updates = suspend_updates
        if unsaved_changes is not None:
            self.unsaved_changes = unsaved_changes

    @property
    def user(self) -> members.SyncObject | None:
        """The User member."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set the User member."""
        self.set_member("User", value)

    @property
    def override_owner_id(self) -> str | None:
        """The OverrideOwnerId field value."""
        member = self.get_member("OverrideOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_owner_id.setter
    def override_owner_id(self, value: str) -> None:
        """Set the OverrideOwnerId field value."""
        member = self.get_member("OverrideOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideOwnerId", fields.FieldString(value=value)
            )

    @property
    def workspace_path(self) -> str | None:
        """The WorkspacePath field value."""
        member = self.get_member("WorkspacePath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @workspace_path.setter
    def workspace_path(self, value: str) -> None:
        """Set the WorkspacePath field value."""
        member = self.get_member("WorkspacePath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorkspacePath", fields.FieldString(value=value)
            )

    @property
    def read_only(self) -> bool | None:
        """The ReadOnly field value."""
        member = self.get_member("ReadOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @read_only.setter
    def read_only(self, value: bool) -> None:
        """Set the ReadOnly field value."""
        member = self.get_member("ReadOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReadOnly", fields.FieldBool(value=value)
            )

    @property
    def autosave_delay(self) -> np.float32 | None:
        """The AutosaveDelay field value."""
        member = self.get_member("AutosaveDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @autosave_delay.setter
    def autosave_delay(self, value: np.float32) -> None:
        """Set the AutosaveDelay field value."""
        member = self.get_member("AutosaveDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutosaveDelay", fields.FieldFloat(value=value)
            )

    @property
    def suspend_updates(self) -> bool | None:
        """The SuspendUpdates field value."""
        member = self.get_member("SuspendUpdates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @suspend_updates.setter
    def suspend_updates(self, value: bool) -> None:
        """Set the SuspendUpdates field value."""
        member = self.get_member("SuspendUpdates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SuspendUpdates", fields.FieldBool(value=value)
            )

    @property
    def unsaved_changes(self) -> bool | None:
        """The _unsavedChanges field value."""
        member = self.get_member("_unsavedChanges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unsaved_changes.setter
    def unsaved_changes(self, value: bool) -> None:
        """Set the _unsavedChanges field value."""
        member = self.get_member("_unsavedChanges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_unsavedChanges", fields.FieldBool(value=value)
            )

