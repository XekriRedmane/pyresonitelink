"""Generated component: AvatarNodeAssigner."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarNodeAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarNodeAssigner.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarNodeAssigner"

    @property
    def node(self) -> members.FieldEnum | None:
        """The Node member."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @node.setter
    def node(self, value: members.FieldEnum) -> None:
        """Set the Node member."""
        self.set_member("Node", value)

    @property
    def targets(self) -> members.SyncList | None:
        """The Targets member."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the Targets member."""
        self.set_member("Targets", value)

