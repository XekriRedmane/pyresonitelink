"""Generated component: AvatarUserPositioner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.user_node import UserNode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserPositioner(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarUserPositioner component is used to position a user to the avatar upon equipping the avatar.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserPositioner"

    def __init__(self, position_node: UserNode | str | None = None, rotation_node: UserNode | str | None = None, position_reference: str | Slot | None = None, rotation_reference: str | Slot | None = None, preserve_up: primitives.Bool | None = None, on_manual_equip_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_node: Initial value for PositionNode.
            rotation_node: Initial value for RotationNode.
            position_reference: Initial value for PositionReference.
            rotation_reference: Initial value for RotationReference.
            preserve_up: Initial value for PreserveUp.
            on_manual_equip_only: Initial value for OnManualEquipOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_node is not None:
            self.position_node = position_node
        if rotation_node is not None:
            self.rotation_node = rotation_node
        if position_reference is not None:
            self.position_reference = position_reference
        if rotation_reference is not None:
            self.rotation_reference = rotation_reference
        if preserve_up is not None:
            self.preserve_up = preserve_up
        if on_manual_equip_only is not None:
            self.on_manual_equip_only = on_manual_equip_only

    @property
    def position_node(self) -> UserNode | None:
        """What node to use to match the position of the user."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @position_node.setter
    def position_node(self, value: UserNode | str) -> None:
        """Set PositionNode. What node to use to match the position of the user."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositionNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def rotation_node(self) -> UserNode | None:
        """What node to use to match the rotation of the user."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @rotation_node.setter
    def rotation_node(self, value: UserNode | str) -> None:
        """Set RotationNode. What node to use to match the rotation of the user."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RotationNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def position_reference(self) -> str | None:
        """The slot to position the user to instead of the slot this component is on when they equip the user."""
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
        """The slot to rotate the user to instead of the slot this component is on when they equip the user."""
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
    def preserve_up(self) -> primitives.Bool | None:
        """Whether to upright the user when they equip the avatar, or set them to the rotation this avatar is in when equipping."""
        member = self.get_member("PreserveUp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_up.setter
    def preserve_up(self, value: primitives.Bool) -> None:
        """Set the PreserveUp field value."""
        member = self.get_member("PreserveUp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUp", fields.FieldBool(value=value)
            )

    @property
    def on_manual_equip_only(self) -> primitives.Bool | None:
        """Whether to trigger this positioner only when the user clicks on the avatar to equip it rather than also triggering when the avatar is equipped through flux."""
        member = self.get_member("OnManualEquipOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @on_manual_equip_only.setter
    def on_manual_equip_only(self, value: primitives.Bool) -> None:
        """Set the OnManualEquipOnly field value."""
        member = self.get_member("OnManualEquipOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OnManualEquipOnly", fields.FieldBool(value=value)
            )

