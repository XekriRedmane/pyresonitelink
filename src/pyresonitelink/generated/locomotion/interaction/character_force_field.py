"""Generated component: CharacterForceField."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.generated._enums.space import Space
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterForceField(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This component creates a force field that allows the setting of or applying force to the velocity of Character Controllers.

    Category: Locomotion/Interaction

    **Behavior**: Needs a collider on the same hierarchy to allow triggering this component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterForceField"

    def __init__(self, triggers_only: primitives.Bool | None = None, force: primitives.Float3 | None = None, force_mode: Mode | str | None = None, force_space: Space | str | None = None, radial_force_radius: primitives.Float | None = None, min_activation_velocity: primitives.Float | None = None, max_force_velocity: primitives.Float | None = None, hold_jump_max_force_velocity: primitives.Float | None = None, preseve_direction_across_plane: primitives.Bool | None = None, ignore_parent_user: primitives.Bool | None = None, no_jump_multiplier: primitives.Float | None = None, hold_jump_multiplier: primitives.Float | None = None, max_character_velocity: primitives.Float | None = None, min_character_velocity: primitives.Float | None = None, character_velocity_dampening_speed: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            triggers_only: Initial value for TriggersOnly.
            force: Initial value for Force.
            force_mode: Initial value for ForceMode.
            force_space: Initial value for ForceSpace.
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
        if force_mode is not None:
            self.force_mode = force_mode
        if force_space is not None:
            self.force_space = force_space
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
    def triggers_only(self) -> primitives.Bool | None:
        """Whether to only allow trigger colliders attached to character controller objects to activate the force field."""
        member = self.get_member("TriggersOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @triggers_only.setter
    def triggers_only(self, value: primitives.Bool) -> None:
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
        """force direction and magnitude to apply a character controller within range with."""
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
    def force_mode(self) -> Mode | None:
        """Whether to use impulse, apply, or set velocity using ``Force``"""
        member = self.get_member("ForceMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @force_mode.setter
    def force_mode(self, value: Mode | str) -> None:
        """Set ForceMode. Whether to use impulse, apply, or set velocity using ``Force``"""
        member = self.get_member("ForceMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ForceMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def force_space(self) -> Space | None:
        """Whether to do the force direction in local or global space (so should ``Force`` be scaled and rotated by the slot this is on or not?)"""
        member = self.get_member("ForceSpace")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Space(member.value)
        return None

    @force_space.setter
    def force_space(self, value: Space | str) -> None:
        """Set ForceSpace. Whether to do the force direction in local or global space (so should ``Force`` be scaled and rotated by the slot this is on or not?)"""
        member = self.get_member("ForceSpace")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ForceSpace",
                members.FieldEnum(value=str(value)),
            )

    @property
    def radial_force_radius(self) -> primitives.Float | None:
        """The range of effect this force field has."""
        member = self.get_member("RadialForceRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radial_force_radius.setter
    def radial_force_radius(self, value: primitives.Float) -> None:
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
        """Override the transform space for ``Force`` with this if set."""
        member = self.get_member("ForceSlotSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @force_slot_space.setter
    def force_slot_space(self, value: members.SyncObject) -> None:
        """Set ForceSlotSpace. Override the transform space for ``Force`` with this if set."""
        self.set_member("ForceSlotSpace", value)

    @property
    def min_activation_velocity(self) -> primitives.Float | None:
        """The minimum velocity a character controller has to be going to trigger this force field."""
        member = self.get_member("MinActivationVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_activation_velocity.setter
    def min_activation_velocity(self, value: primitives.Float) -> None:
        """Set the MinActivationVelocity field value."""
        member = self.get_member("MinActivationVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinActivationVelocity", fields.FieldFloat(value=value)
            )

    @property
    def max_force_velocity(self) -> primitives.Float | None:
        """How fast the character controller's velocity can be at max after being affected by this component when the user isn't holding Jump"""
        member = self.get_member("MaxForceVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_force_velocity.setter
    def max_force_velocity(self, value: primitives.Float) -> None:
        """Set the MaxForceVelocity field value."""
        member = self.get_member("MaxForceVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxForceVelocity", fields.FieldFloat(value=value)
            )

    @property
    def hold_jump_max_force_velocity(self) -> primitives.Float | None:
        """How fast the character controller's velocity can be at max after being affected by this component when the user is holding Jump"""
        member = self.get_member("HoldJumpMaxForceVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_jump_max_force_velocity.setter
    def hold_jump_max_force_velocity(self, value: primitives.Float) -> None:
        """Set the HoldJumpMaxForceVelocity field value."""
        member = self.get_member("HoldJumpMaxForceVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldJumpMaxForceVelocity", fields.FieldFloat(value=value)
            )

    @property
    def preseve_direction_across_plane(self) -> primitives.Bool | None:
        """Calculates a plane that is perpendicular to the vector ``Force`` (like a stick stuck into a piece of paper) and maintains the initial direction of the velocity of the character controller in either the forward or backwards facing direction of this plane."""
        member = self.get_member("PreseveDirectionAcrossPlane")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preseve_direction_across_plane.setter
    def preseve_direction_across_plane(self, value: primitives.Bool) -> None:
        """Set the PreseveDirectionAcrossPlane field value."""
        member = self.get_member("PreseveDirectionAcrossPlane")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreseveDirectionAcrossPlane", fields.FieldBool(value=value)
            )

    @property
    def ignore_parent_user(self) -> primitives.Bool | None:
        """Whether to ignore the active user when finding character controllers within range of ``RadialForceRadius``. This does not ignore character controllers that are simulated by the user."""
        member = self.get_member("IgnoreParentUser")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_parent_user.setter
    def ignore_parent_user(self, value: primitives.Bool) -> None:
        """Set the IgnoreParentUser field value."""
        member = self.get_member("IgnoreParentUser")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreParentUser", fields.FieldBool(value=value)
            )

    @property
    def no_jump_multiplier(self) -> primitives.Float | None:
        """How much to multiply the effect of ``Force`` when the user isn't holding Jump"""
        member = self.get_member("NoJumpMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @no_jump_multiplier.setter
    def no_jump_multiplier(self, value: primitives.Float) -> None:
        """Set the NoJumpMultiplier field value."""
        member = self.get_member("NoJumpMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoJumpMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def hold_jump_multiplier(self) -> primitives.Float | None:
        """How much to multiply the effect of ``Force`` when the user is holding Jump"""
        member = self.get_member("HoldJumpMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_jump_multiplier.setter
    def hold_jump_multiplier(self, value: primitives.Float) -> None:
        """Set the HoldJumpMultiplier field value."""
        member = self.get_member("HoldJumpMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldJumpMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def max_character_velocity(self) -> primitives.Float | None:
        """The maximum velocity this component can set a character controller's speed to after setting a force on it."""
        member = self.get_member("MaxCharacterVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_character_velocity.setter
    def max_character_velocity(self, value: primitives.Float) -> None:
        """Set the MaxCharacterVelocity field value."""
        member = self.get_member("MaxCharacterVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxCharacterVelocity", fields.FieldFloat(value=value)
            )

    @property
    def min_character_velocity(self) -> primitives.Float | None:
        """The minimum velocity this component can set a character controller's speed to after setting a force on it."""
        member = self.get_member("MinCharacterVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_character_velocity.setter
    def min_character_velocity(self, value: primitives.Float) -> None:
        """Set the MinCharacterVelocity field value."""
        member = self.get_member("MinCharacterVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinCharacterVelocity", fields.FieldFloat(value=value)
            )

    @property
    def character_velocity_dampening_speed(self) -> primitives.Float | None:
        """How fast to slow the user down. this can be used to give the effect of jumping into molasses."""
        member = self.get_member("CharacterVelocityDampeningSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @character_velocity_dampening_speed.setter
    def character_velocity_dampening_speed(self, value: primitives.Float) -> None:
        """Set the CharacterVelocityDampeningSpeed field value."""
        member = self.get_member("CharacterVelocityDampeningSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CharacterVelocityDampeningSpeed", fields.FieldFloat(value=value)
            )

