"""Generated component: AvatarNodeAssigner."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.body_node import BodyNode
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarNodeAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarNodeAssigner component only functions on an avatar being equipped or de-equipped by a user. When equipped, the component finds the first AvatarObjectSlot with a body node value that equals ``Node``. if found, it assigns all slot storage fields in ``Targets`` to the slot the AvatarObjectSlot is on. When de-equipped, all slot storage fields in ``Targets`` have their stored slot cleared.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarNodeAssigner"

    def __init__(self, node: BodyNode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node

    @property
    def node(self) -> BodyNode | None:
        """The body node to search for when the avatar this is on is equipped."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BodyNode(member.value)
        return None

    @node.setter
    def node(self, value: BodyNode | str) -> None:
        """Set Node. The body node to search for when the avatar this is on is equipped."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Node",
                members.FieldEnum(value=str(value)),
            )

    @property
    def targets(self) -> members.SyncList | None:
        """The slot storage fields to fill when an Component:AvatarObjectSlot of node type ``Node`` is found."""
        member = self.get_member("Targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set Targets. The slot storage fields to fill when an Component:AvatarObjectSlot of node type ``Node`` is found."""
        self.set_member("Targets", value)

