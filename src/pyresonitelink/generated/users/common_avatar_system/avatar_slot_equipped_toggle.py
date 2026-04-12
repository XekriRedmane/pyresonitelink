"""Generated component: AvatarSlotEquippedToggle."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.avatar_object_slot import AvatarObjectSlot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarSlotEquippedToggle(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AvatarSlotEquippedToggle component drives one or two booleans to a state depending on if an AvatarObjectSlot is equipped or not.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarSlotEquippedToggle"

    def __init__(self, object_slot: str | AvatarObjectSlot | None = None, equipped_drive: str | IField[primitives.Bool] | None = None, dequipped_drive: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            object_slot: Initial value for ObjectSlot.
            equipped_drive: Initial value for EquippedDrive.
            dequipped_drive: Initial value for DequippedDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if object_slot is not None:
            self.object_slot = object_slot
        if equipped_drive is not None:
            self.equipped_drive = equipped_drive
        if dequipped_drive is not None:
            self.dequipped_drive = dequipped_drive

    @property
    def object_slot(self) -> str | None:
        """The Avatar Object Slot to monitor for equipping status."""
        member = self.get_member("ObjectSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_slot.setter
    def object_slot(self, target: str | AvatarObjectSlot | None) -> None:
        """Set the ObjectSlot reference by target ID or AvatarObjectSlot instance."""
        target_id: str | None = target.id if isinstance(target, AvatarObjectSlot) else target  # type: ignore[assignment]
        member = self.get_member("ObjectSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ObjectSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarObjectSlot'),
            )

    @property
    def equipped_drive(self) -> str | None:
        """Drives the target bool to true when ``ObjectSlot`` is equipped. Otherwise false."""
        member = self.get_member("EquippedDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @equipped_drive.setter
    def equipped_drive(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the EquippedDrive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("EquippedDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EquippedDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def dequipped_drive(self) -> str | None:
        """Drives the target bool to false when ``ObjectSlot`` is equipped. Otherwise true."""
        member = self.get_member("DequippedDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dequipped_drive.setter
    def dequipped_drive(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the DequippedDrive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DequippedDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DequippedDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

