"""Generated component: ScreenViewPermissions."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.list_filter_mode import ListFilterMode
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScreenViewPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The ScreenViewPermissions component is a Permissions type component that can apply rules for what certain roles in a session can do with views like third person, free cam, or UI targetting.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScreenViewPermissions"

    def __init__(self, list_mode: ListFilterMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            list_mode: Initial value for ListMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if list_mode is not None:
            self.list_mode = list_mode

    @property
    def list_mode(self) -> ListFilterMode | None:
        """How to filter and handle the list of ``ViewFilters`` for the selected roles."""
        member = self.get_member("ListMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ListFilterMode(member.value)
        return None

    @list_mode.setter
    def list_mode(self, value: ListFilterMode | str) -> None:
        """Set ListMode. How to filter and handle the list of ``ViewFilters`` for the selected roles."""
        member = self.get_member("ListMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ListMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def view_filters(self) -> members.SyncList | None:
        """A list of targetting views to check a user with the selected role(s) with and act accordingly on if they are using one in the list."""
        member = self.get_member("ViewFilters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @view_filters.setter
    def view_filters(self, value: members.SyncList) -> None:
        """Set ViewFilters. A list of targetting views to check a user with the selected role(s) with and act accordingly on if they are using one in the list."""
        self.set_member("ViewFilters", value)

