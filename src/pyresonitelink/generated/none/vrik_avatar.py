"""Generated component: VRIKAvatar."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.vrik import VRIK
from pyresonitelink.generated._types.locomotion_controller import LocomotionController
from pyresonitelink.generated._types.avatar_pose_node import AvatarPoseNode
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iavatar_body_node_event_receiver import IAvatarBodyNodeEventReceiver
from pyresonitelink.generated._types.ineck_offset_source import INeckOffsetSource
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.ilocomotion_animation_metric_source import ILocomotionAnimationMetricSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VRIKAvatar(GeneratedComponent, IAvatarObjectComponent, ICustomInspector, IAvatarBodyNodeEventReceiver, INeckOffsetSource, IInputUpdateReceiver, ILocomotionAnimationMetricSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FinalIK.VRIKAvatar.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FinalIK.VRIKAvatar"

    def __init__(self, ik: str | VRIK | None = None, height_compensation: np.float32 | None = None, avatar_height: np.float32 | None = None, user_resize_threshold: np.float32 | None = None, feet_ignore_other_players: bool | None = None, head_max_fix_distance: np.float32 | None = None, force_use_feet_proxies: bool | None = None, force_use_pelvis_proxy: bool | None = None, force_use_chest_proxy: bool | None = None, force_use_elbow_proxies: bool | None = None, force_use_knee_proxies: bool | None = None, feet_calibrated: bool | None = None, pelvis_calibrated: bool | None = None, ground_check_height_ratio: np.float32 | None = None, feet_hover_height: np.float32 | None = None, feet_hover_smooth_speed: np.float32 | None = None, min_feet_transition_speed: np.float32 | None = None, max_feet_transition_speed: np.float32 | None = None, gait_feet_transition_speed_multiplier: np.float32 | None = None, feet_hover_tilt: np.float32 | None = None, left_foot_float_offset: primitives.Float3 | None = None, right_foot_float_offset: primitives.Float3 | None = None, left_foot_root_height: np.float32 | None = None, right_foot_root_height: np.float32 | None = None, foot_float_speed: np.float32 | None = None, foot_float_angle_magnitude: np.float32 | None = None, foot_float_offset_magnitude: np.float32 | None = None, feet_float_velocity_force: np.float32 | None = None, feet_float_velocity_dampening_speed: np.float32 | None = None, max_feet_velocity_offset: np.float32 | None = None, velocity_average_rate: np.float32 | None = None, hover_velocity_threshold: np.float32 | None = None, horizontal_body_angle: np.float32 | None = None, supress_walk_animation_when_horizontal: bool | None = None, always_use_trackers_when_horizontal: bool | None = None, gait_transition_speed: np.float32 | None = None, gait_movement_direction_smooth_speed: np.float32 | None = None, rig_colliders_radius_ratio: np.float32 | None = None, left_hand_rotation_offset: primitives.FloatQ | None = None, right_hand_rotation_offset: primitives.FloatQ | None = None, current_average_velocity: np.float32 | None = None, current_on_ground: bool | None = None, current_gait_index: np.int32 | None = None, locomotion_controller: str | LocomotionController | None = None, left_hand_node: str | AvatarPoseNode | None = None, right_hand_node: str | AvatarPoseNode | None = None, left_elbow_node: str | AvatarPoseNode | None = None, right_elbow_node: str | AvatarPoseNode | None = None, left_foot_node: str | AvatarPoseNode | None = None, right_foot_node: str | AvatarPoseNode | None = None, left_knee_node: str | AvatarPoseNode | None = None, right_knee_node: str | AvatarPoseNode | None = None, head_node: str | AvatarPoseNode | None = None, pelvis_node: str | AvatarPoseNode | None = None, chest_node: str | AvatarPoseNode | None = None, head_proxy: str | Slot | None = None, pelvis_proxy: str | Slot | None = None, chest_proxy: str | Slot | None = None, left_hand_proxy: str | Slot | None = None, right_hand_proxy: str | Slot | None = None, left_elbow_proxy: str | Slot | None = None, right_elbow_proxy: str | Slot | None = None, left_foot_proxy: str | Slot | None = None, right_foot_proxy: str | Slot | None = None, left_knee_proxy: str | Slot | None = None, right_knee_proxy: str | Slot | None = None, left_knee_default_proxy: str | Slot | None = None, right_knee_default_proxy: str | Slot | None = None, head_target_pos: str | IField[primitives.Float3] | None = None, head_target_rot: str | IField[primitives.FloatQ] | None = None, pelvis_target_pos: str | IField[primitives.Float3] | None = None, pelvis_target_rot: str | IField[primitives.FloatQ] | None = None, chest_target_pos: str | IField[primitives.Float3] | None = None, left_hand_target_pos: str | IField[primitives.Float3] | None = None, left_hand_target_rot: str | IField[primitives.FloatQ] | None = None, right_hand_target_pos: str | IField[primitives.Float3] | None = None, right_hand_target_rot: str | IField[primitives.FloatQ] | None = None, left_elbow_target_pos: str | IField[primitives.Float3] | None = None, right_elbow_target_pos: str | IField[primitives.Float3] | None = None, left_foot_target_pos: str | IField[primitives.Float3] | None = None, left_foot_target_rot: str | IField[primitives.FloatQ] | None = None, right_foot_target_pos: str | IField[primitives.Float3] | None = None, right_foot_target_rot: str | IField[primitives.FloatQ] | None = None, left_knee_target_pos: str | IField[primitives.Float3] | None = None, right_knee_target_pos: str | IField[primitives.Float3] | None = None, pelvis_position_weight: str | IField[np.float32] | None = None, pelvis_rotation_weight: str | IField[np.float32] | None = None, chest_weight: str | IField[np.float32] | None = None, locomotion_weight: str | IField[np.float32] | None = None, left_leg_position_weight: str | IField[np.float32] | None = None, left_leg_rotation_weight: str | IField[np.float32] | None = None, right_leg_position_weight: str | IField[np.float32] | None = None, right_leg_rotation_weight: str | IField[np.float32] | None = None, left_knee_bend_weight: str | IField[np.float32] | None = None, right_knee_bend_weight: str | IField[np.float32] | None = None, left_elbow_bend_weight: str | IField[np.float32] | None = None, right_elbow_bend_weight: str | IField[np.float32] | None = None, left_foot_offset: str | IField[primitives.Float3] | None = None, right_foot_offset: str | IField[primitives.Float3] | None = None, left_foot_relative_to_root: primitives.FloatQ | None = None, right_foot_relative_to_root: primitives.FloatQ | None = None, locomotion_offset: str | IField[primitives.Float3] | None = None, simplified_collider_enabled: str | IField[bool] | None = None, horizontal_tracking_locked: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            ik: Initial value for IK.
            height_compensation: Initial value for HeightCompensation.
            avatar_height: Initial value for AvatarHeight.
            user_resize_threshold: Initial value for UserResizeThreshold.
            feet_ignore_other_players: Initial value for FeetIgnoreOtherPlayers.
            head_max_fix_distance: Initial value for HeadMaxFixDistance.
            force_use_feet_proxies: Initial value for ForceUseFeetProxies.
            force_use_pelvis_proxy: Initial value for ForceUsePelvisProxy.
            force_use_chest_proxy: Initial value for ForceUseChestProxy.
            force_use_elbow_proxies: Initial value for ForceUseElbowProxies.
            force_use_knee_proxies: Initial value for ForceUseKneeProxies.
            feet_calibrated: Initial value for FeetCalibrated.
            pelvis_calibrated: Initial value for PelvisCalibrated.
            ground_check_height_ratio: Initial value for GroundCheckHeightRatio.
            feet_hover_height: Initial value for FeetHoverHeight.
            feet_hover_smooth_speed: Initial value for FeetHoverSmoothSpeed.
            min_feet_transition_speed: Initial value for MinFeetTransitionSpeed.
            max_feet_transition_speed: Initial value for MaxFeetTransitionSpeed.
            gait_feet_transition_speed_multiplier: Initial value for GaitFeetTransitionSpeedMultiplier.
            feet_hover_tilt: Initial value for FeetHoverTilt.
            left_foot_float_offset: Initial value for LeftFootFloatOffset.
            right_foot_float_offset: Initial value for RightFootFloatOffset.
            left_foot_root_height: Initial value for LeftFootRootHeight.
            right_foot_root_height: Initial value for RightFootRootHeight.
            foot_float_speed: Initial value for FootFloatSpeed.
            foot_float_angle_magnitude: Initial value for FootFloatAngleMagnitude.
            foot_float_offset_magnitude: Initial value for FootFloatOffsetMagnitude.
            feet_float_velocity_force: Initial value for FeetFloatVelocityForce.
            feet_float_velocity_dampening_speed: Initial value for FeetFloatVelocityDampeningSpeed.
            max_feet_velocity_offset: Initial value for MaxFeetVelocityOffset.
            velocity_average_rate: Initial value for VelocityAverageRate.
            hover_velocity_threshold: Initial value for HoverVelocityThreshold.
            horizontal_body_angle: Initial value for HorizontalBodyAngle.
            supress_walk_animation_when_horizontal: Initial value for SupressWalkAnimationWhenHorizontal.
            always_use_trackers_when_horizontal: Initial value for AlwaysUseTrackersWhenHorizontal.
            gait_transition_speed: Initial value for GaitTransitionSpeed.
            gait_movement_direction_smooth_speed: Initial value for GaitMovementDirectionSmoothSpeed.
            rig_colliders_radius_ratio: Initial value for RigCollidersRadiusRatio.
            left_hand_rotation_offset: Initial value for LeftHandRotationOffset.
            right_hand_rotation_offset: Initial value for RightHandRotationOffset.
            current_average_velocity: Initial value for CurrentAverageVelocity.
            current_on_ground: Initial value for CurrentOnGround.
            current_gait_index: Initial value for CurrentGaitIndex.
            locomotion_controller: Initial value for _locomotionController.
            left_hand_node: Initial value for _leftHandNode.
            right_hand_node: Initial value for _rightHandNode.
            left_elbow_node: Initial value for _leftElbowNode.
            right_elbow_node: Initial value for _rightElbowNode.
            left_foot_node: Initial value for _leftFootNode.
            right_foot_node: Initial value for _rightFootNode.
            left_knee_node: Initial value for _leftKneeNode.
            right_knee_node: Initial value for _rightKneeNode.
            head_node: Initial value for _headNode.
            pelvis_node: Initial value for _pelvisNode.
            chest_node: Initial value for _chestNode.
            head_proxy: Initial value for _headProxy.
            pelvis_proxy: Initial value for _pelvisProxy.
            chest_proxy: Initial value for _chestProxy.
            left_hand_proxy: Initial value for _leftHandProxy.
            right_hand_proxy: Initial value for _rightHandProxy.
            left_elbow_proxy: Initial value for _leftElbowProxy.
            right_elbow_proxy: Initial value for _rightElbowProxy.
            left_foot_proxy: Initial value for _leftFootProxy.
            right_foot_proxy: Initial value for _rightFootProxy.
            left_knee_proxy: Initial value for _leftKneeProxy.
            right_knee_proxy: Initial value for _rightKneeProxy.
            left_knee_default_proxy: Initial value for _leftKneeDefaultProxy.
            right_knee_default_proxy: Initial value for _rightKneeDefaultProxy.
            head_target_pos: Initial value for _headTargetPos.
            head_target_rot: Initial value for _headTargetRot.
            pelvis_target_pos: Initial value for _pelvisTargetPos.
            pelvis_target_rot: Initial value for _pelvisTargetRot.
            chest_target_pos: Initial value for _chestTargetPos.
            left_hand_target_pos: Initial value for _leftHandTargetPos.
            left_hand_target_rot: Initial value for _leftHandTargetRot.
            right_hand_target_pos: Initial value for _rightHandTargetPos.
            right_hand_target_rot: Initial value for _rightHandTargetRot.
            left_elbow_target_pos: Initial value for _leftElbowTargetPos.
            right_elbow_target_pos: Initial value for _rightElbowTargetPos.
            left_foot_target_pos: Initial value for _leftFootTargetPos.
            left_foot_target_rot: Initial value for _leftFootTargetRot.
            right_foot_target_pos: Initial value for _rightFootTargetPos.
            right_foot_target_rot: Initial value for _rightFootTargetRot.
            left_knee_target_pos: Initial value for _leftKneeTargetPos.
            right_knee_target_pos: Initial value for _rightKneeTargetPos.
            pelvis_position_weight: Initial value for _pelvisPositionWeight.
            pelvis_rotation_weight: Initial value for _pelvisRotationWeight.
            chest_weight: Initial value for _chestWeight.
            locomotion_weight: Initial value for _locomotionWeight.
            left_leg_position_weight: Initial value for _leftLegPositionWeight.
            left_leg_rotation_weight: Initial value for _leftLegRotationWeight.
            right_leg_position_weight: Initial value for _rightLegPositionWeight.
            right_leg_rotation_weight: Initial value for _rightLegRotationWeight.
            left_knee_bend_weight: Initial value for _leftKneeBendWeight.
            right_knee_bend_weight: Initial value for _rightKneeBendWeight.
            left_elbow_bend_weight: Initial value for _leftElbowBendWeight.
            right_elbow_bend_weight: Initial value for _rightElbowBendWeight.
            left_foot_offset: Initial value for _leftFootOffset.
            right_foot_offset: Initial value for _rightFootOffset.
            left_foot_relative_to_root: Initial value for _leftFootRelativeToRoot.
            right_foot_relative_to_root: Initial value for _rightFootRelativeToRoot.
            locomotion_offset: Initial value for _locomotionOffset.
            simplified_collider_enabled: Initial value for _simplifiedColliderEnabled.
            horizontal_tracking_locked: Initial value for _horizontalTrackingLocked.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if ik is not None:
            self.ik = ik
        if height_compensation is not None:
            self.height_compensation = height_compensation
        if avatar_height is not None:
            self.avatar_height = avatar_height
        if user_resize_threshold is not None:
            self.user_resize_threshold = user_resize_threshold
        if feet_ignore_other_players is not None:
            self.feet_ignore_other_players = feet_ignore_other_players
        if head_max_fix_distance is not None:
            self.head_max_fix_distance = head_max_fix_distance
        if force_use_feet_proxies is not None:
            self.force_use_feet_proxies = force_use_feet_proxies
        if force_use_pelvis_proxy is not None:
            self.force_use_pelvis_proxy = force_use_pelvis_proxy
        if force_use_chest_proxy is not None:
            self.force_use_chest_proxy = force_use_chest_proxy
        if force_use_elbow_proxies is not None:
            self.force_use_elbow_proxies = force_use_elbow_proxies
        if force_use_knee_proxies is not None:
            self.force_use_knee_proxies = force_use_knee_proxies
        if feet_calibrated is not None:
            self.feet_calibrated = feet_calibrated
        if pelvis_calibrated is not None:
            self.pelvis_calibrated = pelvis_calibrated
        if ground_check_height_ratio is not None:
            self.ground_check_height_ratio = ground_check_height_ratio
        if feet_hover_height is not None:
            self.feet_hover_height = feet_hover_height
        if feet_hover_smooth_speed is not None:
            self.feet_hover_smooth_speed = feet_hover_smooth_speed
        if min_feet_transition_speed is not None:
            self.min_feet_transition_speed = min_feet_transition_speed
        if max_feet_transition_speed is not None:
            self.max_feet_transition_speed = max_feet_transition_speed
        if gait_feet_transition_speed_multiplier is not None:
            self.gait_feet_transition_speed_multiplier = gait_feet_transition_speed_multiplier
        if feet_hover_tilt is not None:
            self.feet_hover_tilt = feet_hover_tilt
        if left_foot_float_offset is not None:
            self.left_foot_float_offset = left_foot_float_offset
        if right_foot_float_offset is not None:
            self.right_foot_float_offset = right_foot_float_offset
        if left_foot_root_height is not None:
            self.left_foot_root_height = left_foot_root_height
        if right_foot_root_height is not None:
            self.right_foot_root_height = right_foot_root_height
        if foot_float_speed is not None:
            self.foot_float_speed = foot_float_speed
        if foot_float_angle_magnitude is not None:
            self.foot_float_angle_magnitude = foot_float_angle_magnitude
        if foot_float_offset_magnitude is not None:
            self.foot_float_offset_magnitude = foot_float_offset_magnitude
        if feet_float_velocity_force is not None:
            self.feet_float_velocity_force = feet_float_velocity_force
        if feet_float_velocity_dampening_speed is not None:
            self.feet_float_velocity_dampening_speed = feet_float_velocity_dampening_speed
        if max_feet_velocity_offset is not None:
            self.max_feet_velocity_offset = max_feet_velocity_offset
        if velocity_average_rate is not None:
            self.velocity_average_rate = velocity_average_rate
        if hover_velocity_threshold is not None:
            self.hover_velocity_threshold = hover_velocity_threshold
        if horizontal_body_angle is not None:
            self.horizontal_body_angle = horizontal_body_angle
        if supress_walk_animation_when_horizontal is not None:
            self.supress_walk_animation_when_horizontal = supress_walk_animation_when_horizontal
        if always_use_trackers_when_horizontal is not None:
            self.always_use_trackers_when_horizontal = always_use_trackers_when_horizontal
        if gait_transition_speed is not None:
            self.gait_transition_speed = gait_transition_speed
        if gait_movement_direction_smooth_speed is not None:
            self.gait_movement_direction_smooth_speed = gait_movement_direction_smooth_speed
        if rig_colliders_radius_ratio is not None:
            self.rig_colliders_radius_ratio = rig_colliders_radius_ratio
        if left_hand_rotation_offset is not None:
            self.left_hand_rotation_offset = left_hand_rotation_offset
        if right_hand_rotation_offset is not None:
            self.right_hand_rotation_offset = right_hand_rotation_offset
        if current_average_velocity is not None:
            self.current_average_velocity = current_average_velocity
        if current_on_ground is not None:
            self.current_on_ground = current_on_ground
        if current_gait_index is not None:
            self.current_gait_index = current_gait_index
        if locomotion_controller is not None:
            self.locomotion_controller = locomotion_controller
        if left_hand_node is not None:
            self.left_hand_node = left_hand_node
        if right_hand_node is not None:
            self.right_hand_node = right_hand_node
        if left_elbow_node is not None:
            self.left_elbow_node = left_elbow_node
        if right_elbow_node is not None:
            self.right_elbow_node = right_elbow_node
        if left_foot_node is not None:
            self.left_foot_node = left_foot_node
        if right_foot_node is not None:
            self.right_foot_node = right_foot_node
        if left_knee_node is not None:
            self.left_knee_node = left_knee_node
        if right_knee_node is not None:
            self.right_knee_node = right_knee_node
        if head_node is not None:
            self.head_node = head_node
        if pelvis_node is not None:
            self.pelvis_node = pelvis_node
        if chest_node is not None:
            self.chest_node = chest_node
        if head_proxy is not None:
            self.head_proxy = head_proxy
        if pelvis_proxy is not None:
            self.pelvis_proxy = pelvis_proxy
        if chest_proxy is not None:
            self.chest_proxy = chest_proxy
        if left_hand_proxy is not None:
            self.left_hand_proxy = left_hand_proxy
        if right_hand_proxy is not None:
            self.right_hand_proxy = right_hand_proxy
        if left_elbow_proxy is not None:
            self.left_elbow_proxy = left_elbow_proxy
        if right_elbow_proxy is not None:
            self.right_elbow_proxy = right_elbow_proxy
        if left_foot_proxy is not None:
            self.left_foot_proxy = left_foot_proxy
        if right_foot_proxy is not None:
            self.right_foot_proxy = right_foot_proxy
        if left_knee_proxy is not None:
            self.left_knee_proxy = left_knee_proxy
        if right_knee_proxy is not None:
            self.right_knee_proxy = right_knee_proxy
        if left_knee_default_proxy is not None:
            self.left_knee_default_proxy = left_knee_default_proxy
        if right_knee_default_proxy is not None:
            self.right_knee_default_proxy = right_knee_default_proxy
        if head_target_pos is not None:
            self.head_target_pos = head_target_pos
        if head_target_rot is not None:
            self.head_target_rot = head_target_rot
        if pelvis_target_pos is not None:
            self.pelvis_target_pos = pelvis_target_pos
        if pelvis_target_rot is not None:
            self.pelvis_target_rot = pelvis_target_rot
        if chest_target_pos is not None:
            self.chest_target_pos = chest_target_pos
        if left_hand_target_pos is not None:
            self.left_hand_target_pos = left_hand_target_pos
        if left_hand_target_rot is not None:
            self.left_hand_target_rot = left_hand_target_rot
        if right_hand_target_pos is not None:
            self.right_hand_target_pos = right_hand_target_pos
        if right_hand_target_rot is not None:
            self.right_hand_target_rot = right_hand_target_rot
        if left_elbow_target_pos is not None:
            self.left_elbow_target_pos = left_elbow_target_pos
        if right_elbow_target_pos is not None:
            self.right_elbow_target_pos = right_elbow_target_pos
        if left_foot_target_pos is not None:
            self.left_foot_target_pos = left_foot_target_pos
        if left_foot_target_rot is not None:
            self.left_foot_target_rot = left_foot_target_rot
        if right_foot_target_pos is not None:
            self.right_foot_target_pos = right_foot_target_pos
        if right_foot_target_rot is not None:
            self.right_foot_target_rot = right_foot_target_rot
        if left_knee_target_pos is not None:
            self.left_knee_target_pos = left_knee_target_pos
        if right_knee_target_pos is not None:
            self.right_knee_target_pos = right_knee_target_pos
        if pelvis_position_weight is not None:
            self.pelvis_position_weight = pelvis_position_weight
        if pelvis_rotation_weight is not None:
            self.pelvis_rotation_weight = pelvis_rotation_weight
        if chest_weight is not None:
            self.chest_weight = chest_weight
        if locomotion_weight is not None:
            self.locomotion_weight = locomotion_weight
        if left_leg_position_weight is not None:
            self.left_leg_position_weight = left_leg_position_weight
        if left_leg_rotation_weight is not None:
            self.left_leg_rotation_weight = left_leg_rotation_weight
        if right_leg_position_weight is not None:
            self.right_leg_position_weight = right_leg_position_weight
        if right_leg_rotation_weight is not None:
            self.right_leg_rotation_weight = right_leg_rotation_weight
        if left_knee_bend_weight is not None:
            self.left_knee_bend_weight = left_knee_bend_weight
        if right_knee_bend_weight is not None:
            self.right_knee_bend_weight = right_knee_bend_weight
        if left_elbow_bend_weight is not None:
            self.left_elbow_bend_weight = left_elbow_bend_weight
        if right_elbow_bend_weight is not None:
            self.right_elbow_bend_weight = right_elbow_bend_weight
        if left_foot_offset is not None:
            self.left_foot_offset = left_foot_offset
        if right_foot_offset is not None:
            self.right_foot_offset = right_foot_offset
        if left_foot_relative_to_root is not None:
            self.left_foot_relative_to_root = left_foot_relative_to_root
        if right_foot_relative_to_root is not None:
            self.right_foot_relative_to_root = right_foot_relative_to_root
        if locomotion_offset is not None:
            self.locomotion_offset = locomotion_offset
        if simplified_collider_enabled is not None:
            self.simplified_collider_enabled = simplified_collider_enabled
        if horizontal_tracking_locked is not None:
            self.horizontal_tracking_locked = horizontal_tracking_locked

    @property
    def ik(self) -> str | None:
        """Target ID of the IK reference (targets VRIK)."""
        member = self.get_member("IK")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ik.setter
    def ik(self, target: str | VRIK | None) -> None:
        """Set the IK reference by target ID or VRIK instance."""
        target_id: str | None = target.id if isinstance(target, VRIK) else target  # type: ignore[assignment]
        member = self.get_member("IK")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IK",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FinalIK.VRIK'),
            )

    @property
    def height_compensation(self) -> np.float32 | None:
        """The HeightCompensation field value."""
        member = self.get_member("HeightCompensation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_compensation.setter
    def height_compensation(self, value: np.float32) -> None:
        """Set the HeightCompensation field value."""
        member = self.get_member("HeightCompensation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightCompensation", fields.FieldFloat(value=value)
            )

    @property
    def avatar_height(self) -> np.float32 | None:
        """The AvatarHeight field value."""
        member = self.get_member("AvatarHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @avatar_height.setter
    def avatar_height(self, value: np.float32) -> None:
        """Set the AvatarHeight field value."""
        member = self.get_member("AvatarHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AvatarHeight", fields.FieldFloat(value=value)
            )

    @property
    def user_resize_threshold(self) -> np.float32 | None:
        """The UserResizeThreshold field value."""
        member = self.get_member("UserResizeThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_resize_threshold.setter
    def user_resize_threshold(self, value: np.float32) -> None:
        """Set the UserResizeThreshold field value."""
        member = self.get_member("UserResizeThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserResizeThreshold", fields.FieldFloat(value=value)
            )

    @property
    def feet_ignore_other_players(self) -> bool | None:
        """The FeetIgnoreOtherPlayers field value."""
        member = self.get_member("FeetIgnoreOtherPlayers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_ignore_other_players.setter
    def feet_ignore_other_players(self, value: bool) -> None:
        """Set the FeetIgnoreOtherPlayers field value."""
        member = self.get_member("FeetIgnoreOtherPlayers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetIgnoreOtherPlayers", fields.FieldBool(value=value)
            )

    @property
    def feet_collision_list_mode(self) -> members.FieldEnum | None:
        """The FeetCollisionListMode member."""
        member = self.get_member("FeetCollisionListMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @feet_collision_list_mode.setter
    def feet_collision_list_mode(self, value: members.FieldEnum) -> None:
        """Set the FeetCollisionListMode member."""
        self.set_member("FeetCollisionListMode", value)

    @property
    def feet_collision_list(self) -> members.SyncList | None:
        """The FeetCollisionList member."""
        member = self.get_member("FeetCollisionList")
        if isinstance(member, members.SyncList):
            return member
        return None

    @feet_collision_list.setter
    def feet_collision_list(self, value: members.SyncList) -> None:
        """Set the FeetCollisionList member."""
        self.set_member("FeetCollisionList", value)

    @property
    def head_max_fix_distance(self) -> np.float32 | None:
        """The HeadMaxFixDistance field value."""
        member = self.get_member("HeadMaxFixDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_max_fix_distance.setter
    def head_max_fix_distance(self, value: np.float32) -> None:
        """Set the HeadMaxFixDistance field value."""
        member = self.get_member("HeadMaxFixDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadMaxFixDistance", fields.FieldFloat(value=value)
            )

    @property
    def force_use_feet_proxies(self) -> bool | None:
        """The ForceUseFeetProxies field value."""
        member = self.get_member("ForceUseFeetProxies")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_use_feet_proxies.setter
    def force_use_feet_proxies(self, value: bool) -> None:
        """Set the ForceUseFeetProxies field value."""
        member = self.get_member("ForceUseFeetProxies")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceUseFeetProxies", fields.FieldBool(value=value)
            )

    @property
    def force_use_pelvis_proxy(self) -> bool | None:
        """The ForceUsePelvisProxy field value."""
        member = self.get_member("ForceUsePelvisProxy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_use_pelvis_proxy.setter
    def force_use_pelvis_proxy(self, value: bool) -> None:
        """Set the ForceUsePelvisProxy field value."""
        member = self.get_member("ForceUsePelvisProxy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceUsePelvisProxy", fields.FieldBool(value=value)
            )

    @property
    def force_use_chest_proxy(self) -> bool | None:
        """The ForceUseChestProxy field value."""
        member = self.get_member("ForceUseChestProxy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_use_chest_proxy.setter
    def force_use_chest_proxy(self, value: bool) -> None:
        """Set the ForceUseChestProxy field value."""
        member = self.get_member("ForceUseChestProxy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceUseChestProxy", fields.FieldBool(value=value)
            )

    @property
    def force_use_elbow_proxies(self) -> bool | None:
        """The ForceUseElbowProxies field value."""
        member = self.get_member("ForceUseElbowProxies")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_use_elbow_proxies.setter
    def force_use_elbow_proxies(self, value: bool) -> None:
        """Set the ForceUseElbowProxies field value."""
        member = self.get_member("ForceUseElbowProxies")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceUseElbowProxies", fields.FieldBool(value=value)
            )

    @property
    def force_use_knee_proxies(self) -> bool | None:
        """The ForceUseKneeProxies field value."""
        member = self.get_member("ForceUseKneeProxies")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_use_knee_proxies.setter
    def force_use_knee_proxies(self, value: bool) -> None:
        """Set the ForceUseKneeProxies field value."""
        member = self.get_member("ForceUseKneeProxies")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceUseKneeProxies", fields.FieldBool(value=value)
            )

    @property
    def feet_calibrated(self) -> bool | None:
        """The FeetCalibrated field value."""
        member = self.get_member("FeetCalibrated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_calibrated.setter
    def feet_calibrated(self, value: bool) -> None:
        """Set the FeetCalibrated field value."""
        member = self.get_member("FeetCalibrated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetCalibrated", fields.FieldBool(value=value)
            )

    @property
    def pelvis_calibrated(self) -> bool | None:
        """The PelvisCalibrated field value."""
        member = self.get_member("PelvisCalibrated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pelvis_calibrated.setter
    def pelvis_calibrated(self, value: bool) -> None:
        """Set the PelvisCalibrated field value."""
        member = self.get_member("PelvisCalibrated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PelvisCalibrated", fields.FieldBool(value=value)
            )

    @property
    def ground_check_height_ratio(self) -> np.float32 | None:
        """The GroundCheckHeightRatio field value."""
        member = self.get_member("GroundCheckHeightRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ground_check_height_ratio.setter
    def ground_check_height_ratio(self, value: np.float32) -> None:
        """Set the GroundCheckHeightRatio field value."""
        member = self.get_member("GroundCheckHeightRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroundCheckHeightRatio", fields.FieldFloat(value=value)
            )

    @property
    def feet_hover_height(self) -> np.float32 | None:
        """The FeetHoverHeight field value."""
        member = self.get_member("FeetHoverHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_hover_height.setter
    def feet_hover_height(self, value: np.float32) -> None:
        """Set the FeetHoverHeight field value."""
        member = self.get_member("FeetHoverHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetHoverHeight", fields.FieldFloat(value=value)
            )

    @property
    def feet_hover_smooth_speed(self) -> np.float32 | None:
        """The FeetHoverSmoothSpeed field value."""
        member = self.get_member("FeetHoverSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_hover_smooth_speed.setter
    def feet_hover_smooth_speed(self, value: np.float32) -> None:
        """Set the FeetHoverSmoothSpeed field value."""
        member = self.get_member("FeetHoverSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetHoverSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def min_feet_transition_speed(self) -> np.float32 | None:
        """The MinFeetTransitionSpeed field value."""
        member = self.get_member("MinFeetTransitionSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_feet_transition_speed.setter
    def min_feet_transition_speed(self, value: np.float32) -> None:
        """Set the MinFeetTransitionSpeed field value."""
        member = self.get_member("MinFeetTransitionSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinFeetTransitionSpeed", fields.FieldFloat(value=value)
            )

    @property
    def max_feet_transition_speed(self) -> np.float32 | None:
        """The MaxFeetTransitionSpeed field value."""
        member = self.get_member("MaxFeetTransitionSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_feet_transition_speed.setter
    def max_feet_transition_speed(self, value: np.float32) -> None:
        """Set the MaxFeetTransitionSpeed field value."""
        member = self.get_member("MaxFeetTransitionSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxFeetTransitionSpeed", fields.FieldFloat(value=value)
            )

    @property
    def gait_feet_transition_speed_multiplier(self) -> np.float32 | None:
        """The GaitFeetTransitionSpeedMultiplier field value."""
        member = self.get_member("GaitFeetTransitionSpeedMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gait_feet_transition_speed_multiplier.setter
    def gait_feet_transition_speed_multiplier(self, value: np.float32) -> None:
        """Set the GaitFeetTransitionSpeedMultiplier field value."""
        member = self.get_member("GaitFeetTransitionSpeedMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GaitFeetTransitionSpeedMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def feet_hover_tilt(self) -> np.float32 | None:
        """The FeetHoverTilt field value."""
        member = self.get_member("FeetHoverTilt")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_hover_tilt.setter
    def feet_hover_tilt(self, value: np.float32) -> None:
        """Set the FeetHoverTilt field value."""
        member = self.get_member("FeetHoverTilt")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetHoverTilt", fields.FieldFloat(value=value)
            )

    @property
    def left_foot_float_offset(self) -> primitives.Float3 | None:
        """The LeftFootFloatOffset field value."""
        member = self.get_member("LeftFootFloatOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_foot_float_offset.setter
    def left_foot_float_offset(self, value: primitives.Float3) -> None:
        """Set the LeftFootFloatOffset field value."""
        member = self.get_member("LeftFootFloatOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftFootFloatOffset", fields.FieldFloat3(value=value)
            )

    @property
    def right_foot_float_offset(self) -> primitives.Float3 | None:
        """The RightFootFloatOffset field value."""
        member = self.get_member("RightFootFloatOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_foot_float_offset.setter
    def right_foot_float_offset(self, value: primitives.Float3) -> None:
        """Set the RightFootFloatOffset field value."""
        member = self.get_member("RightFootFloatOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightFootFloatOffset", fields.FieldFloat3(value=value)
            )

    @property
    def left_foot_root_height(self) -> np.float32 | None:
        """The LeftFootRootHeight field value."""
        member = self.get_member("LeftFootRootHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_foot_root_height.setter
    def left_foot_root_height(self, value: np.float32) -> None:
        """Set the LeftFootRootHeight field value."""
        member = self.get_member("LeftFootRootHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftFootRootHeight", fields.FieldFloat(value=value)
            )

    @property
    def right_foot_root_height(self) -> np.float32 | None:
        """The RightFootRootHeight field value."""
        member = self.get_member("RightFootRootHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_foot_root_height.setter
    def right_foot_root_height(self, value: np.float32) -> None:
        """Set the RightFootRootHeight field value."""
        member = self.get_member("RightFootRootHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightFootRootHeight", fields.FieldFloat(value=value)
            )

    @property
    def foot_float_speed(self) -> np.float32 | None:
        """The FootFloatSpeed field value."""
        member = self.get_member("FootFloatSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_float_speed.setter
    def foot_float_speed(self, value: np.float32) -> None:
        """Set the FootFloatSpeed field value."""
        member = self.get_member("FootFloatSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootFloatSpeed", fields.FieldFloat(value=value)
            )

    @property
    def foot_float_angle_magnitude(self) -> np.float32 | None:
        """The FootFloatAngleMagnitude field value."""
        member = self.get_member("FootFloatAngleMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_float_angle_magnitude.setter
    def foot_float_angle_magnitude(self, value: np.float32) -> None:
        """Set the FootFloatAngleMagnitude field value."""
        member = self.get_member("FootFloatAngleMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootFloatAngleMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def foot_float_offset_magnitude(self) -> np.float32 | None:
        """The FootFloatOffsetMagnitude field value."""
        member = self.get_member("FootFloatOffsetMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @foot_float_offset_magnitude.setter
    def foot_float_offset_magnitude(self, value: np.float32) -> None:
        """Set the FootFloatOffsetMagnitude field value."""
        member = self.get_member("FootFloatOffsetMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FootFloatOffsetMagnitude", fields.FieldFloat(value=value)
            )

    @property
    def feet_float_velocity_force(self) -> np.float32 | None:
        """The FeetFloatVelocityForce field value."""
        member = self.get_member("FeetFloatVelocityForce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_float_velocity_force.setter
    def feet_float_velocity_force(self, value: np.float32) -> None:
        """Set the FeetFloatVelocityForce field value."""
        member = self.get_member("FeetFloatVelocityForce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetFloatVelocityForce", fields.FieldFloat(value=value)
            )

    @property
    def feet_float_velocity_dampening_speed(self) -> np.float32 | None:
        """The FeetFloatVelocityDampeningSpeed field value."""
        member = self.get_member("FeetFloatVelocityDampeningSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @feet_float_velocity_dampening_speed.setter
    def feet_float_velocity_dampening_speed(self, value: np.float32) -> None:
        """Set the FeetFloatVelocityDampeningSpeed field value."""
        member = self.get_member("FeetFloatVelocityDampeningSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FeetFloatVelocityDampeningSpeed", fields.FieldFloat(value=value)
            )

    @property
    def max_feet_velocity_offset(self) -> np.float32 | None:
        """The MaxFeetVelocityOffset field value."""
        member = self.get_member("MaxFeetVelocityOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_feet_velocity_offset.setter
    def max_feet_velocity_offset(self, value: np.float32) -> None:
        """Set the MaxFeetVelocityOffset field value."""
        member = self.get_member("MaxFeetVelocityOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxFeetVelocityOffset", fields.FieldFloat(value=value)
            )

    @property
    def velocity_average_rate(self) -> np.float32 | None:
        """The VelocityAverageRate field value."""
        member = self.get_member("VelocityAverageRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @velocity_average_rate.setter
    def velocity_average_rate(self, value: np.float32) -> None:
        """Set the VelocityAverageRate field value."""
        member = self.get_member("VelocityAverageRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VelocityAverageRate", fields.FieldFloat(value=value)
            )

    @property
    def hover_velocity_threshold(self) -> np.float32 | None:
        """The HoverVelocityThreshold field value."""
        member = self.get_member("HoverVelocityThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hover_velocity_threshold.setter
    def hover_velocity_threshold(self, value: np.float32) -> None:
        """Set the HoverVelocityThreshold field value."""
        member = self.get_member("HoverVelocityThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoverVelocityThreshold", fields.FieldFloat(value=value)
            )

    @property
    def horizontal_body_angle(self) -> np.float32 | None:
        """The HorizontalBodyAngle field value."""
        member = self.get_member("HorizontalBodyAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_body_angle.setter
    def horizontal_body_angle(self, value: np.float32) -> None:
        """Set the HorizontalBodyAngle field value."""
        member = self.get_member("HorizontalBodyAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HorizontalBodyAngle", fields.FieldFloat(value=value)
            )

    @property
    def supress_walk_animation_when_horizontal(self) -> bool | None:
        """The SupressWalkAnimationWhenHorizontal field value."""
        member = self.get_member("SupressWalkAnimationWhenHorizontal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @supress_walk_animation_when_horizontal.setter
    def supress_walk_animation_when_horizontal(self, value: bool) -> None:
        """Set the SupressWalkAnimationWhenHorizontal field value."""
        member = self.get_member("SupressWalkAnimationWhenHorizontal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SupressWalkAnimationWhenHorizontal", fields.FieldBool(value=value)
            )

    @property
    def always_use_trackers_when_horizontal(self) -> bool | None:
        """The AlwaysUseTrackersWhenHorizontal field value."""
        member = self.get_member("AlwaysUseTrackersWhenHorizontal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @always_use_trackers_when_horizontal.setter
    def always_use_trackers_when_horizontal(self, value: bool) -> None:
        """Set the AlwaysUseTrackersWhenHorizontal field value."""
        member = self.get_member("AlwaysUseTrackersWhenHorizontal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlwaysUseTrackersWhenHorizontal", fields.FieldBool(value=value)
            )

    @property
    def gaits(self) -> members.SyncList | None:
        """The Gaits member."""
        member = self.get_member("Gaits")
        if isinstance(member, members.SyncList):
            return member
        return None

    @gaits.setter
    def gaits(self, value: members.SyncList) -> None:
        """Set the Gaits member."""
        self.set_member("Gaits", value)

    @property
    def gait_transition_speed(self) -> np.float32 | None:
        """The GaitTransitionSpeed field value."""
        member = self.get_member("GaitTransitionSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gait_transition_speed.setter
    def gait_transition_speed(self, value: np.float32) -> None:
        """Set the GaitTransitionSpeed field value."""
        member = self.get_member("GaitTransitionSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GaitTransitionSpeed", fields.FieldFloat(value=value)
            )

    @property
    def gait_movement_direction_smooth_speed(self) -> np.float32 | None:
        """The GaitMovementDirectionSmoothSpeed field value."""
        member = self.get_member("GaitMovementDirectionSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gait_movement_direction_smooth_speed.setter
    def gait_movement_direction_smooth_speed(self, value: np.float32) -> None:
        """Set the GaitMovementDirectionSmoothSpeed field value."""
        member = self.get_member("GaitMovementDirectionSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GaitMovementDirectionSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def rig_colliders_radius_ratio(self) -> np.float32 | None:
        """The RigCollidersRadiusRatio field value."""
        member = self.get_member("RigCollidersRadiusRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rig_colliders_radius_ratio.setter
    def rig_colliders_radius_ratio(self, value: np.float32) -> None:
        """Set the RigCollidersRadiusRatio field value."""
        member = self.get_member("RigCollidersRadiusRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RigCollidersRadiusRatio", fields.FieldFloat(value=value)
            )

    @property
    def left_hand_rotation_offset(self) -> primitives.FloatQ | None:
        """The LeftHandRotationOffset field value."""
        member = self.get_member("LeftHandRotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_hand_rotation_offset.setter
    def left_hand_rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the LeftHandRotationOffset field value."""
        member = self.get_member("LeftHandRotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftHandRotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def right_hand_rotation_offset(self) -> primitives.FloatQ | None:
        """The RightHandRotationOffset field value."""
        member = self.get_member("RightHandRotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_hand_rotation_offset.setter
    def right_hand_rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the RightHandRotationOffset field value."""
        member = self.get_member("RightHandRotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightHandRotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def current_average_velocity(self) -> np.float32 | None:
        """The CurrentAverageVelocity field value."""
        member = self.get_member("CurrentAverageVelocity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_average_velocity.setter
    def current_average_velocity(self, value: np.float32) -> None:
        """Set the CurrentAverageVelocity field value."""
        member = self.get_member("CurrentAverageVelocity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentAverageVelocity", fields.FieldFloat(value=value)
            )

    @property
    def current_on_ground(self) -> bool | None:
        """The CurrentOnGround field value."""
        member = self.get_member("CurrentOnGround")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_on_ground.setter
    def current_on_ground(self, value: bool) -> None:
        """Set the CurrentOnGround field value."""
        member = self.get_member("CurrentOnGround")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentOnGround", fields.FieldBool(value=value)
            )

    @property
    def current_gait_index(self) -> np.int32 | None:
        """The CurrentGaitIndex field value."""
        member = self.get_member("CurrentGaitIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_gait_index.setter
    def current_gait_index(self, value: np.int32) -> None:
        """Set the CurrentGaitIndex field value."""
        member = self.get_member("CurrentGaitIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentGaitIndex", fields.FieldInt(value=value)
            )

    @property
    def locomotion_controller(self) -> str | None:
        """Target ID of the _locomotionController reference (targets LocomotionController)."""
        member = self.get_member("_locomotionController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locomotion_controller.setter
    def locomotion_controller(self, target: str | LocomotionController | None) -> None:
        """Set the _locomotionController reference by target ID or LocomotionController instance."""
        target_id: str | None = target.id if isinstance(target, LocomotionController) else target  # type: ignore[assignment]
        member = self.get_member("_locomotionController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_locomotionController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LocomotionController'),
            )

    @property
    def left_hand_node(self) -> str | None:
        """Target ID of the _leftHandNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_leftHandNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_node.setter
    def left_hand_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _leftHandNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def right_hand_node(self) -> str | None:
        """Target ID of the _rightHandNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_rightHandNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_node.setter
    def right_hand_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _rightHandNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def left_elbow_node(self) -> str | None:
        """Target ID of the _leftElbowNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_leftElbowNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_elbow_node.setter
    def left_elbow_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _leftElbowNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_leftElbowNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftElbowNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def right_elbow_node(self) -> str | None:
        """Target ID of the _rightElbowNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_rightElbowNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_elbow_node.setter
    def right_elbow_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _rightElbowNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_rightElbowNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightElbowNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def left_foot_node(self) -> str | None:
        """Target ID of the _leftFootNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_leftFootNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_node.setter
    def left_foot_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _leftFootNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def right_foot_node(self) -> str | None:
        """Target ID of the _rightFootNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_rightFootNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_node.setter
    def right_foot_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _rightFootNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def left_knee_node(self) -> str | None:
        """Target ID of the _leftKneeNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_leftKneeNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_knee_node.setter
    def left_knee_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _leftKneeNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_leftKneeNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftKneeNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def right_knee_node(self) -> str | None:
        """Target ID of the _rightKneeNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_rightKneeNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_knee_node.setter
    def right_knee_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _rightKneeNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_rightKneeNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightKneeNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def head_node(self) -> str | None:
        """Target ID of the _headNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_headNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head_node.setter
    def head_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _headNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_headNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def pelvis_node(self) -> str | None:
        """Target ID of the _pelvisNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_pelvisNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_node.setter
    def pelvis_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _pelvisNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def chest_node(self) -> str | None:
        """Target ID of the _chestNode reference (targets AvatarPoseNode)."""
        member = self.get_member("_chestNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chest_node.setter
    def chest_node(self, target: str | AvatarPoseNode | None) -> None:
        """Set the _chestNode reference by target ID or AvatarPoseNode instance."""
        target_id: str | None = target.id if isinstance(target, AvatarPoseNode) else target  # type: ignore[assignment]
        member = self.get_member("_chestNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_chestNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarPoseNode'),
            )

    @property
    def head_proxy(self) -> str | None:
        """Target ID of the _headProxy reference (targets Slot)."""
        member = self.get_member("_headProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head_proxy.setter
    def head_proxy(self, target: str | Slot | None) -> None:
        """Set the _headProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_headProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def pelvis_proxy(self) -> str | None:
        """Target ID of the _pelvisProxy reference (targets Slot)."""
        member = self.get_member("_pelvisProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_proxy.setter
    def pelvis_proxy(self, target: str | Slot | None) -> None:
        """Set the _pelvisProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def chest_proxy(self) -> str | None:
        """Target ID of the _chestProxy reference (targets Slot)."""
        member = self.get_member("_chestProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chest_proxy.setter
    def chest_proxy(self, target: str | Slot | None) -> None:
        """Set the _chestProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_chestProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_chestProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_hand_proxy(self) -> str | None:
        """Target ID of the _leftHandProxy reference (targets Slot)."""
        member = self.get_member("_leftHandProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_proxy.setter
    def left_hand_proxy(self, target: str | Slot | None) -> None:
        """Set the _leftHandProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_hand_proxy(self) -> str | None:
        """Target ID of the _rightHandProxy reference (targets Slot)."""
        member = self.get_member("_rightHandProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_proxy.setter
    def right_hand_proxy(self, target: str | Slot | None) -> None:
        """Set the _rightHandProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_elbow_proxy(self) -> str | None:
        """Target ID of the _leftElbowProxy reference (targets Slot)."""
        member = self.get_member("_leftElbowProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_elbow_proxy.setter
    def left_elbow_proxy(self, target: str | Slot | None) -> None:
        """Set the _leftElbowProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftElbowProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftElbowProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_elbow_proxy(self) -> str | None:
        """Target ID of the _rightElbowProxy reference (targets Slot)."""
        member = self.get_member("_rightElbowProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_elbow_proxy.setter
    def right_elbow_proxy(self, target: str | Slot | None) -> None:
        """Set the _rightElbowProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightElbowProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightElbowProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_foot_proxy(self) -> str | None:
        """Target ID of the _leftFootProxy reference (targets Slot)."""
        member = self.get_member("_leftFootProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_proxy.setter
    def left_foot_proxy(self, target: str | Slot | None) -> None:
        """Set the _leftFootProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_foot_proxy(self) -> str | None:
        """Target ID of the _rightFootProxy reference (targets Slot)."""
        member = self.get_member("_rightFootProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_proxy.setter
    def right_foot_proxy(self, target: str | Slot | None) -> None:
        """Set the _rightFootProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_knee_proxy(self) -> str | None:
        """Target ID of the _leftKneeProxy reference (targets Slot)."""
        member = self.get_member("_leftKneeProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_knee_proxy.setter
    def left_knee_proxy(self, target: str | Slot | None) -> None:
        """Set the _leftKneeProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftKneeProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftKneeProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_knee_proxy(self) -> str | None:
        """Target ID of the _rightKneeProxy reference (targets Slot)."""
        member = self.get_member("_rightKneeProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_knee_proxy.setter
    def right_knee_proxy(self, target: str | Slot | None) -> None:
        """Set the _rightKneeProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightKneeProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightKneeProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def left_knee_default_proxy(self) -> str | None:
        """Target ID of the _leftKneeDefaultProxy reference (targets Slot)."""
        member = self.get_member("_leftKneeDefaultProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_knee_default_proxy.setter
    def left_knee_default_proxy(self, target: str | Slot | None) -> None:
        """Set the _leftKneeDefaultProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_leftKneeDefaultProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftKneeDefaultProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def right_knee_default_proxy(self) -> str | None:
        """Target ID of the _rightKneeDefaultProxy reference (targets Slot)."""
        member = self.get_member("_rightKneeDefaultProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_knee_default_proxy.setter
    def right_knee_default_proxy(self, target: str | Slot | None) -> None:
        """Set the _rightKneeDefaultProxy reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_rightKneeDefaultProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightKneeDefaultProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def head_target_pos(self) -> str | None:
        """Target ID of the _headTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_headTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head_target_pos.setter
    def head_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _headTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def head_target_rot(self) -> str | None:
        """Target ID of the _headTargetRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_headTargetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head_target_rot.setter
    def head_target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _headTargetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headTargetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headTargetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def pelvis_target_pos(self) -> str | None:
        """Target ID of the _pelvisTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_pelvisTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_target_pos.setter
    def pelvis_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _pelvisTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def pelvis_target_rot(self) -> str | None:
        """Target ID of the _pelvisTargetRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_pelvisTargetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_target_rot.setter
    def pelvis_target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _pelvisTargetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisTargetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisTargetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def chest_target_pos(self) -> str | None:
        """Target ID of the _chestTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_chestTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chest_target_pos.setter
    def chest_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _chestTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_chestTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_chestTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_hand_target_pos(self) -> str | None:
        """Target ID of the _leftHandTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_leftHandTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_target_pos.setter
    def left_hand_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftHandTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_hand_target_rot(self) -> str | None:
        """Target ID of the _leftHandTargetRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_leftHandTargetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand_target_rot.setter
    def left_hand_target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _leftHandTargetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftHandTargetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftHandTargetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def right_hand_target_pos(self) -> str | None:
        """Target ID of the _rightHandTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_rightHandTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_target_pos.setter
    def right_hand_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightHandTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_hand_target_rot(self) -> str | None:
        """Target ID of the _rightHandTargetRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_rightHandTargetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand_target_rot.setter
    def right_hand_target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rightHandTargetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightHandTargetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightHandTargetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def left_elbow_target_pos(self) -> str | None:
        """Target ID of the _leftElbowTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_leftElbowTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_elbow_target_pos.setter
    def left_elbow_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftElbowTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftElbowTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftElbowTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_elbow_target_pos(self) -> str | None:
        """Target ID of the _rightElbowTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_rightElbowTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_elbow_target_pos.setter
    def right_elbow_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightElbowTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightElbowTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightElbowTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_foot_target_pos(self) -> str | None:
        """Target ID of the _leftFootTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_leftFootTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_target_pos.setter
    def left_foot_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftFootTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_foot_target_rot(self) -> str | None:
        """Target ID of the _leftFootTargetRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_leftFootTargetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_target_rot.setter
    def left_foot_target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _leftFootTargetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootTargetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootTargetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def right_foot_target_pos(self) -> str | None:
        """Target ID of the _rightFootTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_rightFootTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_target_pos.setter
    def right_foot_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightFootTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_foot_target_rot(self) -> str | None:
        """Target ID of the _rightFootTargetRot reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_rightFootTargetRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_target_rot.setter
    def right_foot_target_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rightFootTargetRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootTargetRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootTargetRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def left_knee_target_pos(self) -> str | None:
        """Target ID of the _leftKneeTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_leftKneeTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_knee_target_pos.setter
    def left_knee_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftKneeTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftKneeTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftKneeTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_knee_target_pos(self) -> str | None:
        """Target ID of the _rightKneeTargetPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_rightKneeTargetPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_knee_target_pos.setter
    def right_knee_target_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightKneeTargetPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightKneeTargetPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightKneeTargetPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def pelvis_position_weight(self) -> str | None:
        """Target ID of the _pelvisPositionWeight reference (targets IField[np.float32])."""
        member = self.get_member("_pelvisPositionWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_position_weight.setter
    def pelvis_position_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _pelvisPositionWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisPositionWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisPositionWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def pelvis_rotation_weight(self) -> str | None:
        """Target ID of the _pelvisRotationWeight reference (targets IField[np.float32])."""
        member = self.get_member("_pelvisRotationWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pelvis_rotation_weight.setter
    def pelvis_rotation_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _pelvisRotationWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_pelvisRotationWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pelvisRotationWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def chest_weight(self) -> str | None:
        """Target ID of the _chestWeight reference (targets IField[np.float32])."""
        member = self.get_member("_chestWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chest_weight.setter
    def chest_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _chestWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_chestWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_chestWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def locomotion_weight(self) -> str | None:
        """Target ID of the _locomotionWeight reference (targets IField[np.float32])."""
        member = self.get_member("_locomotionWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locomotion_weight.setter
    def locomotion_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _locomotionWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_locomotionWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_locomotionWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def left_leg_position_weight(self) -> str | None:
        """Target ID of the _leftLegPositionWeight reference (targets IField[np.float32])."""
        member = self.get_member("_leftLegPositionWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_leg_position_weight.setter
    def left_leg_position_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _leftLegPositionWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftLegPositionWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftLegPositionWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def left_leg_rotation_weight(self) -> str | None:
        """Target ID of the _leftLegRotationWeight reference (targets IField[np.float32])."""
        member = self.get_member("_leftLegRotationWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_leg_rotation_weight.setter
    def left_leg_rotation_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _leftLegRotationWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftLegRotationWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftLegRotationWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def right_leg_position_weight(self) -> str | None:
        """Target ID of the _rightLegPositionWeight reference (targets IField[np.float32])."""
        member = self.get_member("_rightLegPositionWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_leg_position_weight.setter
    def right_leg_position_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _rightLegPositionWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightLegPositionWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightLegPositionWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def right_leg_rotation_weight(self) -> str | None:
        """Target ID of the _rightLegRotationWeight reference (targets IField[np.float32])."""
        member = self.get_member("_rightLegRotationWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_leg_rotation_weight.setter
    def right_leg_rotation_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _rightLegRotationWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightLegRotationWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightLegRotationWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def left_knee_bend_weight(self) -> str | None:
        """Target ID of the _leftKneeBendWeight reference (targets IField[np.float32])."""
        member = self.get_member("_leftKneeBendWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_knee_bend_weight.setter
    def left_knee_bend_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _leftKneeBendWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftKneeBendWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftKneeBendWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def right_knee_bend_weight(self) -> str | None:
        """Target ID of the _rightKneeBendWeight reference (targets IField[np.float32])."""
        member = self.get_member("_rightKneeBendWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_knee_bend_weight.setter
    def right_knee_bend_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _rightKneeBendWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightKneeBendWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightKneeBendWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def left_elbow_bend_weight(self) -> str | None:
        """Target ID of the _leftElbowBendWeight reference (targets IField[np.float32])."""
        member = self.get_member("_leftElbowBendWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_elbow_bend_weight.setter
    def left_elbow_bend_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _leftElbowBendWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftElbowBendWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftElbowBendWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def right_elbow_bend_weight(self) -> str | None:
        """Target ID of the _rightElbowBendWeight reference (targets IField[np.float32])."""
        member = self.get_member("_rightElbowBendWeight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_elbow_bend_weight.setter
    def right_elbow_bend_weight(self, target: str | IField[np.float32] | None) -> None:
        """Set the _rightElbowBendWeight reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightElbowBendWeight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightElbowBendWeight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def left_foot_offset(self) -> str | None:
        """Target ID of the _leftFootOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_leftFootOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_foot_offset.setter
    def left_foot_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftFootOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftFootOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftFootOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_foot_offset(self) -> str | None:
        """Target ID of the _rightFootOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_rightFootOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_foot_offset.setter
    def right_foot_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightFootOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightFootOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightFootOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_foot_relative_to_root(self) -> primitives.FloatQ | None:
        """The _leftFootRelativeToRoot field value."""
        member = self.get_member("_leftFootRelativeToRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_foot_relative_to_root.setter
    def left_foot_relative_to_root(self, value: primitives.FloatQ) -> None:
        """Set the _leftFootRelativeToRoot field value."""
        member = self.get_member("_leftFootRelativeToRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_leftFootRelativeToRoot", fields.FieldFloatQ(value=value)
            )

    @property
    def right_foot_relative_to_root(self) -> primitives.FloatQ | None:
        """The _rightFootRelativeToRoot field value."""
        member = self.get_member("_rightFootRelativeToRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_foot_relative_to_root.setter
    def right_foot_relative_to_root(self, value: primitives.FloatQ) -> None:
        """Set the _rightFootRelativeToRoot field value."""
        member = self.get_member("_rightFootRelativeToRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rightFootRelativeToRoot", fields.FieldFloatQ(value=value)
            )

    @property
    def locomotion_offset(self) -> str | None:
        """Target ID of the _locomotionOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_locomotionOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locomotion_offset.setter
    def locomotion_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _locomotionOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_locomotionOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_locomotionOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def simplified_collider_enabled(self) -> str | None:
        """Target ID of the _simplifiedColliderEnabled reference (targets IField[bool])."""
        member = self.get_member("_simplifiedColliderEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @simplified_collider_enabled.setter
    def simplified_collider_enabled(self, target: str | IField[bool] | None) -> None:
        """Set the _simplifiedColliderEnabled reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_simplifiedColliderEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_simplifiedColliderEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def rig_colliders_enabled_states(self) -> members.SyncList | None:
        """The _rigCollidersEnabledStates member."""
        member = self.get_member("_rigCollidersEnabledStates")
        if isinstance(member, members.SyncList):
            return member
        return None

    @rig_colliders_enabled_states.setter
    def rig_colliders_enabled_states(self, value: members.SyncList) -> None:
        """Set the _rigCollidersEnabledStates member."""
        self.set_member("_rigCollidersEnabledStates", value)

    @property
    def horizontal_tracking_locked(self) -> bool | None:
        """The _horizontalTrackingLocked field value."""
        member = self.get_member("_horizontalTrackingLocked")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @horizontal_tracking_locked.setter
    def horizontal_tracking_locked(self, value: bool) -> None:
        """Set the _horizontalTrackingLocked field value."""
        member = self.get_member("_horizontalTrackingLocked")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_horizontalTrackingLocked", fields.FieldBool(value=value)
            )

