"""Generated component: DynamicBoneChain."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
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
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicBoneChain.

    Category: Physics/Dynamic Bones
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicBoneChain"

    def __init__(self, inertia: np.float32 | None = None, inertia_force: np.float32 | None = None, damping: np.float32 | None = None, elasticity: np.float32 | None = None, stiffness: np.float32 | None = None, simulate_terminal_bones: bool | None = None, base_bone_radius: np.float32 | None = None, dynamic_player_collision: bool | None = None, collide_with_own_body: bool | None = None, collide_with_head: bool | None = None, collide_with_body: bool | None = None, collide_with_left_hand: bool | None = None, collide_with_right_hand: bool | None = None, gravity: primitives.Float3 | None = None, use_user_gravity_direction: bool | None = None, local_force: primitives.Float3 | None = None, global_stretch: np.float32 | None = None, max_stretch_ratio: np.float32 | None = None, current_stretch_ratio: np.float32 | None = None, stretch_restore_speed: np.float32 | None = None, use_local_user_space: bool | None = None, visualize_colliders: bool | None = None, visualize_bones: bool | None = None, is_grabbable: bool | None = None, active_user_root_only: bool | None = None, allow_steal: bool | None = None, grab_priority: np.int32 | None = None, ignore_grab_on_first_bone: bool | None = None, grab_radius_tolerance: np.float32 | None = None, grab_release_distance: np.float32 | None = None, grab_slipping: bool | None = None, grab_terminal_bones: bool | None = None, ignore_own_left_hand: bool | None = None, ignore_own_right_hand: bool | None = None, effector_target: str | Slot | None = None, effector_bone_index: np.int32 | None = None, effector_bone_offset: primitives.Float3 | None = None, active_grabber: str | Grabber | None = None, *, component: workers.Component | None = None) -> None:
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
    def inertia(self) -> np.float32 | None:
        """The Inertia field value."""
        member = self.get_member("Inertia")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inertia.setter
    def inertia(self, value: np.float32) -> None:
        """Set the Inertia field value."""
        member = self.get_member("Inertia")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Inertia", fields.FieldFloat(value=value)
            )

    @property
    def inertia_force(self) -> np.float32 | None:
        """The InertiaForce field value."""
        member = self.get_member("InertiaForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @inertia_force.setter
    def inertia_force(self, value: np.float32) -> None:
        """Set the InertiaForce field value."""
        member = self.get_member("InertiaForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InertiaForce", fields.FieldFloat(value=value)
            )

    @property
    def damping(self) -> np.float32 | None:
        """The Damping field value."""
        member = self.get_member("Damping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @damping.setter
    def damping(self, value: np.float32) -> None:
        """Set the Damping field value."""
        member = self.get_member("Damping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Damping", fields.FieldFloat(value=value)
            )

    @property
    def elasticity(self) -> np.float32 | None:
        """The Elasticity field value."""
        member = self.get_member("Elasticity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @elasticity.setter
    def elasticity(self, value: np.float32) -> None:
        """Set the Elasticity field value."""
        member = self.get_member("Elasticity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Elasticity", fields.FieldFloat(value=value)
            )

    @property
    def stiffness(self) -> np.float32 | None:
        """The Stiffness field value."""
        member = self.get_member("Stiffness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stiffness.setter
    def stiffness(self, value: np.float32) -> None:
        """Set the Stiffness field value."""
        member = self.get_member("Stiffness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Stiffness", fields.FieldFloat(value=value)
            )

    @property
    def simulate_terminal_bones(self) -> bool | None:
        """The SimulateTerminalBones field value."""
        member = self.get_member("SimulateTerminalBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simulate_terminal_bones.setter
    def simulate_terminal_bones(self, value: bool) -> None:
        """Set the SimulateTerminalBones field value."""
        member = self.get_member("SimulateTerminalBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimulateTerminalBones", fields.FieldBool(value=value)
            )

    @property
    def base_bone_radius(self) -> np.float32 | None:
        """The BaseBoneRadius field value."""
        member = self.get_member("BaseBoneRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_bone_radius.setter
    def base_bone_radius(self, value: np.float32) -> None:
        """Set the BaseBoneRadius field value."""
        member = self.get_member("BaseBoneRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseBoneRadius", fields.FieldFloat(value=value)
            )

    @property
    def dynamic_player_collision(self) -> bool | None:
        """The DynamicPlayerCollision field value."""
        member = self.get_member("DynamicPlayerCollision")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dynamic_player_collision.setter
    def dynamic_player_collision(self, value: bool) -> None:
        """Set the DynamicPlayerCollision field value."""
        member = self.get_member("DynamicPlayerCollision")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DynamicPlayerCollision", fields.FieldBool(value=value)
            )

    @property
    def collide_with_own_body(self) -> bool | None:
        """The CollideWithOwnBody field value."""
        member = self.get_member("CollideWithOwnBody")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_own_body.setter
    def collide_with_own_body(self, value: bool) -> None:
        """Set the CollideWithOwnBody field value."""
        member = self.get_member("CollideWithOwnBody")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithOwnBody", fields.FieldBool(value=value)
            )

    @property
    def hand_collision_vibration(self) -> members.FieldEnum | None:
        """The HandCollisionVibration member."""
        member = self.get_member("HandCollisionVibration")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @hand_collision_vibration.setter
    def hand_collision_vibration(self, value: members.FieldEnum) -> None:
        """Set the HandCollisionVibration member."""
        self.set_member("HandCollisionVibration", value)

    @property
    def collide_with_head(self) -> bool | None:
        """The CollideWithHead field value."""
        member = self.get_member("CollideWithHead")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_head.setter
    def collide_with_head(self, value: bool) -> None:
        """Set the CollideWithHead field value."""
        member = self.get_member("CollideWithHead")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithHead", fields.FieldBool(value=value)
            )

    @property
    def collide_with_body(self) -> bool | None:
        """The CollideWithBody field value."""
        member = self.get_member("CollideWithBody")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_body.setter
    def collide_with_body(self, value: bool) -> None:
        """Set the CollideWithBody field value."""
        member = self.get_member("CollideWithBody")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithBody", fields.FieldBool(value=value)
            )

    @property
    def collide_with_left_hand(self) -> bool | None:
        """The CollideWithLeftHand field value."""
        member = self.get_member("CollideWithLeftHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_left_hand.setter
    def collide_with_left_hand(self, value: bool) -> None:
        """Set the CollideWithLeftHand field value."""
        member = self.get_member("CollideWithLeftHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CollideWithLeftHand", fields.FieldBool(value=value)
            )

    @property
    def collide_with_right_hand(self) -> bool | None:
        """The CollideWithRightHand field value."""
        member = self.get_member("CollideWithRightHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @collide_with_right_hand.setter
    def collide_with_right_hand(self, value: bool) -> None:
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
        """The Gravity field value."""
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
        """The GravitySpace member."""
        member = self.get_member("GravitySpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @gravity_space.setter
    def gravity_space(self, value: members.SyncObject) -> None:
        """Set the GravitySpace member."""
        self.set_member("GravitySpace", value)

    @property
    def use_user_gravity_direction(self) -> bool | None:
        """The UseUserGravityDirection field value."""
        member = self.get_member("UseUserGravityDirection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_user_gravity_direction.setter
    def use_user_gravity_direction(self, value: bool) -> None:
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
        """The LocalForce field value."""
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
    def global_stretch(self) -> np.float32 | None:
        """The GlobalStretch field value."""
        member = self.get_member("GlobalStretch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_stretch.setter
    def global_stretch(self, value: np.float32) -> None:
        """Set the GlobalStretch field value."""
        member = self.get_member("GlobalStretch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalStretch", fields.FieldFloat(value=value)
            )

    @property
    def max_stretch_ratio(self) -> np.float32 | None:
        """The MaxStretchRatio field value."""
        member = self.get_member("MaxStretchRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_stretch_ratio.setter
    def max_stretch_ratio(self, value: np.float32) -> None:
        """Set the MaxStretchRatio field value."""
        member = self.get_member("MaxStretchRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxStretchRatio", fields.FieldFloat(value=value)
            )

    @property
    def current_stretch_ratio(self) -> np.float32 | None:
        """The CurrentStretchRatio field value."""
        member = self.get_member("CurrentStretchRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_stretch_ratio.setter
    def current_stretch_ratio(self, value: np.float32) -> None:
        """Set the CurrentStretchRatio field value."""
        member = self.get_member("CurrentStretchRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentStretchRatio", fields.FieldFloat(value=value)
            )

    @property
    def stretch_restore_speed(self) -> np.float32 | None:
        """The StretchRestoreSpeed field value."""
        member = self.get_member("StretchRestoreSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stretch_restore_speed.setter
    def stretch_restore_speed(self, value: np.float32) -> None:
        """Set the StretchRestoreSpeed field value."""
        member = self.get_member("StretchRestoreSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StretchRestoreSpeed", fields.FieldFloat(value=value)
            )

    @property
    def use_local_user_space(self) -> bool | None:
        """The UseLocalUserSpace field value."""
        member = self.get_member("UseLocalUserSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_local_user_space.setter
    def use_local_user_space(self, value: bool) -> None:
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
        """The SimulationSpace member."""
        member = self.get_member("SimulationSpace")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @simulation_space.setter
    def simulation_space(self, value: members.SyncObject) -> None:
        """Set the SimulationSpace member."""
        self.set_member("SimulationSpace", value)

    @property
    def static_colliders(self) -> members.SyncList | None:
        """The StaticColliders member."""
        member = self.get_member("StaticColliders")
        if isinstance(member, members.SyncList):
            return member
        return None

    @static_colliders.setter
    def static_colliders(self, value: members.SyncList) -> None:
        """Set the StaticColliders member."""
        self.set_member("StaticColliders", value)

    @property
    def visualize_colliders(self) -> bool | None:
        """The VisualizeColliders field value."""
        member = self.get_member("VisualizeColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visualize_colliders.setter
    def visualize_colliders(self, value: bool) -> None:
        """Set the VisualizeColliders field value."""
        member = self.get_member("VisualizeColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualizeColliders", fields.FieldBool(value=value)
            )

    @property
    def visualize_bones(self) -> bool | None:
        """The VisualizeBones field value."""
        member = self.get_member("VisualizeBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @visualize_bones.setter
    def visualize_bones(self, value: bool) -> None:
        """Set the VisualizeBones field value."""
        member = self.get_member("VisualizeBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VisualizeBones", fields.FieldBool(value=value)
            )

    @property
    def is_grabbable(self) -> bool | None:
        """The IsGrabbable field value."""
        member = self.get_member("IsGrabbable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_grabbable.setter
    def is_grabbable(self, value: bool) -> None:
        """Set the IsGrabbable field value."""
        member = self.get_member("IsGrabbable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsGrabbable", fields.FieldBool(value=value)
            )

    @property
    def active_user_root_only(self) -> bool | None:
        """The ActiveUserRootOnly field value."""
        member = self.get_member("ActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_user_root_only.setter
    def active_user_root_only(self, value: bool) -> None:
        """Set the ActiveUserRootOnly field value."""
        member = self.get_member("ActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveUserRootOnly", fields.FieldBool(value=value)
            )

    @property
    def allow_steal(self) -> bool | None:
        """The AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_steal.setter
    def allow_steal(self, value: bool) -> None:
        """Set the AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSteal", fields.FieldBool(value=value)
            )

    @property
    def grab_priority(self) -> np.int32 | None:
        """The GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority.setter
    def grab_priority(self, value: np.int32) -> None:
        """Set the GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriority", fields.FieldInt(value=value)
            )

    @property
    def ignore_grab_on_first_bone(self) -> bool | None:
        """The IgnoreGrabOnFirstBone field value."""
        member = self.get_member("IgnoreGrabOnFirstBone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_grab_on_first_bone.setter
    def ignore_grab_on_first_bone(self, value: bool) -> None:
        """Set the IgnoreGrabOnFirstBone field value."""
        member = self.get_member("IgnoreGrabOnFirstBone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreGrabOnFirstBone", fields.FieldBool(value=value)
            )

    @property
    def grab_radius_tolerance(self) -> np.float32 | None:
        """The GrabRadiusTolerance field value."""
        member = self.get_member("GrabRadiusTolerance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_radius_tolerance.setter
    def grab_radius_tolerance(self, value: np.float32) -> None:
        """Set the GrabRadiusTolerance field value."""
        member = self.get_member("GrabRadiusTolerance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabRadiusTolerance", fields.FieldFloat(value=value)
            )

    @property
    def grab_release_distance(self) -> np.float32 | None:
        """The GrabReleaseDistance field value."""
        member = self.get_member("GrabReleaseDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_release_distance.setter
    def grab_release_distance(self, value: np.float32) -> None:
        """Set the GrabReleaseDistance field value."""
        member = self.get_member("GrabReleaseDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabReleaseDistance", fields.FieldFloat(value=value)
            )

    @property
    def grab_slipping(self) -> bool | None:
        """The GrabSlipping field value."""
        member = self.get_member("GrabSlipping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_slipping.setter
    def grab_slipping(self, value: bool) -> None:
        """Set the GrabSlipping field value."""
        member = self.get_member("GrabSlipping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabSlipping", fields.FieldBool(value=value)
            )

    @property
    def grab_terminal_bones(self) -> bool | None:
        """The GrabTerminalBones field value."""
        member = self.get_member("GrabTerminalBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_terminal_bones.setter
    def grab_terminal_bones(self, value: bool) -> None:
        """Set the GrabTerminalBones field value."""
        member = self.get_member("GrabTerminalBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabTerminalBones", fields.FieldBool(value=value)
            )

    @property
    def grab_vibration(self) -> members.FieldEnum | None:
        """The GrabVibration member."""
        member = self.get_member("GrabVibration")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @grab_vibration.setter
    def grab_vibration(self, value: members.FieldEnum) -> None:
        """Set the GrabVibration member."""
        self.set_member("GrabVibration", value)

    @property
    def ignore_own_left_hand(self) -> bool | None:
        """The IgnoreOwnLeftHand field value."""
        member = self.get_member("IgnoreOwnLeftHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_own_left_hand.setter
    def ignore_own_left_hand(self, value: bool) -> None:
        """Set the IgnoreOwnLeftHand field value."""
        member = self.get_member("IgnoreOwnLeftHand")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreOwnLeftHand", fields.FieldBool(value=value)
            )

    @property
    def ignore_own_right_hand(self) -> bool | None:
        """The IgnoreOwnRightHand field value."""
        member = self.get_member("IgnoreOwnRightHand")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_own_right_hand.setter
    def ignore_own_right_hand(self, value: bool) -> None:
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
        """Target ID of the EffectorTarget reference (targets Slot)."""
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
    def effector_bone_index(self) -> np.int32 | None:
        """The EffectorBoneIndex field value."""
        member = self.get_member("EffectorBoneIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @effector_bone_index.setter
    def effector_bone_index(self, value: np.int32) -> None:
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
        """The EffectorBoneOffset field value."""
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
        """Target ID of the _activeGrabber reference (targets Grabber)."""
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
        """The Bones member."""
        member = self.get_member("Bones")
        if isinstance(member, members.SyncList):
            return member
        return None

    @bones.setter
    def bones(self, value: members.SyncList) -> None:
        """Set the Bones member."""
        self.set_member("Bones", value)

