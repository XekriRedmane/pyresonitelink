"""Generated component: UpdateTransform."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UpdateTransform(GeneratedComponent, IUndoable, IWorldEventReceiver):
    """Update transform is part of the Undo system, and is used in the Undo Manager to allow undoing and redoing of moving an object.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.UpdateTransform"

    def __init__(self, target: str | Slot | None = None, restore_parent: primitives.Bool | None = None, restore_position: primitives.Bool | None = None, restore_rotation: primitives.Bool | None = None, restore_scale: primitives.Bool | None = None, parent_before: str | Slot | None = None, parent_after: str | Slot | None = None, local_position_before: primitives.Float3 | None = None, local_rotation_before: primitives.FloatQ | None = None, local_scale_before: primitives.Float3 | None = None, global_position_before: primitives.Float3 | None = None, global_rotation_before: primitives.FloatQ | None = None, global_scale_before: primitives.Float3 | None = None, local_position_after: primitives.Float3 | None = None, local_rotation_after: primitives.FloatQ | None = None, local_scale_after: primitives.Float3 | None = None, global_position_after: primitives.Float3 | None = None, global_rotation_after: primitives.FloatQ | None = None, global_scale_after: primitives.Float3 | None = None, performed: primitives.Bool | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            restore_parent: Initial value for RestoreParent.
            restore_position: Initial value for RestorePosition.
            restore_rotation: Initial value for RestoreRotation.
            restore_scale: Initial value for RestoreScale.
            parent_before: Initial value for ParentBefore.
            parent_after: Initial value for ParentAfter.
            local_position_before: Initial value for LocalPositionBefore.
            local_rotation_before: Initial value for LocalRotationBefore.
            local_scale_before: Initial value for LocalScaleBefore.
            global_position_before: Initial value for GlobalPositionBefore.
            global_rotation_before: Initial value for GlobalRotationBefore.
            global_scale_before: Initial value for GlobalScaleBefore.
            local_position_after: Initial value for LocalPositionAfter.
            local_rotation_after: Initial value for LocalRotationAfter.
            local_scale_after: Initial value for LocalScaleAfter.
            global_position_after: Initial value for GlobalPositionAfter.
            global_rotation_after: Initial value for GlobalRotationAfter.
            global_scale_after: Initial value for GlobalScaleAfter.
            performed: Initial value for _performed.
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if restore_parent is not None:
            self.restore_parent = restore_parent
        if restore_position is not None:
            self.restore_position = restore_position
        if restore_rotation is not None:
            self.restore_rotation = restore_rotation
        if restore_scale is not None:
            self.restore_scale = restore_scale
        if parent_before is not None:
            self.parent_before = parent_before
        if parent_after is not None:
            self.parent_after = parent_after
        if local_position_before is not None:
            self.local_position_before = local_position_before
        if local_rotation_before is not None:
            self.local_rotation_before = local_rotation_before
        if local_scale_before is not None:
            self.local_scale_before = local_scale_before
        if global_position_before is not None:
            self.global_position_before = global_position_before
        if global_rotation_before is not None:
            self.global_rotation_before = global_rotation_before
        if global_scale_before is not None:
            self.global_scale_before = global_scale_before
        if local_position_after is not None:
            self.local_position_after = local_position_after
        if local_rotation_after is not None:
            self.local_rotation_after = local_rotation_after
        if local_scale_after is not None:
            self.local_scale_after = local_scale_after
        if global_position_after is not None:
            self.global_position_after = global_position_after
        if global_rotation_after is not None:
            self.global_rotation_after = global_rotation_after
        if global_scale_after is not None:
            self.global_scale_after = global_scale_after
        if performed is not None:
            self.performed = performed
        if description is not None:
            self.description = description

    @property
    def target(self) -> str | None:
        """The slot that was moved."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | Slot | None) -> None:
        """Set the Target reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def restore_parent(self) -> primitives.Bool | None:
        """Whether or not to restore the parent object."""
        member = self.get_member("RestoreParent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @restore_parent.setter
    def restore_parent(self, value: primitives.Bool) -> None:
        """Set the RestoreParent field value."""
        member = self.get_member("RestoreParent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RestoreParent", fields.FieldBool(value=value)
            )

    @property
    def restore_position(self) -> primitives.Bool | None:
        """Whether or not to restore the position of the object."""
        member = self.get_member("RestorePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @restore_position.setter
    def restore_position(self, value: primitives.Bool) -> None:
        """Set the RestorePosition field value."""
        member = self.get_member("RestorePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RestorePosition", fields.FieldBool(value=value)
            )

    @property
    def restore_rotation(self) -> primitives.Bool | None:
        """Whether or not to restore the rotation of the object."""
        member = self.get_member("RestoreRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @restore_rotation.setter
    def restore_rotation(self, value: primitives.Bool) -> None:
        """Set the RestoreRotation field value."""
        member = self.get_member("RestoreRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RestoreRotation", fields.FieldBool(value=value)
            )

    @property
    def restore_scale(self) -> primitives.Bool | None:
        """Whether or not to restore the scale of the object."""
        member = self.get_member("RestoreScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @restore_scale.setter
    def restore_scale(self, value: primitives.Bool) -> None:
        """Set the RestoreScale field value."""
        member = self.get_member("RestoreScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RestoreScale", fields.FieldBool(value=value)
            )

    @property
    def parent_before(self) -> str | None:
        """The parent slot that the object had before the move."""
        member = self.get_member("ParentBefore")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_before.setter
    def parent_before(self, target: str | Slot | None) -> None:
        """Set the ParentBefore reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentBefore")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentBefore",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def parent_after(self) -> str | None:
        """The parent slot the object had after the move."""
        member = self.get_member("ParentAfter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_after.setter
    def parent_after(self, target: str | Slot | None) -> None:
        """Set the ParentAfter reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentAfter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentAfter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def local_position_before(self) -> primitives.Float3 | None:
        """The Local Position that the object had before the move."""
        member = self.get_member("LocalPositionBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_position_before.setter
    def local_position_before(self, value: primitives.Float3) -> None:
        """Set the LocalPositionBefore field value."""
        member = self.get_member("LocalPositionBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalPositionBefore", fields.FieldFloat3(value=value)
            )

    @property
    def local_rotation_before(self) -> primitives.FloatQ | None:
        """The Local Rotation that the object had before the move."""
        member = self.get_member("LocalRotationBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_rotation_before.setter
    def local_rotation_before(self, value: primitives.FloatQ) -> None:
        """Set the LocalRotationBefore field value."""
        member = self.get_member("LocalRotationBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalRotationBefore", fields.FieldFloatQ(value=value)
            )

    @property
    def local_scale_before(self) -> primitives.Float3 | None:
        """The Local Scale that the object had before the move."""
        member = self.get_member("LocalScaleBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_scale_before.setter
    def local_scale_before(self, value: primitives.Float3) -> None:
        """Set the LocalScaleBefore field value."""
        member = self.get_member("LocalScaleBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalScaleBefore", fields.FieldFloat3(value=value)
            )

    @property
    def global_position_before(self) -> primitives.Float3 | None:
        """The Global Position that the object had before the move."""
        member = self.get_member("GlobalPositionBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_position_before.setter
    def global_position_before(self, value: primitives.Float3) -> None:
        """Set the GlobalPositionBefore field value."""
        member = self.get_member("GlobalPositionBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalPositionBefore", fields.FieldFloat3(value=value)
            )

    @property
    def global_rotation_before(self) -> primitives.FloatQ | None:
        """The Global Rotation that the object had before the move."""
        member = self.get_member("GlobalRotationBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_rotation_before.setter
    def global_rotation_before(self, value: primitives.FloatQ) -> None:
        """Set the GlobalRotationBefore field value."""
        member = self.get_member("GlobalRotationBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalRotationBefore", fields.FieldFloatQ(value=value)
            )

    @property
    def global_scale_before(self) -> primitives.Float3 | None:
        """The Global Scale that the object had before the move."""
        member = self.get_member("GlobalScaleBefore")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_scale_before.setter
    def global_scale_before(self, value: primitives.Float3) -> None:
        """Set the GlobalScaleBefore field value."""
        member = self.get_member("GlobalScaleBefore")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalScaleBefore", fields.FieldFloat3(value=value)
            )

    @property
    def local_position_after(self) -> primitives.Float3 | None:
        """The Local Position the object had after the move."""
        member = self.get_member("LocalPositionAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_position_after.setter
    def local_position_after(self, value: primitives.Float3) -> None:
        """Set the LocalPositionAfter field value."""
        member = self.get_member("LocalPositionAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalPositionAfter", fields.FieldFloat3(value=value)
            )

    @property
    def local_rotation_after(self) -> primitives.FloatQ | None:
        """The Local Rotation the object had after the move."""
        member = self.get_member("LocalRotationAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_rotation_after.setter
    def local_rotation_after(self, value: primitives.FloatQ) -> None:
        """Set the LocalRotationAfter field value."""
        member = self.get_member("LocalRotationAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalRotationAfter", fields.FieldFloatQ(value=value)
            )

    @property
    def local_scale_after(self) -> primitives.Float3 | None:
        """The Local Scale the object had after the move."""
        member = self.get_member("LocalScaleAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_scale_after.setter
    def local_scale_after(self, value: primitives.Float3) -> None:
        """Set the LocalScaleAfter field value."""
        member = self.get_member("LocalScaleAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalScaleAfter", fields.FieldFloat3(value=value)
            )

    @property
    def global_position_after(self) -> primitives.Float3 | None:
        """The Global Position the object had after the move."""
        member = self.get_member("GlobalPositionAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_position_after.setter
    def global_position_after(self, value: primitives.Float3) -> None:
        """Set the GlobalPositionAfter field value."""
        member = self.get_member("GlobalPositionAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalPositionAfter", fields.FieldFloat3(value=value)
            )

    @property
    def global_rotation_after(self) -> primitives.FloatQ | None:
        """The Global Rotation the object had after the move."""
        member = self.get_member("GlobalRotationAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_rotation_after.setter
    def global_rotation_after(self, value: primitives.FloatQ) -> None:
        """Set the GlobalRotationAfter field value."""
        member = self.get_member("GlobalRotationAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalRotationAfter", fields.FieldFloatQ(value=value)
            )

    @property
    def global_scale_after(self) -> primitives.Float3 | None:
        """The Global Scale the object had after the move."""
        member = self.get_member("GlobalScaleAfter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_scale_after.setter
    def global_scale_after(self, value: primitives.Float3) -> None:
        """Set the GlobalScaleAfter field value."""
        member = self.get_member("GlobalScaleAfter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalScaleAfter", fields.FieldFloat3(value=value)
            )

    @property
    def performed(self) -> primitives.Bool | None:
        """Whether the action is performed or it is in the future (due to undoing by the user."""
        member = self.get_member("_performed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @performed.setter
    def performed(self, value: primitives.Bool) -> None:
        """Set the _performed field value."""
        member = self.get_member("_performed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_performed", fields.FieldBool(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The description of this move action."""
        member = self.get_member("_description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the _description field value."""
        member = self.get_member("_description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_description", fields.FieldString(value=value)
            )

