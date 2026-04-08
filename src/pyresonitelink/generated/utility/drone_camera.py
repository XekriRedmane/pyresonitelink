"""Generated component: DroneCamera."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DroneCamera(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DroneCamera.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DroneCamera"

    def __init__(self, simulate_on_host: primitives.Bool | None = None, manual_control: primitives.Bool | None = None, slow_speed: primitives.Float | None = None, speed: primitives.Float | None = None, fast_speed: primitives.Float | None = None, mouse_sensitivity: primitives.Float | None = None, field_of_view_source: str | IField[primitives.Float] | None = None, field_of_view: primitives.Float | None = None, aspect_ratio_source: str | IField[primitives.Float] | None = None, aspect_ratio: primitives.Float | None = None, follow_user: str | User | None = None, controller_reject_distance: primitives.Float | None = None, group_search_radius: primitives.Float | None = None, biggest_group_search_interval: primitives.Float | None = None, ignore_other_cameras: primitives.Bool | None = None, head_forward_point_distance: primitives.Float | None = None, head_backward_point_distance: primitives.Float | None = None, head_up_point_distance: primitives.Float | None = None, head_down_point_distance: primitives.Float | None = None, height_offset: primitives.Float | None = None, circle_offset: primitives.Float | None = None, distance_offset: primitives.Float | None = None, circle_speed: primitives.Float | None = None, position_speed: primitives.Float | None = None, look_speed: primitives.Float | None = None, distance_speed: primitives.Float | None = None, user_influence_speed: primitives.Float | None = None, height_amplitude: primitives.Float | None = None, distance_amplitude: primitives.Float | None = None, circle_amplitude: primitives.Float | None = None, height_period: primitives.Float | None = None, distance_period: primitives.Float | None = None, circle_period: primitives.Float | None = None, circle_period_noise_speed: primitives.Float | None = None, circle_period_noise_influence: primitives.Float | None = None, check_occlusion: primitives.Bool | None = None, adjust_height_on_occlusion: primitives.Bool | None = None, teleport_wait_time: primitives.Float | None = None, teleport_trigger_relative_distance: primitives.Float | None = None, teleport_trigger_angle: primitives.Float | None = None, min_randomize_fov_interval: primitives.Float | None = None, max_randomize_fov_interval: primitives.Float | None = None, min_fov: primitives.Float | None = None, max_fov: primitives.Float | None = None, min_change_fov_time: primitives.Float | None = None, max_change_fov_time: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            simulate_on_host: Initial value for SimulateOnHost.
            manual_control: Initial value for ManualControl.
            slow_speed: Initial value for SlowSpeed.
            speed: Initial value for Speed.
            fast_speed: Initial value for FastSpeed.
            mouse_sensitivity: Initial value for MouseSensitivity.
            field_of_view_source: Initial value for FieldOfViewSource.
            field_of_view: Initial value for FieldOfView.
            aspect_ratio_source: Initial value for AspectRatioSource.
            aspect_ratio: Initial value for AspectRatio.
            follow_user: Initial value for FollowUser.
            controller_reject_distance: Initial value for ControllerRejectDistance.
            group_search_radius: Initial value for GroupSearchRadius.
            biggest_group_search_interval: Initial value for BiggestGroupSearchInterval.
            ignore_other_cameras: Initial value for IgnoreOtherCameras.
            head_forward_point_distance: Initial value for HeadForwardPointDistance.
            head_backward_point_distance: Initial value for HeadBackwardPointDistance.
            head_up_point_distance: Initial value for HeadUpPointDistance.
            head_down_point_distance: Initial value for HeadDownPointDistance.
            height_offset: Initial value for HeightOffset.
            circle_offset: Initial value for CircleOffset.
            distance_offset: Initial value for DistanceOffset.
            circle_speed: Initial value for CircleSpeed.
            position_speed: Initial value for PositionSpeed.
            look_speed: Initial value for LookSpeed.
            distance_speed: Initial value for DistanceSpeed.
            user_influence_speed: Initial value for UserInfluenceSpeed.
            height_amplitude: Initial value for HeightAmplitude.
            distance_amplitude: Initial value for DistanceAmplitude.
            circle_amplitude: Initial value for CircleAmplitude.
            height_period: Initial value for HeightPeriod.
            distance_period: Initial value for DistancePeriod.
            circle_period: Initial value for CirclePeriod.
            circle_period_noise_speed: Initial value for CirclePeriodNoiseSpeed.
            circle_period_noise_influence: Initial value for CirclePeriodNoiseInfluence.
            check_occlusion: Initial value for CheckOcclusion.
            adjust_height_on_occlusion: Initial value for AdjustHeightOnOcclusion.
            teleport_wait_time: Initial value for TeleportWaitTime.
            teleport_trigger_relative_distance: Initial value for TeleportTriggerRelativeDistance.
            teleport_trigger_angle: Initial value for TeleportTriggerAngle.
            min_randomize_fov_interval: Initial value for MinRandomizeFovInterval.
            max_randomize_fov_interval: Initial value for MaxRandomizeFovInterval.
            min_fov: Initial value for MinFov.
            max_fov: Initial value for MaxFov.
            min_change_fov_time: Initial value for MinChangeFovTime.
            max_change_fov_time: Initial value for MaxChangeFovTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if simulate_on_host is not None:
            self.simulate_on_host = simulate_on_host
        if manual_control is not None:
            self.manual_control = manual_control
        if slow_speed is not None:
            self.slow_speed = slow_speed
        if speed is not None:
            self.speed = speed
        if fast_speed is not None:
            self.fast_speed = fast_speed
        if mouse_sensitivity is not None:
            self.mouse_sensitivity = mouse_sensitivity
        if field_of_view_source is not None:
            self.field_of_view_source = field_of_view_source
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if aspect_ratio_source is not None:
            self.aspect_ratio_source = aspect_ratio_source
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if follow_user is not None:
            self.follow_user = follow_user
        if controller_reject_distance is not None:
            self.controller_reject_distance = controller_reject_distance
        if group_search_radius is not None:
            self.group_search_radius = group_search_radius
        if biggest_group_search_interval is not None:
            self.biggest_group_search_interval = biggest_group_search_interval
        if ignore_other_cameras is not None:
            self.ignore_other_cameras = ignore_other_cameras
        if head_forward_point_distance is not None:
            self.head_forward_point_distance = head_forward_point_distance
        if head_backward_point_distance is not None:
            self.head_backward_point_distance = head_backward_point_distance
        if head_up_point_distance is not None:
            self.head_up_point_distance = head_up_point_distance
        if head_down_point_distance is not None:
            self.head_down_point_distance = head_down_point_distance
        if height_offset is not None:
            self.height_offset = height_offset
        if circle_offset is not None:
            self.circle_offset = circle_offset
        if distance_offset is not None:
            self.distance_offset = distance_offset
        if circle_speed is not None:
            self.circle_speed = circle_speed
        if position_speed is not None:
            self.position_speed = position_speed
        if look_speed is not None:
            self.look_speed = look_speed
        if distance_speed is not None:
            self.distance_speed = distance_speed
        if user_influence_speed is not None:
            self.user_influence_speed = user_influence_speed
        if height_amplitude is not None:
            self.height_amplitude = height_amplitude
        if distance_amplitude is not None:
            self.distance_amplitude = distance_amplitude
        if circle_amplitude is not None:
            self.circle_amplitude = circle_amplitude
        if height_period is not None:
            self.height_period = height_period
        if distance_period is not None:
            self.distance_period = distance_period
        if circle_period is not None:
            self.circle_period = circle_period
        if circle_period_noise_speed is not None:
            self.circle_period_noise_speed = circle_period_noise_speed
        if circle_period_noise_influence is not None:
            self.circle_period_noise_influence = circle_period_noise_influence
        if check_occlusion is not None:
            self.check_occlusion = check_occlusion
        if adjust_height_on_occlusion is not None:
            self.adjust_height_on_occlusion = adjust_height_on_occlusion
        if teleport_wait_time is not None:
            self.teleport_wait_time = teleport_wait_time
        if teleport_trigger_relative_distance is not None:
            self.teleport_trigger_relative_distance = teleport_trigger_relative_distance
        if teleport_trigger_angle is not None:
            self.teleport_trigger_angle = teleport_trigger_angle
        if min_randomize_fov_interval is not None:
            self.min_randomize_fov_interval = min_randomize_fov_interval
        if max_randomize_fov_interval is not None:
            self.max_randomize_fov_interval = max_randomize_fov_interval
        if min_fov is not None:
            self.min_fov = min_fov
        if max_fov is not None:
            self.max_fov = max_fov
        if min_change_fov_time is not None:
            self.min_change_fov_time = min_change_fov_time
        if max_change_fov_time is not None:
            self.max_change_fov_time = max_change_fov_time

    @property
    def camera_user(self) -> members.SyncObject | None:
        """The CameraUser member."""
        member = self.get_member("CameraUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @camera_user.setter
    def camera_user(self, value: members.SyncObject) -> None:
        """Set the CameraUser member."""
        self.set_member("CameraUser", value)

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
    def manual_control(self) -> primitives.Bool | None:
        """The ManualControl field value."""
        member = self.get_member("ManualControl")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @manual_control.setter
    def manual_control(self, value: primitives.Bool) -> None:
        """Set the ManualControl field value."""
        member = self.get_member("ManualControl")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ManualControl", fields.FieldBool(value=value)
            )

    @property
    def slow_speed(self) -> primitives.Float | None:
        """The SlowSpeed field value."""
        member = self.get_member("SlowSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slow_speed.setter
    def slow_speed(self, value: primitives.Float) -> None:
        """Set the SlowSpeed field value."""
        member = self.get_member("SlowSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlowSpeed", fields.FieldFloat(value=value)
            )

    @property
    def speed(self) -> primitives.Float | None:
        """The Speed field value."""
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
    def fast_speed(self) -> primitives.Float | None:
        """The FastSpeed field value."""
        member = self.get_member("FastSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fast_speed.setter
    def fast_speed(self, value: primitives.Float) -> None:
        """Set the FastSpeed field value."""
        member = self.get_member("FastSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FastSpeed", fields.FieldFloat(value=value)
            )

    @property
    def mouse_sensitivity(self) -> primitives.Float | None:
        """The MouseSensitivity field value."""
        member = self.get_member("MouseSensitivity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouse_sensitivity.setter
    def mouse_sensitivity(self, value: primitives.Float) -> None:
        """Set the MouseSensitivity field value."""
        member = self.get_member("MouseSensitivity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouseSensitivity", fields.FieldFloat(value=value)
            )

    @property
    def field_of_view_source(self) -> str | None:
        """Target ID of the FieldOfViewSource reference (targets IField[primitives.Float])."""
        member = self.get_member("FieldOfViewSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @field_of_view_source.setter
    def field_of_view_source(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the FieldOfViewSource reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FieldOfViewSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FieldOfViewSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def field_of_view(self) -> primitives.Float | None:
        """The FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: primitives.Float) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def aspect_ratio_source(self) -> str | None:
        """Target ID of the AspectRatioSource reference (targets IField[primitives.Float])."""
        member = self.get_member("AspectRatioSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @aspect_ratio_source.setter
    def aspect_ratio_source(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the AspectRatioSource reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AspectRatioSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AspectRatioSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def aspect_ratio(self) -> primitives.Float | None:
        """The AspectRatio field value."""
        member = self.get_member("AspectRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aspect_ratio.setter
    def aspect_ratio(self, value: primitives.Float) -> None:
        """Set the AspectRatio field value."""
        member = self.get_member("AspectRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AspectRatio", fields.FieldFloat(value=value)
            )

    @property
    def follow_user(self) -> str | None:
        """Target ID of the FollowUser reference (targets User)."""
        member = self.get_member("FollowUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @follow_user.setter
    def follow_user(self, target: str | User | None) -> None:
        """Set the FollowUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("FollowUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FollowUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def controller_reject_distance(self) -> primitives.Float | None:
        """The ControllerRejectDistance field value."""
        member = self.get_member("ControllerRejectDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @controller_reject_distance.setter
    def controller_reject_distance(self, value: primitives.Float) -> None:
        """Set the ControllerRejectDistance field value."""
        member = self.get_member("ControllerRejectDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ControllerRejectDistance", fields.FieldFloat(value=value)
            )

    @property
    def group_search_radius(self) -> primitives.Float | None:
        """The GroupSearchRadius field value."""
        member = self.get_member("GroupSearchRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_search_radius.setter
    def group_search_radius(self, value: primitives.Float) -> None:
        """Set the GroupSearchRadius field value."""
        member = self.get_member("GroupSearchRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupSearchRadius", fields.FieldFloat(value=value)
            )

    @property
    def biggest_group_search_interval(self) -> primitives.Float | None:
        """The BiggestGroupSearchInterval field value."""
        member = self.get_member("BiggestGroupSearchInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @biggest_group_search_interval.setter
    def biggest_group_search_interval(self, value: primitives.Float) -> None:
        """Set the BiggestGroupSearchInterval field value."""
        member = self.get_member("BiggestGroupSearchInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BiggestGroupSearchInterval", fields.FieldFloat(value=value)
            )

    @property
    def ignore_other_cameras(self) -> primitives.Bool | None:
        """The IgnoreOtherCameras field value."""
        member = self.get_member("IgnoreOtherCameras")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_other_cameras.setter
    def ignore_other_cameras(self, value: primitives.Bool) -> None:
        """Set the IgnoreOtherCameras field value."""
        member = self.get_member("IgnoreOtherCameras")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreOtherCameras", fields.FieldBool(value=value)
            )

    @property
    def head_forward_point_distance(self) -> primitives.Float | None:
        """The HeadForwardPointDistance field value."""
        member = self.get_member("HeadForwardPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_forward_point_distance.setter
    def head_forward_point_distance(self, value: primitives.Float) -> None:
        """Set the HeadForwardPointDistance field value."""
        member = self.get_member("HeadForwardPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadForwardPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def head_backward_point_distance(self) -> primitives.Float | None:
        """The HeadBackwardPointDistance field value."""
        member = self.get_member("HeadBackwardPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_backward_point_distance.setter
    def head_backward_point_distance(self, value: primitives.Float) -> None:
        """Set the HeadBackwardPointDistance field value."""
        member = self.get_member("HeadBackwardPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadBackwardPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def head_up_point_distance(self) -> primitives.Float | None:
        """The HeadUpPointDistance field value."""
        member = self.get_member("HeadUpPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_up_point_distance.setter
    def head_up_point_distance(self, value: primitives.Float) -> None:
        """Set the HeadUpPointDistance field value."""
        member = self.get_member("HeadUpPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadUpPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def head_down_point_distance(self) -> primitives.Float | None:
        """The HeadDownPointDistance field value."""
        member = self.get_member("HeadDownPointDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_down_point_distance.setter
    def head_down_point_distance(self, value: primitives.Float) -> None:
        """Set the HeadDownPointDistance field value."""
        member = self.get_member("HeadDownPointDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadDownPointDistance", fields.FieldFloat(value=value)
            )

    @property
    def height_offset(self) -> primitives.Float | None:
        """The HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_offset.setter
    def height_offset(self, value: primitives.Float) -> None:
        """Set the HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def circle_offset(self) -> primitives.Float | None:
        """The CircleOffset field value."""
        member = self.get_member("CircleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_offset.setter
    def circle_offset(self, value: primitives.Float) -> None:
        """Set the CircleOffset field value."""
        member = self.get_member("CircleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CircleOffset", fields.FieldFloat(value=value)
            )

    @property
    def distance_offset(self) -> primitives.Float | None:
        """The DistanceOffset field value."""
        member = self.get_member("DistanceOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_offset.setter
    def distance_offset(self, value: primitives.Float) -> None:
        """Set the DistanceOffset field value."""
        member = self.get_member("DistanceOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistanceOffset", fields.FieldFloat(value=value)
            )

    @property
    def circle_speed(self) -> primitives.Float | None:
        """The CircleSpeed field value."""
        member = self.get_member("CircleSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_speed.setter
    def circle_speed(self, value: primitives.Float) -> None:
        """Set the CircleSpeed field value."""
        member = self.get_member("CircleSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CircleSpeed", fields.FieldFloat(value=value)
            )

    @property
    def position_speed(self) -> primitives.Float | None:
        """The PositionSpeed field value."""
        member = self.get_member("PositionSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_speed.setter
    def position_speed(self, value: primitives.Float) -> None:
        """Set the PositionSpeed field value."""
        member = self.get_member("PositionSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSpeed", fields.FieldFloat(value=value)
            )

    @property
    def look_speed(self) -> primitives.Float | None:
        """The LookSpeed field value."""
        member = self.get_member("LookSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @look_speed.setter
    def look_speed(self, value: primitives.Float) -> None:
        """Set the LookSpeed field value."""
        member = self.get_member("LookSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LookSpeed", fields.FieldFloat(value=value)
            )

    @property
    def distance_speed(self) -> primitives.Float | None:
        """The DistanceSpeed field value."""
        member = self.get_member("DistanceSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_speed.setter
    def distance_speed(self, value: primitives.Float) -> None:
        """Set the DistanceSpeed field value."""
        member = self.get_member("DistanceSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistanceSpeed", fields.FieldFloat(value=value)
            )

    @property
    def user_influence_speed(self) -> primitives.Float | None:
        """The UserInfluenceSpeed field value."""
        member = self.get_member("UserInfluenceSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_influence_speed.setter
    def user_influence_speed(self, value: primitives.Float) -> None:
        """Set the UserInfluenceSpeed field value."""
        member = self.get_member("UserInfluenceSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserInfluenceSpeed", fields.FieldFloat(value=value)
            )

    @property
    def height_amplitude(self) -> primitives.Float | None:
        """The HeightAmplitude field value."""
        member = self.get_member("HeightAmplitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_amplitude.setter
    def height_amplitude(self, value: primitives.Float) -> None:
        """Set the HeightAmplitude field value."""
        member = self.get_member("HeightAmplitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightAmplitude", fields.FieldFloat(value=value)
            )

    @property
    def distance_amplitude(self) -> primitives.Float | None:
        """The DistanceAmplitude field value."""
        member = self.get_member("DistanceAmplitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_amplitude.setter
    def distance_amplitude(self, value: primitives.Float) -> None:
        """Set the DistanceAmplitude field value."""
        member = self.get_member("DistanceAmplitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistanceAmplitude", fields.FieldFloat(value=value)
            )

    @property
    def circle_amplitude(self) -> primitives.Float | None:
        """The CircleAmplitude field value."""
        member = self.get_member("CircleAmplitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_amplitude.setter
    def circle_amplitude(self, value: primitives.Float) -> None:
        """Set the CircleAmplitude field value."""
        member = self.get_member("CircleAmplitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CircleAmplitude", fields.FieldFloat(value=value)
            )

    @property
    def height_period(self) -> primitives.Float | None:
        """The HeightPeriod field value."""
        member = self.get_member("HeightPeriod")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_period.setter
    def height_period(self, value: primitives.Float) -> None:
        """Set the HeightPeriod field value."""
        member = self.get_member("HeightPeriod")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightPeriod", fields.FieldFloat(value=value)
            )

    @property
    def distance_period(self) -> primitives.Float | None:
        """The DistancePeriod field value."""
        member = self.get_member("DistancePeriod")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance_period.setter
    def distance_period(self, value: primitives.Float) -> None:
        """Set the DistancePeriod field value."""
        member = self.get_member("DistancePeriod")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DistancePeriod", fields.FieldFloat(value=value)
            )

    @property
    def circle_period(self) -> primitives.Float | None:
        """The CirclePeriod field value."""
        member = self.get_member("CirclePeriod")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_period.setter
    def circle_period(self, value: primitives.Float) -> None:
        """Set the CirclePeriod field value."""
        member = self.get_member("CirclePeriod")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CirclePeriod", fields.FieldFloat(value=value)
            )

    @property
    def circle_period_noise_speed(self) -> primitives.Float | None:
        """The CirclePeriodNoiseSpeed field value."""
        member = self.get_member("CirclePeriodNoiseSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_period_noise_speed.setter
    def circle_period_noise_speed(self, value: primitives.Float) -> None:
        """Set the CirclePeriodNoiseSpeed field value."""
        member = self.get_member("CirclePeriodNoiseSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CirclePeriodNoiseSpeed", fields.FieldFloat(value=value)
            )

    @property
    def circle_period_noise_influence(self) -> primitives.Float | None:
        """The CirclePeriodNoiseInfluence field value."""
        member = self.get_member("CirclePeriodNoiseInfluence")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @circle_period_noise_influence.setter
    def circle_period_noise_influence(self, value: primitives.Float) -> None:
        """Set the CirclePeriodNoiseInfluence field value."""
        member = self.get_member("CirclePeriodNoiseInfluence")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CirclePeriodNoiseInfluence", fields.FieldFloat(value=value)
            )

    @property
    def check_occlusion(self) -> primitives.Bool | None:
        """The CheckOcclusion field value."""
        member = self.get_member("CheckOcclusion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @check_occlusion.setter
    def check_occlusion(self, value: primitives.Bool) -> None:
        """Set the CheckOcclusion field value."""
        member = self.get_member("CheckOcclusion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheckOcclusion", fields.FieldBool(value=value)
            )

    @property
    def adjust_height_on_occlusion(self) -> primitives.Bool | None:
        """The AdjustHeightOnOcclusion field value."""
        member = self.get_member("AdjustHeightOnOcclusion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @adjust_height_on_occlusion.setter
    def adjust_height_on_occlusion(self, value: primitives.Bool) -> None:
        """Set the AdjustHeightOnOcclusion field value."""
        member = self.get_member("AdjustHeightOnOcclusion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AdjustHeightOnOcclusion", fields.FieldBool(value=value)
            )

    @property
    def teleport_wait_time(self) -> primitives.Float | None:
        """The TeleportWaitTime field value."""
        member = self.get_member("TeleportWaitTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @teleport_wait_time.setter
    def teleport_wait_time(self, value: primitives.Float) -> None:
        """Set the TeleportWaitTime field value."""
        member = self.get_member("TeleportWaitTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TeleportWaitTime", fields.FieldFloat(value=value)
            )

    @property
    def teleport_trigger_relative_distance(self) -> primitives.Float | None:
        """The TeleportTriggerRelativeDistance field value."""
        member = self.get_member("TeleportTriggerRelativeDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @teleport_trigger_relative_distance.setter
    def teleport_trigger_relative_distance(self, value: primitives.Float) -> None:
        """Set the TeleportTriggerRelativeDistance field value."""
        member = self.get_member("TeleportTriggerRelativeDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TeleportTriggerRelativeDistance", fields.FieldFloat(value=value)
            )

    @property
    def teleport_trigger_angle(self) -> primitives.Float | None:
        """The TeleportTriggerAngle field value."""
        member = self.get_member("TeleportTriggerAngle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @teleport_trigger_angle.setter
    def teleport_trigger_angle(self, value: primitives.Float) -> None:
        """Set the TeleportTriggerAngle field value."""
        member = self.get_member("TeleportTriggerAngle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TeleportTriggerAngle", fields.FieldFloat(value=value)
            )

    @property
    def min_randomize_fov_interval(self) -> primitives.Float | None:
        """The MinRandomizeFovInterval field value."""
        member = self.get_member("MinRandomizeFovInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_randomize_fov_interval.setter
    def min_randomize_fov_interval(self, value: primitives.Float) -> None:
        """Set the MinRandomizeFovInterval field value."""
        member = self.get_member("MinRandomizeFovInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinRandomizeFovInterval", fields.FieldFloat(value=value)
            )

    @property
    def max_randomize_fov_interval(self) -> primitives.Float | None:
        """The MaxRandomizeFovInterval field value."""
        member = self.get_member("MaxRandomizeFovInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_randomize_fov_interval.setter
    def max_randomize_fov_interval(self, value: primitives.Float) -> None:
        """Set the MaxRandomizeFovInterval field value."""
        member = self.get_member("MaxRandomizeFovInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRandomizeFovInterval", fields.FieldFloat(value=value)
            )

    @property
    def min_fov(self) -> primitives.Float | None:
        """The MinFov field value."""
        member = self.get_member("MinFov")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_fov.setter
    def min_fov(self, value: primitives.Float) -> None:
        """Set the MinFov field value."""
        member = self.get_member("MinFov")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinFov", fields.FieldFloat(value=value)
            )

    @property
    def max_fov(self) -> primitives.Float | None:
        """The MaxFov field value."""
        member = self.get_member("MaxFov")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_fov.setter
    def max_fov(self, value: primitives.Float) -> None:
        """Set the MaxFov field value."""
        member = self.get_member("MaxFov")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxFov", fields.FieldFloat(value=value)
            )

    @property
    def min_change_fov_time(self) -> primitives.Float | None:
        """The MinChangeFovTime field value."""
        member = self.get_member("MinChangeFovTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_change_fov_time.setter
    def min_change_fov_time(self, value: primitives.Float) -> None:
        """Set the MinChangeFovTime field value."""
        member = self.get_member("MinChangeFovTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinChangeFovTime", fields.FieldFloat(value=value)
            )

    @property
    def max_change_fov_time(self) -> primitives.Float | None:
        """The MaxChangeFovTime field value."""
        member = self.get_member("MaxChangeFovTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_change_fov_time.setter
    def max_change_fov_time(self, value: primitives.Float) -> None:
        """Set the MaxChangeFovTime field value."""
        member = self.get_member("MaxChangeFovTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxChangeFovTime", fields.FieldFloat(value=value)
            )

