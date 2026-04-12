"""Generated component: AvatarUserRootOverrideAssigner."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.override_node import OverrideNode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserRootOverrideAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Avatar User Root Override Assigner is a component that allows for changing the user's viewpoint, the user's first person standing location, or the user's ears location. This component works if parented under a user, for that user.

    Category: Users/Common Avatar System

    **Behavior**: Needs to be parented under a user to work, and applies to the parent user. The component requires a slot, and an AvatarObjectSlot. The Avatar Object slot does not need an existing one, so best practice is to add a new Avatar Object Slot to the same Slot as this component, then put it into the ``_equippingSlot`` field. Also, adding the slot this component is on to ``Override`` allows for a self contained settup in one slot that fully works when parented to a user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserRootOverrideAssigner"

    def __init__(self, override: str | Slot | None = None, node: OverrideNode | str | None = None, equipping_slot: str | AvatarObjectSlot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            override: Initial value for Override.
            node: Initial value for Node.
            equipping_slot: Initial value for _equippingSlot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if override is not None:
            self.override = override
        if node is not None:
            self.node = node
        if equipping_slot is not None:
            self.equipping_slot = equipping_slot

    @property
    def override(self) -> str | None:
        """The slot to relocate the user's eyes or ears to."""
        member = self.get_member("Override")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override.setter
    def override(self, target: str | Slot | None) -> None:
        """Set the Override reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Override")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Override",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def node(self) -> OverrideNode | None:
        """Whether to make the user's eyes, Standing position, or ears located at ``Slot`` without changing any slot transforms."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OverrideNode(member.value)
        return None

    @node.setter
    def node(self, value: OverrideNode | str) -> None:
        """Set Node. Whether to make the user's eyes, Standing position, or ears located at ``Slot`` without changing any slot transforms."""
        member = self.get_member("Node")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Node",
                members.FieldEnum(value=str(value)),
            )

    @property
    def equipping_slot(self) -> str | None:
        """an Avatar Object Slot to use for handling this node."""
        member = self.get_member("_equippingSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipping_slot.setter
    def equipping_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the _equippingSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("_equippingSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_equippingSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

