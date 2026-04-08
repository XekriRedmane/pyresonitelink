"""Generated component: AvatarUserPositioner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserPositioner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserPositioner.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserPositioner"

    def __init__(self, position_reference: str | Slot | None = None, rotation_reference: str | Slot | None = None, preserve_up: bool | None = None, on_manual_equip_only: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_reference: Initial value for PositionReference.
            rotation_reference: Initial value for RotationReference.
            preserve_up: Initial value for PreserveUp.
            on_manual_equip_only: Initial value for OnManualEquipOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_reference is not None:
            self.position_reference = position_reference
        if rotation_reference is not None:
            self.rotation_reference = rotation_reference
        if preserve_up is not None:
            self.preserve_up = preserve_up
        if on_manual_equip_only is not None:
            self.on_manual_equip_only = on_manual_equip_only

    @property
    def position_node(self) -> members.FieldEnum | None:
        """The PositionNode member."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @position_node.setter
    def position_node(self, value: members.FieldEnum) -> None:
        """Set the PositionNode member."""
        self.set_member("PositionNode", value)

    @property
    def rotation_node(self) -> members.FieldEnum | None:
        """The RotationNode member."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rotation_node.setter
    def rotation_node(self, value: members.FieldEnum) -> None:
        """Set the RotationNode member."""
        self.set_member("RotationNode", value)

    @property
    def position_reference(self) -> str | None:
        """Target ID of the PositionReference reference (targets Slot)."""
        member = self.get_member("PositionReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_reference.setter
    def position_reference(self, target: str | Slot | None) -> None:
        """Set the PositionReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("PositionReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PositionReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def rotation_reference(self) -> str | None:
        """Target ID of the RotationReference reference (targets Slot)."""
        member = self.get_member("RotationReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_reference.setter
    def rotation_reference(self, target: str | Slot | None) -> None:
        """Set the RotationReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("RotationReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def preserve_up(self) -> bool | None:
        """The PreserveUp field value."""
        member = self.get_member("PreserveUp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_up.setter
    def preserve_up(self, value: bool) -> None:
        """Set the PreserveUp field value."""
        member = self.get_member("PreserveUp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUp", fields.FieldBool(value=value)
            )

    @property
    def on_manual_equip_only(self) -> bool | None:
        """The OnManualEquipOnly field value."""
        member = self.get_member("OnManualEquipOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @on_manual_equip_only.setter
    def on_manual_equip_only(self, value: bool) -> None:
        """Set the OnManualEquipOnly field value."""
        member = self.get_member("OnManualEquipOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OnManualEquipOnly", fields.FieldBool(value=value)
            )

