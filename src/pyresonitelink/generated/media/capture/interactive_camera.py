"""Generated component: InteractiveCamera."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.generated._enums.encode_format import EncodeFormat
from pyresonitelink.generated._enums.camera_positioning_mode import CameraPositioningMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.camera import Camera
from pyresonitelink.generated._types.render_texture_provider import RenderTextureProvider
from pyresonitelink.generated._types.istereo_material import IStereoMaterial
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.audio_clip_player import AudioClipPlayer
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.camera_frustum_mesh import CameraFrustumMesh
from pyresonitelink.generated._types.interactive_camera_anchor import InteractiveCameraAnchor
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.itrigger_action_receiver import ITriggerActionReceiver
from pyresonitelink.generated._types.igrabbable_reparent_block import IGrabbableReparentBlock
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCamera(GeneratedComponent, ITriggerActionReceiver, IGrabbableReparentBlock, IItemMetadataSource, IWorldEventReceiver):
    """The InteractiveCamera component is used in the resonite default camera and is a way of easily taking pictures.

See Camera for more up to date info.

    Category: Media/Capture
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCamera"

    def __init__(self, camera_mode: Mode | str | None = None, preview_width: primitives.Int | None = None, preview_height: primitives.Int | None = None, render_width: primitives.Int | None = None, stereo_separation: primitives.Float | None = None, timer_interval: primitives.Float | None = None, timer_enabled: primitives.Bool | None = None, timer_count_indicator: str | IField[primitives.String] | None = None, timer_color_indicator: str | IField[primitives.ColorX] | None = None, timer_user: str | User | None = None, main_camera: str | Camera | None = None, secondary_camera: str | Camera | None = None, preview_texture: str | RenderTextureProvider | None = None, display_material: str | IStereoMaterial | None = None, format_: EncodeFormat | str | None = None, quality: primitives.Float | None = None, spawn_photo_in_world: primitives.Bool | None = None, photo_spawn_point: str | Slot | None = None, photo_spawn_size: primitives.Float | None = None, panorama_indicator: str | Slot | None = None, panorama_indicator_size: str | IField[primitives.Float3] | None = None, object_target_source: str | Slot | None = None, object_target_source_active: str | IField[primitives.Bool] | None = None, object_auto_pose: primitives.Bool | None = None, hide_lasers_on_capture: primitives.Bool | None = None, capture_sound: str | IAssetProvider[AudioClip] | None = None, timer_start_sound: str | IAssetProvider[AudioClip] | None = None, timer_countdown_slow_player: str | AudioClipPlayer | None = None, timer_countdown_fast_player: str | AudioClipPlayer | None = None, timer_countdown_slow_output: str | AudioOutput | None = None, timer_countdown_fast_output: str | AudioOutput | None = None, preview_scale: primitives.Float2 | None = None, camera_model_override: primitives.String | None = None, frustum_visual: str | CameraFrustumMesh | None = None, default_near_clip: primitives.Float | None = None, default_far_clip: primitives.Float | None = None, frustum_position: str | IField[primitives.Float3] | None = None, frustum_rotation: str | IField[primitives.FloatQ] | None = None, frustum_vertical_fov: str | IField[primitives.Float] | None = None, frustum_horizontal_fov: str | IField[primitives.Float] | None = None, frustum_near: str | IField[primitives.Float] | None = None, frustum_far: str | IField[primitives.Float] | None = None, left_cam_offset: str | IField[primitives.Float3] | None = None, right_cam_offset: str | IField[primitives.Float3] | None = None, left_cam_orientation: str | IField[primitives.FloatQ] | None = None, right_cam_orientation: str | IField[primitives.FloatQ] | None = None, camera_rendering: str | IField[primitives.Bool] | None = None, secondary_camera_rendering: str | IField[primitives.Bool] | None = None, force_visuals_off: primitives.Bool | None = None, auto_hide_proximity: primitives.Float | None = None, positioning_mode: CameraPositioningMode | str | None = None, active_anchor: str | InteractiveCameraAnchor | None = None, anchor_interpolation_speed: primitives.Float | None = None, anchor_linear_interpolation: primitives.Bool | None = None, head_point_offset: primitives.Float3 | None = None, angle_position: primitives.Float | None = None, distance: primitives.Float | None = None, height_offset: primitives.Float | None = None, first_person_pitch: primitives.Float | None = None, first_person_roll: primitives.Float | None = None, first_person_offset: primitives.Float | None = None, group_include_radius: primitives.Float | None = None, group_exclude_radius: primitives.Float | None = None, position_smooth_speed: primitives.Float | None = None, angle_position_smooth_speed: primitives.Float | None = None, framing_smooth_speed: primitives.Float | None = None, wobble_magnitude: primitives.Float3 | None = None, wobble_seed: primitives.Float3 | None = None, wobble_speed: primitives.Float3 | None = None, framing_viewport_position: primitives.Float2 | None = None, avoid_occlusion: primitives.Bool | None = None, occlusion_include_players: primitives.Bool | None = None, occlusion_include_any_colliders: primitives.Bool | None = None, position_stream: str | ValueStream[primitives.Float3] | None = None, rotation_stream: str | ValueStream[primitives.FloatQ] | None = None, position_drive: str | IField[primitives.Float3] | None = None, rotation_drive: str | IField[primitives.FloatQ] | None = None, release_position: primitives.Float3 | None = None, release_rotation: primitives.FloatQ | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            camera_mode: Initial value for CameraMode.
            preview_width: Initial value for PreviewWidth.
            preview_height: Initial value for PreviewHeight.
            render_width: Initial value for RenderWidth.
            stereo_separation: Initial value for StereoSeparation.
            timer_interval: Initial value for TimerInterval.
            timer_enabled: Initial value for TimerEnabled.
            timer_count_indicator: Initial value for TimerCountIndicator.
            timer_color_indicator: Initial value for TimerColorIndicator.
            timer_user: Initial value for _timerUser.
            main_camera: Initial value for MainCamera.
            secondary_camera: Initial value for SecondaryCamera.
            preview_texture: Initial value for PreviewTexture.
            display_material: Initial value for DisplayMaterial.
            format_: Initial value for Format.
            quality: Initial value for Quality.
            spawn_photo_in_world: Initial value for SpawnPhotoInWorld.
            photo_spawn_point: Initial value for PhotoSpawnPoint.
            photo_spawn_size: Initial value for PhotoSpawnSize.
            panorama_indicator: Initial value for PanoramaIndicator.
            panorama_indicator_size: Initial value for PanoramaIndicatorSize.
            object_target_source: Initial value for ObjectTargetSource.
            object_target_source_active: Initial value for ObjectTargetSourceActive.
            object_auto_pose: Initial value for ObjectAutoPose.
            hide_lasers_on_capture: Initial value for HideLasersOnCapture.
            capture_sound: Initial value for CaptureSound.
            timer_start_sound: Initial value for TimerStartSound.
            timer_countdown_slow_player: Initial value for TimerCountdownSlowPlayer.
            timer_countdown_fast_player: Initial value for TimerCountdownFastPlayer.
            timer_countdown_slow_output: Initial value for TimerCountdownSlowOutput.
            timer_countdown_fast_output: Initial value for TimerCountdownFastOutput.
            preview_scale: Initial value for PreviewScale.
            camera_model_override: Initial value for CameraModelOverride.
            frustum_visual: Initial value for FrustumVisual.
            default_near_clip: Initial value for DefaultNearClip.
            default_far_clip: Initial value for DefaultFarClip.
            frustum_position: Initial value for _frustumPosition.
            frustum_rotation: Initial value for _frustumRotation.
            frustum_vertical_fov: Initial value for _frustumVerticalFOV.
            frustum_horizontal_fov: Initial value for _frustumHorizontalFOV.
            frustum_near: Initial value for _frustumNear.
            frustum_far: Initial value for _frustumFar.
            left_cam_offset: Initial value for _leftCamOffset.
            right_cam_offset: Initial value for _rightCamOffset.
            left_cam_orientation: Initial value for _leftCamOrientation.
            right_cam_orientation: Initial value for _rightCamOrientation.
            camera_rendering: Initial value for _cameraRendering.
            secondary_camera_rendering: Initial value for _secondaryCameraRendering.
            force_visuals_off: Initial value for ForceVisualsOff.
            auto_hide_proximity: Initial value for AutoHideProximity.
            positioning_mode: Initial value for PositioningMode.
            active_anchor: Initial value for ActiveAnchor.
            anchor_interpolation_speed: Initial value for AnchorInterpolationSpeed.
            anchor_linear_interpolation: Initial value for AnchorLinearInterpolation.
            head_point_offset: Initial value for HeadPointOffset.
            angle_position: Initial value for AnglePosition.
            distance: Initial value for Distance.
            height_offset: Initial value for HeightOffset.
            first_person_pitch: Initial value for FirstPersonPitch.
            first_person_roll: Initial value for FirstPersonRoll.
            first_person_offset: Initial value for FirstPersonOffset.
            group_include_radius: Initial value for GroupIncludeRadius.
            group_exclude_radius: Initial value for GroupExcludeRadius.
            position_smooth_speed: Initial value for PositionSmoothSpeed.
            angle_position_smooth_speed: Initial value for AnglePositionSmoothSpeed.
            framing_smooth_speed: Initial value for FramingSmoothSpeed.
            wobble_magnitude: Initial value for WobbleMagnitude.
            wobble_seed: Initial value for WobbleSeed.
            wobble_speed: Initial value for WobbleSpeed.
            framing_viewport_position: Initial value for FramingViewportPosition.
            avoid_occlusion: Initial value for AvoidOcclusion.
            occlusion_include_players: Initial value for OcclusionIncludePlayers.
            occlusion_include_any_colliders: Initial value for OcclusionIncludeAnyColliders.
            position_stream: Initial value for _positionStream.
            rotation_stream: Initial value for _rotationStream.
            position_drive: Initial value for _positionDrive.
            rotation_drive: Initial value for _rotationDrive.
            release_position: Initial value for _releasePosition.
            release_rotation: Initial value for _releaseRotation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if camera_mode is not None:
            self.camera_mode = camera_mode
        if preview_width is not None:
            self.preview_width = preview_width
        if preview_height is not None:
            self.preview_height = preview_height
        if render_width is not None:
            self.render_width = render_width
        if stereo_separation is not None:
            self.stereo_separation = stereo_separation
        if timer_interval is not None:
            self.timer_interval = timer_interval
        if timer_enabled is not None:
            self.timer_enabled = timer_enabled
        if timer_count_indicator is not None:
            self.timer_count_indicator = timer_count_indicator
        if timer_color_indicator is not None:
            self.timer_color_indicator = timer_color_indicator
        if timer_user is not None:
            self.timer_user = timer_user
        if main_camera is not None:
            self.main_camera = main_camera
        if secondary_camera is not None:
            self.secondary_camera = secondary_camera
        if preview_texture is not None:
            self.preview_texture = preview_texture
        if display_material is not None:
            self.display_material = display_material
        if format_ is not None:
            self.format_ = format_
        if quality is not None:
            self.quality = quality
        if spawn_photo_in_world is not None:
            self.spawn_photo_in_world = spawn_photo_in_world
        if photo_spawn_point is not None:
            self.photo_spawn_point = photo_spawn_point
        if photo_spawn_size is not None:
            self.photo_spawn_size = photo_spawn_size
        if panorama_indicator is not None:
            self.panorama_indicator = panorama_indicator
        if panorama_indicator_size is not None:
            self.panorama_indicator_size = panorama_indicator_size
        if object_target_source is not None:
            self.object_target_source = object_target_source
        if object_target_source_active is not None:
            self.object_target_source_active = object_target_source_active
        if object_auto_pose is not None:
            self.object_auto_pose = object_auto_pose
        if hide_lasers_on_capture is not None:
            self.hide_lasers_on_capture = hide_lasers_on_capture
        if capture_sound is not None:
            self.capture_sound = capture_sound
        if timer_start_sound is not None:
            self.timer_start_sound = timer_start_sound
        if timer_countdown_slow_player is not None:
            self.timer_countdown_slow_player = timer_countdown_slow_player
        if timer_countdown_fast_player is not None:
            self.timer_countdown_fast_player = timer_countdown_fast_player
        if timer_countdown_slow_output is not None:
            self.timer_countdown_slow_output = timer_countdown_slow_output
        if timer_countdown_fast_output is not None:
            self.timer_countdown_fast_output = timer_countdown_fast_output
        if preview_scale is not None:
            self.preview_scale = preview_scale
        if camera_model_override is not None:
            self.camera_model_override = camera_model_override
        if frustum_visual is not None:
            self.frustum_visual = frustum_visual
        if default_near_clip is not None:
            self.default_near_clip = default_near_clip
        if default_far_clip is not None:
            self.default_far_clip = default_far_clip
        if frustum_position is not None:
            self.frustum_position = frustum_position
        if frustum_rotation is not None:
            self.frustum_rotation = frustum_rotation
        if frustum_vertical_fov is not None:
            self.frustum_vertical_fov = frustum_vertical_fov
        if frustum_horizontal_fov is not None:
            self.frustum_horizontal_fov = frustum_horizontal_fov
        if frustum_near is not None:
            self.frustum_near = frustum_near
        if frustum_far is not None:
            self.frustum_far = frustum_far
        if left_cam_offset is not None:
            self.left_cam_offset = left_cam_offset
        if right_cam_offset is not None:
            self.right_cam_offset = right_cam_offset
        if left_cam_orientation is not None:
            self.left_cam_orientation = left_cam_orientation
        if right_cam_orientation is not None:
            self.right_cam_orientation = right_cam_orientation
        if camera_rendering is not None:
            self.camera_rendering = camera_rendering
        if secondary_camera_rendering is not None:
            self.secondary_camera_rendering = secondary_camera_rendering
        if force_visuals_off is not None:
            self.force_visuals_off = force_visuals_off
        if auto_hide_proximity is not None:
            self.auto_hide_proximity = auto_hide_proximity
        if positioning_mode is not None:
            self.positioning_mode = positioning_mode
        if active_anchor is not None:
            self.active_anchor = active_anchor
        if anchor_interpolation_speed is not None:
            self.anchor_interpolation_speed = anchor_interpolation_speed
        if anchor_linear_interpolation is not None:
            self.anchor_linear_interpolation = anchor_linear_interpolation
        if head_point_offset is not None:
            self.head_point_offset = head_point_offset
        if angle_position is not None:
            self.angle_position = angle_position
        if distance is not None:
            self.distance = distance
        if height_offset is not None:
            self.height_offset = height_offset
        if first_person_pitch is not None:
            self.first_person_pitch = first_person_pitch
        if first_person_roll is not None:
            self.first_person_roll = first_person_roll
        if first_person_offset is not None:
            self.first_person_offset = first_person_offset
        if group_include_radius is not None:
            self.group_include_radius = group_include_radius
        if group_exclude_radius is not None:
            self.group_exclude_radius = group_exclude_radius
        if position_smooth_speed is not None:
            self.position_smooth_speed = position_smooth_speed
        if angle_position_smooth_speed is not None:
            self.angle_position_smooth_speed = angle_position_smooth_speed
        if framing_smooth_speed is not None:
            self.framing_smooth_speed = framing_smooth_speed
        if wobble_magnitude is not None:
            self.wobble_magnitude = wobble_magnitude
        if wobble_seed is not None:
            self.wobble_seed = wobble_seed
        if wobble_speed is not None:
            self.wobble_speed = wobble_speed
        if framing_viewport_position is not None:
            self.framing_viewport_position = framing_viewport_position
        if avoid_occlusion is not None:
            self.avoid_occlusion = avoid_occlusion
        if occlusion_include_players is not None:
            self.occlusion_include_players = occlusion_include_players
        if occlusion_include_any_colliders is not None:
            self.occlusion_include_any_colliders = occlusion_include_any_colliders
        if position_stream is not None:
            self.position_stream = position_stream
        if rotation_stream is not None:
            self.rotation_stream = rotation_stream
        if position_drive is not None:
            self.position_drive = position_drive
        if rotation_drive is not None:
            self.rotation_drive = rotation_drive
        if release_position is not None:
            self.release_position = release_position
        if release_rotation is not None:
            self.release_rotation = release_rotation

    @property
    def camera_mode(self) -> Mode | None:
        """The mode the camera is in for taking pictures."""
        member = self.get_member("CameraMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @camera_mode.setter
    def camera_mode(self, value: Mode | str) -> None:
        """Set CameraMode. The mode the camera is in for taking pictures."""
        member = self.get_member("CameraMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CameraMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def preview_width(self) -> primitives.Int | None:
        """The width in pixels of the preview image on the camera screen."""
        member = self.get_member("PreviewWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preview_width.setter
    def preview_width(self, value: primitives.Int) -> None:
        """Set the PreviewWidth field value."""
        member = self.get_member("PreviewWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreviewWidth", fields.FieldInt(value=value)
            )

    @property
    def preview_height(self) -> primitives.Int | None:
        """The height in pixels of the preview image on the camera screen."""
        member = self.get_member("PreviewHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preview_height.setter
    def preview_height(self, value: primitives.Int) -> None:
        """Set the PreviewHeight field value."""
        member = self.get_member("PreviewHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreviewHeight", fields.FieldInt(value=value)
            )

    @property
    def render_width(self) -> primitives.Int | None:
        """The output width in pixels of the final picture."""
        member = self.get_member("RenderWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_width.setter
    def render_width(self, value: primitives.Int) -> None:
        """Set the RenderWidth field value."""
        member = self.get_member("RenderWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderWidth", fields.FieldInt(value=value)
            )

    @property
    def stereo_separation(self) -> primitives.Float | None:
        """How far apart the left and right eyes should be when taking a stereo picture."""
        member = self.get_member("StereoSeparation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @stereo_separation.setter
    def stereo_separation(self, value: primitives.Float) -> None:
        """Set the StereoSeparation field value."""
        member = self.get_member("StereoSeparation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StereoSeparation", fields.FieldFloat(value=value)
            )

    @property
    def timer_interval(self) -> primitives.Float | None:
        """How long the timer should be for taking a photo."""
        member = self.get_member("TimerInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timer_interval.setter
    def timer_interval(self, value: primitives.Float) -> None:
        """Set the TimerInterval field value."""
        member = self.get_member("TimerInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TimerInterval", fields.FieldFloat(value=value)
            )

    @property
    def timer_enabled(self) -> primitives.Bool | None:
        """Whether the timer mode for taking pictures is enabled."""
        member = self.get_member("TimerEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timer_enabled.setter
    def timer_enabled(self, value: primitives.Bool) -> None:
        """Set the TimerEnabled field value."""
        member = self.get_member("TimerEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TimerEnabled", fields.FieldBool(value=value)
            )

    @property
    def timer_count_indicator(self) -> str | None:
        """The string field to drive with the amount of seconds remaining in the current picture countdown indicator."""
        member = self.get_member("TimerCountIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_count_indicator.setter
    def timer_count_indicator(self, target: str | IField[primitives.String] | None) -> None:
        """Set the TimerCountIndicator reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TimerCountIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerCountIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def timer_color_indicator(self) -> str | None:
        """The color field to drive with the indicator color of the current photo countdown timer."""
        member = self.get_member("TimerColorIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_color_indicator.setter
    def timer_color_indicator(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the TimerColorIndicator reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TimerColorIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerColorIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def timer_user(self) -> str | None:
        """The user that is handling taking the photo and doing the timer countdown."""
        member = self.get_member("_timerUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_user.setter
    def timer_user(self, target: str | User | None) -> None:
        """Set the _timerUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_timerUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def main_camera(self) -> str | None:
        """The main camera being used to preview photos to the screen and render them."""
        member = self.get_member("MainCamera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @main_camera.setter
    def main_camera(self, target: str | Camera | None) -> None:
        """Set the MainCamera reference by target ID or Camera instance."""
        target_id: str | None = target.id if isinstance(target, Camera) else target  # type: ignore[assignment]
        member = self.get_member("MainCamera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MainCamera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Camera'),
            )

    @property
    def secondary_camera(self) -> str | None:
        """The secondary alt camera being used to take photos and render them to the screen."""
        member = self.get_member("SecondaryCamera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_camera.setter
    def secondary_camera(self, target: str | Camera | None) -> None:
        """Set the SecondaryCamera reference by target ID or Camera instance."""
        target_id: str | None = target.id if isinstance(target, Camera) else target  # type: ignore[assignment]
        member = self.get_member("SecondaryCamera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondaryCamera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Camera'),
            )

    @property
    def preview_texture(self) -> str | None:
        """The texture that is being rendered to for the camera screen preview on the back of the camera."""
        member = self.get_member("PreviewTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preview_texture.setter
    def preview_texture(self, target: str | RenderTextureProvider | None) -> None:
        """Set the PreviewTexture reference by target ID or RenderTextureProvider instance."""
        target_id: str | None = target.id if isinstance(target, RenderTextureProvider) else target  # type: ignore[assignment]
        member = self.get_member("PreviewTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PreviewTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RenderTextureProvider'),
            )

    @property
    def display_material(self) -> str | None:
        """The material being used to display the camera preview."""
        member = self.get_member("DisplayMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_material.setter
    def display_material(self, target: str | IStereoMaterial | None) -> None:
        """Set the DisplayMaterial reference by target ID or IStereoMaterial instance."""
        target_id: str | None = target.id if isinstance(target, IStereoMaterial) else target  # type: ignore[assignment]
        member = self.get_member("DisplayMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DisplayMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IStereoMaterial'),
            )

    @property
    def format_(self) -> EncodeFormat | None:
        """In what image type to take pictures in."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EncodeFormat(member.value)
        return None

    @format_.setter
    def format_(self, value: EncodeFormat | str) -> None:
        """Set Format. In what image type to take pictures in."""
        member = self.get_member("Format")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Format",
                members.FieldEnum(value=str(value)),
            )

    @property
    def quality(self) -> primitives.Float | None:
        """The quality encoding for taken pictures."""
        member = self.get_member("Quality")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @quality.setter
    def quality(self, value: primitives.Float) -> None:
        """Set the Quality field value."""
        member = self.get_member("Quality")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Quality", fields.FieldFloat(value=value)
            )

    @property
    def spawn_photo_in_world(self) -> primitives.Bool | None:
        """Whether to spawn taken photos into the world."""
        member = self.get_member("SpawnPhotoInWorld")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_photo_in_world.setter
    def spawn_photo_in_world(self, value: primitives.Bool) -> None:
        """Set the SpawnPhotoInWorld field value."""
        member = self.get_member("SpawnPhotoInWorld")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnPhotoInWorld", fields.FieldBool(value=value)
            )

    @property
    def photo_spawn_point(self) -> str | None:
        """Where to spawn photos and parent them when they are printed out."""
        member = self.get_member("PhotoSpawnPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @photo_spawn_point.setter
    def photo_spawn_point(self, target: str | Slot | None) -> None:
        """Set the PhotoSpawnPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("PhotoSpawnPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PhotoSpawnPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def photo_spawn_size(self) -> primitives.Float | None:
        """How big to spawn the photos."""
        member = self.get_member("PhotoSpawnSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @photo_spawn_size.setter
    def photo_spawn_size(self, value: primitives.Float) -> None:
        """Set the PhotoSpawnSize field value."""
        member = self.get_member("PhotoSpawnSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PhotoSpawnSize", fields.FieldFloat(value=value)
            )

    @property
    def panorama_indicator(self) -> str | None:
        """the slot that holds the panorama indicator visual."""
        member = self.get_member("PanoramaIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panorama_indicator.setter
    def panorama_indicator(self, target: str | Slot | None) -> None:
        """Set the PanoramaIndicator reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("PanoramaIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PanoramaIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def panorama_indicator_size(self) -> str | None:
        """The field to drive so the camera can change the Panorama indicator visual size."""
        member = self.get_member("PanoramaIndicatorSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panorama_indicator_size.setter
    def panorama_indicator_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the PanoramaIndicatorSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PanoramaIndicatorSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PanoramaIndicatorSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def object_target_source(self) -> str | None:
        """The slot to shoot a raycast from for selective rendering a camera when doing the selective object mode."""
        member = self.get_member("ObjectTargetSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_target_source.setter
    def object_target_source(self, target: str | Slot | None) -> None:
        """Set the ObjectTargetSource reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ObjectTargetSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ObjectTargetSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def object_target_source_active(self) -> str | None:
        """The active field of the object target source Laser visual"""
        member = self.get_member("ObjectTargetSourceActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @object_target_source_active.setter
    def object_target_source_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the ObjectTargetSourceActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ObjectTargetSourceActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ObjectTargetSourceActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def object_auto_pose(self) -> primitives.Bool | None:
        """Whether to automatically adjust the camera to look at the targeted object."""
        member = self.get_member("ObjectAutoPose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @object_auto_pose.setter
    def object_auto_pose(self, value: primitives.Bool) -> None:
        """Set the ObjectAutoPose field value."""
        member = self.get_member("ObjectAutoPose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ObjectAutoPose", fields.FieldBool(value=value)
            )

    @property
    def hide_lasers_on_capture(self) -> primitives.Bool | None:
        """Whether to hide user lasers when taking photos."""
        member = self.get_member("HideLasersOnCapture")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_lasers_on_capture.setter
    def hide_lasers_on_capture(self, value: primitives.Bool) -> None:
        """Set the HideLasersOnCapture field value."""
        member = self.get_member("HideLasersOnCapture")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideLasersOnCapture", fields.FieldBool(value=value)
            )

    @property
    def capture_sound(self) -> str | None:
        """The audio clip to play when taking photos."""
        member = self.get_member("CaptureSound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @capture_sound.setter
    def capture_sound(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the CaptureSound reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("CaptureSound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CaptureSound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def timer_start_sound(self) -> str | None:
        """The audio to play when a photo countdown timer starts."""
        member = self.get_member("TimerStartSound")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_start_sound.setter
    def timer_start_sound(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the TimerStartSound reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("TimerStartSound")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerStartSound",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def timer_countdown_slow_player(self) -> str | None:
        """The audio to play when the photo countdown timer is just starting and is counting down."""
        member = self.get_member("TimerCountdownSlowPlayer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_slow_player.setter
    def timer_countdown_slow_player(self, target: str | AudioClipPlayer | None) -> None:
        """Set the TimerCountdownSlowPlayer reference by target ID or AudioClipPlayer instance."""
        target_id: str | None = target.id if isinstance(target, AudioClipPlayer) else target  # type: ignore[assignment]
        member = self.get_member("TimerCountdownSlowPlayer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerCountdownSlowPlayer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioClipPlayer'),
            )

    @property
    def timer_countdown_fast_player(self) -> str | None:
        """The audio to play as the timer for the photo countdown timer is reaching completion."""
        member = self.get_member("TimerCountdownFastPlayer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_fast_player.setter
    def timer_countdown_fast_player(self, target: str | AudioClipPlayer | None) -> None:
        """Set the TimerCountdownFastPlayer reference by target ID or AudioClipPlayer instance."""
        target_id: str | None = target.id if isinstance(target, AudioClipPlayer) else target  # type: ignore[assignment]
        member = self.get_member("TimerCountdownFastPlayer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerCountdownFastPlayer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioClipPlayer'),
            )

    @property
    def timer_countdown_slow_output(self) -> str | None:
        """The audio output component that plays the ``TimerCountdownSlowPlayer``."""
        member = self.get_member("TimerCountdownSlowOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_slow_output.setter
    def timer_countdown_slow_output(self, target: str | AudioOutput | None) -> None:
        """Set the TimerCountdownSlowOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("TimerCountdownSlowOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerCountdownSlowOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def timer_countdown_fast_output(self) -> str | None:
        """The audio output component that plays the ``TimerCountdownFastPlayer``."""
        member = self.get_member("TimerCountdownFastOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_fast_output.setter
    def timer_countdown_fast_output(self, target: str | AudioOutput | None) -> None:
        """Set the TimerCountdownFastOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("TimerCountdownFastOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimerCountdownFastOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def preview_scale(self) -> primitives.Float2 | None:
        """How big the preview display above the camera should be."""
        member = self.get_member("PreviewScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preview_scale.setter
    def preview_scale(self, value: primitives.Float2) -> None:
        """Set the PreviewScale field value."""
        member = self.get_member("PreviewScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreviewScale", fields.FieldFloat2(value=value)
            )

    @property
    def camera_model_override(self) -> primitives.String | None:
        """Overrides the text for what kind of camera took a photo generated by this component in the metadata."""
        member = self.get_member("CameraModelOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_model_override.setter
    def camera_model_override(self, value: primitives.String) -> None:
        """Set the CameraModelOverride field value."""
        member = self.get_member("CameraModelOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraModelOverride", fields.FieldString(value=value)
            )

    @property
    def frustum_visual(self) -> str | None:
        """The mesh that is used to show the camera fustrum"""
        member = self.get_member("FrustumVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_visual.setter
    def frustum_visual(self, target: str | CameraFrustumMesh | None) -> None:
        """Set the FrustumVisual reference by target ID or CameraFrustumMesh instance."""
        target_id: str | None = target.id if isinstance(target, CameraFrustumMesh) else target  # type: ignore[assignment]
        member = self.get_member("FrustumVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FrustumVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CameraFrustumMesh'),
            )

    @property
    def default_near_clip(self) -> primitives.Float | None:
        """The default nearclip to be used with the camera."""
        member = self.get_member("DefaultNearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_near_clip.setter
    def default_near_clip(self, value: primitives.Float) -> None:
        """Set the DefaultNearClip field value."""
        member = self.get_member("DefaultNearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultNearClip", fields.FieldFloat(value=value)
            )

    @property
    def default_far_clip(self) -> primitives.Float | None:
        """The default farclip to be used with the camera."""
        member = self.get_member("DefaultFarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_far_clip.setter
    def default_far_clip(self, value: primitives.Float) -> None:
        """Set the DefaultFarClip field value."""
        member = self.get_member("DefaultFarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultFarClip", fields.FieldFloat(value=value)
            )

    @property
    def frustum_position(self) -> str | None:
        """The field to drive with position of the fustrum visual."""
        member = self.get_member("_frustumPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_position.setter
    def frustum_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _frustumPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frustumPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frustumPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def frustum_rotation(self) -> str | None:
        """The field to drive with the rotation of the fustrum visual."""
        member = self.get_member("_frustumRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_rotation.setter
    def frustum_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _frustumRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frustumRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frustumRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def frustum_vertical_fov(self) -> str | None:
        """The field to drive with the vertical field view angle of the fustrum mesh."""
        member = self.get_member("_frustumVerticalFOV")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_vertical_fov.setter
    def frustum_vertical_fov(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _frustumVerticalFOV reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frustumVerticalFOV")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frustumVerticalFOV",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def frustum_horizontal_fov(self) -> str | None:
        """The field to drive with the horizontal field view angle of the fustrum mesh."""
        member = self.get_member("_frustumHorizontalFOV")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_horizontal_fov.setter
    def frustum_horizontal_fov(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _frustumHorizontalFOV reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frustumHorizontalFOV")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frustumHorizontalFOV",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def frustum_near(self) -> str | None:
        """The field to drive with the nearclip of the fustrum mesh."""
        member = self.get_member("_frustumNear")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_near.setter
    def frustum_near(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _frustumNear reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frustumNear")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frustumNear",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def frustum_far(self) -> str | None:
        """The field to drive with the farclip of the fustrum mesh."""
        member = self.get_member("_frustumFar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frustum_far.setter
    def frustum_far(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _frustumFar reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_frustumFar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frustumFar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def left_cam_offset(self) -> str | None:
        """The field to drive with the offset of the left camera for stero images."""
        member = self.get_member("_leftCamOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_cam_offset.setter
    def left_cam_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _leftCamOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftCamOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftCamOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def right_cam_offset(self) -> str | None:
        """The field to drive with the offset of the right camera for stero images."""
        member = self.get_member("_rightCamOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_cam_offset.setter
    def right_cam_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _rightCamOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightCamOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightCamOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def left_cam_orientation(self) -> str | None:
        """The field to drive with the rotation of the left camera for stero images."""
        member = self.get_member("_leftCamOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_cam_orientation.setter
    def left_cam_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _leftCamOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_leftCamOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_leftCamOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def right_cam_orientation(self) -> str | None:
        """The field to drive with the rotation of the right camera for stero images."""
        member = self.get_member("_rightCamOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_cam_orientation.setter
    def right_cam_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rightCamOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rightCamOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rightCamOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def camera_rendering(self) -> str | None:
        """The field to drive with whether the main camera should be enabled and rendering."""
        member = self.get_member("_cameraRendering")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_rendering.setter
    def camera_rendering(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _cameraRendering reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cameraRendering")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cameraRendering",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def secondary_camera_rendering(self) -> str | None:
        """The field to drive with whether the secondary camera should be enabled and rendering."""
        member = self.get_member("_secondaryCameraRendering")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @secondary_camera_rendering.setter
    def secondary_camera_rendering(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _secondaryCameraRendering reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_secondaryCameraRendering")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_secondaryCameraRendering",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def exclusive_operators(self) -> members.SyncList | None:
        """The users that should be excluded from taken photos due to their privacy settings."""
        member = self.get_member("ExclusiveOperators")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclusive_operators.setter
    def exclusive_operators(self, value: members.SyncList) -> None:
        """Set ExclusiveOperators. The users that should be excluded from taken photos due to their privacy settings."""
        self.set_member("ExclusiveOperators", value)

    @property
    def control_active_fields(self) -> members.SyncList | None:
        """A list of booleans to drive to whether this camera is being auto moved by control rather than manual positioning."""
        member = self.get_member("ControlActiveFields")
        if isinstance(member, members.SyncList):
            return member
        return None

    @control_active_fields.setter
    def control_active_fields(self, value: members.SyncList) -> None:
        """Set ControlActiveFields. A list of booleans to drive to whether this camera is being auto moved by control rather than manual positioning."""
        self.set_member("ControlActiveFields", value)

    @property
    def render_only_for_users(self) -> members.SyncList | None:
        """The users that should only appear in the photo and exlude everyone else."""
        member = self.get_member("RenderOnlyForUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @render_only_for_users.setter
    def render_only_for_users(self, value: members.SyncList) -> None:
        """Set RenderOnlyForUsers. The users that should only appear in the photo and exlude everyone else."""
        self.set_member("RenderOnlyForUsers", value)

    @property
    def force_visuals_off(self) -> primitives.Bool | None:
        """Whether to force this camera's visuals to off."""
        member = self.get_member("ForceVisualsOff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_visuals_off.setter
    def force_visuals_off(self, value: primitives.Bool) -> None:
        """Set the ForceVisualsOff field value."""
        member = self.get_member("ForceVisualsOff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceVisualsOff", fields.FieldBool(value=value)
            )

    @property
    def visual_active_fields(self) -> members.SyncList | None:
        """A list of boolean fields to drive for the visuals of this camera."""
        member = self.get_member("VisualActiveFields")
        if isinstance(member, members.SyncList):
            return member
        return None

    @visual_active_fields.setter
    def visual_active_fields(self, value: members.SyncList) -> None:
        """Set VisualActiveFields. A list of boolean fields to drive for the visuals of this camera."""
        self.set_member("VisualActiveFields", value)

    @property
    def auto_hide_proximity(self) -> primitives.Float | None:
        """How close the camera can be before it hides itself for the local user."""
        member = self.get_member("AutoHideProximity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_hide_proximity.setter
    def auto_hide_proximity(self, value: primitives.Float) -> None:
        """Set the AutoHideProximity field value."""
        member = self.get_member("AutoHideProximity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoHideProximity", fields.FieldFloat(value=value)
            )

    @property
    def force_eye_attention_users(self) -> members.SyncList | None:
        """The list of users to force their eyes to look at the camera."""
        member = self.get_member("ForceEyeAttentionUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @force_eye_attention_users.setter
    def force_eye_attention_users(self, value: members.SyncList) -> None:
        """Set ForceEyeAttentionUsers. The list of users to force their eyes to look at the camera."""
        self.set_member("ForceEyeAttentionUsers", value)

    @property
    def simulating_user(self) -> members.SyncObject | None:
        """The user that is handling the processing for this camera."""
        member = self.get_member("SimulatingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @simulating_user.setter
    def simulating_user(self, value: members.SyncObject) -> None:
        """Set SimulatingUser. The user that is handling the processing for this camera."""
        self.set_member("SimulatingUser", value)

    @property
    def destroy_on_user_leave(self) -> members.SyncObject | None:
        """The user that when leaving will trigger the destruction of this camera."""
        member = self.get_member("DestroyOnUserLeave")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @destroy_on_user_leave.setter
    def destroy_on_user_leave(self, value: members.SyncObject) -> None:
        """Set DestroyOnUserLeave. The user that when leaving will trigger the destruction of this camera."""
        self.set_member("DestroyOnUserLeave", value)

    @property
    def positioning_mode(self) -> CameraPositioningMode | None:
        """How the camera should position itself."""
        member = self.get_member("PositioningMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CameraPositioningMode(member.value)
        return None

    @positioning_mode.setter
    def positioning_mode(self, value: CameraPositioningMode | str) -> None:
        """Set PositioningMode. How the camera should position itself."""
        member = self.get_member("PositioningMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PositioningMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def active_anchor(self) -> str | None:
        """The current camera anchor this camera is on."""
        member = self.get_member("ActiveAnchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_anchor.setter
    def active_anchor(self, target: str | InteractiveCameraAnchor | None) -> None:
        """Set the ActiveAnchor reference by target ID or InteractiveCameraAnchor instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraAnchor) else target  # type: ignore[assignment]
        member = self.get_member("ActiveAnchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ActiveAnchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraAnchor'),
            )

    @property
    def anchor_interpolation_speed(self) -> primitives.Float | None:
        """How fast to move between anchors."""
        member = self.get_member("AnchorInterpolationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_interpolation_speed.setter
    def anchor_interpolation_speed(self, value: primitives.Float) -> None:
        """Set the AnchorInterpolationSpeed field value."""
        member = self.get_member("AnchorInterpolationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorInterpolationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def anchor_linear_interpolation(self) -> primitives.Bool | None:
        """Whether the camera should move between anchors in a linear speed fashion."""
        member = self.get_member("AnchorLinearInterpolation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_linear_interpolation.setter
    def anchor_linear_interpolation(self, value: primitives.Bool) -> None:
        """Set the AnchorLinearInterpolation field value."""
        member = self.get_member("AnchorLinearInterpolation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorLinearInterpolation", fields.FieldBool(value=value)
            )

    @property
    def frame_target_user(self) -> members.SyncObject | None:
        """The user to frame in the shot."""
        member = self.get_member("FrameTargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @frame_target_user.setter
    def frame_target_user(self, value: members.SyncObject) -> None:
        """Set FrameTargetUser. The user to frame in the shot."""
        self.set_member("FrameTargetUser", value)

    @property
    def head_point_offset(self) -> primitives.Float3 | None:
        """How much to add an offset to a user's head when targeting it."""
        member = self.get_member("HeadPointOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @head_point_offset.setter
    def head_point_offset(self, value: primitives.Float3) -> None:
        """Set the HeadPointOffset field value."""
        member = self.get_member("HeadPointOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeadPointOffset", fields.FieldFloat3(value=value)
            )

    @property
    def angle_position(self) -> primitives.Float | None:
        """tilt of the camera side to side"""
        member = self.get_member("AnglePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_position.setter
    def angle_position(self, value: primitives.Float) -> None:
        """Set the AnglePosition field value."""
        member = self.get_member("AnglePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnglePosition", fields.FieldFloat(value=value)
            )

    @property
    def distance(self) -> primitives.Float | None:
        """How far away to stay from a subject during auto tracking."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: primitives.Float) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def height_offset(self) -> primitives.Float | None:
        """How much offset to add to targeting a user's head vertically."""
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
    def first_person_pitch(self) -> primitives.Float | None:
        """The current first person rotation transform pitch."""
        member = self.get_member("FirstPersonPitch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_pitch.setter
    def first_person_pitch(self, value: primitives.Float) -> None:
        """Set the FirstPersonPitch field value."""
        member = self.get_member("FirstPersonPitch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonPitch", fields.FieldFloat(value=value)
            )

    @property
    def first_person_roll(self) -> primitives.Float | None:
        """The current first person rotation transform roll."""
        member = self.get_member("FirstPersonRoll")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_roll.setter
    def first_person_roll(self, value: primitives.Float) -> None:
        """Set the FirstPersonRoll field value."""
        member = self.get_member("FirstPersonRoll")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonRoll", fields.FieldFloat(value=value)
            )

    @property
    def first_person_offset(self) -> primitives.Float | None:
        """The offset forward or backwards in first person currently."""
        member = self.get_member("FirstPersonOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_offset.setter
    def first_person_offset(self, value: primitives.Float) -> None:
        """Set the FirstPersonOffset field value."""
        member = self.get_member("FirstPersonOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonOffset", fields.FieldFloat(value=value)
            )

    @property
    def group_include_radius(self) -> primitives.Float | None:
        """How close a user needs to be to others to be in a group."""
        member = self.get_member("GroupIncludeRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_include_radius.setter
    def group_include_radius(self, value: primitives.Float) -> None:
        """Set the GroupIncludeRadius field value."""
        member = self.get_member("GroupIncludeRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupIncludeRadius", fields.FieldFloat(value=value)
            )

    @property
    def group_exclude_radius(self) -> primitives.Float | None:
        """How far a user needs to move from a group before they are removed as being part of a group."""
        member = self.get_member("GroupExcludeRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_exclude_radius.setter
    def group_exclude_radius(self, value: primitives.Float) -> None:
        """Set the GroupExcludeRadius field value."""
        member = self.get_member("GroupExcludeRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupExcludeRadius", fields.FieldFloat(value=value)
            )

    @property
    def force_group_include(self) -> members.SyncList | None:
        """A list of users to force include into the target group."""
        member = self.get_member("ForceGroupInclude")
        if isinstance(member, members.SyncList):
            return member
        return None

    @force_group_include.setter
    def force_group_include(self, value: members.SyncList) -> None:
        """Set ForceGroupInclude. A list of users to force include into the target group."""
        self.set_member("ForceGroupInclude", value)

    @property
    def force_group_exclude(self) -> members.SyncList | None:
        """A list of users to force exclude from the target group."""
        member = self.get_member("ForceGroupExclude")
        if isinstance(member, members.SyncList):
            return member
        return None

    @force_group_exclude.setter
    def force_group_exclude(self, value: members.SyncList) -> None:
        """Set ForceGroupExclude. A list of users to force exclude from the target group."""
        self.set_member("ForceGroupExclude", value)

    @property
    def position_smooth_speed(self) -> primitives.Float | None:
        """The smooth speed of the camera's position during auto tracking."""
        member = self.get_member("PositionSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_smooth_speed.setter
    def position_smooth_speed(self, value: primitives.Float) -> None:
        """Set the PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def angle_position_smooth_speed(self) -> primitives.Float | None:
        """The smooth speed of the camera's angle position during auto tracking."""
        member = self.get_member("AnglePositionSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_position_smooth_speed.setter
    def angle_position_smooth_speed(self, value: primitives.Float) -> None:
        """Set the AnglePositionSmoothSpeed field value."""
        member = self.get_member("AnglePositionSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnglePositionSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def framing_smooth_speed(self) -> primitives.Float | None:
        """The smooth speed of the camera's position during auto tracking for framing."""
        member = self.get_member("FramingSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_smooth_speed.setter
    def framing_smooth_speed(self, value: primitives.Float) -> None:
        """Set the FramingSmoothSpeed field value."""
        member = self.get_member("FramingSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramingSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def wobble_magnitude(self) -> primitives.Float3 | None:
        """How much the camera's position should randomly wobble."""
        member = self.get_member("WobbleMagnitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @wobble_magnitude.setter
    def wobble_magnitude(self, value: primitives.Float3) -> None:
        """Set the WobbleMagnitude field value."""
        member = self.get_member("WobbleMagnitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WobbleMagnitude", fields.FieldFloat3(value=value)
            )

    @property
    def wobble_seed(self) -> primitives.Float3 | None:
        """The seed of the randomization algorithm of the camera's wobble."""
        member = self.get_member("WobbleSeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @wobble_seed.setter
    def wobble_seed(self, value: primitives.Float3) -> None:
        """Set the WobbleSeed field value."""
        member = self.get_member("WobbleSeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WobbleSeed", fields.FieldFloat3(value=value)
            )

    @property
    def wobble_speed(self) -> primitives.Float3 | None:
        """How fast the camera should randomly wobble."""
        member = self.get_member("WobbleSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @wobble_speed.setter
    def wobble_speed(self, value: primitives.Float3) -> None:
        """Set the WobbleSpeed field value."""
        member = self.get_member("WobbleSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WobbleSpeed", fields.FieldFloat3(value=value)
            )

    @property
    def framing_viewport_position(self) -> primitives.Float2 | None:
        """Where to frame the target object in the viewport of the camera rather than the center of the image."""
        member = self.get_member("FramingViewportPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_viewport_position.setter
    def framing_viewport_position(self, value: primitives.Float2) -> None:
        """Set the FramingViewportPosition field value."""
        member = self.get_member("FramingViewportPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramingViewportPosition", fields.FieldFloat2(value=value)
            )

    @property
    def avoid_occlusion(self) -> primitives.Bool | None:
        """Whether to take target player(s) colliders into account when framing users. Can help with clipping off arms or legs."""
        member = self.get_member("AvoidOcclusion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @avoid_occlusion.setter
    def avoid_occlusion(self, value: primitives.Bool) -> None:
        """Set the AvoidOcclusion field value."""
        member = self.get_member("AvoidOcclusion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AvoidOcclusion", fields.FieldBool(value=value)
            )

    @property
    def occlusion_include_players(self) -> primitives.Bool | None:
        """Whether occlusion should try to keep players in view."""
        member = self.get_member("OcclusionIncludePlayers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_include_players.setter
    def occlusion_include_players(self, value: primitives.Bool) -> None:
        """Set the OcclusionIncludePlayers field value."""
        member = self.get_member("OcclusionIncludePlayers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionIncludePlayers", fields.FieldBool(value=value)
            )

    @property
    def occlusion_include_any_colliders(self) -> primitives.Bool | None:
        """Whether the occlusion should include any collider. If false, ignores character colliders."""
        member = self.get_member("OcclusionIncludeAnyColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @occlusion_include_any_colliders.setter
    def occlusion_include_any_colliders(self, value: primitives.Bool) -> None:
        """Set the OcclusionIncludeAnyColliders field value."""
        member = self.get_member("OcclusionIncludeAnyColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OcclusionIncludeAnyColliders", fields.FieldBool(value=value)
            )

    @property
    def position_stream(self) -> str | None:
        """The stream of the position data for this camera when auto tracking."""
        member = self.get_member("_positionStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_stream.setter
    def position_stream(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the _positionStream reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_positionStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positionStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def rotation_stream(self) -> str | None:
        """The stream of the rotation data for this camera when auto tracking."""
        member = self.get_member("_rotationStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_stream.setter
    def rotation_stream(self, target: str | ValueStream[primitives.FloatQ] | None) -> None:
        """Set the _rotationStream reference by target ID or ValueStream[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("_rotationStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotationStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<floatQ>'),
            )

    @property
    def position_drive(self) -> str | None:
        """The field to drive for the position of the camera when auto tracking."""
        member = self.get_member("_positionDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_drive.setter
    def position_drive(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _positionDrive reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_positionDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positionDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation_drive(self) -> str | None:
        """The field to drive for the rotation of the camera when auto tracking."""
        member = self.get_member("_rotationDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_drive.setter
    def rotation_drive(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _rotationDrive reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rotationDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rotationDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def release_position(self) -> primitives.Float3 | None:
        """The position at the time ``_positionDrive`` became null."""
        member = self.get_member("_releasePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_position.setter
    def release_position(self, value: primitives.Float3) -> None:
        """Set the _releasePosition field value."""
        member = self.get_member("_releasePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_releasePosition", fields.FieldFloat3(value=value)
            )

    @property
    def release_rotation(self) -> primitives.FloatQ | None:
        """The rotation at the time ``_rotationDrive`` became null."""
        member = self.get_member("_releaseRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @release_rotation.setter
    def release_rotation(self, value: primitives.FloatQ) -> None:
        """Set the _releaseRotation field value."""
        member = self.get_member("_releaseRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_releaseRotation", fields.FieldFloatQ(value=value)
            )

    async def trigger(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Tells camera to take photo as if the user pressed the picture button themselves.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Trigger", {}, debug,
        )

    async def capture(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Tells the camera to instantly take a photo.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Capture", {}, debug,
        )

