"""Generated component: TouchablePermissions."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchablePermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TouchablePermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TouchablePermissions"

    @property
    def tags(self) -> members.SyncObject | None:
        """The Tags member."""
        member = self.get_member("Tags")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @tags.setter
    def tags(self, value: members.SyncObject) -> None:
        """Set the Tags member."""
        self.set_member("Tags", value)

    @property
    def components(self) -> members.SyncObject | None:
        """The Components member."""
        member = self.get_member("Components")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @components.setter
    def components(self, value: members.SyncObject) -> None:
        """Set the Components member."""
        self.set_member("Components", value)

