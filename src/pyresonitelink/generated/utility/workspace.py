"""Generated component: Workspace."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.imodified_event_receiver import IModifiedEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Workspace(GeneratedComponent, ICustomInspector, IModifiedEventReceiver, IWorldEventReceiver):
    """The Workspace component allows for doing work inside of a containerized slot, where the user can add or remove items which gets saved every interval specified. These workspaces can be public or private, and work similarly in concept to Cloud Variables except greatly simplified and store an entire hierarchy instead of a single value. Workspaces have a path to them, which allow for having multiple different workspaces per user. Workspaces take up storage as a saved item would, and automatically synchronize in real time. Multiple users working on workspaces at the same time can cause issues however, since workspaces save their changes before loading from the cloud unless ``ReadOnly`` is enabled.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Workspace"

    def __init__(self, override_owner_id: primitives.String | None = None, workspace_path: primitives.String | None = None, read_only: primitives.Bool | None = None, autosave_delay: primitives.Float | None = None, suspend_updates: primitives.Bool | None = None, unsaved_changes: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """The user to manage reading and writing the contents of this workspace to the cloud for."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set User. The user to manage reading and writing the contents of this workspace to the cloud for."""
        self.set_member("User", value)

    @property
    def override_owner_id(self) -> primitives.String | None:
        """The override for the owner of this workspace to read and write the data for, which allows for reading public workspaces from others."""
        member = self.get_member("OverrideOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_owner_id.setter
    def override_owner_id(self, value: primitives.String) -> None:
        """Set the OverrideOwnerId field value."""
        member = self.get_member("OverrideOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideOwnerId", fields.FieldString(value=value)
            )

    @property
    def workspace_path(self) -> primitives.String | None:
        """The path of the workspace on the Cloud. Adding "public/" (case ignored) to the start of the path allows for public workspaces anyone can edit. Public workspaces must exist first before another user than the owner can save to them."""
        member = self.get_member("WorkspacePath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @workspace_path.setter
    def workspace_path(self, value: primitives.String) -> None:
        """Set the WorkspacePath field value."""
        member = self.get_member("WorkspacePath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WorkspacePath", fields.FieldString(value=value)
            )

    @property
    def read_only(self) -> primitives.Bool | None:
        """Whether to only read the contents of this workspace from the cloud and not save it."""
        member = self.get_member("ReadOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @read_only.setter
    def read_only(self, value: primitives.Bool) -> None:
        """Set the ReadOnly field value."""
        member = self.get_member("ReadOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReadOnly", fields.FieldBool(value=value)
            )

    @property
    def autosave_delay(self) -> primitives.Float | None:
        """How long to wait between save attempts before trying to save again. saves only happen if there have been changes."""
        member = self.get_member("AutosaveDelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @autosave_delay.setter
    def autosave_delay(self, value: primitives.Float) -> None:
        """Set the AutosaveDelay field value."""
        member = self.get_member("AutosaveDelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutosaveDelay", fields.FieldFloat(value=value)
            )

    @property
    def suspend_updates(self) -> primitives.Bool | None:
        """Whether to pause the loading and saving of this workspace to the cloud."""
        member = self.get_member("SuspendUpdates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @suspend_updates.setter
    def suspend_updates(self, value: primitives.Bool) -> None:
        """Set the SuspendUpdates field value."""
        member = self.get_member("SuspendUpdates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SuspendUpdates", fields.FieldBool(value=value)
            )

    @property
    def unsaved_changes(self) -> primitives.Bool | None:
        """Whether this workspace has changes that should be saved to the cloud upon the next save."""
        member = self.get_member("_unsavedChanges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unsaved_changes.setter
    def unsaved_changes(self, value: primitives.Bool) -> None:
        """Set the _unsavedChanges field value."""
        member = self.get_member("_unsavedChanges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_unsavedChanges", fields.FieldBool(value=value)
            )

