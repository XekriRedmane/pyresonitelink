"""Generated component: Canvas."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.box_collider import BoxCollider
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.itouch_grabbable import ITouchGrabbable
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.ilaser_interaction_modifier import ILaserInteractionModifier
from pyresonitelink.generated._types.iinteraction_target import IInteractionTarget
from pyresonitelink.generated._types.icontext_menu_action_receiver import IContextMenuActionReceiver
from pyresonitelink.generated._types.isecondary_action_receiver import ISecondaryActionReceiver
from pyresonitelink.generated._types.iaxis_action_receiver import IAxisActionReceiver
from pyresonitelink.generated._types.iui_interface import IUIInterface
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Canvas(GeneratedComponent, ITouchable, ITouchGrabbable, IBounded, ILaserInteractionModifier, IInteractionTarget, IContextMenuActionReceiver, ISecondaryActionReceiver, IAxisActionReceiver, IUIInterface, IRenderable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.Canvas.

    Category: UIX
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Canvas"

    def __init__(self, root_rect: str | RectTransform | None = None, collider: str | BoxCollider | None = None, collider_size: str | IField[primitives.Float3] | None = None, collider_offset: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root_rect: Initial value for _rootRect.
            collider: Initial value for Collider.
            collider_size: Initial value for _colliderSize.
            collider_offset: Initial value for _colliderOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root_rect is not None:
            self.root_rect = root_rect
        if collider is not None:
            self.collider = collider
        if collider_size is not None:
            self.collider_size = collider_size
        if collider_offset is not None:
            self.collider_offset = collider_offset

    @property
    def size(self) -> primitives.Float2 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float2) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat2(value=value)
            )

    @property
    def edit_mode_only(self) -> bool | None:
        """The EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_physical_touch(self) -> bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_existing_touch(self) -> bool | None:
        """The AcceptExistingTouch field value."""
        member = self.get_member("AcceptExistingTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_existing_touch.setter
    def accept_existing_touch(self, value: bool) -> None:
        """Set the AcceptExistingTouch field value."""
        member = self.get_member("AcceptExistingTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptExistingTouch", fields.FieldBool(value=value)
            )

    @property
    def high_priority_integration(self) -> bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def ignore_touches_from_behind(self) -> bool | None:
        """The IgnoreTouchesFromBehind field value."""
        member = self.get_member("IgnoreTouchesFromBehind")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_touches_from_behind.setter
    def ignore_touches_from_behind(self, value: bool) -> None:
        """Set the IgnoreTouchesFromBehind field value."""
        member = self.get_member("IgnoreTouchesFromBehind")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreTouchesFromBehind", fields.FieldBool(value=value)
            )

    @property
    def block_all_interactions(self) -> bool | None:
        """The BlockAllInteractions field value."""
        member = self.get_member("BlockAllInteractions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_all_interactions.setter
    def block_all_interactions(self, value: bool) -> None:
        """Set the BlockAllInteractions field value."""
        member = self.get_member("BlockAllInteractions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockAllInteractions", fields.FieldBool(value=value)
            )

    @property
    def laser_pass_through(self) -> bool | None:
        """The LaserPassThrough field value."""
        member = self.get_member("LaserPassThrough")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laser_pass_through.setter
    def laser_pass_through(self, value: bool) -> None:
        """Set the LaserPassThrough field value."""
        member = self.get_member("LaserPassThrough")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LaserPassThrough", fields.FieldBool(value=value)
            )

    @property
    def pixel_scale(self) -> np.float32 | None:
        """The PixelScale field value."""
        member = self.get_member("PixelScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pixel_scale.setter
    def pixel_scale(self, value: np.float32) -> None:
        """Set the PixelScale field value."""
        member = self.get_member("PixelScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PixelScale", fields.FieldFloat(value=value)
            )

    @property
    def unit_scale(self) -> np.float32 | None:
        """The UnitScale field value."""
        member = self.get_member("UnitScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unit_scale.setter
    def unit_scale(self, value: np.float32) -> None:
        """Set the UnitScale field value."""
        member = self.get_member("UnitScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnitScale", fields.FieldFloat(value=value)
            )

    @property
    def root_rect(self) -> str | None:
        """Target ID of the _rootRect reference (targets RectTransform)."""
        member = self.get_member("_rootRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_rect.setter
    def root_rect(self, target: str | RectTransform | None) -> None:
        """Set the _rootRect reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_rootRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rootRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def collider(self) -> str | None:
        """Target ID of the Collider reference (targets BoxCollider)."""
        member = self.get_member("Collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | BoxCollider | None) -> None:
        """Set the Collider reference by target ID or BoxCollider instance."""
        target_id: str | None = target.id if isinstance(target, BoxCollider) else target  # type: ignore[assignment]
        member = self.get_member("Collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BoxCollider'),
            )

    @property
    def default_culling(self) -> members.FieldEnum | None:
        """The DefaultCulling member."""
        member = self.get_member("DefaultCulling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @default_culling.setter
    def default_culling(self, value: members.FieldEnum) -> None:
        """Set the DefaultCulling member."""
        self.set_member("DefaultCulling", value)

    @property
    def collider_size(self) -> str | None:
        """Target ID of the _colliderSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def collider_offset(self) -> str | None:
        """Target ID of the _colliderOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_colliderOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_offset.setter
    def collider_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def starting_offset(self) -> np.int32 | None:
        """The StartingOffset field value."""
        member = self.get_member("StartingOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @starting_offset.setter
    def starting_offset(self, value: np.int32) -> None:
        """Set the StartingOffset field value."""
        member = self.get_member("StartingOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartingOffset", fields.FieldInt(value=value)
            )

    @property
    def starting_mask_depth(self) -> np.int32 | None:
        """The StartingMaskDepth field value."""
        member = self.get_member("StartingMaskDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @starting_mask_depth.setter
    def starting_mask_depth(self, value: np.int32) -> None:
        """Set the StartingMaskDepth field value."""
        member = self.get_member("StartingMaskDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartingMaskDepth", fields.FieldInt(value=value)
            )

