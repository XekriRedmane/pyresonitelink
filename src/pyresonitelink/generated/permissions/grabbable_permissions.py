"""Generated component: GrabbablePermissions."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.list_filter_mode import ListFilterMode
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbablePermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The GrabbablePermissions component is used to control what roles can pick up what items.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbablePermissions"

    def __init__(self, validate_type_list_mode: ListFilterMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            validate_type_list_mode: Initial value for ValidateTypeListMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if validate_type_list_mode is not None:
            self.validate_type_list_mode = validate_type_list_mode

    @property
    def tags(self) -> members.SyncObject | None:
        """A tag filter to filter what tags can or can't be grabbed by the selected roles."""
        member = self.get_member("Tags")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @tags.setter
    def tags(self, value: members.SyncObject) -> None:
        """Set Tags. A tag filter to filter what tags can or can't be grabbed by the selected roles."""
        self.set_member("Tags", value)

    @property
    def validate_type_list_mode(self) -> ListFilterMode | None:
        """how to use the ``ValidateTypes`` list for the selected roles."""
        member = self.get_member("ValidateTypeListMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ListFilterMode(member.value)
        return None

    @validate_type_list_mode.setter
    def validate_type_list_mode(self, value: ListFilterMode | str) -> None:
        """Set ValidateTypeListMode. how to use the ``ValidateTypes`` list for the selected roles."""
        member = self.get_member("ValidateTypeListMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ValidateTypeListMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def validate_types(self) -> members.SyncList | None:
        """A list of C# types that will have ``ValidateTypeListMode`` applied to them."""
        member = self.get_member("ValidateTypes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @validate_types.setter
    def validate_types(self, value: members.SyncList) -> None:
        """Set ValidateTypes. A list of C# types that will have ``ValidateTypeListMode`` applied to them."""
        self.set_member("ValidateTypes", value)

