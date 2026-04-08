"""Generated component: AvatarUserReferenceAssigner."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserReferenceAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserReferenceAssigner.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserReferenceAssigner"

    @property
    def assign_mode(self) -> members.FieldEnum | None:
        """The AssignMode member."""
        member = self.get_member("AssignMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @assign_mode.setter
    def assign_mode(self, value: members.FieldEnum) -> None:
        """Set the AssignMode member."""
        self.set_member("AssignMode", value)

    @property
    def references(self) -> members.SyncList | None:
        """The References member."""
        member = self.get_member("References")
        if isinstance(member, members.SyncList):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncList) -> None:
        """Set the References member."""
        self.set_member("References", value)

