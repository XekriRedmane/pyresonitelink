"""Generated component: InteractiveCameraAudioSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraAudioSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraAudioSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraAudioSettings"

    def __init__(self, render_own_voice_on_camera: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            render_own_voice_on_camera: Initial value for RenderOwnVoiceOnCamera.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if render_own_voice_on_camera is not None:
            self.render_own_voice_on_camera = render_own_voice_on_camera

    @property
    def render_own_voice_on_camera(self) -> bool | None:
        """The RenderOwnVoiceOnCamera field value."""
        member = self.get_member("RenderOwnVoiceOnCamera")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_own_voice_on_camera.setter
    def render_own_voice_on_camera(self, value: bool) -> None:
        """Set the RenderOwnVoiceOnCamera field value."""
        member = self.get_member("RenderOwnVoiceOnCamera")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderOwnVoiceOnCamera", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

