"""Generated component: AvatarUserMeshHider."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserMeshHider(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserMeshHider.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserMeshHider"

    @property
    def method(self) -> members.FieldEnum | None:
        """The Method member."""
        member = self.get_member("Method")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @method.setter
    def method(self, value: members.FieldEnum) -> None:
        """Set the Method member."""
        self.set_member("Method", value)

    @property
    def exclude(self) -> members.SyncList | None:
        """The Exclude member."""
        member = self.get_member("Exclude")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclude.setter
    def exclude(self, value: members.SyncList) -> None:
        """Set the Exclude member."""
        self.set_member("Exclude", value)

