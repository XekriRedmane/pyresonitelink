"""Generated component: PhotoCaptureManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.photo_encode_format import PhotoEncodeFormat
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.render_texture_provider import RenderTextureProvider
from pyresonitelink.generated._types.quad_mesh import QuadMesh
from pyresonitelink.generated._types.frame_mesh import FrameMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.camera import Camera
from pyresonitelink.generated._types.unlit_material import UnlitMaterial
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.audio_clip_player import AudioClipPlayer
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PhotoCaptureManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The PhotoCaptureManager component is used to manage the finger photo capture ability for users and what settings to use for it.

    Not used directly by the user. auto generated.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotoCaptureManager"

    def __init__(self, finger_gesture_enabled: primitives.Bool | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, min_fov: primitives.Float | None = None, max_fov: primitives.Float | None = None, preview_resolution: primitives.Int2 | None = None, normal_resolution: primitives.Int2 | None = None, timer_resolution: primitives.Int2 | None = None, capture_stereo: primitives.Bool | None = None, stereo_separation: primitives.Float | None = None, timer_seconds: primitives.Float | None = None, hide_all_nameplates: primitives.Bool | None = None, encode_format: PhotoEncodeFormat | str | None = None, debug_gesture: primitives.Bool | None = None, timer_active: primitives.Bool | None = None, original_parent: str | Slot | None = None, original_position: primitives.Float3 | None = None, original_rotation: primitives.FloatQ | None = None, original_scale: primitives.Float3 | None = None, root: str | Slot | None = None, preview_root: str | Slot | None = None, render_tex: str | RenderTextureProvider | None = None, quad: str | QuadMesh | None = None, frame: str | FrameMesh | None = None, camera_root: str | Slot | None = None, camera_pos: str | IField[primitives.Float3] | None = None, camera_rot: str | IField[primitives.FloatQ] | None = None, camera: str | Camera | None = None, frame_material: str | UnlitMaterial | None = None, timer_text_root: str | Slot | None = None, timer_text: str | TextRenderer | None = None, shutter_clip: str | IAssetProvider[AudioClip] | None = None, timer_start_clip: str | IAssetProvider[AudioClip] | None = None, timer_countdown_slow_player: str | AudioClipPlayer | None = None, timer_countdown_fast_player: str | AudioClipPlayer | None = None, timer_countdown_slow_output: str | AudioOutput | None = None, timer_countdown_fast_output: str | AudioOutput | None = None, timer_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            finger_gesture_enabled: Initial value for FingerGestureEnabled.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            min_fov: Initial value for MinFOV.
            max_fov: Initial value for MaxFOV.
            preview_resolution: Initial value for PreviewResolution.
            normal_resolution: Initial value for NormalResolution.
            timer_resolution: Initial value for TimerResolution.
            capture_stereo: Initial value for CaptureStereo.
            stereo_separation: Initial value for StereoSeparation.
            timer_seconds: Initial value for TimerSeconds.
            hide_all_nameplates: Initial value for HideAllNameplates.
            encode_format: Initial value for EncodeFormat.
            debug_gesture: Initial value for DebugGesture.
            timer_active: Initial value for _timerActive.
            original_parent: Initial value for _originalParent.
            original_position: Initial value for _originalPosition.
            original_rotation: Initial value for _originalRotation.
            original_scale: Initial value for _originalScale.
            root: Initial value for _root.
            preview_root: Initial value for _previewRoot.
            render_tex: Initial value for _renderTex.
            quad: Initial value for _quad.
            frame: Initial value for _frame.
            camera_root: Initial value for _cameraRoot.
            camera_pos: Initial value for _cameraPos.
            camera_rot: Initial value for _cameraRot.
            camera: Initial value for _camera.
            frame_material: Initial value for _frameMaterial.
            timer_text_root: Initial value for _timerTextRoot.
            timer_text: Initial value for _timerText.
            shutter_clip: Initial value for _shutterClip.
            timer_start_clip: Initial value for _timerStartClip.
            timer_countdown_slow_player: Initial value for _timerCountdownSlowPlayer.
            timer_countdown_fast_player: Initial value for _timerCountdownFastPlayer.
            timer_countdown_slow_output: Initial value for _timerCountdownSlowOutput.
            timer_countdown_fast_output: Initial value for _timerCountdownFastOutput.
            timer_root: Initial value for _timerRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if finger_gesture_enabled is not None:
            self.finger_gesture_enabled = finger_gesture_enabled
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if min_fov is not None:
            self.min_fov = min_fov
        if max_fov is not None:
            self.max_fov = max_fov
        if preview_resolution is not None:
            self.preview_resolution = preview_resolution
        if normal_resolution is not None:
            self.normal_resolution = normal_resolution
        if timer_resolution is not None:
            self.timer_resolution = timer_resolution
        if capture_stereo is not None:
            self.capture_stereo = capture_stereo
        if stereo_separation is not None:
            self.stereo_separation = stereo_separation
        if timer_seconds is not None:
            self.timer_seconds = timer_seconds
        if hide_all_nameplates is not None:
            self.hide_all_nameplates = hide_all_nameplates
        if encode_format is not None:
            self.encode_format = encode_format
        if debug_gesture is not None:
            self.debug_gesture = debug_gesture
        if timer_active is not None:
            self.timer_active = timer_active
        if original_parent is not None:
            self.original_parent = original_parent
        if original_position is not None:
            self.original_position = original_position
        if original_rotation is not None:
            self.original_rotation = original_rotation
        if original_scale is not None:
            self.original_scale = original_scale
        if root is not None:
            self.root = root
        if preview_root is not None:
            self.preview_root = preview_root
        if render_tex is not None:
            self.render_tex = render_tex
        if quad is not None:
            self.quad = quad
        if frame is not None:
            self.frame = frame
        if camera_root is not None:
            self.camera_root = camera_root
        if camera_pos is not None:
            self.camera_pos = camera_pos
        if camera_rot is not None:
            self.camera_rot = camera_rot
        if camera is not None:
            self.camera = camera
        if frame_material is not None:
            self.frame_material = frame_material
        if timer_text_root is not None:
            self.timer_text_root = timer_text_root
        if timer_text is not None:
            self.timer_text = timer_text
        if shutter_clip is not None:
            self.shutter_clip = shutter_clip
        if timer_start_clip is not None:
            self.timer_start_clip = timer_start_clip
        if timer_countdown_slow_player is not None:
            self.timer_countdown_slow_player = timer_countdown_slow_player
        if timer_countdown_fast_player is not None:
            self.timer_countdown_fast_player = timer_countdown_fast_player
        if timer_countdown_slow_output is not None:
            self.timer_countdown_slow_output = timer_countdown_slow_output
        if timer_countdown_fast_output is not None:
            self.timer_countdown_fast_output = timer_countdown_fast_output
        if timer_root is not None:
            self.timer_root = timer_root

    @property
    def finger_gesture_enabled(self) -> primitives.Bool | None:
        """Whether the finger photo gesture can be used or not."""
        member = self.get_member("FingerGestureEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @finger_gesture_enabled.setter
    def finger_gesture_enabled(self, value: primitives.Bool) -> None:
        """Set the FingerGestureEnabled field value."""
        member = self.get_member("FingerGestureEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FingerGestureEnabled", fields.FieldBool(value=value)
            )

    @property
    def min_distance(self) -> primitives.Float | None:
        """The distance from the view to use for minimum FOV point."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: primitives.Float) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """The distance from the view to use for maximum FOV point."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def min_fov(self) -> primitives.Float | None:
        """The minimum FOV that can be achieved by moving the finger photo closer to the viewpoint."""
        member = self.get_member("MinFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_fov.setter
    def min_fov(self, value: primitives.Float) -> None:
        """Set the MinFOV field value."""
        member = self.get_member("MinFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinFOV", fields.FieldFloat(value=value)
            )

    @property
    def max_fov(self) -> primitives.Float | None:
        """The maximum FOV that can be achieved by moving the finger photo further from the viewpoint."""
        member = self.get_member("MaxFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_fov.setter
    def max_fov(self, value: primitives.Float) -> None:
        """Set the MaxFOV field value."""
        member = self.get_member("MaxFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxFOV", fields.FieldFloat(value=value)
            )

    @property
    def preview_resolution(self) -> primitives.Int2 | None:
        """The resolution of the texture shown on the preview graphic."""
        member = self.get_member("PreviewResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preview_resolution.setter
    def preview_resolution(self, value: primitives.Int2) -> None:
        """Set the PreviewResolution field value."""
        member = self.get_member("PreviewResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreviewResolution", fields.FieldInt2(value=value)
            )

    @property
    def normal_resolution(self) -> primitives.Int2 | None:
        """The resolution of the picture taken normally."""
        member = self.get_member("NormalResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_resolution.setter
    def normal_resolution(self, value: primitives.Int2) -> None:
        """Set the NormalResolution field value."""
        member = self.get_member("NormalResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalResolution", fields.FieldInt2(value=value)
            )

    @property
    def timer_resolution(self) -> primitives.Int2 | None:
        """The resolution of the picture taken via camera."""
        member = self.get_member("TimerResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timer_resolution.setter
    def timer_resolution(self, value: primitives.Int2) -> None:
        """Set the TimerResolution field value."""
        member = self.get_member("TimerResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TimerResolution", fields.FieldInt2(value=value)
            )

    @property
    def capture_stereo(self) -> primitives.Bool | None:
        """Whether the finger photo should capture a 3D photo."""
        member = self.get_member("CaptureStereo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @capture_stereo.setter
    def capture_stereo(self, value: primitives.Bool) -> None:
        """Set the CaptureStereo field value."""
        member = self.get_member("CaptureStereo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CaptureStereo", fields.FieldBool(value=value)
            )

    @property
    def stereo_separation(self) -> primitives.Float | None:
        """How much to separate the L and R "eye" positions for the camera capture."""
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
    def timer_seconds(self) -> primitives.Float | None:
        """How many seconds the finger photo timer should be."""
        member = self.get_member("TimerSeconds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timer_seconds.setter
    def timer_seconds(self, value: primitives.Float) -> None:
        """Set the TimerSeconds field value."""
        member = self.get_member("TimerSeconds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TimerSeconds", fields.FieldFloat(value=value)
            )

    @property
    def hide_all_nameplates(self) -> primitives.Bool | None:
        """Whether to hide all nameplates for taking the photo."""
        member = self.get_member("HideAllNameplates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_all_nameplates.setter
    def hide_all_nameplates(self, value: primitives.Bool) -> None:
        """Set the HideAllNameplates field value."""
        member = self.get_member("HideAllNameplates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideAllNameplates", fields.FieldBool(value=value)
            )

    @property
    def encode_format(self) -> PhotoEncodeFormat | None:
        """What format to encode the resulting picture in."""
        member = self.get_member("EncodeFormat")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhotoEncodeFormat(member.value)
        return None

    @encode_format.setter
    def encode_format(self, value: PhotoEncodeFormat | str) -> None:
        """Set EncodeFormat. What format to encode the resulting picture in."""
        member = self.get_member("EncodeFormat")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "EncodeFormat",
                members.FieldEnum(value=str(value)),
            )

    @property
    def debug_gesture(self) -> primitives.Bool | None:
        """Whether to debug the user's gesture angles/position for achieving a valid finger photo gesture position."""
        member = self.get_member("DebugGesture")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_gesture.setter
    def debug_gesture(self, value: primitives.Bool) -> None:
        """Set the DebugGesture field value."""
        member = self.get_member("DebugGesture")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DebugGesture", fields.FieldBool(value=value)
            )

    @property
    def timer_active(self) -> primitives.Bool | None:
        """Whether the timer is currently going or not."""
        member = self.get_member("_timerActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timer_active.setter
    def timer_active(self, value: primitives.Bool) -> None:
        """Set the _timerActive field value."""
        member = self.get_member("_timerActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_timerActive", fields.FieldBool(value=value)
            )

    @property
    def original_parent(self) -> str | None:
        """The original parent of this manager."""
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_parent.setter
    def original_parent(self, target: str | Slot | None) -> None:
        """Set the _originalParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_originalParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_originalParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def original_position(self) -> primitives.Float3 | None:
        """The original position of this manager."""
        member = self.get_member("_originalPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_position.setter
    def original_position(self, value: primitives.Float3) -> None:
        """Set the _originalPosition field value."""
        member = self.get_member("_originalPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalPosition", fields.FieldFloat3(value=value)
            )

    @property
    def original_rotation(self) -> primitives.FloatQ | None:
        """The original rotation of this manager."""
        member = self.get_member("_originalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_rotation.setter
    def original_rotation(self, value: primitives.FloatQ) -> None:
        """Set the _originalRotation field value."""
        member = self.get_member("_originalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def original_scale(self) -> primitives.Float3 | None:
        """The original scale of this manager."""
        member = self.get_member("_originalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @original_scale.setter
    def original_scale(self, value: primitives.Float3) -> None:
        """Set the _originalScale field value."""
        member = self.get_member("_originalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_originalScale", fields.FieldFloat3(value=value)
            )

    @property
    def root(self) -> str | None:
        """The root of this entire finger photo manager."""
        member = self.get_member("_root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the _root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def preview_root(self) -> str | None:
        """The slot that is the root of the preview graphic."""
        member = self.get_member("_previewRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @preview_root.setter
    def preview_root(self, target: str | Slot | None) -> None:
        """Set the _previewRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_previewRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previewRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def render_tex(self) -> str | None:
        """The texture being used for the preview render graphic."""
        member = self.get_member("_renderTex")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_tex.setter
    def render_tex(self, target: str | RenderTextureProvider | None) -> None:
        """Set the _renderTex reference by target ID or RenderTextureProvider instance."""
        target_id: str | None = target.id if isinstance(target, RenderTextureProvider) else target  # type: ignore[assignment]
        member = self.get_member("_renderTex")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderTex",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RenderTextureProvider'),
            )

    @property
    def quad(self) -> str | None:
        """The quad to render the preview with."""
        member = self.get_member("_quad")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @quad.setter
    def quad(self, target: str | QuadMesh | None) -> None:
        """Set the _quad reference by target ID or QuadMesh instance."""
        target_id: str | None = target.id if isinstance(target, QuadMesh) else target  # type: ignore[assignment]
        member = self.get_member("_quad")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_quad",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.QuadMesh'),
            )

    @property
    def frame(self) -> str | None:
        """The frame mesh being used for the preview graphic."""
        member = self.get_member("_frame")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frame.setter
    def frame(self, target: str | FrameMesh | None) -> None:
        """Set the _frame reference by target ID or FrameMesh instance."""
        target_id: str | None = target.id if isinstance(target, FrameMesh) else target  # type: ignore[assignment]
        member = self.get_member("_frame")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frame",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FrameMesh'),
            )

    @property
    def camera_root(self) -> str | None:
        """The slot being used for the camera's transforms."""
        member = self.get_member("_cameraRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_root.setter
    def camera_root(self, target: str | Slot | None) -> None:
        """Set the _cameraRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_cameraRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cameraRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def camera_pos(self) -> str | None:
        """The position field of the camera."""
        member = self.get_member("_cameraPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_pos.setter
    def camera_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _cameraPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cameraPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cameraPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def camera_rot(self) -> str | None:
        """The rotation field of the camera."""
        member = self.get_member("_cameraRot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera_rot.setter
    def camera_rot(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _cameraRot reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_cameraRot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_cameraRot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def camera(self) -> str | None:
        """The camera component reference itself."""
        member = self.get_member("_camera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera.setter
    def camera(self, target: str | Camera | None) -> None:
        """Set the _camera reference by target ID or Camera instance."""
        target_id: str | None = target.id if isinstance(target, Camera) else target  # type: ignore[assignment]
        member = self.get_member("_camera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_camera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Camera'),
            )

    @property
    def frame_material(self) -> str | None:
        """The material being used for the frame visual for the preview graphic."""
        member = self.get_member("_frameMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @frame_material.setter
    def frame_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _frameMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_frameMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_frameMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def timer_text_root(self) -> str | None:
        """The root slot of the visual being used for the timer text."""
        member = self.get_member("_timerTextRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_text_root.setter
    def timer_text_root(self, target: str | Slot | None) -> None:
        """Set the _timerTextRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_timerTextRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerTextRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def timer_text(self) -> str | None:
        """The component being used to display the timer text."""
        member = self.get_member("_timerText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_text.setter
    def timer_text(self, target: str | TextRenderer | None) -> None:
        """Set the _timerText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_timerText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def shutter_clip(self) -> str | None:
        """The audio to play when a photo is taken."""
        member = self.get_member("_shutterClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shutter_clip.setter
    def shutter_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _shutterClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_shutterClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shutterClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def timer_start_clip(self) -> str | None:
        """The audio to play when the timer starts."""
        member = self.get_member("_timerStartClip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_start_clip.setter
    def timer_start_clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the _timerStartClip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_timerStartClip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerStartClip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    @property
    def timer_countdown_slow_player(self) -> str | None:
        """The audio to play when the timer has plenty of time left."""
        member = self.get_member("_timerCountdownSlowPlayer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_slow_player.setter
    def timer_countdown_slow_player(self, target: str | AudioClipPlayer | None) -> None:
        """Set the _timerCountdownSlowPlayer reference by target ID or AudioClipPlayer instance."""
        target_id: str | None = target.id if isinstance(target, AudioClipPlayer) else target  # type: ignore[assignment]
        member = self.get_member("_timerCountdownSlowPlayer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerCountdownSlowPlayer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioClipPlayer'),
            )

    @property
    def timer_countdown_fast_player(self) -> str | None:
        """The audio to play when the timer is close to being finished."""
        member = self.get_member("_timerCountdownFastPlayer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_fast_player.setter
    def timer_countdown_fast_player(self, target: str | AudioClipPlayer | None) -> None:
        """Set the _timerCountdownFastPlayer reference by target ID or AudioClipPlayer instance."""
        target_id: str | None = target.id if isinstance(target, AudioClipPlayer) else target  # type: ignore[assignment]
        member = self.get_member("_timerCountdownFastPlayer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerCountdownFastPlayer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioClipPlayer'),
            )

    @property
    def timer_countdown_slow_output(self) -> str | None:
        """The audio output component outputting the timer has plenty of time sound."""
        member = self.get_member("_timerCountdownSlowOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_slow_output.setter
    def timer_countdown_slow_output(self, target: str | AudioOutput | None) -> None:
        """Set the _timerCountdownSlowOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("_timerCountdownSlowOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerCountdownSlowOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def timer_countdown_fast_output(self) -> str | None:
        """The audio output component outputting the timer is close to being done sound."""
        member = self.get_member("_timerCountdownFastOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_countdown_fast_output.setter
    def timer_countdown_fast_output(self, target: str | AudioOutput | None) -> None:
        """Set the _timerCountdownFastOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("_timerCountdownFastOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerCountdownFastOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def timer_root(self) -> str | None:
        """The root slot of the entire timer visual and mechanism."""
        member = self.get_member("_timerRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @timer_root.setter
    def timer_root(self, target: str | Slot | None) -> None:
        """Set the _timerRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_timerRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_timerRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

