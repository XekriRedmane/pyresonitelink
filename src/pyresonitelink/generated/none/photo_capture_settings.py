"""Generated component: PhotoCaptureSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.photo_encode_format import PhotoEncodeFormat
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class PhotoCaptureSettings(GeneratedComponent, ICustomInspector):
    """The PhotoCaptureSettings component is used to control the behavior of the PhotoCaptureManager and what it does.

See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotoCaptureSettings"

    def __init__(self, finger_gesture_enabled: primitives.Bool | None = None, normal_capture_resolution: primitives.Int2 | None = None, timer_capture_resolution: primitives.Int2 | None = None, timer_seconds: primitives.Float | None = None, hands_near_fov: primitives.Float | None = None, hands_far_fov: primitives.Float | None = None, capture_private_ui: primitives.Bool | None = None, capture_stereo: primitives.Bool | None = None, stereo_separation: primitives.Float | None = None, always_hide_nameplates: primitives.Bool | None = None, encode_format: PhotoEncodeFormat | str | None = None, photo_autosave_path: primitives.String | None = None, autosave_active: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            finger_gesture_enabled: Initial value for FingerGestureEnabled.
            normal_capture_resolution: Initial value for NormalCaptureResolution.
            timer_capture_resolution: Initial value for TimerCaptureResolution.
            timer_seconds: Initial value for TimerSeconds.
            hands_near_fov: Initial value for HandsNearFOV.
            hands_far_fov: Initial value for HandsFarFOV.
            capture_private_ui: Initial value for CapturePrivateUI.
            capture_stereo: Initial value for CaptureStereo.
            stereo_separation: Initial value for StereoSeparation.
            always_hide_nameplates: Initial value for AlwaysHideNameplates.
            encode_format: Initial value for EncodeFormat.
            photo_autosave_path: Initial value for PhotoAutosavePath.
            autosave_active: Initial value for AutosaveActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if finger_gesture_enabled is not None:
            self.finger_gesture_enabled = finger_gesture_enabled
        if normal_capture_resolution is not None:
            self.normal_capture_resolution = normal_capture_resolution
        if timer_capture_resolution is not None:
            self.timer_capture_resolution = timer_capture_resolution
        if timer_seconds is not None:
            self.timer_seconds = timer_seconds
        if hands_near_fov is not None:
            self.hands_near_fov = hands_near_fov
        if hands_far_fov is not None:
            self.hands_far_fov = hands_far_fov
        if capture_private_ui is not None:
            self.capture_private_ui = capture_private_ui
        if capture_stereo is not None:
            self.capture_stereo = capture_stereo
        if stereo_separation is not None:
            self.stereo_separation = stereo_separation
        if always_hide_nameplates is not None:
            self.always_hide_nameplates = always_hide_nameplates
        if encode_format is not None:
            self.encode_format = encode_format
        if photo_autosave_path is not None:
            self.photo_autosave_path = photo_autosave_path
        if autosave_active is not None:
            self.autosave_active = autosave_active

    @property
    def finger_gesture_enabled(self) -> primitives.Bool | None:
        """Whether the finger photos should even render."""
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
    def normal_capture_resolution(self) -> primitives.Int2 | None:
        """The resolution of pictures taken without timer."""
        member = self.get_member("NormalCaptureResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_capture_resolution.setter
    def normal_capture_resolution(self, value: primitives.Int2) -> None:
        """Set the NormalCaptureResolution field value."""
        member = self.get_member("NormalCaptureResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalCaptureResolution", fields.FieldInt2(value=value)
            )

    @property
    def timer_capture_resolution(self) -> primitives.Int2 | None:
        """The resolution of pictures taken with timer."""
        member = self.get_member("TimerCaptureResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timer_capture_resolution.setter
    def timer_capture_resolution(self, value: primitives.Int2) -> None:
        """Set the TimerCaptureResolution field value."""
        member = self.get_member("TimerCaptureResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TimerCaptureResolution", fields.FieldInt2(value=value)
            )

    @property
    def timer_seconds(self) -> primitives.Float | None:
        """How long the timer should be for timed photos."""
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
    def hands_near_fov(self) -> primitives.Float | None:
        """The HandsNearFOV field value."""
        member = self.get_member("HandsNearFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hands_near_fov.setter
    def hands_near_fov(self, value: primitives.Float) -> None:
        """Set the HandsNearFOV field value."""
        member = self.get_member("HandsNearFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandsNearFOV", fields.FieldFloat(value=value)
            )

    @property
    def hands_far_fov(self) -> primitives.Float | None:
        """The HandsFarFOV field value."""
        member = self.get_member("HandsFarFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hands_far_fov.setter
    def hands_far_fov(self, value: primitives.Float) -> None:
        """Set the HandsFarFOV field value."""
        member = self.get_member("HandsFarFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HandsFarFOV", fields.FieldFloat(value=value)
            )

    @property
    def capture_private_ui(self) -> primitives.Bool | None:
        """Whether finger photos should capture private ui elements like the dash."""
        member = self.get_member("CapturePrivateUI")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @capture_private_ui.setter
    def capture_private_ui(self, value: primitives.Bool) -> None:
        """Set the CapturePrivateUI field value."""
        member = self.get_member("CapturePrivateUI")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CapturePrivateUI", fields.FieldBool(value=value)
            )

    @property
    def capture_stereo(self) -> primitives.Bool | None:
        """Whether photos should be 3D with a left and right "eye"."""
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
        """how far apart the left and right "eye" are when taking stereo photos."""
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
    def always_hide_nameplates(self) -> primitives.Bool | None:
        """Whether to always hide nameplates in taken photos."""
        member = self.get_member("AlwaysHideNameplates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @always_hide_nameplates.setter
    def always_hide_nameplates(self, value: primitives.Bool) -> None:
        """Set the AlwaysHideNameplates field value."""
        member = self.get_member("AlwaysHideNameplates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlwaysHideNameplates", fields.FieldBool(value=value)
            )

    @property
    def encode_format(self) -> PhotoEncodeFormat | None:
        """The format taken photos should output as."""
        member = self.get_member("EncodeFormat")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PhotoEncodeFormat(member.value)
        return None

    @encode_format.setter
    def encode_format(self, value: PhotoEncodeFormat | str) -> None:
        """Set EncodeFormat. The format taken photos should output as."""
        member = self.get_member("EncodeFormat")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "EncodeFormat",
                members.FieldEnum(value=str(value)),
            )

    @property
    def photo_autosave_path(self) -> primitives.String | None:
        """Where to auto save photos in the inventory to."""
        member = self.get_member("PhotoAutosavePath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @photo_autosave_path.setter
    def photo_autosave_path(self, value: primitives.String) -> None:
        """Set the PhotoAutosavePath field value."""
        member = self.get_member("PhotoAutosavePath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PhotoAutosavePath", fields.FieldString(value=value)
            )

    @property
    def autosave_active(self) -> primitives.Bool | None:
        """Whether to use the auto save photos to inventory feature."""
        member = self.get_member("AutosaveActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @autosave_active.setter
    def autosave_active(self, value: primitives.Bool) -> None:
        """Set the AutosaveActive field value."""
        member = self.get_member("AutosaveActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutosaveActive", fields.FieldBool(value=value)
            )

    async def open_autosave_path(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Opens the auto save path set in the settings.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OpenAutosavePath", {}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

