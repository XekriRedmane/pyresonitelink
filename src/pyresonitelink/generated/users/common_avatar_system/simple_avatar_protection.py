"""Generated component: SimpleAvatarProtection."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iitem_permissions import IItemPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.ipackage_import_event_receiver import IPackageImportEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimpleAvatarProtection(GeneratedComponent, IItemPermissions, ICustomInspector, IPackageImportEventReceiver, IWorldEventReceiver):
    """SimpleAvatarProtection prevents other users from wearing an avatar or saving it.

    Category: Users/Common Avatar System

    **Behavior**: When attached anywhere on an avatar, the SimpleAvatarProtection component prevents all users, other than the single user listed on the component, from saving the avatar, grabbing materials off of it, or equipping it.

The component is automatically attached to an avatar if "Protect Avatar" is checked in the Avatar Creator when creating it.

All instances of SimpleAvatarProtection on an avatar can be removed by its owner by clicking the "Remove All Instances" button. No other user can remove the component. This is useful if you are trying to clear protection from an avatar, but cannot remember where the component was; you can simply add another instance and remove them all at once.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.SimpleAvatarProtection"

    def __init__(self, reassign_user_on_package_import: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """The user who is permitted to use the avatar."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set User. The user who is permitted to use the avatar."""
        self.set_member("User", value)

    @property
    def reassign_user_on_package_import(self) -> primitives.Bool | None:
        """See ResonitePackage#Simple_Avatar_Protection_handling."""
        member = self.get_member("ReassignUserOnPackageImport")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reassign_user_on_package_import.setter
    def reassign_user_on_package_import(self, value: primitives.Bool) -> None:
        """Set the ReassignUserOnPackageImport field value."""
        member = self.get_member("ReassignUserOnPackageImport")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReassignUserOnPackageImport", fields.FieldBool(value=value)
            )

