"""Generated component: AvatarParentNode."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_object import IAvatarObject
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarParentNode(GeneratedComponent, IAvatarObject, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarParentNode.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarParentNode"

    def __init__(self, destroy_on_dequip: bool | None = None, scale: primitives.Float3 | None = None, equip_order_priority: np.int32 | None = None, original_parent: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            destroy_on_dequip: Initial value for DestroyOnDequip.
            scale: Initial value for Scale.
            equip_order_priority: Initial value for EquipOrderPriority.
            original_parent: Initial value for _originalParent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if destroy_on_dequip is not None:
            self.destroy_on_dequip = destroy_on_dequip
        if scale is not None:
            self.scale = scale
        if equip_order_priority is not None:
            self.equip_order_priority = equip_order_priority
        if original_parent is not None:
            self.original_parent = original_parent

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
    def destroy_on_dequip(self) -> bool | None:
        """The DestroyOnDequip field value."""
        member = self.get_member("DestroyOnDequip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @destroy_on_dequip.setter
    def destroy_on_dequip(self, value: bool) -> None:
        """Set the DestroyOnDequip field value."""
        member = self.get_member("DestroyOnDequip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DestroyOnDequip", fields.FieldBool(value=value)
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

    @property
    def equip_order_priority(self) -> np.int32 | None:
        """The EquipOrderPriority field value."""
        member = self.get_member("EquipOrderPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_order_priority.setter
    def equip_order_priority(self, value: np.int32) -> None:
        """Set the EquipOrderPriority field value."""
        member = self.get_member("EquipOrderPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquipOrderPriority", fields.FieldInt(value=value)
            )

    @property
    def original_parent(self) -> str | None:
        """Target ID of the _originalParent reference (targets Slot)."""
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_parent.setter
    def original_parent(self, target: str | Slot | None) -> None:
        """Set the _originalParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_originalParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

