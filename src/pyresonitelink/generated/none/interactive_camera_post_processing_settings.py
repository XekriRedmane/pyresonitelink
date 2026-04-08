"""Generated component: InteractiveCameraPostProcessingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraPostProcessingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraPostProcessingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraPostProcessingSettings"

    def __init__(self, motion_blur: bool | None = None, screen_space_reflections: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            motion_blur: Initial value for MotionBlur.
            screen_space_reflections: Initial value for ScreenSpaceReflections.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if motion_blur is not None:
            self.motion_blur = motion_blur
        if screen_space_reflections is not None:
            self.screen_space_reflections = screen_space_reflections

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

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

