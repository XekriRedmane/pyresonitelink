"""Generated component: DesktopRenderSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DesktopRenderSettings(GeneratedComponent, ICustomInspector):
    """The DesktopRenderSettings component is used to set Settings used in Desktop mode.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopRenderSettings"

    def __init__(self, field_of_view: primitives.Float | None = None, sprint_field_of_view_zoom: primitives.Bool | None = None, vsync: primitives.Bool | None = None, limit_framerate_when_unfocused: primitives.Bool | None = None, maximum_background_framerate: primitives.Int | None = None, frame_pacing_options_enabled: primitives.Bool | None = None, background_framerate_enabled: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            field_of_view: Initial value for FieldOfView.
            sprint_field_of_view_zoom: Initial value for SprintFieldOfViewZoom.
            vsync: Initial value for VSync.
            limit_framerate_when_unfocused: Initial value for LimitFramerateWhenUnfocused.
            maximum_background_framerate: Initial value for MaximumBackgroundFramerate.
            frame_pacing_options_enabled: Initial value for FramePacingOptionsEnabled.
            background_framerate_enabled: Initial value for BackgroundFramerateEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if sprint_field_of_view_zoom is not None:
            self.sprint_field_of_view_zoom = sprint_field_of_view_zoom
        if vsync is not None:
            self.vsync = vsync
        if limit_framerate_when_unfocused is not None:
            self.limit_framerate_when_unfocused = limit_framerate_when_unfocused
        if maximum_background_framerate is not None:
            self.maximum_background_framerate = maximum_background_framerate
        if frame_pacing_options_enabled is not None:
            self.frame_pacing_options_enabled = frame_pacing_options_enabled
        if background_framerate_enabled is not None:
            self.background_framerate_enabled = background_framerate_enabled

    @property
    def field_of_view(self) -> primitives.Float | None:
        """The fov of the desktop client."""
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
    def sprint_field_of_view_zoom(self) -> primitives.Bool | None:
        """Whether to multiply the FOV when sprinting"""
        member = self.get_member("SprintFieldOfViewZoom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @sprint_field_of_view_zoom.setter
    def sprint_field_of_view_zoom(self, value: primitives.Bool) -> None:
        """Set the SprintFieldOfViewZoom field value."""
        member = self.get_member("SprintFieldOfViewZoom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SprintFieldOfViewZoom", fields.FieldBool(value=value)
            )

    @property
    def vsync(self) -> primitives.Bool | None:
        """Whether to use VSync"""
        member = self.get_member("VSync")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vsync.setter
    def vsync(self, value: primitives.Bool) -> None:
        """Set the VSync field value."""
        member = self.get_member("VSync")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VSync", fields.FieldBool(value=value)
            )

    @property
    def limit_framerate_when_unfocused(self) -> primitives.Bool | None:
        """Whether to limit framerate when the game is unfocused."""
        member = self.get_member("LimitFramerateWhenUnfocused")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @limit_framerate_when_unfocused.setter
    def limit_framerate_when_unfocused(self, value: primitives.Bool) -> None:
        """Set the LimitFramerateWhenUnfocused field value."""
        member = self.get_member("LimitFramerateWhenUnfocused")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LimitFramerateWhenUnfocused", fields.FieldBool(value=value)
            )

    @property
    def maximum_background_framerate(self) -> primitives.Int | None:
        """How much to limit the framerate when unfocused and ``LimitFramerateWhenUnfocused`` is true."""
        member = self.get_member("MaximumBackgroundFramerate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @maximum_background_framerate.setter
    def maximum_background_framerate(self, value: primitives.Int) -> None:
        """Set the MaximumBackgroundFramerate field value."""
        member = self.get_member("MaximumBackgroundFramerate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaximumBackgroundFramerate", fields.FieldInt(value=value)
            )

    @property
    def frame_pacing_options_enabled(self) -> primitives.Bool | None:
        """Whether to pace frames due to options like ``MaximumBackgroundFramerate`` is being used."""
        member = self.get_member("FramePacingOptionsEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frame_pacing_options_enabled.setter
    def frame_pacing_options_enabled(self, value: primitives.Bool) -> None:
        """Set the FramePacingOptionsEnabled field value."""
        member = self.get_member("FramePacingOptionsEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FramePacingOptionsEnabled", fields.FieldBool(value=value)
            )

    @property
    def background_framerate_enabled(self) -> primitives.Bool | None:
        """Whether to render new frames when in the background."""
        member = self.get_member("BackgroundFramerateEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @background_framerate_enabled.setter
    def background_framerate_enabled(self, value: primitives.Bool) -> None:
        """Set the BackgroundFramerateEnabled field value."""
        member = self.get_member("BackgroundFramerateEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackgroundFramerateEnabled", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

