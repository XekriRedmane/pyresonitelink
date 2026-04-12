"""Generated component: DynamicBoneChain."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.vibrate_preset import VibratePreset
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.idestroy_block import IDestroyBlock
from pyresonitelink.generated._types.iduplicate_block import IDuplicateBlock
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicBoneChain(GeneratedComponent, ICustomInspector, IGrabbable, IDestroyBlock, IDuplicateBlock, IWorldEventReceiver):
    """Dynamic Bone Chain is a component that allows you to add rigidbody physics to the bones of a rigged model or avatar. Bones with rigid body physics are called dynamic bones.

For examples on how to set up Dynamic Bones, including and troubleshooting, see: Usage

The Dynamic Bone Chain component contains various properties for adjusting the physical behavior of the bone chain. The most important properties in the component are Inertia, InertiaForce, Damping, Elasticity, and Stiffness. The descriptions of each are listed below.

    Category: Physics/Dynamic Bones

    To add dynamic bones to a model, navigate through the model's armature
    in the Inspector until you locate the bone you want to use as the "root"
    or "master" bone. Then, attach the Dynamic Bone Chain component, and
    click Setup From Children. This will add the root bone and all its
    children to the dynamic bone chain. Tips/Problems: * Chain is not
    grabbable. ** Make sure the "Collide" and "DynamicPlayerCollision" bools
    are set on bones. * You can use the ProtoFlux Grabbable to detect
    someone grabbing the chain. * Make tails sway with the Wobbler3D
    component.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBoneChain"

    def __init__(self, inertia: primitives.Float | None = None, inertia_force: primitives.Float | None = None, damping: primitives.Float | None = None, elasticity: primitives.Float | None = None, stiffness: primitives.Float | None = None, simulate_terminal_bones: primitives.Bool | None = None, base_bone_radius: primitives.Float | None = None, dynamic_player_collision: primitives.Bool | None = None, collide_with_own_body: primitives.Bool | None = None, hand_collision_vibration: VibratePreset | str | None = None, collide_with_head: primitives.Bool | None = None, collide_with_body: primitives.Bool | None = None, collide_with_left_hand: primitives.Bool | None = None, collide_with_right_hand: primitives.Bool | None = None, gravity: primitives.Float3 | None = None, use_user_gravity_direction: primitives.Bool | None = None, local_force: primitives.Float3 | None = None, global_stretch: primitives.Float | None = None, max_stretch_ratio: primitives.Float | None = None, current_stretch_ratio: primitives.Float | None = None, stretch_restore_speed: primitives.Float | None = None, use_local_user_space: primitives.Bool | None = None, visualize_colliders: primitives.Bool | None = None, visualize_bones: primitives.Bool | None = None, is_grabbable: primitives.Bool | None = None, active_user_root_only: primitives.Bool | None = None, allow_steal: primitives.Bool | None = None, grab_priority: primitives.Int | None = None, ignore_grab_on_first_bone: primitives.Bool | None = None, grab_radius_tolerance: primitives.Float | None = None, grab_release_distance: primitives.Float | None = None, grab_slipping: primitives.Bool | None = None, grab_terminal_bones: primitives.Bool | None = None, grab_vibration: VibratePreset | str | None = None, ignore_own_left_hand: primitives.Bool | None = None, ignore_own_right_hand: primitives.Bool | None = None, effector_target: str | Slot | None = None, effector_bone_index: primitives.Int | None = None, effector_bone_offset: primitives.Float3 | None = None, active_grabber: str | Grabber | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            inertia: Initial value for Inertia.
            inertia_force: Initial value for InertiaForce.
            damping: Initial value for Damping.
            elasticity: Initial value for Elasticity.
            stiffness: Initial value for Stiffness.
            simulate_terminal_bones: Initial value for SimulateTerminalBones.
            base_bone_radius: Initial value for BaseBoneRadius.
            dynamic_player_collision: Initial value for DynamicPlayerCollision.
            collide_with_own_body: Initial value for CollideWithOwnBody.
            hand_collision_vibration: Initial value for HandCollisionVibration.
            collide_with_head: Initial value for CollideWithHead.
            collide_with_body: Initial value for CollideWithBody.
            collide_with_left_hand: Initial value for CollideWithLeftHand.
            collide_with_right_hand: Initial value for CollideWithRightHand.
            gravity: Initial value for Gravity.
            use_user_gravity_direction: Initial value for UseUserGravityDirection.
            local_force: Initial value for LocalForce.
            global_stretch: Initial value for GlobalStretch.
            max_stretch_ratio: Initial value for MaxStretchRatio.
            current_stretch_ratio: Initial value for CurrentStretchRatio.
            stretch_restore_speed: Initial value for StretchRestoreSpeed.
            use_local_user_space: Initial value for UseLocalUserSpace.
            visualize_colliders: Initial value for VisualizeColliders.
            visualize_bones: Initial value for VisualizeBones.
            is_grabbable: Initial value for IsGrabbable.
            active_user_root_only: Initial value for ActiveUserRootOnly.
            allow_steal: Initial value for AllowSteal.
            grab_priority: Initial value for GrabPriority.
            ignore_grab_on_first_bone: Initial value for IgnoreGrabOnFirstBone.
            grab_radius_tolerance: Initial value for GrabRadiusTolerance.
            grab_release_distance: Initial value for GrabReleaseDistance.
            grab_slipping: Initial value for GrabSlipping.
            grab_terminal_bones: Initial value for GrabTerminalBones.
            grab_vibration: Initial value for GrabVibration.
            ignore_own_left_hand: Initial value for IgnoreOwnLeftHand.
            ignore_own_right_hand: Initial value for IgnoreOwnRightHand.
            effector_target: Initial value for EffectorTarget.
            effector_bone_index: Initial value for EffectorBoneIndex.
            effector_bone_offset: Initial value for EffectorBoneOffset.
            active_grabber: Initial value for _activeGrabber.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if inertia is not None:
            self.inertia = inertia
        if inertia_force is not None:
            self.inertia_force = inertia_force
        if damping is not None:
            self.damping = damping
        if elasticity is not None:
            self.elasticity = elasticity
        if stiffness is not None:
            self.stiffness = stiffness
        if simulate_terminal_bones is not None:
            self.simulate_terminal_bones = simulate_terminal_bones
        if base_bone_radius is not None:
            self.base_bone_radius = base_bone_radius
        if dynamic_player_collision is not None:
            self.dynamic_player_collision = dynamic_player_collision
        if collide_with_own_body is not None:
            self.collide_with_own_body = collide_with_own_body
        if hand_collision_vibration is not None:
            self.hand_collision_vibration = hand_collision_vibration
        if collide_with_head is not None:
            self.collide_with_head = collide_with_head
        if collide_with_body is not None:
            self.collide_with_body = collide_with_body
        if collide_with_left_hand is not None:
            self.collide_with_left_hand = collide_with_left_hand
        if collide_with_right_hand is not None:
            self.collide_with_right_hand = collide_with_right_hand
        if gravity is not None:
            self.gravity = gravity
        if use_user_gravity_direction is not None:
            self.use_user_gravity_direction = use_user_gravity_direction
        if local_force is not None:
            self.local_force = local_force
        if global_stretch is not None:
            self.global_stretch = global_stretch
        if max_stretch_ratio is not None:
            self.max_stretch_ratio = max_stretch_ratio
        if current_stretch_ratio is not None:
            self.current_stretch_ratio = current_stretch_ratio
        if stretch_restore_speed is not None:
            self.stretch_restore_speed = stretch_restore_speed
        if use_local_user_space is not None:
            self.use_local_user_space = use_local_user_space
        if visualize_colliders is not None:
            self.visualize_colliders = visualize_colliders
        if visualize_bones is not None:
            self.visualize_bones = visualize_bones
        if is_grabbable is not None:
            self.is_grabbable = is_grabbable
        if active_user_root_only is not None:
            self.active_user_root_only = active_user_root_only
        if allow_steal is not None:
            self.allow_steal = allow_steal
        if grab_priority is not None:
            self.grab_priority = grab_priority
        if ignore_grab_on_first_bone is not None:
            self.ignore_grab_on_first_bone = ignore_grab_on_first_bone
        if grab_radius_tolerance is not None:
            self.grab_radius_tolerance = grab_radius_tolerance
        if grab_release_distance is not None:
            self.grab_release_distance = grab_release_distance
        if grab_slipping is not None:
            self.grab_slipping = grab_slipping
        if grab_terminal_bones is not None:
            self.grab_terminal_bones = grab_terminal_bones
        if grab_vibration is not None:
            self.grab_vibration = grab_vibration
        if ignore_own_left_hand is not None:
            self.ignore_own_left_hand = ignore_own_left_hand
        if ignore_own_right_hand is not None:
            self.ignore_own_right_hand = ignore_own_right_hand
        if effector_target is not None:
            self.effector_target = effector_target
        if effector_bone_index is not None:
            self.effector_bone_index = effector_bone_index
        if effector_bone_offset is not None:
            self.effector_bone_offset = effector_bone_offset
        if active_grabber is not None:
            self.active_grabber = active_grabber

    @property
    def inertia(self) -> primitives.Float | None:
        """Controls the amount of inertia a bone experiences. Does not affect acceleration of bones."""
        member = self.get_member("Inertia")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inertia.setter
    def inertia(self, value: primitives.Float) -> None:
        """Set the Inertia field value."""
        member = self.get_member("Inertia")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Inertia", fields.FieldFloat(value=value)
            )

    @property
    def inertia_force(self) -> primitives.Float | None:
        """Controls the amount of inertia a bone experiences. Does affect acceleration of bones."""
        member = self.get_member("InertiaForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inertia_force.setter
    def inertia_force(self, value: primitives.Float) -> None:
        """Set the InertiaForce field value."""
        member = self.get_member("InertiaForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InertiaForce", fields.FieldFloat(value=value)
            )

    @property
    def damping(self) -> primitives.Float | None:
        """Controls the amount of damping a bone experiences. A high damping value will cause bones to decelerate quickly."""
        member = self.get_member("Damping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @damping.setter
    def damping(self, value: primitives.Float) -> None:
        """Set the Damping field value."""
        member = self.get_member("Damping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Damping", fields.FieldFloat(value=value)
            )

    @property
    def elasticity(self) -> primitives.Float | None:
        """Controls the elasticity of bone joints. A high elasticity value will cause bones to accelerate toward their starting rotation more quickly."""
        member = self.get_member("Elasticity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @elasticity.setter
    def elasticity(self, value: primitives.Float) -> None:
        """Set the Elasticity field value."""
        member = self.get_member("Elasticity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Elasticity", fields.FieldFloat(value=value)
            )

    @property
    def stiffness(self) -> primitives.Float | None:
        """Controls the stiffness of bone joints."""
        member = self.get_member("Stiffness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stiffness.setter
    def stiffness(self, value: primitives.Float) -> None:
        """Set the Stiffness field value."""
        member = self.get_member("Stiffness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Stiffness", fields.FieldFloat(value=value)
            )

    @property
    def simulate_terminal_bones(self) -> primitives.Bool | None:
        """Whether or not to use the last bone in the chain. If your armature has end bones that do not control anything, you probably want this off."""
        member = self.get_member("SimulateTerminalBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simulate_terminal_bones.setter
    def simulate_terminal_bones(self, value: primitives.Bool) -> None:
        """Set the SimulateTerminalBones field value."""
        member = self.get_member("SimulateTerminalBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimulateTerminalBones", fields.FieldBool(value=value)
            )

    @property
    def base_bone_radius(self) -> primitives.Float | None:
        """The default size of the sphere that allows a bone to be interacted with."""
        member = self.get_member("BaseBoneRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_bone_radius.setter
    def base_bone_radius(self, value: primitives.Float) -> None:
        """Set the BaseBoneRadius field value."""
        member = self.get_member("BaseBoneRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseBoneRadius", fields.FieldFloat(value=value)
            )

    @property
    def dynamic_player_collision(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to collide with players."""
        member = self.get_member("DynamicPlayerCollision")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dynamic_player_collision.setter
    def dynamic_player_collision(self, value: primitives.Bool) -> None:
        """Set the DynamicPlayerCollision field value."""
        member = self.get_member("DynamicPlayerCollision")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DynamicPlayerCollision", fields.FieldBool(value=value)
            )

    @property
    def collide_with_own_body(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to collide with the active user of the dynamic bone chain."""
        member = self.get_member("CollideWithOwnBody")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_own_body.setter
    def collide_with_own_body(self, value: primitives.Bool) -> None:
        """Set the CollideWithOwnBody field value."""
        member = self.get_member("CollideWithOwnBody")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithOwnBody", fields.FieldBool(value=value)
            )

    @property
    def hand_collision_vibration(self) -> VibratePreset | None:
        """The vibration intensity when touching the chain colliders with a hand."""
        member = self.get_member("HandCollisionVibration")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @hand_collision_vibration.setter
    def hand_collision_vibration(self, value: VibratePreset | str) -> None:
        """Set HandCollisionVibration. The vibration intensity when touching the chain colliders with a hand."""
        member = self.get_member("HandCollisionVibration")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "HandCollisionVibration",
                members.FieldEnum(value=str(value)),
            )

    @property
    def collide_with_head(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to collide with player heads."""
        member = self.get_member("CollideWithHead")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_head.setter
    def collide_with_head(self, value: primitives.Bool) -> None:
        """Set the CollideWithHead field value."""
        member = self.get_member("CollideWithHead")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithHead", fields.FieldBool(value=value)
            )

    @property
    def collide_with_body(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to collide with player body parts."""
        member = self.get_member("CollideWithBody")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_body.setter
    def collide_with_body(self, value: primitives.Bool) -> None:
        """Set the CollideWithBody field value."""
        member = self.get_member("CollideWithBody")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithBody", fields.FieldBool(value=value)
            )

    @property
    def collide_with_left_hand(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to collide with a player's left hand."""
        member = self.get_member("CollideWithLeftHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_left_hand.setter
    def collide_with_left_hand(self, value: primitives.Bool) -> None:
        """Set the CollideWithLeftHand field value."""
        member = self.get_member("CollideWithLeftHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithLeftHand", fields.FieldBool(value=value)
            )

    @property
    def collide_with_right_hand(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to collide with a player's right hand."""
        member = self.get_member("CollideWithRightHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_right_hand.setter
    def collide_with_right_hand(self, value: primitives.Bool) -> None:
        """Set the CollideWithRightHand field value."""
        member = self.get_member("CollideWithRightHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithRightHand", fields.FieldBool(value=value)
            )

    @property
    def gravity(self) -> primitives.Float3 | None:
        """A force like gravity in ``GravitySpace`` space that should be applied to the bone chain at all times."""
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
        """The coordinate space to apply ``Gravity`` in."""
        member = self.get_member("GravitySpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @gravity_space.setter
    def gravity_space(self, value: members.SyncObject) -> None:
        """Set GravitySpace. The coordinate space to apply ``Gravity`` in."""
        self.set_member("GravitySpace", value)

    @property
    def use_user_gravity_direction(self) -> primitives.Bool | None:
        """Whether or not to use the active user of the dynamic bone chain's character controller gravity for the gravity direction"""
        member = self.get_member("UseUserGravityDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_user_gravity_direction.setter
    def use_user_gravity_direction(self, value: primitives.Bool) -> None:
        """Set the UseUserGravityDirection field value."""
        member = self.get_member("UseUserGravityDirection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseUserGravityDirection", fields.FieldBool(value=value)
            )

    @property
    def local_force(self) -> primitives.Float3 | None:
        """Constant force being applied to the bone in the dynamic bone chain's local space."""
        member = self.get_member("LocalForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @local_force.setter
    def local_force(self, value: primitives.Float3) -> None:
        """Set the LocalForce field value."""
        member = self.get_member("LocalForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocalForce", fields.FieldFloat3(value=value)
            )

    @property
    def global_stretch(self) -> primitives.Float | None:
        """How stretched out the bone chain should be at rest."""
        member = self.get_member("GlobalStretch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_stretch.setter
    def global_stretch(self, value: primitives.Float) -> None:
        """Set the GlobalStretch field value."""
        member = self.get_member("GlobalStretch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalStretch", fields.FieldFloat(value=value)
            )

    @property
    def max_stretch_ratio(self) -> primitives.Float | None:
        """The maximum amount of stretching that can be caused by pulling on the bones."""
        member = self.get_member("MaxStretchRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_stretch_ratio.setter
    def max_stretch_ratio(self, value: primitives.Float) -> None:
        """Set the MaxStretchRatio field value."""
        member = self.get_member("MaxStretchRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxStretchRatio", fields.FieldFloat(value=value)
            )

    @property
    def current_stretch_ratio(self) -> primitives.Float | None:
        """The current amount of stretching applied to the bones."""
        member = self.get_member("CurrentStretchRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_stretch_ratio.setter
    def current_stretch_ratio(self, value: primitives.Float) -> None:
        """Set the CurrentStretchRatio field value."""
        member = self.get_member("CurrentStretchRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentStretchRatio", fields.FieldFloat(value=value)
            )

    @property
    def stretch_restore_speed(self) -> primitives.Float | None:
        """How quickly extra stretching dissipates."""
        member = self.get_member("StretchRestoreSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stretch_restore_speed.setter
    def stretch_restore_speed(self, value: primitives.Float) -> None:
        """Set the StretchRestoreSpeed field value."""
        member = self.get_member("StretchRestoreSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StretchRestoreSpeed", fields.FieldFloat(value=value)
            )

    @property
    def use_local_user_space(self) -> primitives.Bool | None:
        """Whether or not to make the dynamic bone only respond to movements generated from the user slot's local position changing."""
        member = self.get_member("UseLocalUserSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_local_user_space.setter
    def use_local_user_space(self, value: primitives.Bool) -> None:
        """Set the UseLocalUserSpace field value."""
        member = self.get_member("UseLocalUserSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseLocalUserSpace", fields.FieldBool(value=value)
            )

    @property
    def simulation_space(self) -> members.SyncObject | None:
        """The coordinate space that movement in should affect this dynamic bone chain."""
        member = self.get_member("SimulationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @simulation_space.setter
    def simulation_space(self, value: members.SyncObject) -> None:
        """Set SimulationSpace. The coordinate space that movement in should affect this dynamic bone chain."""
        self.set_member("SimulationSpace", value)

    @property
    def static_colliders(self) -> members.SyncList | None:
        """A list of dynamic bone collider components to be used."""
        member = self.get_member("StaticColliders")
        if isinstance(member, members.SyncList):
            return member
        return None

    @static_colliders.setter
    def static_colliders(self, value: members.SyncList) -> None:
        """Set StaticColliders. A list of dynamic bone collider components to be used."""
        self.set_member("StaticColliders", value)

    @property
    def visualize_colliders(self) -> primitives.Bool | None:
        """Causes all bone colliders colliding with this bone to be displayed."""
        member = self.get_member("VisualizeColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visualize_colliders.setter
    def visualize_colliders(self, value: primitives.Bool) -> None:
        """Set the VisualizeColliders field value."""
        member = self.get_member("VisualizeColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualizeColliders", fields.FieldBool(value=value)
            )

    @property
    def visualize_bones(self) -> primitives.Bool | None:
        """Causes the bones, their colliders, and the connections between them to be displayed."""
        member = self.get_member("VisualizeBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visualize_bones.setter
    def visualize_bones(self, value: primitives.Bool) -> None:
        """Set the VisualizeBones field value."""
        member = self.get_member("VisualizeBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualizeBones", fields.FieldBool(value=value)
            )

    @property
    def is_grabbable(self) -> primitives.Bool | None:
        """Allows you to grab bones by touching them and grabbing. Requires DynamicPlayerCollision to be checked."""
        member = self.get_member("IsGrabbable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_grabbable.setter
    def is_grabbable(self, value: primitives.Bool) -> None:
        """Set the IsGrabbable field value."""
        member = self.get_member("IsGrabbable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsGrabbable", fields.FieldBool(value=value)
            )

    @property
    def active_user_root_only(self) -> primitives.Bool | None:
        """Allows the active user of the dynamic bone chain to be the only user that can grab it."""
        member = self.get_member("ActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_user_root_only.setter
    def active_user_root_only(self, value: primitives.Bool) -> None:
        """Set the ActiveUserRootOnly field value."""
        member = self.get_member("ActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUserRootOnly", fields.FieldBool(value=value)
            )

    @property
    def allow_steal(self) -> primitives.Bool | None:
        """Whether or not a second user can grab the chain while someone is holding it."""
        member = self.get_member("AllowSteal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_steal.setter
    def allow_steal(self, value: primitives.Bool) -> None:
        """Set the AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSteal", fields.FieldBool(value=value)
            )

    @property
    def grab_priority(self) -> primitives.Int | None:
        """The GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority.setter
    def grab_priority(self, value: primitives.Int) -> None:
        """Set the GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriority", fields.FieldInt(value=value)
            )

    @property
    def ignore_grab_on_first_bone(self) -> primitives.Bool | None:
        """Prevents EffectorBoneIndex from being 0 while being grabbed."""
        member = self.get_member("IgnoreGrabOnFirstBone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_grab_on_first_bone.setter
    def ignore_grab_on_first_bone(self, value: primitives.Bool) -> None:
        """Set the IgnoreGrabOnFirstBone field value."""
        member = self.get_member("IgnoreGrabOnFirstBone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreGrabOnFirstBone", fields.FieldBool(value=value)
            )

    @property
    def grab_radius_tolerance(self) -> primitives.Float | None:
        """how much further a user can grab a bone with their grab sphere despite the radius of the bone not being in contact with their grab sphere."""
        member = self.get_member("GrabRadiusTolerance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_radius_tolerance.setter
    def grab_radius_tolerance(self, value: primitives.Float) -> None:
        """Set the GrabRadiusTolerance field value."""
        member = self.get_member("GrabRadiusTolerance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabRadiusTolerance", fields.FieldFloat(value=value)
            )

    @property
    def grab_release_distance(self) -> primitives.Float | None:
        """How far a bone can be dragged before it automatically releases."""
        member = self.get_member("GrabReleaseDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_release_distance.setter
    def grab_release_distance(self, value: primitives.Float) -> None:
        """Set the GrabReleaseDistance field value."""
        member = self.get_member("GrabReleaseDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabReleaseDistance", fields.FieldFloat(value=value)
            )

    @property
    def grab_slipping(self) -> primitives.Bool | None:
        """Whether or not to make the EffectorBoneIndex increase as the hand moves along the bone chain away from the first bone in the chain. Does not let EffectorBoneIndex decrease unless re-grabbed."""
        member = self.get_member("GrabSlipping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_slipping.setter
    def grab_slipping(self, value: primitives.Bool) -> None:
        """Set the GrabSlipping field value."""
        member = self.get_member("GrabSlipping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabSlipping", fields.FieldBool(value=value)
            )

    @property
    def grab_terminal_bones(self) -> primitives.Bool | None:
        """Whether or not the final bone in the chain can be grabbed."""
        member = self.get_member("GrabTerminalBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_terminal_bones.setter
    def grab_terminal_bones(self, value: primitives.Bool) -> None:
        """Set the GrabTerminalBones field value."""
        member = self.get_member("GrabTerminalBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabTerminalBones", fields.FieldBool(value=value)
            )

    @property
    def grab_vibration(self) -> VibratePreset | None:
        """The vibration intensity when grabbing the chain with a hand."""
        member = self.get_member("GrabVibration")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @grab_vibration.setter
    def grab_vibration(self, value: VibratePreset | str) -> None:
        """Set GrabVibration. The vibration intensity when grabbing the chain with a hand."""
        member = self.get_member("GrabVibration")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "GrabVibration",
                members.FieldEnum(value=str(value)),
            )

    @property
    def ignore_own_left_hand(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to be grabbed with the left hand of the active user of the dynamic bone chain."""
        member = self.get_member("IgnoreOwnLeftHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_own_left_hand.setter
    def ignore_own_left_hand(self, value: primitives.Bool) -> None:
        """Set the IgnoreOwnLeftHand field value."""
        member = self.get_member("IgnoreOwnLeftHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreOwnLeftHand", fields.FieldBool(value=value)
            )

    @property
    def ignore_own_right_hand(self) -> primitives.Bool | None:
        """Whether or not to allow this bone chain to be grabbed with the right hand of the active user of the dynamic bone chain."""
        member = self.get_member("IgnoreOwnRightHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_own_right_hand.setter
    def ignore_own_right_hand(self, value: primitives.Bool) -> None:
        """Set the IgnoreOwnRightHand field value."""
        member = self.get_member("IgnoreOwnRightHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreOwnRightHand", fields.FieldBool(value=value)
            )

    @property
    def effector_target(self) -> str | None:
        """The chain tries to position one if its bones at this slot (used for grabbing)"""
        member = self.get_member("EffectorTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @effector_target.setter
    def effector_target(self, target: str | Slot | None) -> None:
        """Set the EffectorTarget reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("EffectorTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EffectorTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def effector_bone_index(self) -> primitives.Int | None:
        """Which bone is being positioned, every other bone after this acts as if it is not being grabbed"""
        member = self.get_member("EffectorBoneIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @effector_bone_index.setter
    def effector_bone_index(self, value: primitives.Int) -> None:
        """Set the EffectorBoneIndex field value."""
        member = self.get_member("EffectorBoneIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EffectorBoneIndex", fields.FieldInt(value=value)
            )

    @property
    def effector_bone_offset(self) -> primitives.Float3 | None:
        """acts as an offset from the grabbing slot in the grabbing slot's local space at the moment the bone was grabbed. Essentially prevents the bone from snapping to the center of the hand's grab sphere and keeps an offset for a smoother grabbing experience. Is automatically set every grab."""
        member = self.get_member("EffectorBoneOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @effector_bone_offset.setter
    def effector_bone_offset(self, value: primitives.Float3) -> None:
        """Set the EffectorBoneOffset field value."""
        member = self.get_member("EffectorBoneOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EffectorBoneOffset", fields.FieldFloat3(value=value)
            )

    @property
    def active_grabber(self) -> str | None:
        """The grabber component that is grabbing this bone chain currently"""
        member = self.get_member("_activeGrabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_grabber.setter
    def active_grabber(self, target: str | Grabber | None) -> None:
        """Set the _activeGrabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_activeGrabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeGrabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def bones(self) -> members.SyncList | None:
        """The bones that should be controlled by this dynamic bone chain."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncList) -> None:
        """Set Bones. The bones that should be controlled by this dynamic bone chain."""
        self.set_member("Bones", value)

