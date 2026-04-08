"""Generated component: CharacterForceField."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterForceField(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CharacterForceField.

    Category: Locomotion/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterForceField"

    def __init__(self, triggers_only: bool | None = None, force: primitives.Float3 | None = None, radial_force_radius: np.float32 | None = None, min_activation_velocity: np.float32 | None = None, max_force_velocity: np.float32 | None = None, hold_jump_max_force_velocity: np.float32 | None = None, preseve_direction_across_plane: bool | None = None, ignore_parent_user: bool | None = None, no_jump_multiplier: np.float32 | None = None, hold_jump_multiplier: np.float32 | None = None, max_character_velocity: np.float32 | None = None, min_character_velocity: np.float32 | None = None, character_velocity_dampening_speed: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            force: Initial value for Force.
            radial_force_radius: Initial value for RadialForceRadius.
            min_activation_velocity: Initial value for MinActivationVelocity.
            max_force_velocity: Initial value for MaxForceVelocity.
            hold_jump_max_force_velocity: Initial value for HoldJumpMaxForceVelocity.
            preseve_direction_across_plane: Initial value for PreseveDirectionAcrossPlane.
            ignore_parent_user: Initial value for IgnoreParentUser.
            no_jump_multiplier: Initial value for NoJumpMultiplier.
            hold_jump_multiplier: Initial value for HoldJumpMultiplier.
            max_character_velocity: Initial value for MaxCharacterVelocity.
            min_character_velocity: Initial value for MinCharacterVelocity.
            character_velocity_dampening_speed: Initial value for CharacterVelocityDampeningSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if triggers_only is not None:
            self.triggers_only = triggers_only
        if force is not None:
            self.force = force
        if radial_force_radius is not None:
            self.radial_force_radius = radial_force_radius
        if min_activation_velocity is not None:
            self.min_activation_velocity = min_activation_velocity
        if max_force_velocity is not None:
            self.max_force_velocity = max_force_velocity
        if hold_jump_max_force_velocity is not None:
            self.hold_jump_max_force_velocity = hold_jump_max_force_velocity
        if preseve_direction_across_plane is not None:
            self.preseve_direction_across_plane = preseve_direction_across_plane
        if ignore_parent_user is not None:
            self.ignore_parent_user = ignore_parent_user
        if no_jump_multiplier is not None:
            self.no_jump_multiplier = no_jump_multiplier
        if hold_jump_multiplier is not None:
            self.hold_jump_multiplier = hold_jump_multiplier
        if max_character_velocity is not None:
            self.max_character_velocity = max_character_velocity
        if min_character_velocity is not None:
            self.min_character_velocity = min_character_velocity
        if character_velocity_dampening_speed is not None:
            self.character_velocity_dampening_speed = character_velocity_dampening_speed

    @property
    def triggers_only(self) -> bool | None:
        """The TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triggers_only.setter
    def triggers_only(self, value: bool) -> None:
        """Set the TriggersOnly field value."""
        member = self.get_member("TriggersOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TriggersOnly", fields.FieldBool(value=value)
            )

    @property
    def force(self) -> primitives.Float3 | None:
        """The Force field value."""
        member = self.get_member("Force")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force.setter
    def force(self, value: primitives.Float3) -> None:
        """Set the Force field value."""
        member = self.get_member("Force")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Force", fields.FieldFloat3(value=value)
            )

    @property
    def force_mode(self) -> members.FieldEnum | None:
        """The ForceMode member."""
        member = self.get_member("ForceMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @force_mode.setter
    def force_mode(self, value: members.FieldEnum) -> None:
        """Set the ForceMode member."""
        self.set_member("ForceMode", value)

    @property
    def force_space(self) -> members.FieldEnum | None:
        """The ForceSpace member."""
        member = self.get_member("ForceSpace")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @force_space.setter
    def force_space(self, value: members.FieldEnum) -> None:
        """Set the ForceSpace member."""
        self.set_member("ForceSpace", value)

    @property
    def radial_force_radius(self) -> np.float32 | None:
        """The RadialForceRadius field value."""
        member = self.get_member("RadialForceRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radial_force_radius.setter
    def radial_force_radius(self, value: np.float32) -> None:
        """Set the RadialForceRadius field value."""
        member = self.get_member("RadialForceRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RadialForceRadius", fields.FieldFloat(value=value)
            )

    @property
    def force_slot_space(self) -> members.SyncObject | None:
        """The ForceSlotSpace member."""
        member = self.get_member("ForceSlotSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @force_slot_space.setter
    def force_slot_space(self, value: members.SyncObject) -> None:
        """Set the ForceSlotSpace member."""
        self.set_member("ForceSlotSpace", value)

    @property
    def min_activation_velocity(self) -> np.float32 | None:
        """The MinActivationVelocity field value."""
        member = self.get_member("MinActivationVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_activation_velocity.setter
    def min_activation_velocity(self, value: np.float32) -> None:
        """Set the MinActivationVelocity field value."""
        member = self.get_member("MinActivationVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinActivationVelocity", fields.FieldFloat(value=value)
            )

    @property
    def max_force_velocity(self) -> np.float32 | None:
        """The MaxForceVelocity field value."""
        member = self.get_member("MaxForceVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_force_velocity.setter
    def max_force_velocity(self, value: np.float32) -> None:
        """Set the MaxForceVelocity field value."""
        member = self.get_member("MaxForceVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxForceVelocity", fields.FieldFloat(value=value)
            )

    @property
    def hold_jump_max_force_velocity(self) -> np.float32 | None:
        """The HoldJumpMaxForceVelocity field value."""
        member = self.get_member("HoldJumpMaxForceVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_jump_max_force_velocity.setter
    def hold_jump_max_force_velocity(self, value: np.float32) -> None:
        """Set the HoldJumpMaxForceVelocity field value."""
        member = self.get_member("HoldJumpMaxForceVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldJumpMaxForceVelocity", fields.FieldFloat(value=value)
            )

    @property
    def preseve_direction_across_plane(self) -> bool | None:
        """The PreseveDirectionAcrossPlane field value."""
        member = self.get_member("PreseveDirectionAcrossPlane")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preseve_direction_across_plane.setter
    def preseve_direction_across_plane(self, value: bool) -> None:
        """Set the PreseveDirectionAcrossPlane field value."""
        member = self.get_member("PreseveDirectionAcrossPlane")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreseveDirectionAcrossPlane", fields.FieldBool(value=value)
            )

    @property
    def ignore_parent_user(self) -> bool | None:
        """The IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_parent_user.setter
    def ignore_parent_user(self, value: bool) -> None:
        """Set the IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreParentUser", fields.FieldBool(value=value)
            )

    @property
    def no_jump_multiplier(self) -> np.float32 | None:
        """The NoJumpMultiplier field value."""
        member = self.get_member("NoJumpMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @no_jump_multiplier.setter
    def no_jump_multiplier(self, value: np.float32) -> None:
        """Set the NoJumpMultiplier field value."""
        member = self.get_member("NoJumpMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoJumpMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def hold_jump_multiplier(self) -> np.float32 | None:
        """The HoldJumpMultiplier field value."""
        member = self.get_member("HoldJumpMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_jump_multiplier.setter
    def hold_jump_multiplier(self, value: np.float32) -> None:
        """Set the HoldJumpMultiplier field value."""
        member = self.get_member("HoldJumpMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldJumpMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def max_character_velocity(self) -> np.float32 | None:
        """The MaxCharacterVelocity field value."""
        member = self.get_member("MaxCharacterVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_character_velocity.setter
    def max_character_velocity(self, value: np.float32) -> None:
        """Set the MaxCharacterVelocity field value."""
        member = self.get_member("MaxCharacterVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxCharacterVelocity", fields.FieldFloat(value=value)
            )

    @property
    def min_character_velocity(self) -> np.float32 | None:
        """The MinCharacterVelocity field value."""
        member = self.get_member("MinCharacterVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_character_velocity.setter
    def min_character_velocity(self, value: np.float32) -> None:
        """Set the MinCharacterVelocity field value."""
        member = self.get_member("MinCharacterVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinCharacterVelocity", fields.FieldFloat(value=value)
            )

    @property
    def character_velocity_dampening_speed(self) -> np.float32 | None:
        """The CharacterVelocityDampeningSpeed field value."""
        member = self.get_member("CharacterVelocityDampeningSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @character_velocity_dampening_speed.setter
    def character_velocity_dampening_speed(self, value: np.float32) -> None:
        """Set the CharacterVelocityDampeningSpeed field value."""
        member = self.get_member("CharacterVelocityDampeningSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CharacterVelocityDampeningSpeed", fields.FieldFloat(value=value)
            )

