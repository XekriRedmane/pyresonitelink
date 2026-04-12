"""Generated component: CharacterController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.physics_scaling_mode import PhysicsScalingMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterController(GeneratedComponent, IBounded, IWorldEventReceiver):
    """This component is usually used internally by Resonite to simulate user movement physics like walking and climbing.

    Category: Physics

    This component is usually used internally by Resonite to simulate user
    movement physics like walking and climbing. But the component can also
    be manipulated to create "Fake Players" commonly known by Resonite users
    as "NPC's". Before doing this, know that the physics simulation is
    always inconsistent when viewed by different players in the same
    session. It also causes high amounts of networking and FPS lag. Use too
    many and you may start rising in Queued Packets. The character
    controller can also be used as a ball and simulates rolling, falling,
    collisions and momentum transfer, but for individual things that fly or
    bounce, using a Trajectory Position ProtoFlux node is vastly superior.
    This component is also used in certain types of vehicles and making them
    controllable by the user. This is done by having a vehicle you want to
    make controllable, then making an anchor for the user to sit in, then
    setting up this component to make that user become the simulating user,
    thus making their controls change in such a way where they are
    controlling a vehicle they are sitting on. The CharacterRoot slot input
    when null will do its transforms on the slot the CharacterController
    component is on, however when given a slot the component will instead
    make those transforms happen on the slot inputted. Combined with
    defining the HeadReference, you can control external slots without
    moving where the CharacterController component is and have them work
    with physical obstacles. For a quick example of this behavior, you can
    modify your current active locomotion's CharacterController on the
    CharacterRoot field to point towards another slot while defining the
    HeadReference to instead move the inputted slot while you stand still.
    This component can use sphere, box and other colliders that have volume
    in addition to the capsule collider. Note, due to the unique behavior of
    the HeadReference input defining where the CharacterController's
    collider is in the simulation, visualizing the collider via the
    inspector will not be correct.

    **Description**: The Character Controller component is primarily designed to be part of the Locomotion system and is what used for user movement and simulating physics relating to this.

It has many settings and values that can alter the way on how a user can control either their self or another slot (For example: Vehicles). These Settings allow you to control the mass, speed, force, etc. This flexibility also allows for uses far beyond it's original intended design.

Keep in mind that the character controller under the user root slot is currently useless (as in, not used besides it needing to be there) at this time. And removing it just recreates it back on the user root slot.

For this component, when using some features, you may need to either write/drive the field ``SimulatingUser``. This will activate the character controller on the slot and make it start simulating. Doing this also lets you use some nodes such as Is Character Controller and Is Character On Ground, and without a simulating user, the values from some nodes would not be updated.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CharacterController"

    def __init__(self, simulating_user: str | User | None = None, character_root: str | Slot | None = None, head_reference: str | Slot | None = None, simulate_rotation: primitives.Bool | None = None, mass_scaling: PhysicsScalingMode | str | None = None, force_scaling: PhysicsScalingMode | str | None = None, speed_scaling: PhysicsScalingMode | str | None = None, jump_scaling: PhysicsScalingMode | str | None = None, gravity_scaling: PhysicsScalingMode | str | None = None, linear_damping: primitives.Float | None = None, angular_damping: primitives.Float | None = None, margin: primitives.Float | None = None, step_up_height: primitives.Float | None = None, step_up_check_distance: primitives.Float | None = None, kill_vertical_velocity_after_step_up: primitives.Bool | None = None, edge_detection_depth: primitives.Float | None = None, speed: primitives.Float | None = None, sliding_speed: primitives.Float | None = None, air_speed: primitives.Float | None = None, traction_force: primitives.Float | None = None, sliding_force: primitives.Float | None = None, air_force: primitives.Float | None = None, maximum_glue_force: primitives.Float | None = None, maximum_traction_slope: primitives.Float | None = None, maximum_support_slope: primitives.Float | None = None, jump_speed: primitives.Float | None = None, sliding_jump_speed: primitives.Float | None = None, gravity: primitives.Float3 | None = None, debug_visual_duration: primitives.Float | None = None, height: primitives.Float | None = None, radius: primitives.Float | None = None, mass: primitives.Float | None = None, collide_with_other_characters: primitives.Bool | None = None, ignore_raycasts: primitives.Bool | None = None, root_at_bottom: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            simulating_user: Initial value for SimulatingUser.
            character_root: Initial value for CharacterRoot.
            head_reference: Initial value for HeadReference.
            simulate_rotation: Initial value for SimulateRotation.
            mass_scaling: Initial value for MassScaling.
            force_scaling: Initial value for ForceScaling.
            speed_scaling: Initial value for SpeedScaling.
            jump_scaling: Initial value for JumpScaling.
            gravity_scaling: Initial value for GravityScaling.
            linear_damping: Initial value for LinearDamping.
            angular_damping: Initial value for AngularDamping.
            margin: Initial value for Margin.
            step_up_height: Initial value for StepUpHeight.
            step_up_check_distance: Initial value for StepUpCheckDistance.
            kill_vertical_velocity_after_step_up: Initial value for KillVerticalVelocityAfterStepUp.
            edge_detection_depth: Initial value for EdgeDetectionDepth.
            speed: Initial value for Speed.
            sliding_speed: Initial value for SlidingSpeed.
            air_speed: Initial value for AirSpeed.
            traction_force: Initial value for TractionForce.
            sliding_force: Initial value for SlidingForce.
            air_force: Initial value for AirForce.
            maximum_glue_force: Initial value for MaximumGlueForce.
            maximum_traction_slope: Initial value for MaximumTractionSlope.
            maximum_support_slope: Initial value for MaximumSupportSlope.
            jump_speed: Initial value for JumpSpeed.
            sliding_jump_speed: Initial value for SlidingJumpSpeed.
            gravity: Initial value for Gravity.
            debug_visual_duration: Initial value for DebugVisualDuration.
            height: Initial value for __height.
            radius: Initial value for __radius.
            mass: Initial value for __mass.
            collide_with_other_characters: Initial value for __collideWithOtherCharacters.
            ignore_raycasts: Initial value for __ignoreRaycasts.
            root_at_bottom: Initial value for __rootAtBottom.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if simulating_user is not None:
            self.simulating_user = simulating_user
        if character_root is not None:
            self.character_root = character_root
        if head_reference is not None:
            self.head_reference = head_reference
        if simulate_rotation is not None:
            self.simulate_rotation = simulate_rotation
        if mass_scaling is not None:
            self.mass_scaling = mass_scaling
        if force_scaling is not None:
            self.force_scaling = force_scaling
        if speed_scaling is not None:
            self.speed_scaling = speed_scaling
        if jump_scaling is not None:
            self.jump_scaling = jump_scaling
        if gravity_scaling is not None:
            self.gravity_scaling = gravity_scaling
        if linear_damping is not None:
            self.linear_damping = linear_damping
        if angular_damping is not None:
            self.angular_damping = angular_damping
        if margin is not None:
            self.margin = margin
        if step_up_height is not None:
            self.step_up_height = step_up_height
        if step_up_check_distance is not None:
            self.step_up_check_distance = step_up_check_distance
        if kill_vertical_velocity_after_step_up is not None:
            self.kill_vertical_velocity_after_step_up = kill_vertical_velocity_after_step_up
        if edge_detection_depth is not None:
            self.edge_detection_depth = edge_detection_depth
        if speed is not None:
            self.speed = speed
        if sliding_speed is not None:
            self.sliding_speed = sliding_speed
        if air_speed is not None:
            self.air_speed = air_speed
        if traction_force is not None:
            self.traction_force = traction_force
        if sliding_force is not None:
            self.sliding_force = sliding_force
        if air_force is not None:
            self.air_force = air_force
        if maximum_glue_force is not None:
            self.maximum_glue_force = maximum_glue_force
        if maximum_traction_slope is not None:
            self.maximum_traction_slope = maximum_traction_slope
        if maximum_support_slope is not None:
            self.maximum_support_slope = maximum_support_slope
        if jump_speed is not None:
            self.jump_speed = jump_speed
        if sliding_jump_speed is not None:
            self.sliding_jump_speed = sliding_jump_speed
        if gravity is not None:
            self.gravity = gravity
        if debug_visual_duration is not None:
            self.debug_visual_duration = debug_visual_duration
        if height is not None:
            self.height = height
        if radius is not None:
            self.radius = radius
        if mass is not None:
            self.mass = mass
        if collide_with_other_characters is not None:
            self.collide_with_other_characters = collide_with_other_characters
        if ignore_raycasts is not None:
            self.ignore_raycasts = ignore_raycasts
        if root_at_bottom is not None:
            self.root_at_bottom = root_at_bottom

    @property
    def simulating_user(self) -> str | None:
        """The user who is currently simulating and networking this Character Controller."""
        member = self.get_member("SimulatingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @simulating_user.setter
    def simulating_user(self, target: str | User | None) -> None:
        """Set the SimulatingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("SimulatingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SimulatingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def character_root(self) -> str | None:
        """The slot to simulate, can be any inputted slot."""
        member = self.get_member("CharacterRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @character_root.setter
    def character_root(self, target: str | Slot | None) -> None:
        """Set the CharacterRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("CharacterRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CharacterRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def head_reference(self) -> str | None:
        """Dictates where to simulate the collider and based on the slot's forward direction, will decide what a "forward" movement is based on your joystick/input. SimulateRotation Bool Allow the object simulated by this object to rotate, essentially making it a rigid body. See warning."""
        member = self.get_member("HeadReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head_reference.setter
    def head_reference(self, target: str | Slot | None) -> None:
        """Set the HeadReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("HeadReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HeadReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def simulate_rotation(self) -> primitives.Bool | None:
        """The SimulateRotation field value."""
        member = self.get_member("SimulateRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simulate_rotation.setter
    def simulate_rotation(self, value: primitives.Bool) -> None:
        """Set the SimulateRotation field value."""
        member = self.get_member("SimulateRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimulateRotation", fields.FieldBool(value=value)
            )

    @property
    def mass_scaling(self) -> PhysicsScalingMode | None:
        """How to scale the mass based on this component's slot scale."""
        member = self.get_member("MassScaling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhysicsScalingMode(member.value)
        return None

    @mass_scaling.setter
    def mass_scaling(self, value: PhysicsScalingMode | str) -> None:
        """Set MassScaling. How to scale the mass based on this component's slot scale."""
        member = self.get_member("MassScaling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MassScaling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def force_scaling(self) -> PhysicsScalingMode | None:
        """How to scale the force based on this component's slot scale."""
        member = self.get_member("ForceScaling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhysicsScalingMode(member.value)
        return None

    @force_scaling.setter
    def force_scaling(self, value: PhysicsScalingMode | str) -> None:
        """Set ForceScaling. How to scale the force based on this component's slot scale."""
        member = self.get_member("ForceScaling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ForceScaling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def speed_scaling(self) -> PhysicsScalingMode | None:
        """How to scale the speed based on this component's slot scale."""
        member = self.get_member("SpeedScaling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhysicsScalingMode(member.value)
        return None

    @speed_scaling.setter
    def speed_scaling(self, value: PhysicsScalingMode | str) -> None:
        """Set SpeedScaling. How to scale the speed based on this component's slot scale."""
        member = self.get_member("SpeedScaling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SpeedScaling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def jump_scaling(self) -> PhysicsScalingMode | None:
        """How to scale the jump force based on this component's slot scale."""
        member = self.get_member("JumpScaling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhysicsScalingMode(member.value)
        return None

    @jump_scaling.setter
    def jump_scaling(self, value: PhysicsScalingMode | str) -> None:
        """Set JumpScaling. How to scale the jump force based on this component's slot scale."""
        member = self.get_member("JumpScaling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "JumpScaling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def gravity_scaling(self) -> PhysicsScalingMode | None:
        """How to scale the gravity effect based on this component's slot scale."""
        member = self.get_member("GravityScaling")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhysicsScalingMode(member.value)
        return None

    @gravity_scaling.setter
    def gravity_scaling(self, value: PhysicsScalingMode | str) -> None:
        """Set GravityScaling. How to scale the gravity effect based on this component's slot scale."""
        member = self.get_member("GravityScaling")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "GravityScaling",
                members.FieldEnum(value=str(value)),
            )

    @property
    def linear_damping(self) -> primitives.Float | None:
        """how fast the character controller slows down when no other forces are being applied to it"""
        member = self.get_member("LinearDamping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @linear_damping.setter
    def linear_damping(self, value: primitives.Float) -> None:
        """Set the LinearDamping field value."""
        member = self.get_member("LinearDamping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LinearDamping", fields.FieldFloat(value=value)
            )

    @property
    def angular_damping(self) -> primitives.Float | None:
        """how fast thus character slows down its rotation when no other forces are being applied to it."""
        member = self.get_member("AngularDamping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angular_damping.setter
    def angular_damping(self, value: primitives.Float) -> None:
        """Set the AngularDamping field value."""
        member = self.get_member("AngularDamping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngularDamping", fields.FieldFloat(value=value)
            )

    @property
    def margin(self) -> primitives.Float | None:
        """Unused."""
        member = self.get_member("Margin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @margin.setter
    def margin(self, value: primitives.Float) -> None:
        """Set the Margin field value."""
        member = self.get_member("Margin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Margin", fields.FieldFloat(value=value)
            )

    @property
    def step_up_height(self) -> primitives.Float | None:
        """How big of a ledge the character controller can step up"""
        member = self.get_member("StepUpHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @step_up_height.setter
    def step_up_height(self, value: primitives.Float) -> None:
        """Set the StepUpHeight field value."""
        member = self.get_member("StepUpHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StepUpHeight", fields.FieldFloat(value=value)
            )

    @property
    def step_up_check_distance(self) -> primitives.Float | None:
        """determines the distance the shape is swept in the movement direction to determine if it's free of other obstacles"""
        member = self.get_member("StepUpCheckDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @step_up_check_distance.setter
    def step_up_check_distance(self, value: primitives.Float) -> None:
        """Set the StepUpCheckDistance field value."""
        member = self.get_member("StepUpCheckDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StepUpCheckDistance", fields.FieldFloat(value=value)
            )

    @property
    def kill_vertical_velocity_after_step_up(self) -> primitives.Bool | None:
        """will convert any vertical velocity into directional one in the current planar direction of the movement and push the player back down, preventing the player from getting too much air when running off a ramp or stairs."""
        member = self.get_member("KillVerticalVelocityAfterStepUp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @kill_vertical_velocity_after_step_up.setter
    def kill_vertical_velocity_after_step_up(self, value: primitives.Bool) -> None:
        """Set the KillVerticalVelocityAfterStepUp field value."""
        member = self.get_member("KillVerticalVelocityAfterStepUp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KillVerticalVelocityAfterStepUp", fields.FieldBool(value=value)
            )

    @property
    def edge_detection_depth(self) -> primitives.Float | None:
        """the smallest size an edge can be that the character can stand on while against a wall"""
        member = self.get_member("EdgeDetectionDepth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edge_detection_depth.setter
    def edge_detection_depth(self, value: primitives.Float) -> None:
        """Set the EdgeDetectionDepth field value."""
        member = self.get_member("EdgeDetectionDepth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EdgeDetectionDepth", fields.FieldFloat(value=value)
            )

    @property
    def speed(self) -> primitives.Float | None:
        """How fast this character controller can move."""
        member = self.get_member("Speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: primitives.Float) -> None:
        """Set the Speed field value."""
        member = self.get_member("Speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Speed", fields.FieldFloat(value=value)
            )

    @property
    def sliding_speed(self) -> primitives.Float | None:
        """how fast the character controller moves when sliding down a slope"""
        member = self.get_member("SlidingSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sliding_speed.setter
    def sliding_speed(self, value: primitives.Float) -> None:
        """Set the SlidingSpeed field value."""
        member = self.get_member("SlidingSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlidingSpeed", fields.FieldFloat(value=value)
            )

    @property
    def air_speed(self) -> primitives.Float | None:
        """how fast the character moves in the air"""
        member = self.get_member("AirSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @air_speed.setter
    def air_speed(self, value: primitives.Float) -> None:
        """Set the AirSpeed field value."""
        member = self.get_member("AirSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AirSpeed", fields.FieldFloat(value=value)
            )

    @property
    def traction_force(self) -> primitives.Float | None:
        """How much force is needed to overcome standing friction."""
        member = self.get_member("TractionForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @traction_force.setter
    def traction_force(self, value: primitives.Float) -> None:
        """Set the TractionForce field value."""
        member = self.get_member("TractionForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TractionForce", fields.FieldFloat(value=value)
            )

    @property
    def sliding_force(self) -> primitives.Float | None:
        """How much force is needed to stay moving"""
        member = self.get_member("SlidingForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sliding_force.setter
    def sliding_force(self, value: primitives.Float) -> None:
        """Set the SlidingForce field value."""
        member = self.get_member("SlidingForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlidingForce", fields.FieldFloat(value=value)
            )

    @property
    def air_force(self) -> primitives.Float | None:
        """the force needed to move in the air"""
        member = self.get_member("AirForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @air_force.setter
    def air_force(self, value: primitives.Float) -> None:
        """Set the AirForce field value."""
        member = self.get_member("AirForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AirForce", fields.FieldFloat(value=value)
            )

    @property
    def maximum_glue_force(self) -> primitives.Float | None:
        """Reduces the velocity of breaking contact from a surface vertically be under this speed. This is useful for simulating sticky surfaces, where the user cannot jump as high."""
        member = self.get_member("MaximumGlueForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_glue_force.setter
    def maximum_glue_force(self, value: primitives.Float) -> None:
        """Set the MaximumGlueForce field value."""
        member = self.get_member("MaximumGlueForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumGlueForce", fields.FieldFloat(value=value)
            )

    @property
    def maximum_traction_slope(self) -> primitives.Float | None:
        """Maximum Traction angle (degrees) before user slides down a slope, even if they are actively trying to walk up it."""
        member = self.get_member("MaximumTractionSlope")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_traction_slope.setter
    def maximum_traction_slope(self, value: primitives.Float) -> None:
        """Set the MaximumTractionSlope field value."""
        member = self.get_member("MaximumTractionSlope")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumTractionSlope", fields.FieldFloat(value=value)
            )

    @property
    def maximum_support_slope(self) -> primitives.Float | None:
        """Maximum Support angle (degrees) before user slides down a slope, when not working against the slope."""
        member = self.get_member("MaximumSupportSlope")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_support_slope.setter
    def maximum_support_slope(self, value: primitives.Float) -> None:
        """Set the MaximumSupportSlope field value."""
        member = self.get_member("MaximumSupportSlope")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumSupportSlope", fields.FieldFloat(value=value)
            )

    @property
    def jump_speed(self) -> primitives.Float | None:
        """The speed of the velocity applied when jumping on a slope with an angle less than or equal to ``MaximumTractionSlope``."""
        member = self.get_member("JumpSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @jump_speed.setter
    def jump_speed(self, value: primitives.Float) -> None:
        """Set the JumpSpeed field value."""
        member = self.get_member("JumpSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "JumpSpeed", fields.FieldFloat(value=value)
            )

    @property
    def sliding_jump_speed(self) -> primitives.Float | None:
        """The speed of the velocity applied when jumping on a slope with an angle greater than ``MaximuSupportSlope``."""
        member = self.get_member("SlidingJumpSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sliding_jump_speed.setter
    def sliding_jump_speed(self, value: primitives.Float) -> None:
        """Set the SlidingJumpSpeed field value."""
        member = self.get_member("SlidingJumpSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlidingJumpSpeed", fields.FieldFloat(value=value)
            )

    @property
    def gravity(self) -> primitives.Float3 | None:
        """Force of Gravity for this character controller"""
        member = self.get_member("Gravity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gravity.setter
    def gravity(self, value: primitives.Float3) -> None:
        """Set the Gravity field value."""
        member = self.get_member("Gravity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gravity", fields.FieldFloat3(value=value)
            )

    @property
    def gravity_space(self) -> members.SyncObject | None:
        """The coordinate space in which ``Gravity`` is applied in. applying gravity to world space using this field, can allow a user to stay upright despite a floor they're parented under is being rotated. which generates interesting effects."""
        member = self.get_member("GravitySpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @gravity_space.setter
    def gravity_space(self, value: members.SyncObject) -> None:
        """Set GravitySpace. The coordinate space in which ``Gravity`` is applied in. applying gravity to world space using this field, can allow a user to stay upright despite a floor they're parented under is being rotated. which generates interesting effects."""
        self.set_member("GravitySpace", value)

    @property
    def debug_visual_duration(self) -> primitives.Float | None:
        """Allows for the component to visualize the force vectors acting on the character simulator if set above 0."""
        member = self.get_member("DebugVisualDuration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_visual_duration.setter
    def debug_visual_duration(self, value: primitives.Float) -> None:
        """Set the DebugVisualDuration field value."""
        member = self.get_member("DebugVisualDuration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DebugVisualDuration", fields.FieldNullableFloat(value=value)
            )

    @property
    def height(self) -> primitives.Float | None:
        """Height of the driven CapsuleCollider (Component) Currently does nothing."""
        member = self.get_member("__height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the __height field value."""
        member = self.get_member("__height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__height", fields.FieldFloat(value=value)
            )

    @property
    def radius(self) -> primitives.Float | None:
        """Radius of the driven CapsuleCollider (Component) Currently does nothing."""
        member = self.get_member("__radius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @radius.setter
    def radius(self, value: primitives.Float) -> None:
        """Set the __radius field value."""
        member = self.get_member("__radius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__radius", fields.FieldFloat(value=value)
            )

    @property
    def mass(self) -> primitives.Float | None:
        """Mass of the of the driven CapsuleCollider (Component) Currently does nothing."""
        member = self.get_member("__mass")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mass.setter
    def mass(self, value: primitives.Float) -> None:
        """Set the __mass field value."""
        member = self.get_member("__mass")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__mass", fields.FieldFloat(value=value)
            )

    @property
    def collide_with_other_characters(self) -> primitives.Bool | None:
        """Currently does nothing."""
        member = self.get_member("__collideWithOtherCharacters")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_other_characters.setter
    def collide_with_other_characters(self, value: primitives.Bool) -> None:
        """Set the __collideWithOtherCharacters field value."""
        member = self.get_member("__collideWithOtherCharacters")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__collideWithOtherCharacters", fields.FieldBool(value=value)
            )

    @property
    def ignore_raycasts(self) -> primitives.Bool | None:
        """Currently does nothing."""
        member = self.get_member("__ignoreRaycasts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_raycasts.setter
    def ignore_raycasts(self, value: primitives.Bool) -> None:
        """Set the __ignoreRaycasts field value."""
        member = self.get_member("__ignoreRaycasts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__ignoreRaycasts", fields.FieldBool(value=value)
            )

    @property
    def root_at_bottom(self) -> primitives.Bool | None:
        """Currently does nothing."""
        member = self.get_member("__rootAtBottom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @root_at_bottom.setter
    def root_at_bottom(self, value: primitives.Bool) -> None:
        """Set the __rootAtBottom field value."""
        member = self.get_member("__rootAtBottom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__rootAtBottom", fields.FieldBool(value=value)
            )

