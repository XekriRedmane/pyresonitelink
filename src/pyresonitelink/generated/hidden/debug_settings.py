"""Generated component: DebugSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DebugSettings(GeneratedComponent, ICustomInspector):
    """The DebugSettings component is a component updated during Resonite updates to contain bleeding edge settings for the game.

    Category: Hidden
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugSettings"

    def __init__(self, debug_input_bindings: primitives.Bool | None = None, show_media_mtx_window: primitives.Bool | None = None, use_proton_for_media_mtx: primitives.Bool | None = None, force_software_video_encoder: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            debug_input_bindings: Initial value for DebugInputBindings.
            show_media_mtx_window: Initial value for ShowMediaMTXWindow.
            use_proton_for_media_mtx: Initial value for UseProtonForMediaMTX.
            force_software_video_encoder: Initial value for ForceSoftwareVideoEncoder.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if debug_input_bindings is not None:
            self.debug_input_bindings = debug_input_bindings
        if show_media_mtx_window is not None:
            self.show_media_mtx_window = show_media_mtx_window
        if use_proton_for_media_mtx is not None:
            self.use_proton_for_media_mtx = use_proton_for_media_mtx
        if force_software_video_encoder is not None:
            self.force_software_video_encoder = force_software_video_encoder

    @property
    def debug_input_bindings(self) -> primitives.Bool | None:
        """Whether to display the user's controller inputs on their hands in userspace."""
        member = self.get_member("DebugInputBindings")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_input_bindings.setter
    def debug_input_bindings(self, value: primitives.Bool) -> None:
        """Set the DebugInputBindings field value."""
        member = self.get_member("DebugInputBindings")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DebugInputBindings", fields.FieldBool(value=value)
            )

    @property
    def show_media_mtx_window(self) -> primitives.Bool | None:
        """The ShowMediaMTXWindow field value."""
        member = self.get_member("ShowMediaMTXWindow")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_media_mtx_window.setter
    def show_media_mtx_window(self, value: primitives.Bool) -> None:
        """Set the ShowMediaMTXWindow field value."""
        member = self.get_member("ShowMediaMTXWindow")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowMediaMTXWindow", fields.FieldBool(value=value)
            )

    @property
    def use_proton_for_media_mtx(self) -> primitives.Bool | None:
        """The UseProtonForMediaMTX field value."""
        member = self.get_member("UseProtonForMediaMTX")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_proton_for_media_mtx.setter
    def use_proton_for_media_mtx(self, value: primitives.Bool) -> None:
        """Set the UseProtonForMediaMTX field value."""
        member = self.get_member("UseProtonForMediaMTX")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseProtonForMediaMTX", fields.FieldBool(value=value)
            )

    @property
    def force_software_video_encoder(self) -> primitives.Bool | None:
        """The ForceSoftwareVideoEncoder field value."""
        member = self.get_member("ForceSoftwareVideoEncoder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_software_video_encoder.setter
    def force_software_video_encoder(self, value: primitives.Bool) -> None:
        """Set the ForceSoftwareVideoEncoder field value."""
        member = self.get_member("ForceSoftwareVideoEncoder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceSoftwareVideoEncoder", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

