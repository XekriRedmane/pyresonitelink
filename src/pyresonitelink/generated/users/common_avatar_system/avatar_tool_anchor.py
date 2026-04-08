"""Generated component: AvatarToolAnchor."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarToolAnchor(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarToolAnchor.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarToolAnchor"

    @property
    def anchor_point(self) -> members.FieldEnum | None:
        """The AnchorPoint member."""
        member = self.get_member("AnchorPoint")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @anchor_point.setter
    def anchor_point(self, value: members.FieldEnum) -> None:
        """Set the AnchorPoint member."""
        self.set_member("AnchorPoint", value)

