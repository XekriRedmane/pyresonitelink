"""Generated component: ScreenViewPermissions."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScreenViewPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScreenViewPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScreenViewPermissions"

    @property
    def list_mode(self) -> members.FieldEnum | None:
        """The ListMode member."""
        member = self.get_member("ListMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @list_mode.setter
    def list_mode(self, value: members.FieldEnum) -> None:
        """Set the ListMode member."""
        self.set_member("ListMode", value)

    @property
    def view_filters(self) -> members.SyncList | None:
        """The ViewFilters member."""
        member = self.get_member("ViewFilters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @view_filters.setter
    def view_filters(self, value: members.SyncList) -> None:
        """Set the ViewFilters member."""
        self.set_member("ViewFilters", value)

