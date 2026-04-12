"""Generated component: PostProcessingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.anti_aliasing_method import AntiAliasingMethod
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class PostProcessingSettings(GeneratedComponent, ICustomInspector):
    """See Post Processing Settings.

    See Post Processing Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PostProcessingSettings"

    def __init__(self, motion_blur_intensity: primitives.Float | None = None, bloom_intensity: primitives.Float | None = None, ambient_occlusion_intensity: primitives.Float | None = None, screen_space_reflections: primitives.Bool | None = None, antialiasing: AntiAliasingMethod | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            motion_blur_intensity: Initial value for MotionBlurIntensity.
            bloom_intensity: Initial value for BloomIntensity.
            ambient_occlusion_intensity: Initial value for AmbientOcclusionIntensity.
            screen_space_reflections: Initial value for ScreenSpaceReflections.
            antialiasing: Initial value for Antialiasing.
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
        if antialiasing is not None:
            self.antialiasing = antialiasing

    @property
    def motion_blur_intensity(self) -> primitives.Float | None:
        """Controls the strength of motion blur, disabled entirely if set to 0%."""
        member = self.get_member("MotionBlurIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @motion_blur_intensity.setter
    def motion_blur_intensity(self, value: primitives.Float) -> None:
        """Set the MotionBlurIntensity field value."""
        member = self.get_member("MotionBlurIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MotionBlurIntensity", fields.FieldFloat(value=value)
            )

    @property
    def bloom_intensity(self) -> primitives.Float | None:
        """The Bloom effect causes a glow to appear around bright objects in the scene, disabled entirely if set to 0%."""
        member = self.get_member("BloomIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bloom_intensity.setter
    def bloom_intensity(self, value: primitives.Float) -> None:
        """Set the BloomIntensity field value."""
        member = self.get_member("BloomIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BloomIntensity", fields.FieldFloat(value=value)
            )

    @property
    def ambient_occlusion_intensity(self) -> primitives.Float | None:
        """Adds shading in corners and area that'd receive less light. Controls the strength of Ambient Occlusion, disabled entirely if set to 0%."""
        member = self.get_member("AmbientOcclusionIntensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ambient_occlusion_intensity.setter
    def ambient_occlusion_intensity(self, value: primitives.Float) -> None:
        """Set the AmbientOcclusionIntensity field value."""
        member = self.get_member("AmbientOcclusionIntensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AmbientOcclusionIntensity", fields.FieldFloat(value=value)
            )

    @property
    def screen_space_reflections(self) -> primitives.Bool | None:
        """When enabled, any parts of the scene currently visible to the camera will reflect off shiny surfaces in realtime."""
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
    def antialiasing(self) -> AntiAliasingMethod | None:
        """Smooths out jagged edges on objects. Some may not work or be suitable for VR."""
        member = self.get_member("Antialiasing")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AntiAliasingMethod(member.value)
        return None

    @antialiasing.setter
    def antialiasing(self, value: AntiAliasingMethod | str) -> None:
        """Set Antialiasing. Smooths out jagged edges on objects. Some may not work or be suitable for VR."""
        member = self.get_member("Antialiasing")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Antialiasing",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

