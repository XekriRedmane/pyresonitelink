"""Generated component: AvatarObjectPermissions."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarObjectPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The AvatarObjectPermission component is a Permissions component which determines which avatars users are allowed to equip if the avatar is tagged properly.

    Category: Permissions

    This permission allows or disallows specific avatars to be used. Tags
    are used to determine to in-/equipability of such tagged avatars.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectPermissions"

    @property
    def tags(self) -> members.SyncObject | None:
        """The list of tags and whether they are white listed or black listed"""
        member = self.get_member("Tags")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @tags.setter
    def tags(self, value: members.SyncObject) -> None:
        """Set Tags. The list of tags and whether they are white listed or black listed"""
        self.set_member("Tags", value)

