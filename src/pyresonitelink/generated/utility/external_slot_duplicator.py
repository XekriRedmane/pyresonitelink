"""Generated component: ExternalSlotDuplicator."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ExternalSlotDuplicator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ExternalSlotDuplicator component parents ``TargetSlot`` under itself when this component is duplicated. If this component is parented under a larger hiearchy, the slot will only be parented if it's not anywhere under this larger hiearchy or this component's hiearchy. When the slot is parented back under this component, any non null specified transform values for this component are applied to the slot.

If ``DoNotRestoreOriginalTransform`` is enabled, it will parent the slot back where it came from and restore the original local transform values after duplication.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ExternalSlotDuplicator"

    def __init__(self, target_slot: str | Slot | None = None, local_position_override: primitives.Float3 | None = None, local_rotation_override: primitives.FloatQ | None = None, local_scale_override: primitives.Float3 | None = None, active_self_override: primitives.Bool | None = None, do_not_restore_original_transform: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_slot: Initial value for TargetSlot.
            local_position_override: Initial value for LocalPositionOverride.
            local_rotation_override: Initial value for LocalRotationOverride.
            local_scale_override: Initial value for LocalScaleOverride.
            active_self_override: Initial value for ActiveSelfOverride.
            do_not_restore_original_transform: Initial value for DoNotRestoreOriginalTransform.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_slot is not None:
            self.target_slot = target_slot
        if local_position_override is not None:
            self.local_position_override = local_position_override
        if local_rotation_override is not None:
            self.local_rotation_override = local_rotation_override
        if local_scale_override is not None:
            self.local_scale_override = local_scale_override
        if active_self_override is not None:
            self.active_self_override = active_self_override
        if do_not_restore_original_transform is not None:
            self.do_not_restore_original_transform = do_not_restore_original_transform

    @property
    def target_slot(self) -> str | None:
        """The slot to parent and write values for during duplication."""
        member = self.get_member("TargetSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_slot.setter
    def target_slot(self, target: str | Slot | None) -> None:
        """Set the TargetSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TargetSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def local_position_override(self) -> primitives.Float3 | None:
        """The local position to apply to ``TargetSlot`` when parenting under this slot during duplication if this is not null."""
        member = self.get_member("LocalPositionOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_position_override.setter
    def local_position_override(self, value: primitives.Float3) -> None:
        """Set the LocalPositionOverride field value."""
        member = self.get_member("LocalPositionOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalPositionOverride", fields.FieldNullableFloat3(value=value)
            )

    @property
    def local_rotation_override(self) -> primitives.FloatQ | None:
        """The local rotation to apply to ``TargetSlot`` when parenting under this component's slot during duplication if this is not null."""
        member = self.get_member("LocalRotationOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_rotation_override.setter
    def local_rotation_override(self, value: primitives.FloatQ) -> None:
        """Set the LocalRotationOverride field value."""
        member = self.get_member("LocalRotationOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalRotationOverride", fields.FieldNullableFloatQ(value=value)
            )

    @property
    def local_scale_override(self) -> primitives.Float3 | None:
        """The local scale to apply to ``TargetSlot`` when parenting under this component's slot during duplication if this is not null."""
        member = self.get_member("LocalScaleOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_scale_override.setter
    def local_scale_override(self, value: primitives.Float3) -> None:
        """Set the LocalScaleOverride field value."""
        member = self.get_member("LocalScaleOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalScaleOverride", fields.FieldNullableFloat3(value=value)
            )

    @property
    def active_self_override(self) -> primitives.Bool | None:
        """The active state to apply to ``TargetSlot``'s active field when parenting under this component's slot during duplication if this is not null."""
        member = self.get_member("ActiveSelfOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_self_override.setter
    def active_self_override(self, value: primitives.Bool) -> None:
        """Set the ActiveSelfOverride field value."""
        member = self.get_member("ActiveSelfOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveSelfOverride", fields.FieldNullableBool(value=value)
            )

    @property
    def do_not_restore_original_transform(self) -> primitives.Bool | None:
        """Whether to parent the slot back where it came from after duplication, Undoing all overrides and setting all values back to their originals."""
        member = self.get_member("DoNotRestoreOriginalTransform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @do_not_restore_original_transform.setter
    def do_not_restore_original_transform(self, value: primitives.Bool) -> None:
        """Set the DoNotRestoreOriginalTransform field value."""
        member = self.get_member("DoNotRestoreOriginalTransform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoNotRestoreOriginalTransform", fields.FieldBool(value=value)
            )

