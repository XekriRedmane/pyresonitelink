"""Generated component: ExternalSlotSaver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iitem_permissions import IItemPermissions
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ExternalSlotSaver(GeneratedComponent, IItemPermissions, IWorldEventReceiver):
    """The ExternalSlotSaver will ensure that the ``TargetSlot`` is saved as a child of the slot this component is on if the slot isn't already in the hierarchy.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ExternalSlotSaver"

    def __init__(self, target_slot: str | Slot | None = None, save_active_self_override: primitives.Bool | None = None, save_local_position_override: primitives.Float3 | None = None, save_local_rotation_override: primitives.FloatQ | None = None, save_local_scale_override: primitives.Float3 | None = None, ignore_when_non_persistent_self: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_slot: Initial value for TargetSlot.
            save_active_self_override: Initial value for SaveActiveSelfOverride.
            save_local_position_override: Initial value for SaveLocalPositionOverride.
            save_local_rotation_override: Initial value for SaveLocalRotationOverride.
            save_local_scale_override: Initial value for SaveLocalScaleOverride.
            ignore_when_non_persistent_self: Initial value for IgnoreWhenNonPersistentSelf.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_slot is not None:
            self.target_slot = target_slot
        if save_active_self_override is not None:
            self.save_active_self_override = save_active_self_override
        if save_local_position_override is not None:
            self.save_local_position_override = save_local_position_override
        if save_local_rotation_override is not None:
            self.save_local_rotation_override = save_local_rotation_override
        if save_local_scale_override is not None:
            self.save_local_scale_override = save_local_scale_override
        if ignore_when_non_persistent_self is not None:
            self.ignore_when_non_persistent_self = ignore_when_non_persistent_self

    @property
    def target_slot(self) -> str | None:
        """The slot to target when saving."""
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
    def save_active_self_override(self) -> primitives.Bool | None:
        """When not null, save this rather than ``TargetSlot``'s current active self value."""
        member = self.get_member("SaveActiveSelfOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @save_active_self_override.setter
    def save_active_self_override(self, value: primitives.Bool) -> None:
        """Set the SaveActiveSelfOverride field value."""
        member = self.get_member("SaveActiveSelfOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaveActiveSelfOverride", fields.FieldNullableBool(value=value)
            )

    @property
    def save_local_position_override(self) -> primitives.Float3 | None:
        """When not null, save this rather than ``TargetSlot``'s current position value."""
        member = self.get_member("SaveLocalPositionOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @save_local_position_override.setter
    def save_local_position_override(self, value: primitives.Float3) -> None:
        """Set the SaveLocalPositionOverride field value."""
        member = self.get_member("SaveLocalPositionOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaveLocalPositionOverride", fields.FieldNullableFloat3(value=value)
            )

    @property
    def save_local_rotation_override(self) -> primitives.FloatQ | None:
        """When not null, save this rather than ``TargetSlot``'s current rotation value."""
        member = self.get_member("SaveLocalRotationOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @save_local_rotation_override.setter
    def save_local_rotation_override(self, value: primitives.FloatQ) -> None:
        """Set the SaveLocalRotationOverride field value."""
        member = self.get_member("SaveLocalRotationOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaveLocalRotationOverride", fields.FieldNullableFloatQ(value=value)
            )

    @property
    def save_local_scale_override(self) -> primitives.Float3 | None:
        """When not null, save this rather than ``TargetSlot``'s current scale value."""
        member = self.get_member("SaveLocalScaleOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @save_local_scale_override.setter
    def save_local_scale_override(self, value: primitives.Float3) -> None:
        """Set the SaveLocalScaleOverride field value."""
        member = self.get_member("SaveLocalScaleOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaveLocalScaleOverride", fields.FieldNullableFloat3(value=value)
            )

    @property
    def ignore_when_non_persistent_self(self) -> primitives.Bool | None:
        """Whether to not save the external slot if we are non persistent ourselves."""
        member = self.get_member("IgnoreWhenNonPersistentSelf")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_when_non_persistent_self.setter
    def ignore_when_non_persistent_self(self, value: primitives.Bool) -> None:
        """Set the IgnoreWhenNonPersistentSelf field value."""
        member = self.get_member("IgnoreWhenNonPersistentSelf")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreWhenNonPersistentSelf", fields.FieldBool(value=value)
            )

