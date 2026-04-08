"""Generated component: InteractiveCameraControl."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.legacy_panel import LegacyPanel
from pyresonitelink.generated._types.render_texture_proxy_provider import RenderTextureProxyProvider
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.interactive_camera_user_control import InteractiveCameraUserControl
from pyresonitelink.generated._types.interactive_camera_control_settings import InteractiveCameraControlSettings
from pyresonitelink.generated._types.interactive_camera_control_positioning import InteractiveCameraControlPositioning
from pyresonitelink.generated._types.interactive_camera_control_anchors import InteractiveCameraControlAnchors
from pyresonitelink.generated._types.interactive_camera_obs import InteractiveCameraOBS
from pyresonitelink.generated._types.twitch_chat_dialog import TwitchChatDialog
from pyresonitelink.generated._types.ui_unlit_material import UI_UnlitMaterial
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraControl(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraControl.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraControl"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, field_of_view: np.float32 | None = None, angle_position: np.float32 | None = None, distance: np.float32 | None = None, height_offset: np.float32 | None = None, first_person_pitch: np.float32 | None = None, first_person_roll: np.float32 | None = None, first_person_offset: np.float32 | None = None, framing_viewport_position: primitives.Float2 | None = None, mirror: bool | None = None, group_detection_radius: np.float32 | None = None, group_leave_boundary: np.float32 | None = None, position_smooth_speed: np.float32 | None = None, angle_smooth_speed: np.float32 | None = None, framing_smooth_speed: np.float32 | None = None, interpolate_between_anchors: bool | None = None, anchor_interpolation_speed: np.float32 | None = None, anchor_linear_interpolation: bool | None = None, framing_target_override: str | None = None, render_for_everyone: bool | None = None, anyone_can_interact: bool | None = None, render_private_ui: bool | None = None, motion_blur: bool | None = None, screen_space_reflections: bool | None = None, spawn_photo_in_world: bool | None = None, flip_preview: bool | None = None, render_texture_proxy: str | RenderTextureProxyProvider | None = None, framing_reticle: str | RectTransform | None = None, mirror_message: str | RectTransform | None = None, smooth_first_person_button: str | Button | None = None, third_person_button: str | Button | None = None, group_button: str | Button | None = None, world_button: str | Button | None = None, manual_button: str | Button | None = None, mirror_button: str | Button | None = None, users_button: str | Button | None = None, angle_increase_button: str | Button | None = None, angle_decrease_button: str | Button | None = None, height_increase_button: str | Button | None = None, height_decrease_button: str | Button | None = None, distance_increase_button: str | Button | None = None, distance_decrease_button: str | Button | None = None, reset_button: str | Button | None = None, fov_slider: str | Slider[np.float32] | None = None, avoid_occlusion: str | Checkbox | None = None, keep_in_world_space: str | Checkbox | None = None, movement_wobble: str | Checkbox | None = None, aim_in_front_of_head: str | Checkbox | None = None, force_eyes_on_camera: str | Checkbox | None = None, hide_camera: str | Checkbox | None = None, hide_badge: str | Checkbox | None = None, hide_lasers: str | Checkbox | None = None, show_frustum: str | Checkbox | None = None, timer: str | Checkbox | None = None, force_live: str | Checkbox | None = None, audio_from_camera_viewpoint: str | Checkbox | None = None, user_control: str | InteractiveCameraUserControl | None = None, settings_dialog: str | InteractiveCameraControlSettings | None = None, positioning_dialog: str | InteractiveCameraControlPositioning | None = None, anchors_dialog: str | InteractiveCameraControlAnchors | None = None, obs_dialog: str | InteractiveCameraOBS | None = None, twitch_dialog: str | TwitchChatDialog | None = None, settings_button: str | Button | None = None, positioning_button: str | Button | None = None, anchors_button: str | Button | None = None, obs_button: str | Button | None = None, twitch_button: str | Button | None = None, preview_material: str | UI_UnlitMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            canvas: Initial value for _canvas.
            panel: Initial value for _panel.
            field_of_view: Initial value for FieldOfView.
            angle_position: Initial value for AnglePosition.
            distance: Initial value for Distance.
            height_offset: Initial value for HeightOffset.
            first_person_pitch: Initial value for FirstPersonPitch.
            first_person_roll: Initial value for FirstPersonRoll.
            first_person_offset: Initial value for FirstPersonOffset.
            framing_viewport_position: Initial value for FramingViewportPosition.
            mirror: Initial value for Mirror.
            group_detection_radius: Initial value for GroupDetectionRadius.
            group_leave_boundary: Initial value for GroupLeaveBoundary.
            position_smooth_speed: Initial value for PositionSmoothSpeed.
            angle_smooth_speed: Initial value for AngleSmoothSpeed.
            framing_smooth_speed: Initial value for FramingSmoothSpeed.
            interpolate_between_anchors: Initial value for InterpolateBetweenAnchors.
            anchor_interpolation_speed: Initial value for AnchorInterpolationSpeed.
            anchor_linear_interpolation: Initial value for AnchorLinearInterpolation.
            framing_target_override: Initial value for FramingTargetOverride.
            render_for_everyone: Initial value for RenderForEveryone.
            anyone_can_interact: Initial value for AnyoneCanInteract.
            render_private_ui: Initial value for RenderPrivateUI.
            motion_blur: Initial value for MotionBlur.
            screen_space_reflections: Initial value for ScreenSpaceReflections.
            spawn_photo_in_world: Initial value for SpawnPhotoInWorld.
            flip_preview: Initial value for FlipPreview.
            render_texture_proxy: Initial value for _renderTextureProxy.
            framing_reticle: Initial value for _framingReticle.
            mirror_message: Initial value for _mirrorMessage.
            smooth_first_person_button: Initial value for _smoothFirstPersonButton.
            third_person_button: Initial value for _thirdPersonButton.
            group_button: Initial value for _groupButton.
            world_button: Initial value for _worldButton.
            manual_button: Initial value for _manualButton.
            mirror_button: Initial value for _mirrorButton.
            users_button: Initial value for _usersButton.
            angle_increase_button: Initial value for _angleIncreaseButton.
            angle_decrease_button: Initial value for _angleDecreaseButton.
            height_increase_button: Initial value for _heightIncreaseButton.
            height_decrease_button: Initial value for _heightDecreaseButton.
            distance_increase_button: Initial value for _distanceIncreaseButton.
            distance_decrease_button: Initial value for _distanceDecreaseButton.
            reset_button: Initial value for _resetButton.
            fov_slider: Initial value for _fovSlider.
            avoid_occlusion: Initial value for _avoidOcclusion.
            keep_in_world_space: Initial value for _keepInWorldSpace.
            movement_wobble: Initial value for _movementWobble.
            aim_in_front_of_head: Initial value for _aimInFrontOfHead.
            force_eyes_on_camera: Initial value for _forceEyesOnCamera.
            hide_camera: Initial value for _hideCamera.
            hide_badge: Initial value for _hideBadge.
            hide_lasers: Initial value for _hideLasers.
            show_frustum: Initial value for _showFrustum.
            timer: Initial value for _timer.
            force_live: Initial value for _forceLive.
            audio_from_camera_viewpoint: Initial value for _audioFromCameraViewpoint.
            user_control: Initial value for _userControl.
            settings_dialog: Initial value for _settingsDialog.
            positioning_dialog: Initial value for _positioningDialog.
            anchors_dialog: Initial value for _anchorsDialog.
            obs_dialog: Initial value for _OBS_Dialog.
            twitch_dialog: Initial value for _twitchDialog.
            settings_button: Initial value for _settingsButton.
            positioning_button: Initial value for _positioningButton.
            anchors_button: Initial value for _anchorsButton.
            obs_button: Initial value for _OBS_Button.
            twitch_button: Initial value for _twitchButton.
            preview_material: Initial value for _previewMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if canvas is not None:
            self.canvas = canvas
        if panel is not None:
            self.panel = panel
        if field_of_view is not None:
            self.field_of_view = field_of_view
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
        if framing_viewport_position is not None:
            self.framing_viewport_position = framing_viewport_position
        if mirror is not None:
            self.mirror = mirror
        if group_detection_radius is not None:
            self.group_detection_radius = group_detection_radius
        if group_leave_boundary is not None:
            self.group_leave_boundary = group_leave_boundary
        if position_smooth_speed is not None:
            self.position_smooth_speed = position_smooth_speed
        if angle_smooth_speed is not None:
            self.angle_smooth_speed = angle_smooth_speed
        if framing_smooth_speed is not None:
            self.framing_smooth_speed = framing_smooth_speed
        if interpolate_between_anchors is not None:
            self.interpolate_between_anchors = interpolate_between_anchors
        if anchor_interpolation_speed is not None:
            self.anchor_interpolation_speed = anchor_interpolation_speed
        if anchor_linear_interpolation is not None:
            self.anchor_linear_interpolation = anchor_linear_interpolation
        if framing_target_override is not None:
            self.framing_target_override = framing_target_override
        if render_for_everyone is not None:
            self.render_for_everyone = render_for_everyone
        if anyone_can_interact is not None:
            self.anyone_can_interact = anyone_can_interact
        if render_private_ui is not None:
            self.render_private_ui = render_private_ui
        if motion_blur is not None:
            self.motion_blur = motion_blur
        if screen_space_reflections is not None:
            self.screen_space_reflections = screen_space_reflections
        if spawn_photo_in_world is not None:
            self.spawn_photo_in_world = spawn_photo_in_world
        if flip_preview is not None:
            self.flip_preview = flip_preview
        if render_texture_proxy is not None:
            self.render_texture_proxy = render_texture_proxy
        if framing_reticle is not None:
            self.framing_reticle = framing_reticle
        if mirror_message is not None:
            self.mirror_message = mirror_message
        if smooth_first_person_button is not None:
            self.smooth_first_person_button = smooth_first_person_button
        if third_person_button is not None:
            self.third_person_button = third_person_button
        if group_button is not None:
            self.group_button = group_button
        if world_button is not None:
            self.world_button = world_button
        if manual_button is not None:
            self.manual_button = manual_button
        if mirror_button is not None:
            self.mirror_button = mirror_button
        if users_button is not None:
            self.users_button = users_button
        if angle_increase_button is not None:
            self.angle_increase_button = angle_increase_button
        if angle_decrease_button is not None:
            self.angle_decrease_button = angle_decrease_button
        if height_increase_button is not None:
            self.height_increase_button = height_increase_button
        if height_decrease_button is not None:
            self.height_decrease_button = height_decrease_button
        if distance_increase_button is not None:
            self.distance_increase_button = distance_increase_button
        if distance_decrease_button is not None:
            self.distance_decrease_button = distance_decrease_button
        if reset_button is not None:
            self.reset_button = reset_button
        if fov_slider is not None:
            self.fov_slider = fov_slider
        if avoid_occlusion is not None:
            self.avoid_occlusion = avoid_occlusion
        if keep_in_world_space is not None:
            self.keep_in_world_space = keep_in_world_space
        if movement_wobble is not None:
            self.movement_wobble = movement_wobble
        if aim_in_front_of_head is not None:
            self.aim_in_front_of_head = aim_in_front_of_head
        if force_eyes_on_camera is not None:
            self.force_eyes_on_camera = force_eyes_on_camera
        if hide_camera is not None:
            self.hide_camera = hide_camera
        if hide_badge is not None:
            self.hide_badge = hide_badge
        if hide_lasers is not None:
            self.hide_lasers = hide_lasers
        if show_frustum is not None:
            self.show_frustum = show_frustum
        if timer is not None:
            self.timer = timer
        if force_live is not None:
            self.force_live = force_live
        if audio_from_camera_viewpoint is not None:
            self.audio_from_camera_viewpoint = audio_from_camera_viewpoint
        if user_control is not None:
            self.user_control = user_control
        if settings_dialog is not None:
            self.settings_dialog = settings_dialog
        if positioning_dialog is not None:
            self.positioning_dialog = positioning_dialog
        if anchors_dialog is not None:
            self.anchors_dialog = anchors_dialog
        if obs_dialog is not None:
            self.obs_dialog = obs_dialog
        if twitch_dialog is not None:
            self.twitch_dialog = twitch_dialog
        if settings_button is not None:
            self.settings_button = settings_button
        if positioning_button is not None:
            self.positioning_button = positioning_button
        if anchors_button is not None:
            self.anchors_button = anchors_button
        if obs_button is not None:
            self.obs_button = obs_button
        if twitch_button is not None:
            self.twitch_button = twitch_button
        if preview_material is not None:
            self.preview_material = preview_material

    @property
    def canvas(self) -> str | None:
        """Target ID of the _canvas reference (targets Canvas)."""
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas.setter
    def canvas(self, target: str | Canvas | None) -> None:
        """Set the _canvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def panel(self) -> str | None:
        """Target ID of the _panel reference (targets LegacyPanel)."""
        member = self.get_member("_panel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panel.setter
    def panel(self, target: str | LegacyPanel | None) -> None:
        """Set the _panel reference by target ID or LegacyPanel instance."""
        target_id: str | None = target.id if isinstance(target, LegacyPanel) else target  # type: ignore[assignment]
        member = self.get_member("_panel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_panel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyPanel'),
            )

    @property
    def field_of_view(self) -> np.float32 | None:
        """The FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: np.float32) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def angle_position(self) -> np.float32 | None:
        """The AnglePosition field value."""
        member = self.get_member("AnglePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_position.setter
    def angle_position(self, value: np.float32) -> None:
        """Set the AnglePosition field value."""
        member = self.get_member("AnglePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnglePosition", fields.FieldFloat(value=value)
            )

    @property
    def distance(self) -> np.float32 | None:
        """The Distance field value."""
        member = self.get_member("Distance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @distance.setter
    def distance(self, value: np.float32) -> None:
        """Set the Distance field value."""
        member = self.get_member("Distance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Distance", fields.FieldFloat(value=value)
            )

    @property
    def height_offset(self) -> np.float32 | None:
        """The HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_offset.setter
    def height_offset(self, value: np.float32) -> None:
        """Set the HeightOffset field value."""
        member = self.get_member("HeightOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightOffset", fields.FieldFloat(value=value)
            )

    @property
    def first_person_pitch(self) -> np.float32 | None:
        """The FirstPersonPitch field value."""
        member = self.get_member("FirstPersonPitch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_pitch.setter
    def first_person_pitch(self, value: np.float32) -> None:
        """Set the FirstPersonPitch field value."""
        member = self.get_member("FirstPersonPitch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonPitch", fields.FieldFloat(value=value)
            )

    @property
    def first_person_roll(self) -> np.float32 | None:
        """The FirstPersonRoll field value."""
        member = self.get_member("FirstPersonRoll")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_roll.setter
    def first_person_roll(self, value: np.float32) -> None:
        """Set the FirstPersonRoll field value."""
        member = self.get_member("FirstPersonRoll")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonRoll", fields.FieldFloat(value=value)
            )

    @property
    def first_person_offset(self) -> np.float32 | None:
        """The FirstPersonOffset field value."""
        member = self.get_member("FirstPersonOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @first_person_offset.setter
    def first_person_offset(self, value: np.float32) -> None:
        """Set the FirstPersonOffset field value."""
        member = self.get_member("FirstPersonOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FirstPersonOffset", fields.FieldFloat(value=value)
            )

    @property
    def framing_viewport_position(self) -> primitives.Float2 | None:
        """The FramingViewportPosition field value."""
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
    def mirror(self) -> bool | None:
        """The Mirror field value."""
        member = self.get_member("Mirror")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mirror.setter
    def mirror(self, value: bool) -> None:
        """Set the Mirror field value."""
        member = self.get_member("Mirror")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mirror", fields.FieldBool(value=value)
            )

    @property
    def group_detection_radius(self) -> np.float32 | None:
        """The GroupDetectionRadius field value."""
        member = self.get_member("GroupDetectionRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_detection_radius.setter
    def group_detection_radius(self, value: np.float32) -> None:
        """Set the GroupDetectionRadius field value."""
        member = self.get_member("GroupDetectionRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupDetectionRadius", fields.FieldFloat(value=value)
            )

    @property
    def group_leave_boundary(self) -> np.float32 | None:
        """The GroupLeaveBoundary field value."""
        member = self.get_member("GroupLeaveBoundary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_leave_boundary.setter
    def group_leave_boundary(self, value: np.float32) -> None:
        """Set the GroupLeaveBoundary field value."""
        member = self.get_member("GroupLeaveBoundary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupLeaveBoundary", fields.FieldFloat(value=value)
            )

    @property
    def position_smooth_speed(self) -> np.float32 | None:
        """The PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_smooth_speed.setter
    def position_smooth_speed(self, value: np.float32) -> None:
        """Set the PositionSmoothSpeed field value."""
        member = self.get_member("PositionSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def angle_smooth_speed(self) -> np.float32 | None:
        """The AngleSmoothSpeed field value."""
        member = self.get_member("AngleSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_smooth_speed.setter
    def angle_smooth_speed(self, value: np.float32) -> None:
        """Set the AngleSmoothSpeed field value."""
        member = self.get_member("AngleSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngleSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def framing_smooth_speed(self) -> np.float32 | None:
        """The FramingSmoothSpeed field value."""
        member = self.get_member("FramingSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_smooth_speed.setter
    def framing_smooth_speed(self, value: np.float32) -> None:
        """Set the FramingSmoothSpeed field value."""
        member = self.get_member("FramingSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramingSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def interpolate_between_anchors(self) -> bool | None:
        """The InterpolateBetweenAnchors field value."""
        member = self.get_member("InterpolateBetweenAnchors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interpolate_between_anchors.setter
    def interpolate_between_anchors(self, value: bool) -> None:
        """Set the InterpolateBetweenAnchors field value."""
        member = self.get_member("InterpolateBetweenAnchors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterpolateBetweenAnchors", fields.FieldBool(value=value)
            )

    @property
    def anchor_interpolation_speed(self) -> np.float32 | None:
        """The AnchorInterpolationSpeed field value."""
        member = self.get_member("AnchorInterpolationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_interpolation_speed.setter
    def anchor_interpolation_speed(self, value: np.float32) -> None:
        """Set the AnchorInterpolationSpeed field value."""
        member = self.get_member("AnchorInterpolationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorInterpolationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def anchor_linear_interpolation(self) -> bool | None:
        """The AnchorLinearInterpolation field value."""
        member = self.get_member("AnchorLinearInterpolation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anchor_linear_interpolation.setter
    def anchor_linear_interpolation(self, value: bool) -> None:
        """Set the AnchorLinearInterpolation field value."""
        member = self.get_member("AnchorLinearInterpolation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnchorLinearInterpolation", fields.FieldBool(value=value)
            )

    @property
    def mode(self) -> members.FieldEnum | None:
        """The Mode member."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mode.setter
    def mode(self, value: members.FieldEnum) -> None:
        """Set the Mode member."""
        self.set_member("Mode", value)

    @property
    def framing_target_override(self) -> str | None:
        """The FramingTargetOverride field value."""
        member = self.get_member("FramingTargetOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_target_override.setter
    def framing_target_override(self, value: str) -> None:
        """Set the FramingTargetOverride field value."""
        member = self.get_member("FramingTargetOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramingTargetOverride", fields.FieldString(value=value)
            )

    @property
    def camera_operators(self) -> members.SyncList | None:
        """The CameraOperators member."""
        member = self.get_member("CameraOperators")
        if isinstance(member, members.SyncList):
            return member
        return None

    @camera_operators.setter
    def camera_operators(self, value: members.SyncList) -> None:
        """Set the CameraOperators member."""
        self.set_member("CameraOperators", value)

    @property
    def group_include_users(self) -> members.SyncList | None:
        """The GroupIncludeUsers member."""
        member = self.get_member("GroupIncludeUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @group_include_users.setter
    def group_include_users(self, value: members.SyncList) -> None:
        """Set the GroupIncludeUsers member."""
        self.set_member("GroupIncludeUsers", value)

    @property
    def group_exclude_users(self) -> members.SyncList | None:
        """The GroupExcludeUsers member."""
        member = self.get_member("GroupExcludeUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @group_exclude_users.setter
    def group_exclude_users(self, value: members.SyncList) -> None:
        """Set the GroupExcludeUsers member."""
        self.set_member("GroupExcludeUsers", value)

    @property
    def render_for_everyone(self) -> bool | None:
        """The RenderForEveryone field value."""
        member = self.get_member("RenderForEveryone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_for_everyone.setter
    def render_for_everyone(self, value: bool) -> None:
        """Set the RenderForEveryone field value."""
        member = self.get_member("RenderForEveryone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderForEveryone", fields.FieldBool(value=value)
            )

    @property
    def anyone_can_interact(self) -> bool | None:
        """The AnyoneCanInteract field value."""
        member = self.get_member("AnyoneCanInteract")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anyone_can_interact.setter
    def anyone_can_interact(self, value: bool) -> None:
        """Set the AnyoneCanInteract field value."""
        member = self.get_member("AnyoneCanInteract")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnyoneCanInteract", fields.FieldBool(value=value)
            )

    @property
    def render_private_ui(self) -> bool | None:
        """The RenderPrivateUI field value."""
        member = self.get_member("RenderPrivateUI")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_private_ui.setter
    def render_private_ui(self, value: bool) -> None:
        """Set the RenderPrivateUI field value."""
        member = self.get_member("RenderPrivateUI")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderPrivateUI", fields.FieldBool(value=value)
            )

    @property
    def motion_blur(self) -> bool | None:
        """The MotionBlur field value."""
        member = self.get_member("MotionBlur")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @motion_blur.setter
    def motion_blur(self, value: bool) -> None:
        """Set the MotionBlur field value."""
        member = self.get_member("MotionBlur")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MotionBlur", fields.FieldBool(value=value)
            )

    @property
    def screen_space_reflections(self) -> bool | None:
        """The ScreenSpaceReflections field value."""
        member = self.get_member("ScreenSpaceReflections")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_space_reflections.setter
    def screen_space_reflections(self, value: bool) -> None:
        """Set the ScreenSpaceReflections field value."""
        member = self.get_member("ScreenSpaceReflections")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenSpaceReflections", fields.FieldBool(value=value)
            )

    @property
    def spawn_photo_in_world(self) -> bool | None:
        """The SpawnPhotoInWorld field value."""
        member = self.get_member("SpawnPhotoInWorld")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_photo_in_world.setter
    def spawn_photo_in_world(self, value: bool) -> None:
        """Set the SpawnPhotoInWorld field value."""
        member = self.get_member("SpawnPhotoInWorld")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnPhotoInWorld", fields.FieldBool(value=value)
            )

    @property
    def flip_preview(self) -> bool | None:
        """The FlipPreview field value."""
        member = self.get_member("FlipPreview")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_preview.setter
    def flip_preview(self, value: bool) -> None:
        """Set the FlipPreview field value."""
        member = self.get_member("FlipPreview")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipPreview", fields.FieldBool(value=value)
            )

    @property
    def render_texture_proxy(self) -> str | None:
        """Target ID of the _renderTextureProxy reference (targets RenderTextureProxyProvider)."""
        member = self.get_member("_renderTextureProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_texture_proxy.setter
    def render_texture_proxy(self, target: str | RenderTextureProxyProvider | None) -> None:
        """Set the _renderTextureProxy reference by target ID or RenderTextureProxyProvider instance."""
        target_id: str | None = target.id if isinstance(target, RenderTextureProxyProvider) else target  # type: ignore[assignment]
        member = self.get_member("_renderTextureProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderTextureProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RenderTextureProxyProvider'),
            )

    @property
    def framing_reticle(self) -> str | None:
        """Target ID of the _framingReticle reference (targets RectTransform)."""
        member = self.get_member("_framingReticle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @framing_reticle.setter
    def framing_reticle(self, target: str | RectTransform | None) -> None:
        """Set the _framingReticle reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_framingReticle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_framingReticle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def mirror_message(self) -> str | None:
        """Target ID of the _mirrorMessage reference (targets RectTransform)."""
        member = self.get_member("_mirrorMessage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mirror_message.setter
    def mirror_message(self, target: str | RectTransform | None) -> None:
        """Set the _mirrorMessage reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_mirrorMessage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mirrorMessage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def smooth_first_person_button(self) -> str | None:
        """Target ID of the _smoothFirstPersonButton reference (targets Button)."""
        member = self.get_member("_smoothFirstPersonButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @smooth_first_person_button.setter
    def smooth_first_person_button(self, target: str | Button | None) -> None:
        """Set the _smoothFirstPersonButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_smoothFirstPersonButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_smoothFirstPersonButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def third_person_button(self) -> str | None:
        """Target ID of the _thirdPersonButton reference (targets Button)."""
        member = self.get_member("_thirdPersonButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @third_person_button.setter
    def third_person_button(self, target: str | Button | None) -> None:
        """Set the _thirdPersonButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_thirdPersonButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thirdPersonButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def group_button(self) -> str | None:
        """Target ID of the _groupButton reference (targets Button)."""
        member = self.get_member("_groupButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @group_button.setter
    def group_button(self, target: str | Button | None) -> None:
        """Set the _groupButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_groupButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_groupButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def world_button(self) -> str | None:
        """Target ID of the _worldButton reference (targets Button)."""
        member = self.get_member("_worldButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_button.setter
    def world_button(self, target: str | Button | None) -> None:
        """Set the _worldButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_worldButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worldButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def manual_button(self) -> str | None:
        """Target ID of the _manualButton reference (targets Button)."""
        member = self.get_member("_manualButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @manual_button.setter
    def manual_button(self, target: str | Button | None) -> None:
        """Set the _manualButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_manualButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_manualButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def mirror_button(self) -> str | None:
        """Target ID of the _mirrorButton reference (targets Button)."""
        member = self.get_member("_mirrorButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mirror_button.setter
    def mirror_button(self, target: str | Button | None) -> None:
        """Set the _mirrorButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_mirrorButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_mirrorButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def users_button(self) -> str | None:
        """Target ID of the _usersButton reference (targets Button)."""
        member = self.get_member("_usersButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @users_button.setter
    def users_button(self, target: str | Button | None) -> None:
        """Set the _usersButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_usersButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_usersButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def angle_increase_button(self) -> str | None:
        """Target ID of the _angleIncreaseButton reference (targets Button)."""
        member = self.get_member("_angleIncreaseButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @angle_increase_button.setter
    def angle_increase_button(self, target: str | Button | None) -> None:
        """Set the _angleIncreaseButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_angleIncreaseButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_angleIncreaseButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def angle_decrease_button(self) -> str | None:
        """Target ID of the _angleDecreaseButton reference (targets Button)."""
        member = self.get_member("_angleDecreaseButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @angle_decrease_button.setter
    def angle_decrease_button(self, target: str | Button | None) -> None:
        """Set the _angleDecreaseButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_angleDecreaseButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_angleDecreaseButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def height_increase_button(self) -> str | None:
        """Target ID of the _heightIncreaseButton reference (targets Button)."""
        member = self.get_member("_heightIncreaseButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_increase_button.setter
    def height_increase_button(self, target: str | Button | None) -> None:
        """Set the _heightIncreaseButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_heightIncreaseButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_heightIncreaseButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def height_decrease_button(self) -> str | None:
        """Target ID of the _heightDecreaseButton reference (targets Button)."""
        member = self.get_member("_heightDecreaseButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_decrease_button.setter
    def height_decrease_button(self, target: str | Button | None) -> None:
        """Set the _heightDecreaseButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_heightDecreaseButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_heightDecreaseButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def distance_increase_button(self) -> str | None:
        """Target ID of the _distanceIncreaseButton reference (targets Button)."""
        member = self.get_member("_distanceIncreaseButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance_increase_button.setter
    def distance_increase_button(self, target: str | Button | None) -> None:
        """Set the _distanceIncreaseButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_distanceIncreaseButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_distanceIncreaseButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def distance_decrease_button(self) -> str | None:
        """Target ID of the _distanceDecreaseButton reference (targets Button)."""
        member = self.get_member("_distanceDecreaseButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance_decrease_button.setter
    def distance_decrease_button(self, target: str | Button | None) -> None:
        """Set the _distanceDecreaseButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_distanceDecreaseButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_distanceDecreaseButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def reset_button(self) -> str | None:
        """Target ID of the _resetButton reference (targets Button)."""
        member = self.get_member("_resetButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reset_button.setter
    def reset_button(self, target: str | Button | None) -> None:
        """Set the _resetButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_resetButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_resetButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def fov_slider(self) -> str | None:
        """Target ID of the _fovSlider reference (targets Slider[np.float32])."""
        member = self.get_member("_fovSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fov_slider.setter
    def fov_slider(self, target: str | Slider[np.float32] | None) -> None:
        """Set the _fovSlider reference by target ID or Slider[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_fovSlider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fovSlider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Slider<float>'),
            )

    @property
    def avoid_occlusion(self) -> str | None:
        """Target ID of the _avoidOcclusion reference (targets Checkbox)."""
        member = self.get_member("_avoidOcclusion")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @avoid_occlusion.setter
    def avoid_occlusion(self, target: str | Checkbox | None) -> None:
        """Set the _avoidOcclusion reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_avoidOcclusion")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_avoidOcclusion",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def keep_in_world_space(self) -> str | None:
        """Target ID of the _keepInWorldSpace reference (targets Checkbox)."""
        member = self.get_member("_keepInWorldSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @keep_in_world_space.setter
    def keep_in_world_space(self, target: str | Checkbox | None) -> None:
        """Set the _keepInWorldSpace reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_keepInWorldSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_keepInWorldSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def movement_wobble(self) -> str | None:
        """Target ID of the _movementWobble reference (targets Checkbox)."""
        member = self.get_member("_movementWobble")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @movement_wobble.setter
    def movement_wobble(self, target: str | Checkbox | None) -> None:
        """Set the _movementWobble reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_movementWobble")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_movementWobble",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def aim_in_front_of_head(self) -> str | None:
        """Target ID of the _aimInFrontOfHead reference (targets Checkbox)."""
        member = self.get_member("_aimInFrontOfHead")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @aim_in_front_of_head.setter
    def aim_in_front_of_head(self, target: str | Checkbox | None) -> None:
        """Set the _aimInFrontOfHead reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_aimInFrontOfHead")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_aimInFrontOfHead",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def force_eyes_on_camera(self) -> str | None:
        """Target ID of the _forceEyesOnCamera reference (targets Checkbox)."""
        member = self.get_member("_forceEyesOnCamera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @force_eyes_on_camera.setter
    def force_eyes_on_camera(self, target: str | Checkbox | None) -> None:
        """Set the _forceEyesOnCamera reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_forceEyesOnCamera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_forceEyesOnCamera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def hide_camera(self) -> str | None:
        """Target ID of the _hideCamera reference (targets Checkbox)."""
        member = self.get_member("_hideCamera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hide_camera.setter
    def hide_camera(self, target: str | Checkbox | None) -> None:
        """Set the _hideCamera reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_hideCamera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hideCamera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def hide_badge(self) -> str | None:
        """Target ID of the _hideBadge reference (targets Checkbox)."""
        member = self.get_member("_hideBadge")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hide_badge.setter
    def hide_badge(self, target: str | Checkbox | None) -> None:
        """Set the _hideBadge reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_hideBadge")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hideBadge",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def hide_lasers(self) -> str | None:
        """Target ID of the _hideLasers reference (targets Checkbox)."""
        member = self.get_member("_hideLasers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hide_lasers.setter
    def hide_lasers(self, target: str | Checkbox | None) -> None:
        """Set the _hideLasers reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_hideLasers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hideLasers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def show_frustum(self) -> str | None:
        """Target ID of the _showFrustum reference (targets Checkbox)."""
        member = self.get_member("_showFrustum")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @show_frustum.setter
    def show_frustum(self, target: str | Checkbox | None) -> None:
        """Set the _showFrustum reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_showFrustum")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_showFrustum",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def timer(self) -> str | None:
        """Target ID of the _timer reference (targets Checkbox)."""
        member = self.get_member("_timer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer.setter
    def timer(self, target: str | Checkbox | None) -> None:
        """Set the _timer reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_timer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def force_live(self) -> str | None:
        """Target ID of the _forceLive reference (targets Checkbox)."""
        member = self.get_member("_forceLive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @force_live.setter
    def force_live(self, target: str | Checkbox | None) -> None:
        """Set the _forceLive reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_forceLive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_forceLive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def audio_from_camera_viewpoint(self) -> str | None:
        """Target ID of the _audioFromCameraViewpoint reference (targets Checkbox)."""
        member = self.get_member("_audioFromCameraViewpoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_from_camera_viewpoint.setter
    def audio_from_camera_viewpoint(self, target: str | Checkbox | None) -> None:
        """Set the _audioFromCameraViewpoint reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_audioFromCameraViewpoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_audioFromCameraViewpoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def user_control(self) -> str | None:
        """Target ID of the _userControl reference (targets InteractiveCameraUserControl)."""
        member = self.get_member("_userControl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user_control.setter
    def user_control(self, target: str | InteractiveCameraUserControl | None) -> None:
        """Set the _userControl reference by target ID or InteractiveCameraUserControl instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraUserControl) else target  # type: ignore[assignment]
        member = self.get_member("_userControl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_userControl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraUserControl'),
            )

    @property
    def settings_dialog(self) -> str | None:
        """Target ID of the _settingsDialog reference (targets InteractiveCameraControlSettings)."""
        member = self.get_member("_settingsDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @settings_dialog.setter
    def settings_dialog(self, target: str | InteractiveCameraControlSettings | None) -> None:
        """Set the _settingsDialog reference by target ID or InteractiveCameraControlSettings instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraControlSettings) else target  # type: ignore[assignment]
        member = self.get_member("_settingsDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_settingsDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraControlSettings'),
            )

    @property
    def positioning_dialog(self) -> str | None:
        """Target ID of the _positioningDialog reference (targets InteractiveCameraControlPositioning)."""
        member = self.get_member("_positioningDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @positioning_dialog.setter
    def positioning_dialog(self, target: str | InteractiveCameraControlPositioning | None) -> None:
        """Set the _positioningDialog reference by target ID or InteractiveCameraControlPositioning instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraControlPositioning) else target  # type: ignore[assignment]
        member = self.get_member("_positioningDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positioningDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraControlPositioning'),
            )

    @property
    def anchors_dialog(self) -> str | None:
        """Target ID of the _anchorsDialog reference (targets InteractiveCameraControlAnchors)."""
        member = self.get_member("_anchorsDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchors_dialog.setter
    def anchors_dialog(self, target: str | InteractiveCameraControlAnchors | None) -> None:
        """Set the _anchorsDialog reference by target ID or InteractiveCameraControlAnchors instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraControlAnchors) else target  # type: ignore[assignment]
        member = self.get_member("_anchorsDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_anchorsDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraControlAnchors'),
            )

    @property
    def obs_dialog(self) -> str | None:
        """Target ID of the _OBS_Dialog reference (targets InteractiveCameraOBS)."""
        member = self.get_member("_OBS_Dialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @obs_dialog.setter
    def obs_dialog(self, target: str | InteractiveCameraOBS | None) -> None:
        """Set the _OBS_Dialog reference by target ID or InteractiveCameraOBS instance."""
        target_id: str | None = target.id if isinstance(target, InteractiveCameraOBS) else target  # type: ignore[assignment]
        member = self.get_member("_OBS_Dialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_OBS_Dialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractiveCameraOBS'),
            )

    @property
    def twitch_dialog(self) -> str | None:
        """Target ID of the _twitchDialog reference (targets TwitchChatDialog)."""
        member = self.get_member("_twitchDialog")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @twitch_dialog.setter
    def twitch_dialog(self, target: str | TwitchChatDialog | None) -> None:
        """Set the _twitchDialog reference by target ID or TwitchChatDialog instance."""
        target_id: str | None = target.id if isinstance(target, TwitchChatDialog) else target  # type: ignore[assignment]
        member = self.get_member("_twitchDialog")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_twitchDialog",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TwitchChatDialog'),
            )

    @property
    def settings_button(self) -> str | None:
        """Target ID of the _settingsButton reference (targets Button)."""
        member = self.get_member("_settingsButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @settings_button.setter
    def settings_button(self, target: str | Button | None) -> None:
        """Set the _settingsButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_settingsButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_settingsButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def positioning_button(self) -> str | None:
        """Target ID of the _positioningButton reference (targets Button)."""
        member = self.get_member("_positioningButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @positioning_button.setter
    def positioning_button(self, target: str | Button | None) -> None:
        """Set the _positioningButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_positioningButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_positioningButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def anchors_button(self) -> str | None:
        """Target ID of the _anchorsButton reference (targets Button)."""
        member = self.get_member("_anchorsButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchors_button.setter
    def anchors_button(self, target: str | Button | None) -> None:
        """Set the _anchorsButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_anchorsButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_anchorsButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def obs_button(self) -> str | None:
        """Target ID of the _OBS_Button reference (targets Button)."""
        member = self.get_member("_OBS_Button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @obs_button.setter
    def obs_button(self, target: str | Button | None) -> None:
        """Set the _OBS_Button reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_OBS_Button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_OBS_Button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def twitch_button(self) -> str | None:
        """Target ID of the _twitchButton reference (targets Button)."""
        member = self.get_member("_twitchButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @twitch_button.setter
    def twitch_button(self, target: str | Button | None) -> None:
        """Set the _twitchButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_twitchButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_twitchButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def preview_material(self) -> str | None:
        """Target ID of the _previewMaterial reference (targets UI_UnlitMaterial)."""
        member = self.get_member("_previewMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preview_material.setter
    def preview_material(self, target: str | UI_UnlitMaterial | None) -> None:
        """Set the _previewMaterial reference by target ID or UI_UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UI_UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_previewMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previewMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_UnlitMaterial'),
            )

