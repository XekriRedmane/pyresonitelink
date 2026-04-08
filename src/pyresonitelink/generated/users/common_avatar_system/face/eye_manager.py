"""Generated component: EyeManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ieye_data_source_component import IEyeDataSourceComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EyeManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.EyeManager.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.EyeManager"

    def __init__(self, target_point: primitives.Float3 | None = None, left_eye_target_point: primitives.Float3 | None = None, right_eye_target_point: primitives.Float3 | None = None, left_eye_close: primitives.Float | None = None, right_eye_close: primitives.Float | None = None, combined_eye_close: primitives.Float | None = None, left_eye_pupil_size_millimeters: primitives.Float | None = None, right_eye_pupil_size_millimeters: primitives.Float | None = None, combined_eye_pupil_size_millimeters: primitives.Float | None = None, left_eye_widen: primitives.Float | None = None, right_eye_widen: primitives.Float | None = None, combined_eye_widen: primitives.Float | None = None, left_eye_squeeze: primitives.Float | None = None, right_eye_squeeze: primitives.Float | None = None, combined_eye_squeeze: primitives.Float | None = None, left_eye_frown: primitives.Float | None = None, right_eye_frown: primitives.Float | None = None, combined_eye_frown: primitives.Float | None = None, left_eye_inner_brow_vertical: primitives.Float | None = None, right_eye_inner_brow_vertical: primitives.Float | None = None, combined_eye_inner_brow_vertical: primitives.Float | None = None, left_eye_outer_brow_vertical: primitives.Float | None = None, right_eye_outer_brow_vertical: primitives.Float | None = None, combined_eye_outer_brow_vertical: primitives.Float | None = None, eye_data_source: str | IEyeDataSourceComponent | None = None, simulating_user: str | User | None = None, simulate_on_host: primitives.Bool | None = None, ignore_local_user_head: primitives.Bool | None = None, user_head_weight: primitives.Float | None = None, user_hand_weight: primitives.Float | None = None, gripping_hand_weight: primitives.Float | None = None, camera_weight: primitives.Float | None = None, forced_camera_weight: primitives.Float | None = None, eye_reference: str | Slot | None = None, eye_separation: primitives.Float | None = None, saccade_speed: primitives.Float | None = None, look_target_root: str | Slot | None = None, look_target_local_point: primitives.Float3 | None = None, left_eye_target_offset: primitives.Float3 | None = None, right_eye_target_offset: primitives.Float3 | None = None, look_target_offset: primitives.Float3 | None = None, min_random_saccade_interval: primitives.Float | None = None, max_random_saccade_interval: primitives.Float | None = None, min_target_saccade_interval: primitives.Float | None = None, max_target_saccade_interval: primitives.Float | None = None, max_random_saccade_offset: primitives.Float | None = None, default_accept_angle: primitives.Float | None = None, default_break_angle: primitives.Float | None = None, head_accept_angle: primitives.Float | None = None, head_break_angle: primitives.Float | None = None, camera_accept_angle: primitives.Float | None = None, camera_break_angle: primitives.Float | None = None, hand_accept_angle: primitives.Float | None = None, hand_break_angle: primitives.Float | None = None, distance_compensation_exp: primitives.Float | None = None, left_eye_close_override: primitives.Float | None = None, right_eye_close_override: primitives.Float | None = None, min_blink_interval: primitives.Float | None = None, max_blink_interval: primitives.Float | None = None, blink_min_speed: primitives.Float | None = None, blink_max_speed: primitives.Float | None = None, blink_speed_spread: primitives.Float | None = None, min_pupil_size: primitives.Float | None = None, max_pupil_size: primitives.Float | None = None, pupil_size_noise_speed: primitives.Float | None = None, pupil_size_noise_offset: primitives.Float | None = None, eye_tracking_pupil_size_smooth_speed: primitives.Float | None = None, mini_expression_probability: primitives.Float | None = None, mini_expression_interval: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_point: Initial value for TargetPoint.
            left_eye_target_point: Initial value for LeftEyeTargetPoint.
            right_eye_target_point: Initial value for RightEyeTargetPoint.
            left_eye_close: Initial value for LeftEyeClose.
            right_eye_close: Initial value for RightEyeClose.
            combined_eye_close: Initial value for CombinedEyeClose.
            left_eye_pupil_size_millimeters: Initial value for LeftEyePupilSizeMillimeters.
            right_eye_pupil_size_millimeters: Initial value for RightEyePupilSizeMillimeters.
            combined_eye_pupil_size_millimeters: Initial value for CombinedEyePupilSizeMillimeters.
            left_eye_widen: Initial value for LeftEyeWiden.
            right_eye_widen: Initial value for RightEyeWiden.
            combined_eye_widen: Initial value for CombinedEyeWiden.
            left_eye_squeeze: Initial value for LeftEyeSqueeze.
            right_eye_squeeze: Initial value for RightEyeSqueeze.
            combined_eye_squeeze: Initial value for CombinedEyeSqueeze.
            left_eye_frown: Initial value for LeftEyeFrown.
            right_eye_frown: Initial value for RightEyeFrown.
            combined_eye_frown: Initial value for CombinedEyeFrown.
            left_eye_inner_brow_vertical: Initial value for LeftEyeInnerBrowVertical.
            right_eye_inner_brow_vertical: Initial value for RightEyeInnerBrowVertical.
            combined_eye_inner_brow_vertical: Initial value for CombinedEyeInnerBrowVertical.
            left_eye_outer_brow_vertical: Initial value for LeftEyeOuterBrowVertical.
            right_eye_outer_brow_vertical: Initial value for RightEyeOuterBrowVertical.
            combined_eye_outer_brow_vertical: Initial value for CombinedEyeOuterBrowVertical.
            eye_data_source: Initial value for EyeDataSource.
            simulating_user: Initial value for SimulatingUser.
            simulate_on_host: Initial value for SimulateOnHost.
            ignore_local_user_head: Initial value for IgnoreLocalUserHead.
            user_head_weight: Initial value for UserHeadWeight.
            user_hand_weight: Initial value for UserHandWeight.
            gripping_hand_weight: Initial value for GrippingHandWeight.
            camera_weight: Initial value for CameraWeight.
            forced_camera_weight: Initial value for ForcedCameraWeight.
            eye_reference: Initial value for EyeReference.
            eye_separation: Initial value for EyeSeparation.
            saccade_speed: Initial value for SaccadeSpeed.
            look_target_root: Initial value for LookTargetRoot.
            look_target_local_point: Initial value for LookTargetLocalPoint.
            left_eye_target_offset: Initial value for LeftEyeTargetOffset.
            right_eye_target_offset: Initial value for RightEyeTargetOffset.
            look_target_offset: Initial value for LookTargetOffset.
            min_random_saccade_interval: Initial value for MinRandomSaccadeInterval.
            max_random_saccade_interval: Initial value for MaxRandomSaccadeInterval.
            min_target_saccade_interval: Initial value for MinTargetSaccadeInterval.
            max_target_saccade_interval: Initial value for MaxTargetSaccadeInterval.
            max_random_saccade_offset: Initial value for MaxRandomSaccadeOffset.
            default_accept_angle: Initial value for DefaultAcceptAngle.
            default_break_angle: Initial value for DefaultBreakAngle.
            head_accept_angle: Initial value for HeadAcceptAngle.
            head_break_angle: Initial value for HeadBreakAngle.
            camera_accept_angle: Initial value for CameraAcceptAngle.
            camera_break_angle: Initial value for CameraBreakAngle.
            hand_accept_angle: Initial value for HandAcceptAngle.
            hand_break_angle: Initial value for HandBreakAngle.
            distance_compensation_exp: Initial value for DistanceCompensationExp.
            left_eye_close_override: Initial value for LeftEyeCloseOverride.
            right_eye_close_override: Initial value for RightEyeCloseOverride.
            min_blink_interval: Initial value for MinBlinkInterval.
            max_blink_interval: Initial value for MaxBlinkInterval.
            blink_min_speed: Initial value for BlinkMinSpeed.
            blink_max_speed: Initial value for BlinkMaxSpeed.
            blink_speed_spread: Initial value for BlinkSpeedSpread.
            min_pupil_size: Initial value for MinPupilSize.
            max_pupil_size: Initial value for MaxPupilSize.
            pupil_size_noise_speed: Initial value for PupilSizeNoiseSpeed.
            pupil_size_noise_offset: Initial value for PupilSizeNoiseOffset.
            eye_tracking_pupil_size_smooth_speed: Initial value for EyeTrackingPupilSizeSmoothSpeed.
            mini_expression_probability: Initial value for MiniExpressionProbability.
            mini_expression_interval: Initial value for MiniExpressionInterval.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_point is not None:
            self.target_point = target_point
        if left_eye_target_point is not None:
            self.left_eye_target_point = left_eye_target_point
        if right_eye_target_point is not None:
            self.right_eye_target_point = right_eye_target_point
        if left_eye_close is not None:
            self.left_eye_close = left_eye_close
        if right_eye_close is not None:
            self.right_eye_close = right_eye_close
        if combined_eye_close is not None:
            self.combined_eye_close = combined_eye_close
        if left_eye_pupil_size_millimeters is not None:
            self.left_eye_pupil_size_millimeters = left_eye_pupil_size_millimeters
        if right_eye_pupil_size_millimeters is not None:
            self.right_eye_pupil_size_millimeters = right_eye_pupil_size_millimeters
        if combined_eye_pupil_size_millimeters is not None:
            self.combined_eye_pupil_size_millimeters = combined_eye_pupil_size_millimeters
        if left_eye_widen is not None:
            self.left_eye_widen = left_eye_widen
        if right_eye_widen is not None:
            self.right_eye_widen = right_eye_widen
        if combined_eye_widen is not None:
            self.combined_eye_widen = combined_eye_widen
        if left_eye_squeeze is not None:
            self.left_eye_squeeze = left_eye_squeeze
        if right_eye_squeeze is not None:
            self.right_eye_squeeze = right_eye_squeeze
        if combined_eye_squeeze is not None:
            self.combined_eye_squeeze = combined_eye_squeeze
        if left_eye_frown is not None:
            self.left_eye_frown = left_eye_frown
        if right_eye_frown is not None:
            self.right_eye_frown = right_eye_frown
        if combined_eye_frown is not None:
            self.combined_eye_frown = combined_eye_frown
        if left_eye_inner_brow_vertical is not None:
            self.left_eye_inner_brow_vertical = left_eye_inner_brow_vertical
        if right_eye_inner_brow_vertical is not None:
            self.right_eye_inner_brow_vertical = right_eye_inner_brow_vertical
        if combined_eye_inner_brow_vertical is not None:
            self.combined_eye_inner_brow_vertical = combined_eye_inner_brow_vertical
        if left_eye_outer_brow_vertical is not None:
            self.left_eye_outer_brow_vertical = left_eye_outer_brow_vertical
        if right_eye_outer_brow_vertical is not None:
            self.right_eye_outer_brow_vertical = right_eye_outer_brow_vertical
        if combined_eye_outer_brow_vertical is not None:
            self.combined_eye_outer_brow_vertical = combined_eye_outer_brow_vertical
        if eye_data_source is not None:
            self.eye_data_source = eye_data_source
        if simulating_user is not None:
            self.simulating_user = simulating_user
        if simulate_on_host is not None:
            self.simulate_on_host = simulate_on_host
        if ignore_local_user_head is not None:
            self.ignore_local_user_head = ignore_local_user_head
        if user_head_weight is not None:
            self.user_head_weight = user_head_weight
        if user_hand_weight is not None:
            self.user_hand_weight = user_hand_weight
        if gripping_hand_weight is not None:
            self.gripping_hand_weight = gripping_hand_weight
        if camera_weight is not None:
            self.camera_weight = camera_weight
        if forced_camera_weight is not None:
            self.forced_camera_weight = forced_camera_weight
        if eye_reference is not None:
            self.eye_reference = eye_reference
        if eye_separation is not None:
            self.eye_separation = eye_separation
        if saccade_speed is not None:
            self.saccade_speed = saccade_speed
        if look_target_root is not None:
            self.look_target_root = look_target_root
        if look_target_local_point is not None:
            self.look_target_local_point = look_target_local_point
        if left_eye_target_offset is not None:
            self.left_eye_target_offset = left_eye_target_offset
        if right_eye_target_offset is not None:
            self.right_eye_target_offset = right_eye_target_offset
        if look_target_offset is not None:
            self.look_target_offset = look_target_offset
        if min_random_saccade_interval is not None:
            self.min_random_saccade_interval = min_random_saccade_interval
        if max_random_saccade_interval is not None:
            self.max_random_saccade_interval = max_random_saccade_interval
        if min_target_saccade_interval is not None:
            self.min_target_saccade_interval = min_target_saccade_interval
        if max_target_saccade_interval is not None:
            self.max_target_saccade_interval = max_target_saccade_interval
        if max_random_saccade_offset is not None:
            self.max_random_saccade_offset = max_random_saccade_offset
        if default_accept_angle is not None:
            self.default_accept_angle = default_accept_angle
        if default_break_angle is not None:
            self.default_break_angle = default_break_angle
        if head_accept_angle is not None:
            self.head_accept_angle = head_accept_angle
        if head_break_angle is not None:
            self.head_break_angle = head_break_angle
        if camera_accept_angle is not None:
            self.camera_accept_angle = camera_accept_angle
        if camera_break_angle is not None:
            self.camera_break_angle = camera_break_angle
        if hand_accept_angle is not None:
            self.hand_accept_angle = hand_accept_angle
        if hand_break_angle is not None:
            self.hand_break_angle = hand_break_angle
        if distance_compensation_exp is not None:
            self.distance_compensation_exp = distance_compensation_exp
        if left_eye_close_override is not None:
            self.left_eye_close_override = left_eye_close_override
        if right_eye_close_override is not None:
            self.right_eye_close_override = right_eye_close_override
        if min_blink_interval is not None:
            self.min_blink_interval = min_blink_interval
        if max_blink_interval is not None:
            self.max_blink_interval = max_blink_interval
        if blink_min_speed is not None:
            self.blink_min_speed = blink_min_speed
        if blink_max_speed is not None:
            self.blink_max_speed = blink_max_speed
        if blink_speed_spread is not None:
            self.blink_speed_spread = blink_speed_spread
        if min_pupil_size is not None:
            self.min_pupil_size = min_pupil_size
        if max_pupil_size is not None:
            self.max_pupil_size = max_pupil_size
        if pupil_size_noise_speed is not None:
            self.pupil_size_noise_speed = pupil_size_noise_speed
        if pupil_size_noise_offset is not None:
            self.pupil_size_noise_offset = pupil_size_noise_offset
        if eye_tracking_pupil_size_smooth_speed is not None:
            self.eye_tracking_pupil_size_smooth_speed = eye_tracking_pupil_size_smooth_speed
        if mini_expression_probability is not None:
            self.mini_expression_probability = mini_expression_probability
        if mini_expression_interval is not None:
            self.mini_expression_interval = mini_expression_interval

    @property
    def target_point(self) -> primitives.Float3 | None:
        """The TargetPoint field value."""
        member = self.get_member("TargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_point.setter
    def target_point(self, value: primitives.Float3) -> None:
        """Set the TargetPoint field value."""
        member = self.get_member("TargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def left_eye_target_point(self) -> primitives.Float3 | None:
        """The LeftEyeTargetPoint field value."""
        member = self.get_member("LeftEyeTargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_target_point.setter
    def left_eye_target_point(self, value: primitives.Float3) -> None:
        """Set the LeftEyeTargetPoint field value."""
        member = self.get_member("LeftEyeTargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeTargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def right_eye_target_point(self) -> primitives.Float3 | None:
        """The RightEyeTargetPoint field value."""
        member = self.get_member("RightEyeTargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_target_point.setter
    def right_eye_target_point(self, value: primitives.Float3) -> None:
        """Set the RightEyeTargetPoint field value."""
        member = self.get_member("RightEyeTargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeTargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def left_eye_close(self) -> primitives.Float | None:
        """The LeftEyeClose field value."""
        member = self.get_member("LeftEyeClose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_close.setter
    def left_eye_close(self, value: primitives.Float) -> None:
        """Set the LeftEyeClose field value."""
        member = self.get_member("LeftEyeClose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeClose", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_close(self) -> primitives.Float | None:
        """The RightEyeClose field value."""
        member = self.get_member("RightEyeClose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_close.setter
    def right_eye_close(self, value: primitives.Float) -> None:
        """Set the RightEyeClose field value."""
        member = self.get_member("RightEyeClose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeClose", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_close(self) -> primitives.Float | None:
        """The CombinedEyeClose field value."""
        member = self.get_member("CombinedEyeClose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_close.setter
    def combined_eye_close(self, value: primitives.Float) -> None:
        """Set the CombinedEyeClose field value."""
        member = self.get_member("CombinedEyeClose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyeClose", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_pupil_size_millimeters(self) -> primitives.Float | None:
        """The LeftEyePupilSizeMillimeters field value."""
        member = self.get_member("LeftEyePupilSizeMillimeters")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_pupil_size_millimeters.setter
    def left_eye_pupil_size_millimeters(self, value: primitives.Float) -> None:
        """Set the LeftEyePupilSizeMillimeters field value."""
        member = self.get_member("LeftEyePupilSizeMillimeters")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyePupilSizeMillimeters", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_pupil_size_millimeters(self) -> primitives.Float | None:
        """The RightEyePupilSizeMillimeters field value."""
        member = self.get_member("RightEyePupilSizeMillimeters")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_pupil_size_millimeters.setter
    def right_eye_pupil_size_millimeters(self, value: primitives.Float) -> None:
        """Set the RightEyePupilSizeMillimeters field value."""
        member = self.get_member("RightEyePupilSizeMillimeters")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyePupilSizeMillimeters", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_pupil_size_millimeters(self) -> primitives.Float | None:
        """The CombinedEyePupilSizeMillimeters field value."""
        member = self.get_member("CombinedEyePupilSizeMillimeters")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_pupil_size_millimeters.setter
    def combined_eye_pupil_size_millimeters(self, value: primitives.Float) -> None:
        """Set the CombinedEyePupilSizeMillimeters field value."""
        member = self.get_member("CombinedEyePupilSizeMillimeters")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyePupilSizeMillimeters", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_widen(self) -> primitives.Float | None:
        """The LeftEyeWiden field value."""
        member = self.get_member("LeftEyeWiden")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_widen.setter
    def left_eye_widen(self, value: primitives.Float) -> None:
        """Set the LeftEyeWiden field value."""
        member = self.get_member("LeftEyeWiden")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeWiden", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_widen(self) -> primitives.Float | None:
        """The RightEyeWiden field value."""
        member = self.get_member("RightEyeWiden")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_widen.setter
    def right_eye_widen(self, value: primitives.Float) -> None:
        """Set the RightEyeWiden field value."""
        member = self.get_member("RightEyeWiden")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeWiden", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_widen(self) -> primitives.Float | None:
        """The CombinedEyeWiden field value."""
        member = self.get_member("CombinedEyeWiden")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_widen.setter
    def combined_eye_widen(self, value: primitives.Float) -> None:
        """Set the CombinedEyeWiden field value."""
        member = self.get_member("CombinedEyeWiden")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyeWiden", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_squeeze(self) -> primitives.Float | None:
        """The LeftEyeSqueeze field value."""
        member = self.get_member("LeftEyeSqueeze")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_squeeze.setter
    def left_eye_squeeze(self, value: primitives.Float) -> None:
        """Set the LeftEyeSqueeze field value."""
        member = self.get_member("LeftEyeSqueeze")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeSqueeze", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_squeeze(self) -> primitives.Float | None:
        """The RightEyeSqueeze field value."""
        member = self.get_member("RightEyeSqueeze")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_squeeze.setter
    def right_eye_squeeze(self, value: primitives.Float) -> None:
        """Set the RightEyeSqueeze field value."""
        member = self.get_member("RightEyeSqueeze")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeSqueeze", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_squeeze(self) -> primitives.Float | None:
        """The CombinedEyeSqueeze field value."""
        member = self.get_member("CombinedEyeSqueeze")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_squeeze.setter
    def combined_eye_squeeze(self, value: primitives.Float) -> None:
        """Set the CombinedEyeSqueeze field value."""
        member = self.get_member("CombinedEyeSqueeze")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyeSqueeze", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_frown(self) -> primitives.Float | None:
        """The LeftEyeFrown field value."""
        member = self.get_member("LeftEyeFrown")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_frown.setter
    def left_eye_frown(self, value: primitives.Float) -> None:
        """Set the LeftEyeFrown field value."""
        member = self.get_member("LeftEyeFrown")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeFrown", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_frown(self) -> primitives.Float | None:
        """The RightEyeFrown field value."""
        member = self.get_member("RightEyeFrown")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_frown.setter
    def right_eye_frown(self, value: primitives.Float) -> None:
        """Set the RightEyeFrown field value."""
        member = self.get_member("RightEyeFrown")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeFrown", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_frown(self) -> primitives.Float | None:
        """The CombinedEyeFrown field value."""
        member = self.get_member("CombinedEyeFrown")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_frown.setter
    def combined_eye_frown(self, value: primitives.Float) -> None:
        """Set the CombinedEyeFrown field value."""
        member = self.get_member("CombinedEyeFrown")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyeFrown", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_inner_brow_vertical(self) -> primitives.Float | None:
        """The LeftEyeInnerBrowVertical field value."""
        member = self.get_member("LeftEyeInnerBrowVertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_inner_brow_vertical.setter
    def left_eye_inner_brow_vertical(self, value: primitives.Float) -> None:
        """Set the LeftEyeInnerBrowVertical field value."""
        member = self.get_member("LeftEyeInnerBrowVertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeInnerBrowVertical", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_inner_brow_vertical(self) -> primitives.Float | None:
        """The RightEyeInnerBrowVertical field value."""
        member = self.get_member("RightEyeInnerBrowVertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_inner_brow_vertical.setter
    def right_eye_inner_brow_vertical(self, value: primitives.Float) -> None:
        """Set the RightEyeInnerBrowVertical field value."""
        member = self.get_member("RightEyeInnerBrowVertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeInnerBrowVertical", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_inner_brow_vertical(self) -> primitives.Float | None:
        """The CombinedEyeInnerBrowVertical field value."""
        member = self.get_member("CombinedEyeInnerBrowVertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_inner_brow_vertical.setter
    def combined_eye_inner_brow_vertical(self, value: primitives.Float) -> None:
        """Set the CombinedEyeInnerBrowVertical field value."""
        member = self.get_member("CombinedEyeInnerBrowVertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyeInnerBrowVertical", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_outer_brow_vertical(self) -> primitives.Float | None:
        """The LeftEyeOuterBrowVertical field value."""
        member = self.get_member("LeftEyeOuterBrowVertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_outer_brow_vertical.setter
    def left_eye_outer_brow_vertical(self, value: primitives.Float) -> None:
        """Set the LeftEyeOuterBrowVertical field value."""
        member = self.get_member("LeftEyeOuterBrowVertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeOuterBrowVertical", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_outer_brow_vertical(self) -> primitives.Float | None:
        """The RightEyeOuterBrowVertical field value."""
        member = self.get_member("RightEyeOuterBrowVertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_outer_brow_vertical.setter
    def right_eye_outer_brow_vertical(self, value: primitives.Float) -> None:
        """Set the RightEyeOuterBrowVertical field value."""
        member = self.get_member("RightEyeOuterBrowVertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeOuterBrowVertical", fields.FieldFloat(value=value)
            )

    @property
    def combined_eye_outer_brow_vertical(self) -> primitives.Float | None:
        """The CombinedEyeOuterBrowVertical field value."""
        member = self.get_member("CombinedEyeOuterBrowVertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @combined_eye_outer_brow_vertical.setter
    def combined_eye_outer_brow_vertical(self, value: primitives.Float) -> None:
        """Set the CombinedEyeOuterBrowVertical field value."""
        member = self.get_member("CombinedEyeOuterBrowVertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CombinedEyeOuterBrowVertical", fields.FieldFloat(value=value)
            )

    @property
    def eye_data_source(self) -> str | None:
        """Target ID of the EyeDataSource reference (targets IEyeDataSourceComponent)."""
        member = self.get_member("EyeDataSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eye_data_source.setter
    def eye_data_source(self, target: str | IEyeDataSourceComponent | None) -> None:
        """Set the EyeDataSource reference by target ID or IEyeDataSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IEyeDataSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("EyeDataSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EyeDataSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IEyeDataSourceComponent'),
            )

    @property
    def simulating_user(self) -> str | None:
        """Target ID of the SimulatingUser reference (targets User)."""
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
    def simulate_on_host(self) -> primitives.Bool | None:
        """The SimulateOnHost field value."""
        member = self.get_member("SimulateOnHost")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @simulate_on_host.setter
    def simulate_on_host(self, value: primitives.Bool) -> None:
        """Set the SimulateOnHost field value."""
        member = self.get_member("SimulateOnHost")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SimulateOnHost", fields.FieldBool(value=value)
            )

    @property
    def ignore_local_user_head(self) -> primitives.Bool | None:
        """The IgnoreLocalUserHead field value."""
        member = self.get_member("IgnoreLocalUserHead")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_local_user_head.setter
    def ignore_local_user_head(self, value: primitives.Bool) -> None:
        """Set the IgnoreLocalUserHead field value."""
        member = self.get_member("IgnoreLocalUserHead")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreLocalUserHead", fields.FieldBool(value=value)
            )

    @property
    def user_head_weight(self) -> primitives.Float | None:
        """The UserHeadWeight field value."""
        member = self.get_member("UserHeadWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_head_weight.setter
    def user_head_weight(self, value: primitives.Float) -> None:
        """Set the UserHeadWeight field value."""
        member = self.get_member("UserHeadWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserHeadWeight", fields.FieldFloat(value=value)
            )

    @property
    def user_hand_weight(self) -> primitives.Float | None:
        """The UserHandWeight field value."""
        member = self.get_member("UserHandWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_hand_weight.setter
    def user_hand_weight(self, value: primitives.Float) -> None:
        """Set the UserHandWeight field value."""
        member = self.get_member("UserHandWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserHandWeight", fields.FieldFloat(value=value)
            )

    @property
    def gripping_hand_weight(self) -> primitives.Float | None:
        """The GrippingHandWeight field value."""
        member = self.get_member("GrippingHandWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gripping_hand_weight.setter
    def gripping_hand_weight(self, value: primitives.Float) -> None:
        """Set the GrippingHandWeight field value."""
        member = self.get_member("GrippingHandWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrippingHandWeight", fields.FieldFloat(value=value)
            )

    @property
    def camera_weight(self) -> primitives.Float | None:
        """The CameraWeight field value."""
        member = self.get_member("CameraWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_weight.setter
    def camera_weight(self, value: primitives.Float) -> None:
        """Set the CameraWeight field value."""
        member = self.get_member("CameraWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraWeight", fields.FieldFloat(value=value)
            )

    @property
    def forced_camera_weight(self) -> primitives.Float | None:
        """The ForcedCameraWeight field value."""
        member = self.get_member("ForcedCameraWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @forced_camera_weight.setter
    def forced_camera_weight(self, value: primitives.Float) -> None:
        """Set the ForcedCameraWeight field value."""
        member = self.get_member("ForcedCameraWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForcedCameraWeight", fields.FieldFloat(value=value)
            )

    @property
    def eye_reference(self) -> str | None:
        """Target ID of the EyeReference reference (targets Slot)."""
        member = self.get_member("EyeReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eye_reference.setter
    def eye_reference(self, target: str | Slot | None) -> None:
        """Set the EyeReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("EyeReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EyeReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def eye_separation(self) -> primitives.Float | None:
        """The EyeSeparation field value."""
        member = self.get_member("EyeSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eye_separation.setter
    def eye_separation(self, value: primitives.Float) -> None:
        """Set the EyeSeparation field value."""
        member = self.get_member("EyeSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EyeSeparation", fields.FieldFloat(value=value)
            )

    @property
    def saccade_speed(self) -> primitives.Float | None:
        """The SaccadeSpeed field value."""
        member = self.get_member("SaccadeSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @saccade_speed.setter
    def saccade_speed(self, value: primitives.Float) -> None:
        """Set the SaccadeSpeed field value."""
        member = self.get_member("SaccadeSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaccadeSpeed", fields.FieldFloat(value=value)
            )

    @property
    def look_target_root(self) -> str | None:
        """Target ID of the LookTargetRoot reference (targets Slot)."""
        member = self.get_member("LookTargetRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @look_target_root.setter
    def look_target_root(self, target: str | Slot | None) -> None:
        """Set the LookTargetRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("LookTargetRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LookTargetRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def look_target_local_point(self) -> primitives.Float3 | None:
        """The LookTargetLocalPoint field value."""
        member = self.get_member("LookTargetLocalPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @look_target_local_point.setter
    def look_target_local_point(self, value: primitives.Float3) -> None:
        """Set the LookTargetLocalPoint field value."""
        member = self.get_member("LookTargetLocalPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LookTargetLocalPoint", fields.FieldFloat3(value=value)
            )

    @property
    def left_eye_target_offset(self) -> primitives.Float3 | None:
        """The LeftEyeTargetOffset field value."""
        member = self.get_member("LeftEyeTargetOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_target_offset.setter
    def left_eye_target_offset(self, value: primitives.Float3) -> None:
        """Set the LeftEyeTargetOffset field value."""
        member = self.get_member("LeftEyeTargetOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeTargetOffset", fields.FieldFloat3(value=value)
            )

    @property
    def right_eye_target_offset(self) -> primitives.Float3 | None:
        """The RightEyeTargetOffset field value."""
        member = self.get_member("RightEyeTargetOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_target_offset.setter
    def right_eye_target_offset(self, value: primitives.Float3) -> None:
        """Set the RightEyeTargetOffset field value."""
        member = self.get_member("RightEyeTargetOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeTargetOffset", fields.FieldFloat3(value=value)
            )

    @property
    def look_target_offset(self) -> primitives.Float3 | None:
        """The LookTargetOffset field value."""
        member = self.get_member("LookTargetOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @look_target_offset.setter
    def look_target_offset(self, value: primitives.Float3) -> None:
        """Set the LookTargetOffset field value."""
        member = self.get_member("LookTargetOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LookTargetOffset", fields.FieldFloat3(value=value)
            )

    @property
    def min_random_saccade_interval(self) -> primitives.Float | None:
        """The MinRandomSaccadeInterval field value."""
        member = self.get_member("MinRandomSaccadeInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_random_saccade_interval.setter
    def min_random_saccade_interval(self, value: primitives.Float) -> None:
        """Set the MinRandomSaccadeInterval field value."""
        member = self.get_member("MinRandomSaccadeInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinRandomSaccadeInterval", fields.FieldFloat(value=value)
            )

    @property
    def max_random_saccade_interval(self) -> primitives.Float | None:
        """The MaxRandomSaccadeInterval field value."""
        member = self.get_member("MaxRandomSaccadeInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_random_saccade_interval.setter
    def max_random_saccade_interval(self, value: primitives.Float) -> None:
        """Set the MaxRandomSaccadeInterval field value."""
        member = self.get_member("MaxRandomSaccadeInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRandomSaccadeInterval", fields.FieldFloat(value=value)
            )

    @property
    def min_target_saccade_interval(self) -> primitives.Float | None:
        """The MinTargetSaccadeInterval field value."""
        member = self.get_member("MinTargetSaccadeInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_target_saccade_interval.setter
    def min_target_saccade_interval(self, value: primitives.Float) -> None:
        """Set the MinTargetSaccadeInterval field value."""
        member = self.get_member("MinTargetSaccadeInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinTargetSaccadeInterval", fields.FieldFloat(value=value)
            )

    @property
    def max_target_saccade_interval(self) -> primitives.Float | None:
        """The MaxTargetSaccadeInterval field value."""
        member = self.get_member("MaxTargetSaccadeInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_target_saccade_interval.setter
    def max_target_saccade_interval(self, value: primitives.Float) -> None:
        """Set the MaxTargetSaccadeInterval field value."""
        member = self.get_member("MaxTargetSaccadeInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxTargetSaccadeInterval", fields.FieldFloat(value=value)
            )

    @property
    def max_random_saccade_offset(self) -> primitives.Float | None:
        """The MaxRandomSaccadeOffset field value."""
        member = self.get_member("MaxRandomSaccadeOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_random_saccade_offset.setter
    def max_random_saccade_offset(self, value: primitives.Float) -> None:
        """Set the MaxRandomSaccadeOffset field value."""
        member = self.get_member("MaxRandomSaccadeOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRandomSaccadeOffset", fields.FieldFloat(value=value)
            )

    @property
    def default_accept_angle(self) -> primitives.Float | None:
        """The DefaultAcceptAngle field value."""
        member = self.get_member("DefaultAcceptAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_accept_angle.setter
    def default_accept_angle(self, value: primitives.Float) -> None:
        """Set the DefaultAcceptAngle field value."""
        member = self.get_member("DefaultAcceptAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultAcceptAngle", fields.FieldFloat(value=value)
            )

    @property
    def default_break_angle(self) -> primitives.Float | None:
        """The DefaultBreakAngle field value."""
        member = self.get_member("DefaultBreakAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_break_angle.setter
    def default_break_angle(self, value: primitives.Float) -> None:
        """Set the DefaultBreakAngle field value."""
        member = self.get_member("DefaultBreakAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultBreakAngle", fields.FieldFloat(value=value)
            )

    @property
    def head_accept_angle(self) -> primitives.Float | None:
        """The HeadAcceptAngle field value."""
        member = self.get_member("HeadAcceptAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_accept_angle.setter
    def head_accept_angle(self, value: primitives.Float) -> None:
        """Set the HeadAcceptAngle field value."""
        member = self.get_member("HeadAcceptAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadAcceptAngle", fields.FieldFloat(value=value)
            )

    @property
    def head_break_angle(self) -> primitives.Float | None:
        """The HeadBreakAngle field value."""
        member = self.get_member("HeadBreakAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_break_angle.setter
    def head_break_angle(self, value: primitives.Float) -> None:
        """Set the HeadBreakAngle field value."""
        member = self.get_member("HeadBreakAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadBreakAngle", fields.FieldFloat(value=value)
            )

    @property
    def camera_accept_angle(self) -> primitives.Float | None:
        """The CameraAcceptAngle field value."""
        member = self.get_member("CameraAcceptAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_accept_angle.setter
    def camera_accept_angle(self, value: primitives.Float) -> None:
        """Set the CameraAcceptAngle field value."""
        member = self.get_member("CameraAcceptAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraAcceptAngle", fields.FieldFloat(value=value)
            )

    @property
    def camera_break_angle(self) -> primitives.Float | None:
        """The CameraBreakAngle field value."""
        member = self.get_member("CameraBreakAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_break_angle.setter
    def camera_break_angle(self, value: primitives.Float) -> None:
        """Set the CameraBreakAngle field value."""
        member = self.get_member("CameraBreakAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraBreakAngle", fields.FieldFloat(value=value)
            )

    @property
    def hand_accept_angle(self) -> primitives.Float | None:
        """The HandAcceptAngle field value."""
        member = self.get_member("HandAcceptAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_accept_angle.setter
    def hand_accept_angle(self, value: primitives.Float) -> None:
        """Set the HandAcceptAngle field value."""
        member = self.get_member("HandAcceptAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandAcceptAngle", fields.FieldFloat(value=value)
            )

    @property
    def hand_break_angle(self) -> primitives.Float | None:
        """The HandBreakAngle field value."""
        member = self.get_member("HandBreakAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hand_break_angle.setter
    def hand_break_angle(self, value: primitives.Float) -> None:
        """Set the HandBreakAngle field value."""
        member = self.get_member("HandBreakAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandBreakAngle", fields.FieldFloat(value=value)
            )

    @property
    def distance_compensation_exp(self) -> primitives.Float | None:
        """The DistanceCompensationExp field value."""
        member = self.get_member("DistanceCompensationExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_compensation_exp.setter
    def distance_compensation_exp(self, value: primitives.Float) -> None:
        """Set the DistanceCompensationExp field value."""
        member = self.get_member("DistanceCompensationExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistanceCompensationExp", fields.FieldFloat(value=value)
            )

    @property
    def left_eye_close_override(self) -> primitives.Float | None:
        """The LeftEyeCloseOverride field value."""
        member = self.get_member("LeftEyeCloseOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @left_eye_close_override.setter
    def left_eye_close_override(self, value: primitives.Float) -> None:
        """Set the LeftEyeCloseOverride field value."""
        member = self.get_member("LeftEyeCloseOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LeftEyeCloseOverride", fields.FieldFloat(value=value)
            )

    @property
    def right_eye_close_override(self) -> primitives.Float | None:
        """The RightEyeCloseOverride field value."""
        member = self.get_member("RightEyeCloseOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @right_eye_close_override.setter
    def right_eye_close_override(self, value: primitives.Float) -> None:
        """Set the RightEyeCloseOverride field value."""
        member = self.get_member("RightEyeCloseOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RightEyeCloseOverride", fields.FieldFloat(value=value)
            )

    @property
    def min_blink_interval(self) -> primitives.Float | None:
        """The MinBlinkInterval field value."""
        member = self.get_member("MinBlinkInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_blink_interval.setter
    def min_blink_interval(self, value: primitives.Float) -> None:
        """Set the MinBlinkInterval field value."""
        member = self.get_member("MinBlinkInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinBlinkInterval", fields.FieldFloat(value=value)
            )

    @property
    def max_blink_interval(self) -> primitives.Float | None:
        """The MaxBlinkInterval field value."""
        member = self.get_member("MaxBlinkInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_blink_interval.setter
    def max_blink_interval(self, value: primitives.Float) -> None:
        """Set the MaxBlinkInterval field value."""
        member = self.get_member("MaxBlinkInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxBlinkInterval", fields.FieldFloat(value=value)
            )

    @property
    def blink_min_speed(self) -> primitives.Float | None:
        """The BlinkMinSpeed field value."""
        member = self.get_member("BlinkMinSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blink_min_speed.setter
    def blink_min_speed(self, value: primitives.Float) -> None:
        """Set the BlinkMinSpeed field value."""
        member = self.get_member("BlinkMinSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlinkMinSpeed", fields.FieldFloat(value=value)
            )

    @property
    def blink_max_speed(self) -> primitives.Float | None:
        """The BlinkMaxSpeed field value."""
        member = self.get_member("BlinkMaxSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blink_max_speed.setter
    def blink_max_speed(self, value: primitives.Float) -> None:
        """Set the BlinkMaxSpeed field value."""
        member = self.get_member("BlinkMaxSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlinkMaxSpeed", fields.FieldFloat(value=value)
            )

    @property
    def blink_speed_spread(self) -> primitives.Float | None:
        """The BlinkSpeedSpread field value."""
        member = self.get_member("BlinkSpeedSpread")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blink_speed_spread.setter
    def blink_speed_spread(self, value: primitives.Float) -> None:
        """Set the BlinkSpeedSpread field value."""
        member = self.get_member("BlinkSpeedSpread")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlinkSpeedSpread", fields.FieldFloat(value=value)
            )

    @property
    def min_pupil_size(self) -> primitives.Float | None:
        """The MinPupilSize field value."""
        member = self.get_member("MinPupilSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_pupil_size.setter
    def min_pupil_size(self, value: primitives.Float) -> None:
        """Set the MinPupilSize field value."""
        member = self.get_member("MinPupilSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinPupilSize", fields.FieldFloat(value=value)
            )

    @property
    def max_pupil_size(self) -> primitives.Float | None:
        """The MaxPupilSize field value."""
        member = self.get_member("MaxPupilSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_pupil_size.setter
    def max_pupil_size(self, value: primitives.Float) -> None:
        """Set the MaxPupilSize field value."""
        member = self.get_member("MaxPupilSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxPupilSize", fields.FieldFloat(value=value)
            )

    @property
    def pupil_size_noise_speed(self) -> primitives.Float | None:
        """The PupilSizeNoiseSpeed field value."""
        member = self.get_member("PupilSizeNoiseSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pupil_size_noise_speed.setter
    def pupil_size_noise_speed(self, value: primitives.Float) -> None:
        """Set the PupilSizeNoiseSpeed field value."""
        member = self.get_member("PupilSizeNoiseSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PupilSizeNoiseSpeed", fields.FieldFloat(value=value)
            )

    @property
    def pupil_size_noise_offset(self) -> primitives.Float | None:
        """The PupilSizeNoiseOffset field value."""
        member = self.get_member("PupilSizeNoiseOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pupil_size_noise_offset.setter
    def pupil_size_noise_offset(self, value: primitives.Float) -> None:
        """Set the PupilSizeNoiseOffset field value."""
        member = self.get_member("PupilSizeNoiseOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PupilSizeNoiseOffset", fields.FieldFloat(value=value)
            )

    @property
    def eye_tracking_pupil_size_smooth_speed(self) -> primitives.Float | None:
        """The EyeTrackingPupilSizeSmoothSpeed field value."""
        member = self.get_member("EyeTrackingPupilSizeSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @eye_tracking_pupil_size_smooth_speed.setter
    def eye_tracking_pupil_size_smooth_speed(self, value: primitives.Float) -> None:
        """Set the EyeTrackingPupilSizeSmoothSpeed field value."""
        member = self.get_member("EyeTrackingPupilSizeSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EyeTrackingPupilSizeSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def mini_expression_probability(self) -> primitives.Float | None:
        """The MiniExpressionProbability field value."""
        member = self.get_member("MiniExpressionProbability")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mini_expression_probability.setter
    def mini_expression_probability(self, value: primitives.Float) -> None:
        """Set the MiniExpressionProbability field value."""
        member = self.get_member("MiniExpressionProbability")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MiniExpressionProbability", fields.FieldFloat(value=value)
            )

    @property
    def mini_expression_interval(self) -> primitives.Float | None:
        """The MiniExpressionInterval field value."""
        member = self.get_member("MiniExpressionInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mini_expression_interval.setter
    def mini_expression_interval(self, value: primitives.Float) -> None:
        """Set the MiniExpressionInterval field value."""
        member = self.get_member("MiniExpressionInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MiniExpressionInterval", fields.FieldFloat(value=value)
            )

    @property
    def mini_expressions(self) -> members.SyncList | None:
        """The MiniExpressions member."""
        member = self.get_member("MiniExpressions")
        if isinstance(member, members.SyncList):
            return member
        return None

    @mini_expressions.setter
    def mini_expressions(self, value: members.SyncList) -> None:
        """Set the MiniExpressions member."""
        self.set_member("MiniExpressions", value)

