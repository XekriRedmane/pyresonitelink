"""Generated component: SimpleAvatarProtection."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iitem_permissions import IItemPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.ipackage_import_event_receiver import IPackageImportEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimpleAvatarProtection(GeneratedComponent, IItemPermissions, ICustomInspector, IPackageImportEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.SimpleAvatarProtection.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.SimpleAvatarProtection"

    def __init__(self, reassign_user_on_package_import: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reassign_user_on_package_import: Initial value for ReassignUserOnPackageImport.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reassign_user_on_package_import is not None:
            self.reassign_user_on_package_import = reassign_user_on_package_import

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
    def reassign_user_on_package_import(self) -> bool | None:
        """The ReassignUserOnPackageImport field value."""
        member = self.get_member("ReassignUserOnPackageImport")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reassign_user_on_package_import.setter
    def reassign_user_on_package_import(self, value: bool) -> None:
        """Set the ReassignUserOnPackageImport field value."""
        member = self.get_member("ReassignUserOnPackageImport")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReassignUserOnPackageImport", fields.FieldBool(value=value)
            )

