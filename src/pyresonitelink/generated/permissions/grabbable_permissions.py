"""Generated component: GrabbablePermissions."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabbablePermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabbablePermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabbablePermissions"

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
    def validate_type_list_mode(self) -> members.FieldEnum | None:
        """The ValidateTypeListMode member."""
        member = self.get_member("ValidateTypeListMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @validate_type_list_mode.setter
    def validate_type_list_mode(self, value: members.FieldEnum) -> None:
        """Set the ValidateTypeListMode member."""
        self.set_member("ValidateTypeListMode", value)

    @property
    def validate_types(self) -> members.SyncList | None:
        """The ValidateTypes member."""
        member = self.get_member("ValidateTypes")
        if isinstance(member, members.SyncList):
            return member
        return None

    @validate_types.setter
    def validate_types(self, value: members.SyncList) -> None:
        """Set the ValidateTypes member."""
        self.set_member("ValidateTypes", value)

