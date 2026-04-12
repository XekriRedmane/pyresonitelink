"""Generated component: TouchablePermissions."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchablePermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The TouchablePermissions component is used in worlds to manage what certain roles that users get assigned to can and cannot do.

    Category: Permissions

    Found in the world permissions slot. When attaching a new one for
    granular control, make sure to select the roles you want the filters to
    apply to. Then make the filters and edits you need. Don't forget to save
    the world!
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchablePermissions"

    @property
    def tags(self) -> members.SyncObject | None:
        """Slot tag object to determine the kinds of tags to filter for the selected roles."""
        member = self.get_member("Tags")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @tags.setter
    def tags(self, value: members.SyncObject) -> None:
        """Set Tags. Slot tag object to determine the kinds of tags to filter for the selected roles."""
        self.set_member("Tags", value)

    @property
    def components(self) -> members.SyncObject | None:
        """A component filter that applies to the selected roles."""
        member = self.get_member("Components")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @components.setter
    def components(self, value: members.SyncObject) -> None:
        """Set Components. A component filter that applies to the selected roles."""
        self.set_member("Components", value)

