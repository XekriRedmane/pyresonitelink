"""Generated component: PostProcessingSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class PostProcessingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.PostProcessingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PostProcessingSettings"

    def __init__(self, motion_blur_intensity: np.float32 | None = None, bloom_intensity: np.float32 | None = None, ambient_occlusion_intensity: np.float32 | None = None, screen_space_reflections: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            motion_blur_intensity: Initial value for MotionBlurIntensity.
            bloom_intensity: Initial value for BloomIntensity.
            ambient_occlusion_intensity: Initial value for AmbientOcclusionIntensity.
            screen_space_reflections: Initial value for ScreenSpaceReflections.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if motion_blur_intensity is not None:
            self.motion_blur_intensity = motion_blur_intensity
        if bloom_intensity is not None:
            self.bloom_intensity = bloom_intensity
        if ambient_occlusion_intensity is not None:
            self.ambient_occlusion_intensity = ambient_occlusion_intensity
        if screen_space_reflections is not None:
            self.screen_space_reflections = screen_space_reflections

    @property
    def motion_blur_intensity(self) -> np.float32 | None:
        """The MotionBlurIntensity field value."""
        member = self.get_member("MotionBlurIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @motion_blur_intensity.setter
    def motion_blur_intensity(self, value: np.float32) -> None:
        """Set the MotionBlurIntensity field value."""
        member = self.get_member("MotionBlurIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MotionBlurIntensity", fields.FieldFloat(value=value)
            )

    @property
    def bloom_intensity(self) -> np.float32 | None:
        """The BloomIntensity field value."""
        member = self.get_member("BloomIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bloom_intensity.setter
    def bloom_intensity(self, value: np.float32) -> None:
        """Set the BloomIntensity field value."""
        member = self.get_member("BloomIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BloomIntensity", fields.FieldFloat(value=value)
            )

    @property
    def ambient_occlusion_intensity(self) -> np.float32 | None:
        """The AmbientOcclusionIntensity field value."""
        member = self.get_member("AmbientOcclusionIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ambient_occlusion_intensity.setter
    def ambient_occlusion_intensity(self, value: np.float32) -> None:
        """Set the AmbientOcclusionIntensity field value."""
        member = self.get_member("AmbientOcclusionIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AmbientOcclusionIntensity", fields.FieldFloat(value=value)
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
    def antialiasing(self) -> members.FieldEnum | None:
        """The Antialiasing member."""
        member = self.get_member("Antialiasing")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @antialiasing.setter
    def antialiasing(self, value: members.FieldEnum) -> None:
        """Set the Antialiasing member."""
        self.set_member("Antialiasing", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

