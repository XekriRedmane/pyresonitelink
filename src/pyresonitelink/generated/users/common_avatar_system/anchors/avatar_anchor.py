"""Generated component: AvatarAnchor."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iavatar_anchor import IAvatarAnchor
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAnchor(GeneratedComponent, IAvatarAnchor, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor.

    Category: Users/Common Avatar System/Anchors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor"

    def __init__(self, highlight: bool | None = None, min_scale: np.float32 | None = None, max_scale: np.float32 | None = None, position_reference: str | Slot | None = None, rotation_reference: str | Slot | None = None, preserve_up_on_enter: bool | None = None, preserve_up_on_exit: bool | None = None, unparent_everything_on_destroy: bool | None = None, restore_reference: str | Slot | None = None, original_space: str | Slot | None = None, original_position: primitives.Float3 | None = None, original_rotation: primitives.FloatQ | None = None, original_scale: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            highlight: Initial value for Highlight.
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            position_reference: Initial value for PositionReference.
            rotation_reference: Initial value for RotationReference.
            preserve_up_on_enter: Initial value for PreserveUpOnEnter.
            preserve_up_on_exit: Initial value for PreserveUpOnExit.
            unparent_everything_on_destroy: Initial value for UnparentEverythingOnDestroy.
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
        if position_reference is not None:
            self.position_reference = position_reference
        if rotation_reference is not None:
            self.rotation_reference = rotation_reference
        if preserve_up_on_enter is not None:
            self.preserve_up_on_enter = preserve_up_on_enter
        if preserve_up_on_exit is not None:
            self.preserve_up_on_exit = preserve_up_on_exit
        if unparent_everything_on_destroy is not None:
            self.unparent_everything_on_destroy = unparent_everything_on_destroy
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
    def highlight(self) -> bool | None:
        """The Highlight field value."""
        member = self.get_member("Highlight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight.setter
    def highlight(self, value: bool) -> None:
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
        """The ParentSpace member."""
        member = self.get_member("ParentSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @parent_space.setter
    def parent_space(self, value: members.SyncObject) -> None:
        """Set the ParentSpace member."""
        self.set_member("ParentSpace", value)

    @property
    def min_scale(self) -> np.float32 | None:
        """The MinScale field value."""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: np.float32) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat(value=value)
            )

    @property
    def max_scale(self) -> np.float32 | None:
        """The MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: np.float32) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat(value=value)
            )

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
    def preserve_up_on_enter(self) -> bool | None:
        """The PreserveUpOnEnter field value."""
        member = self.get_member("PreserveUpOnEnter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_up_on_enter.setter
    def preserve_up_on_enter(self, value: bool) -> None:
        """Set the PreserveUpOnEnter field value."""
        member = self.get_member("PreserveUpOnEnter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUpOnEnter", fields.FieldBool(value=value)
            )

    @property
    def preserve_up_on_exit(self) -> bool | None:
        """The PreserveUpOnExit field value."""
        member = self.get_member("PreserveUpOnExit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_up_on_exit.setter
    def preserve_up_on_exit(self, value: bool) -> None:
        """Set the PreserveUpOnExit field value."""
        member = self.get_member("PreserveUpOnExit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUpOnExit", fields.FieldBool(value=value)
            )

    @property
    def unparent_everything_on_destroy(self) -> bool | None:
        """The UnparentEverythingOnDestroy field value."""
        member = self.get_member("UnparentEverythingOnDestroy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unparent_everything_on_destroy.setter
    def unparent_everything_on_destroy(self, value: bool) -> None:
        """Set the UnparentEverythingOnDestroy field value."""
        member = self.get_member("UnparentEverythingOnDestroy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnparentEverythingOnDestroy", fields.FieldBool(value=value)
            )

    @property
    def transform_restore_mode(self) -> members.FieldEnum | None:
        """The TransformRestoreMode member."""
        member = self.get_member("TransformRestoreMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @transform_restore_mode.setter
    def transform_restore_mode(self, value: members.FieldEnum) -> None:
        """Set the TransformRestoreMode member."""
        self.set_member("TransformRestoreMode", value)

    @property
    def restore_node(self) -> members.FieldEnum | None:
        """The RestoreNode member."""
        member = self.get_member("RestoreNode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @restore_node.setter
    def restore_node(self, value: members.FieldEnum) -> None:
        """Set the RestoreNode member."""
        self.set_member("RestoreNode", value)

    @property
    def restore_reference(self) -> str | None:
        """Target ID of the RestoreReference reference (targets Slot)."""
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
        """The Filters member."""
        member = self.get_member("Filters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @filters.setter
    def filters(self, value: members.SyncList) -> None:
        """Set the Filters member."""
        self.set_member("Filters", value)

    @property
    def user_filters(self) -> members.SyncList | None:
        """The UserFilters member."""
        member = self.get_member("UserFilters")
        if isinstance(member, members.SyncList):
            return member
        return None

    @user_filters.setter
    def user_filters(self, value: members.SyncList) -> None:
        """Set the UserFilters member."""
        self.set_member("UserFilters", value)

    @property
    def original_space(self) -> str | None:
        """Target ID of the _originalSpace reference (targets Slot)."""
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
        """The _originalPosition field value."""
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
        """The _originalRotation field value."""
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
    def original_scale(self) -> np.float32 | None:
        """The _originalScale field value."""
        member = self.get_member("_originalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_scale.setter
    def original_scale(self, value: np.float32) -> None:
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
        """The _dummyObjectSlots member."""
        member = self.get_member("_dummyObjectSlots")
        if isinstance(member, members.SyncList):
            return member
        return None

    @dummy_object_slots.setter
    def dummy_object_slots(self, value: members.SyncList) -> None:
        """Set the _dummyObjectSlots member."""
        self.set_member("_dummyObjectSlots", value)

