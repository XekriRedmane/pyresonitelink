"""Generated component: AvatarAnchor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.user_node import UserNode
from pyresonitelink.generated._enums.restore_mode import RestoreMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_anchor import IAvatarAnchor
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAnchor(GeneratedComponent, IAvatarAnchor, IWorldEventReceiver):
    """An anchor allows for an avatar to be attached to a slot. This component can also allow for pinning of a user's limb(s) for posing, and is most commonly used as a seat.

    Category: Users/Common Avatar System/Anchors

    **Behavior**: By itself, an AvatarAnchor does nothing. It requires either an AvatarAnchorTouchTrigger component or a Anchor User ProtoFlux node to place an avatar into it.

To exit an anchor, a AvatarAnchorLocomotionRelease component or a Release User ProtoFlux node needs to be used.

When a user is anchored to an an anchor, first ``TransformRestoreMode`` takes it's effect on the settings (see above table for any field descriptions). Next the user root slot is parented under ``ParentSpace``. Then ``MinScale`` and ``MaxScale`` are applied to keep the avatar within the right size. After that the global rotation and position of the user's root slot is set to the global position and rotation of the ``PositionReference`` and ``RotationReference`` slots using their specified nodes. Lastly the avatar's filters are applied.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor"

    def __init__(self, highlight: primitives.Bool | None = None, min_scale: primitives.Float | None = None, max_scale: primitives.Float | None = None, position_node: UserNode | str | None = None, position_reference: str | Slot | None = None, rotation_node: UserNode | str | None = None, rotation_reference: str | Slot | None = None, preserve_up_on_enter: primitives.Bool | None = None, preserve_up_on_exit: primitives.Bool | None = None, unparent_everything_on_destroy: primitives.Bool | None = None, transform_restore_mode: RestoreMode | str | None = None, restore_node: UserNode | str | None = None, restore_reference: str | Slot | None = None, original_space: str | Slot | None = None, original_position: primitives.Float3 | None = None, original_rotation: primitives.FloatQ | None = None, original_scale: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            highlight: Initial value for Highlight.
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            position_node: Initial value for PositionNode.
            position_reference: Initial value for PositionReference.
            rotation_node: Initial value for RotationNode.
            rotation_reference: Initial value for RotationReference.
            preserve_up_on_enter: Initial value for PreserveUpOnEnter.
            preserve_up_on_exit: Initial value for PreserveUpOnExit.
            unparent_everything_on_destroy: Initial value for UnparentEverythingOnDestroy.
            transform_restore_mode: Initial value for TransformRestoreMode.
            restore_node: Initial value for RestoreNode.
            restore_reference: Initial value for RestoreReference.
            original_space: Initial value for _originalSpace.
            original_position: Initial value for _originalPosition.
            original_rotation: Initial value for _originalRotation.
            original_scale: Initial value for _originalScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if highlight is not None:
            self.highlight = highlight
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if position_node is not None:
            self.position_node = position_node
        if position_reference is not None:
            self.position_reference = position_reference
        if rotation_node is not None:
            self.rotation_node = rotation_node
        if rotation_reference is not None:
            self.rotation_reference = rotation_reference
        if preserve_up_on_enter is not None:
            self.preserve_up_on_enter = preserve_up_on_enter
        if preserve_up_on_exit is not None:
            self.preserve_up_on_exit = preserve_up_on_exit
        if unparent_everything_on_destroy is not None:
            self.unparent_everything_on_destroy = unparent_everything_on_destroy
        if transform_restore_mode is not None:
            self.transform_restore_mode = transform_restore_mode
        if restore_node is not None:
            self.restore_node = restore_node
        if restore_reference is not None:
            self.restore_reference = restore_reference
        if original_space is not None:
            self.original_space = original_space
        if original_position is not None:
            self.original_position = original_position
        if original_rotation is not None:
            self.original_rotation = original_rotation
        if original_scale is not None:
            self.original_scale = original_scale

    @property
    def highlight(self) -> primitives.Bool | None:
        """Whether a user is pointing at this anchor and it is possible for them to activate the enter dialogue by pressing Primary at this moment."""
        member = self.get_member("Highlight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight.setter
    def highlight(self, value: primitives.Bool) -> None:
        """Set the Highlight field value."""
        member = self.get_member("Highlight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Highlight", fields.FieldBool(value=value)
            )

    @property
    def parent_space(self) -> members.SyncObject | None:
        """The coordinate space in which to work with the avatar."""
        member = self.get_member("ParentSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @parent_space.setter
    def parent_space(self, value: members.SyncObject) -> None:
        """Set ParentSpace. The coordinate space in which to work with the avatar."""
        self.set_member("ParentSpace", value)

    @property
    def min_scale(self) -> primitives.Float | None:
        """If an avatar has a scale below the MinScale, it will be scaled up to that size."""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: primitives.Float) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat(value=value)
            )

    @property
    def max_scale(self) -> primitives.Float | None:
        """If an avatar has a scale above the MaxScale, it will be scaled down to that size."""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: primitives.Float) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat(value=value)
            )

    @property
    def position_node(self) -> UserNode | None:
        """Which part of the avatar to use to position the avatar."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @position_node.setter
    def position_node(self, value: UserNode | str) -> None:
        """Set PositionNode. Which part of the avatar to use to position the avatar."""
        member = self.get_member("PositionNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositionNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def position_reference(self) -> str | None:
        """Where to position the avatar to."""
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
    def rotation_node(self) -> UserNode | None:
        """Which part of the avatar to use to rotate the avatar."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @rotation_node.setter
    def rotation_node(self, value: UserNode | str) -> None:
        """Set RotationNode. Which part of the avatar to use to rotate the avatar."""
        member = self.get_member("RotationNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RotationNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def rotation_reference(self) -> str | None:
        """Where to rotate the avatar to."""
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
    def preserve_up_on_enter(self) -> primitives.Bool | None:
        """Whether to keep the user's root slot's up direction pointing the same direction it was in global space before entering, or to align them to the up of the slot of the anchor. This is disabled when ``RotationNode`` and ``RotationReference`` are set to not none."""
        member = self.get_member("PreserveUpOnEnter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_up_on_enter.setter
    def preserve_up_on_enter(self, value: primitives.Bool) -> None:
        """Set the PreserveUpOnEnter field value."""
        member = self.get_member("PreserveUpOnEnter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUpOnEnter", fields.FieldBool(value=value)
            )

    @property
    def preserve_up_on_exit(self) -> primitives.Bool | None:
        """Whether to keep the user's root slot's up direction pointing the same direction it was in global space before exiting, or to align them to the up of the slot they get parented back under. This is disabled when ``TransformRestoreMode`` and ``RestoreNode`` are set to not none."""
        member = self.get_member("PreserveUpOnExit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_up_on_exit.setter
    def preserve_up_on_exit(self, value: primitives.Bool) -> None:
        """Set the PreserveUpOnExit field value."""
        member = self.get_member("PreserveUpOnExit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUpOnExit", fields.FieldBool(value=value)
            )

    @property
    def unparent_everything_on_destroy(self) -> primitives.Bool | None:
        """Unparent all slots under ``ParentSpace``'s Space slot and parent them under the parent of the nearest ObjectRoot (doesn't need an explicit ObjectRoot component). If ``ParentSpace``'s Space slot is null, or the ObjectRoot parent is null, then all children are deleted anyway."""
        member = self.get_member("UnparentEverythingOnDestroy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unparent_everything_on_destroy.setter
    def unparent_everything_on_destroy(self, value: primitives.Bool) -> None:
        """Set the UnparentEverythingOnDestroy field value."""
        member = self.get_member("UnparentEverythingOnDestroy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnparentEverythingOnDestroy", fields.FieldBool(value=value)
            )

    @property
    def transform_restore_mode(self) -> RestoreMode | None:
        """What slot or space to use when setting the user's transforms to what they were before they entered the anchor."""
        member = self.get_member("TransformRestoreMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RestoreMode(member.value)
        return None

    @transform_restore_mode.setter
    def transform_restore_mode(self, value: RestoreMode | str) -> None:
        """Set TransformRestoreMode. What slot or space to use when setting the user's transforms to what they were before they entered the anchor."""
        member = self.get_member("TransformRestoreMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TransformRestoreMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def restore_node(self) -> UserNode | None:
        """The part of the user's avatar that the transforms should be changed to ``_originalPosition``, ``_originalRotation``, and ``_originalScale`` when the user exits the anchor. Which space the transforms refer to (aka what it would be parented to) depends on what ``TransformRestoreMode`` is set to."""
        member = self.get_member("RestoreNode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return UserNode(member.value)
        return None

    @restore_node.setter
    def restore_node(self, value: UserNode | str) -> None:
        """Set RestoreNode. The part of the user's avatar that the transforms should be changed to ``_originalPosition``, ``_originalRotation``, and ``_originalScale`` when the user exits the anchor. Which space the transforms refer to (aka what it would be parented to) depends on what ``TransformRestoreMode`` is set to."""
        member = self.get_member("RestoreNode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RestoreNode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def restore_reference(self) -> str | None:
        """This will be used from when ``TransformRestoreMode`` is set to "Reference". The specified ``RestoreNode``'s transform will be set to this slot's space using ``_originalPosition``, ``_originalRotation``, and ``_originalScale``."""
        member = self.get_member("RestoreReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @restore_reference.setter
    def restore_reference(self, target: str | Slot | None) -> None:
        """Set the RestoreReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("RestoreReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RestoreReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def filters(self) -> members.SyncList | None:
        """A list of pose filters to use. Each one can control the position, rotation, and/or speed of a specific body node"""
        member = self.get_member("Filters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @filters.setter
    def filters(self, value: members.SyncList) -> None:
        """Set Filters. A list of pose filters to use. Each one can control the position, rotation, and/or speed of a specific body node"""
        self.set_member("Filters", value)

    @property
    def user_filters(self) -> members.SyncList | None:
        """Nothing currently implements IAvatarAnchorUserFilter so this currently does nothing."""
        member = self.get_member("UserFilters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @user_filters.setter
    def user_filters(self, value: members.SyncList) -> None:
        """Set UserFilters. Nothing currently implements IAvatarAnchorUserFilter so this currently does nothing."""
        self.set_member("UserFilters", value)

    @property
    def original_space(self) -> str | None:
        """Internal"""
        member = self.get_member("_originalSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_space.setter
    def original_space(self, target: str | Slot | None) -> None:
        """Set the _originalSpace reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_originalSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_originalSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def original_position(self) -> primitives.Float3 | None:
        """Internal"""
        member = self.get_member("_originalPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_position.setter
    def original_position(self, value: primitives.Float3) -> None:
        """Set the _originalPosition field value."""
        member = self.get_member("_originalPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalPosition", fields.FieldFloat3(value=value)
            )

    @property
    def original_rotation(self) -> primitives.FloatQ | None:
        """Internal"""
        member = self.get_member("_originalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_rotation.setter
    def original_rotation(self, value: primitives.FloatQ) -> None:
        """Set the _originalRotation field value."""
        member = self.get_member("_originalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def original_scale(self) -> primitives.Float | None:
        """Internal"""
        member = self.get_member("_originalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_scale.setter
    def original_scale(self, value: primitives.Float) -> None:
        """Set the _originalScale field value."""
        member = self.get_member("_originalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalScale", fields.FieldFloat(value=value)
            )

    @property
    def dummy_object_slots(self) -> members.SyncList | None:
        """Internal"""
        member = self.get_member("_dummyObjectSlots")
        if isinstance(member, members.SyncList):
            return member
        return None

    @dummy_object_slots.setter
    def dummy_object_slots(self, value: members.SyncList) -> None:
        """Set _dummyObjectSlots. Internal"""
        self.set_member("_dummyObjectSlots", value)

