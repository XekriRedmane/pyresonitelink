"""Generated component: Canvas."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.culling import Culling
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
    """The Canvas component is the starting point for anything based on UIX. It provides the bounds of the UI and controls how users can interact with it.

- DefaultCulling: Especially for rendering the back side of the canvas.|warning}}

}}

    Category: UIX

    This component is needed for UIX, without it, your other components that
    relay on UIX, canvas, elements, and rects will not work as expected.
    Using a canvas not only organizes your other components, it renders them
    and makes them usable and interactable.

    **See also**: * When a child slot is created when under a Slot that has a canvas component, the new child slot will automatically create a RectTransform component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.Canvas"

    def __init__(self, size: primitives.Float2 | None = None, edit_mode_only: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_existing_touch: primitives.Bool | None = None, high_priority_integration: primitives.Bool | None = None, ignore_touches_from_behind: primitives.Bool | None = None, block_all_interactions: primitives.Bool | None = None, laser_pass_through: primitives.Bool | None = None, pixel_scale: primitives.Float | None = None, unit_scale: primitives.Float | None = None, root_rect: str | RectTransform | None = None, collider: str | BoxCollider | None = None, default_culling: Culling | str | None = None, collider_size: str | IField[primitives.Float3] | None = None, collider_offset: str | IField[primitives.Float3] | None = None, starting_offset: primitives.Int | None = None, starting_mask_depth: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            size: Initial value for Size.
            edit_mode_only: Initial value for EditModeOnly.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_existing_touch: Initial value for AcceptExistingTouch.
            high_priority_integration: Initial value for HighPriorityIntegration.
            ignore_touches_from_behind: Initial value for IgnoreTouchesFromBehind.
            block_all_interactions: Initial value for BlockAllInteractions.
            laser_pass_through: Initial value for LaserPassThrough.
            pixel_scale: Initial value for PixelScale.
            unit_scale: Initial value for UnitScale.
            root_rect: Initial value for _rootRect.
            collider: Initial value for Collider.
            default_culling: Initial value for DefaultCulling.
            collider_size: Initial value for _colliderSize.
            collider_offset: Initial value for _colliderOffset.
            starting_offset: Initial value for StartingOffset.
            starting_mask_depth: Initial value for StartingMaskDepth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if size is not None:
            self.size = size
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_existing_touch is not None:
            self.accept_existing_touch = accept_existing_touch
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if ignore_touches_from_behind is not None:
            self.ignore_touches_from_behind = ignore_touches_from_behind
        if block_all_interactions is not None:
            self.block_all_interactions = block_all_interactions
        if laser_pass_through is not None:
            self.laser_pass_through = laser_pass_through
        if pixel_scale is not None:
            self.pixel_scale = pixel_scale
        if unit_scale is not None:
            self.unit_scale = unit_scale
        if root_rect is not None:
            self.root_rect = root_rect
        if collider is not None:
            self.collider = collider
        if default_culling is not None:
            self.default_culling = default_culling
        if collider_size is not None:
            self.collider_size = collider_size
        if collider_offset is not None:
            self.collider_offset = collider_offset
        if starting_offset is not None:
            self.starting_offset = starting_offset
        if starting_mask_depth is not None:
            self.starting_mask_depth = starting_mask_depth

    @property
    def size(self) -> primitives.Float2 | None:
        """The dimensions of the canvas. At normal scale, this is equivalent to meters"""
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
    def edit_mode_only(self) -> primitives.Bool | None:
        """This makes this component only editable in Edit Mode"""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: primitives.Bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_existing_touch(self) -> primitives.Bool | None:
        """If this canvas is already being touched (physically or remotely), accept the input"""
        member = self.get_member("AcceptExistingTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_existing_touch.setter
    def accept_existing_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptExistingTouch field value."""
        member = self.get_member("AcceptExistingTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptExistingTouch", fields.FieldBool(value=value)
            )

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def ignore_touches_from_behind(self) -> primitives.Bool | None:
        """Makes the canvas ignore all touches from behind"""
        member = self.get_member("IgnoreTouchesFromBehind")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_touches_from_behind.setter
    def ignore_touches_from_behind(self, value: primitives.Bool) -> None:
        """Set the IgnoreTouchesFromBehind field value."""
        member = self.get_member("IgnoreTouchesFromBehind")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreTouchesFromBehind", fields.FieldBool(value=value)
            )

    @property
    def block_all_interactions(self) -> primitives.Bool | None:
        """Prevents any interaction if enabled"""
        member = self.get_member("BlockAllInteractions")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_all_interactions.setter
    def block_all_interactions(self, value: primitives.Bool) -> None:
        """Set the BlockAllInteractions field value."""
        member = self.get_member("BlockAllInteractions")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockAllInteractions", fields.FieldBool(value=value)
            )

    @property
    def laser_pass_through(self) -> primitives.Bool | None:
        """Allows the laser to go through the canvas"""
        member = self.get_member("LaserPassThrough")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laser_pass_through.setter
    def laser_pass_through(self, value: primitives.Bool) -> None:
        """Set the LaserPassThrough field value."""
        member = self.get_member("LaserPassThrough")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LaserPassThrough", fields.FieldBool(value=value)
            )

    @property
    def pixel_scale(self) -> primitives.Float | None:
        """Sets the pixel scale for this canvas and its contents"""
        member = self.get_member("PixelScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pixel_scale.setter
    def pixel_scale(self, value: primitives.Float) -> None:
        """Set the PixelScale field value."""
        member = self.get_member("PixelScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PixelScale", fields.FieldFloat(value=value)
            )

    @property
    def unit_scale(self) -> primitives.Float | None:
        """Scales the contents of this canvas, higher number makes the contents smaller"""
        member = self.get_member("UnitScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unit_scale.setter
    def unit_scale(self, value: primitives.Float) -> None:
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
        """Internal - The root rect of this canvas"""
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
        """The collider that receives touches from this canvas"""
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
    def default_culling(self) -> Culling | None:
        """Culling for this canvas"""
        member = self.get_member("DefaultCulling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Culling(member.value)
        return None

    @default_culling.setter
    def default_culling(self, value: Culling | str) -> None:
        """Set DefaultCulling. Culling for this canvas"""
        member = self.get_member("DefaultCulling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DefaultCulling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def collider_size(self) -> str | None:
        """Internal - Takes in a box collider and uses it for the canvas"""
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
        """Internal - Offsets this box collider for this canvas"""
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
    def starting_offset(self) -> primitives.Int | None:
        """The visibility order of rendering this canvas (lower number gets drawn over higher numbers)"""
        member = self.get_member("StartingOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @starting_offset.setter
    def starting_offset(self, value: primitives.Int) -> None:
        """Set the StartingOffset field value."""
        member = self.get_member("StartingOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartingOffset", fields.FieldInt(value=value)
            )

    @property
    def starting_mask_depth(self) -> primitives.Int | None:
        """Masking layer for the canvas"""
        member = self.get_member("StartingMaskDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @starting_mask_depth.setter
    def starting_mask_depth(self, value: primitives.Int) -> None:
        """Set the StartingMaskDepth field value."""
        member = self.get_member("StartingMaskDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartingMaskDepth", fields.FieldInt(value=value)
            )

