"""Generated component: AvatarUserRootOverrideAssigner."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserRootOverrideAssigner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserRootOverrideAssigner.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserRootOverrideAssigner"

    def __init__(self, override: str | Slot | None = None, equipping_slot: str | AvatarObjectSlot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            override: Initial value for Override.
            equipping_slot: Initial value for _equippingSlot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if override is not None:
            self.override = override
        if equipping_slot is not None:
            self.equipping_slot = equipping_slot

    @property
    def override(self) -> str | None:
        """Target ID of the Override reference (targets Slot)."""
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
    def equipping_slot(self) -> str | None:
        """Target ID of the _equippingSlot reference (targets AvatarObjectSlot)."""
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

