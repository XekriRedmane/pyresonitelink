"""Generated component: InteractiveCameraControl."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.camera_positioning_mode import CameraPositioningMode
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
    """See Camera.

    See Camera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraControl"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, field_of_view: primitives.Float | None = None, angle_position: primitives.Float | None = None, distance: primitives.Float | None = None, height_offset: primitives.Float | None = None, first_person_pitch: primitives.Float | None = None, first_person_roll: primitives.Float | None = None, first_person_offset: primitives.Float | None = None, framing_viewport_position: primitives.Float2 | None = None, mirror: primitives.Bool | None = None, group_detection_radius: primitives.Float | None = None, group_leave_boundary: primitives.Float | None = None, position_smooth_speed: primitives.Float | None = None, angle_smooth_speed: primitives.Float | None = None, framing_smooth_speed: primitives.Float | None = None, interpolate_between_anchors: primitives.Bool | None = None, anchor_interpolation_speed: primitives.Float | None = None, anchor_linear_interpolation: primitives.Bool | None = None, mode: CameraPositioningMode | str | None = None, framing_target_override: primitives.String | None = None, render_for_everyone: primitives.Bool | None = None, anyone_can_interact: primitives.Bool | None = None, render_private_ui: primitives.Bool | None = None, motion_blur: primitives.Bool | None = None, screen_space_reflections: primitives.Bool | None = None, spawn_photo_in_world: primitives.Bool | None = None, flip_preview: primitives.Bool | None = None, render_texture_proxy: str | RenderTextureProxyProvider | None = None, framing_reticle: str | RectTransform | None = None, mirror_message: str | RectTransform | None = None, smooth_first_person_button: str | Button | None = None, third_person_button: str | Button | None = None, group_button: str | Button | None = None, world_button: str | Button | None = None, manual_button: str | Button | None = None, mirror_button: str | Button | None = None, users_button: str | Button | None = None, angle_increase_button: str | Button | None = None, angle_decrease_button: str | Button | None = None, height_increase_button: str | Button | None = None, height_decrease_button: str | Button | None = None, distance_increase_button: str | Button | None = None, distance_decrease_button: str | Button | None = None, reset_button: str | Button | None = None, fov_slider: str | Slider[primitives.Float] | None = None, avoid_occlusion: str | Checkbox | None = None, keep_in_world_space: str | Checkbox | None = None, movement_wobble: str | Checkbox | None = None, aim_in_front_of_head: str | Checkbox | None = None, force_eyes_on_camera: str | Checkbox | None = None, hide_camera: str | Checkbox | None = None, hide_badge: str | Checkbox | None = None, hide_lasers: str | Checkbox | None = None, show_frustum: str | Checkbox | None = None, timer: str | Checkbox | None = None, force_live: str | Checkbox | None = None, audio_from_camera_viewpoint: str | Checkbox | None = None, user_control: str | InteractiveCameraUserControl | None = None, settings_dialog: str | InteractiveCameraControlSettings | None = None, positioning_dialog: str | InteractiveCameraControlPositioning | None = None, anchors_dialog: str | InteractiveCameraControlAnchors | None = None, obs_dialog: str | InteractiveCameraOBS | None = None, twitch_dialog: str | TwitchChatDialog | None = None, settings_button: str | Button | None = None, positioning_button: str | Button | None = None, anchors_button: str | Button | None = None, obs_button: str | Button | None = None, twitch_button: str | Button | None = None, preview_material: str | UI_UnlitMaterial | None = None, *, component: workers.Component | None = None) -> None:
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
            mode: Initial value for Mode.
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
        if mode is not None:
            self.mode = mode
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
        """The canvas being used to show settings."""
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
        """The legacy panel being used as a base to interact with the settings."""
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
    def field_of_view(self) -> primitives.Float | None:
        """The field of view for the camera. The default is ``60``."""
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
    def angle_position(self) -> primitives.Float | None:
        """The rotation around the subject. The default is ``0.00``."""
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
        """The distance from the camera and the subject. The default is ``1.50``."""
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
        """The height for this camera to be at. The default is ``0``."""
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
        """Adjust the up and down angle of the camera when the camera is in ``Smooth POV`` mode. The default is ``5.00``."""
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
        """Adjust the rotation of the camera when the camera is in ``Smooth POV`` mode. The default is ``0.00``."""
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
        """Adjust the forward offset of the camera when the camera is in ``Smooth POV`` mode. The default is ``0.02``."""
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
    def framing_viewport_position(self) -> primitives.Float2 | None:
        """How to shift the camera framing like an offset."""
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
    def mirror(self) -> primitives.Bool | None:
        """Mirrors the camera view."""
        member = self.get_member("Mirror")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mirror.setter
    def mirror(self, value: primitives.Bool) -> None:
        """Set the Mirror field value."""
        member = self.get_member("Mirror")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mirror", fields.FieldBool(value=value)
            )

    @property
    def group_detection_radius(self) -> primitives.Float | None:
        """This is the range to include users into a group photo and to have the camera focus all of them as the subject."""
        member = self.get_member("GroupDetectionRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_detection_radius.setter
    def group_detection_radius(self, value: primitives.Float) -> None:
        """Set the GroupDetectionRadius field value."""
        member = self.get_member("GroupDetectionRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupDetectionRadius", fields.FieldFloat(value=value)
            )

    @property
    def group_leave_boundary(self) -> primitives.Float | None:
        """This is the far range to exclude other users from the group range."""
        member = self.get_member("GroupLeaveBoundary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @group_leave_boundary.setter
    def group_leave_boundary(self, value: primitives.Float) -> None:
        """Set the GroupLeaveBoundary field value."""
        member = self.get_member("GroupLeaveBoundary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GroupLeaveBoundary", fields.FieldFloat(value=value)
            )

    @property
    def position_smooth_speed(self) -> primitives.Float | None:
        """How fast or slow the camera position movement should be smoothed."""
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
    def angle_smooth_speed(self) -> primitives.Float | None:
        """The smoothness of how fast this camera turns and rotates to adjust for movement, to focus towards the subject."""
        member = self.get_member("AngleSmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @angle_smooth_speed.setter
    def angle_smooth_speed(self, value: primitives.Float) -> None:
        """Set the AngleSmoothSpeed field value."""
        member = self.get_member("AngleSmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AngleSmoothSpeed", fields.FieldFloat(value=value)
            )

    @property
    def framing_smooth_speed(self) -> primitives.Float | None:
        """This is how fast the camera will move in frame towards the subject."""
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
    def interpolate_between_anchors(self) -> primitives.Bool | None:
        """This allows the camera to smoothly go between anchor positions and rotations. If this is off, the camera will instantly go to the anchor instead of being smooth."""
        member = self.get_member("InterpolateBetweenAnchors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @interpolate_between_anchors.setter
    def interpolate_between_anchors(self, value: primitives.Bool) -> None:
        """Set the InterpolateBetweenAnchors field value."""
        member = self.get_member("InterpolateBetweenAnchors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InterpolateBetweenAnchors", fields.FieldBool(value=value)
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
    def mode(self) -> CameraPositioningMode | None:
        """How the camera should position itself."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CameraPositioningMode(member.value)
        return None

    @mode.setter
    def mode(self, value: CameraPositioningMode | str) -> None:
        """Set Mode. How the camera should position itself."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def framing_target_override(self) -> primitives.String | None:
        """Frame only the user with this username."""
        member = self.get_member("FramingTargetOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @framing_target_override.setter
    def framing_target_override(self, value: primitives.String) -> None:
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
        """A list of people who can interact with the camera."""
        member = self.get_member("CameraOperators")
        if isinstance(member, members.SyncList):
            return member
        return None

    @camera_operators.setter
    def camera_operators(self, value: members.SyncList) -> None:
        """Set CameraOperators. A list of people who can interact with the camera."""
        self.set_member("CameraOperators", value)

    @property
    def group_include_users(self) -> members.SyncList | None:
        """A list of users to force include into the target group."""
        member = self.get_member("GroupIncludeUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @group_include_users.setter
    def group_include_users(self, value: members.SyncList) -> None:
        """Set GroupIncludeUsers. A list of users to force include into the target group."""
        self.set_member("GroupIncludeUsers", value)

    @property
    def group_exclude_users(self) -> members.SyncList | None:
        """A list of users to force exclude from the target group."""
        member = self.get_member("GroupExcludeUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @group_exclude_users.setter
    def group_exclude_users(self, value: members.SyncList) -> None:
        """Set GroupExcludeUsers. A list of users to force exclude from the target group."""
        self.set_member("GroupExcludeUsers", value)

    @property
    def render_for_everyone(self) -> primitives.Bool | None:
        """This shows the preview to any user that is looking at the preview window on the camera."""
        member = self.get_member("RenderForEveryone")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_for_everyone.setter
    def render_for_everyone(self, value: primitives.Bool) -> None:
        """Set the RenderForEveryone field value."""
        member = self.get_member("RenderForEveryone")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderForEveryone", fields.FieldBool(value=value)
            )

    @property
    def anyone_can_interact(self) -> primitives.Bool | None:
        """This allows any user to interact with the your camera."""
        member = self.get_member("AnyoneCanInteract")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anyone_can_interact.setter
    def anyone_can_interact(self, value: primitives.Bool) -> None:
        """Set the AnyoneCanInteract field value."""
        member = self.get_member("AnyoneCanInteract")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnyoneCanInteract", fields.FieldBool(value=value)
            )

    @property
    def render_private_ui(self) -> primitives.Bool | None:
        """This shows the Camera Controls Panel to be shown in the preview and pictures."""
        member = self.get_member("RenderPrivateUI")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_private_ui.setter
    def render_private_ui(self, value: primitives.Bool) -> None:
        """Set the RenderPrivateUI field value."""
        member = self.get_member("RenderPrivateUI")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderPrivateUI", fields.FieldBool(value=value)
            )

    @property
    def motion_blur(self) -> primitives.Bool | None:
        """This enables the camera to have motion blue as it moves."""
        member = self.get_member("MotionBlur")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @motion_blur.setter
    def motion_blur(self, value: primitives.Bool) -> None:
        """Set the MotionBlur field value."""
        member = self.get_member("MotionBlur")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MotionBlur", fields.FieldBool(value=value)
            )

    @property
    def screen_space_reflections(self) -> primitives.Bool | None:
        """This shows screen space reflection through the preview and pictures."""
        member = self.get_member("ScreenSpaceReflections")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_space_reflections.setter
    def screen_space_reflections(self, value: primitives.Bool) -> None:
        """Set the ScreenSpaceReflections field value."""
        member = self.get_member("ScreenSpaceReflections")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenSpaceReflections", fields.FieldBool(value=value)
            )

    @property
    def spawn_photo_in_world(self) -> primitives.Bool | None:
        """This will spawn the photo in to the world after a picture is taken. If this is off, it will only be saved on your device."""
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
    def flip_preview(self) -> primitives.Bool | None:
        """This flips the preview window, but not for the photo being taken. This also reverses the direction for the preview window when clicking on it as well."""
        member = self.get_member("FlipPreview")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_preview.setter
    def flip_preview(self, value: primitives.Bool) -> None:
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
        """The texture to render to."""
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
        """The rectangle to frame with."""
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
        """The text for the label for the mirroring button."""
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
        """Enable/disable button for smooth first person."""
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
        """Enable/disable button for"""
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
        """Enable/disable button for"""
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
        """Enable/disable button for"""
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
        """Enable/disable button for"""
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
        """Enable/disable button for"""
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
        """Enable/disable button for"""
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
        """adjust button for"""
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
        """adjust button for"""
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
        """adjust button for"""
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
        """adjust button for"""
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
        """adjust button for"""
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
        """adjust button for"""
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
        """resets the selected options to the default value."""
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
        """Slider for the Field of view amount."""
        member = self.get_member("_fovSlider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fov_slider.setter
    def fov_slider(self, target: str | Slider[primitives.Float] | None) -> None:
        """Set the _fovSlider reference by target ID or Slider[primitives.Float] instance."""
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
        """When the camera is behind a wall or anything that is collidable, it will zoom the view in front of it to focus on the subject. This will not work in manual mode."""
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
        """This keeps the camera in world space."""
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
        """This makes the camera have gradual movement in different positions around the subject. This only works with Third Person or Group modes."""
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
        """This aims the camera view more towards the user's head, specifically a few inches/centimeters in front of the head proxy's forward direction. This only works for the Third Person, Group, and World modes."""
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
        """This makes the user's avatar's eyes lock on to the camera position."""
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
        """This hides the camera visual, but will still track the subject or stay in place as before with manual mode or with camera anchors."""
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
        """This hides the user's badges (including the nameplate) from the camera preview and any pictures taken."""
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
        """This hides the user's lasers from the camera preview and any pictures taken."""
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
        """This shows where the camera is aimed and focused at in 3D space."""
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
        """Sets up the camera to have a timer when the photo button is pressed. The timer can be set to have a preset amount of time or a custom time, found on the back of the camera itself."""
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
        """Shows the live badge to let other user's know that you are live and streaming to somewhere external from Resonite."""
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
        """This moves your audio listeners (your audio output or ears) to where the camera is, overriding thier position to take in audio from. This can be checked for using the local output category in ProtoFlux."""
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
        """see Interactive Camera User Control."""
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
        """see Interactive Camera Control Settings."""
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
        """see Interactive Camera Control Positioning."""
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
        """see Interactive Camera Control Anchors."""
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
        """see Interactive Camera OBS."""
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
        """see Twitch Chat Dialog."""
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
        """opens the settings for the camera."""
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
        """Allows for changing the positioning"""
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
        """Allows for changing the anchor points."""
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
        """Allows for showing and changing the OBS settings."""
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
        """Allows for showing and changing the Twitch settings."""
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
        """Shows the camera preview."""
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

