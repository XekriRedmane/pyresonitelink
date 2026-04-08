"""Generated component: ResolutionSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class ResolutionSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.ResolutionSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ResolutionSettings"

    def __init__(self, fullscreen: bool | None = None, window_resolution: primitives.Int2 | None = None, fullscreen_resolution: primitives.Int2 | None = None, commited_window_resolution: primitives.Int2 | None = None, commited_fullscreen_resolution: primitives.Int2 | None = None, needs_to_apply_resolution: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            fullscreen: Initial value for Fullscreen.
            window_resolution: Initial value for WindowResolution.
            fullscreen_resolution: Initial value for FullscreenResolution.
            commited_window_resolution: Initial value for CommitedWindowResolution.
            commited_fullscreen_resolution: Initial value for CommitedFullscreenResolution.
            needs_to_apply_resolution: Initial value for NeedsToApplyResolution.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if fullscreen is not None:
            self.fullscreen = fullscreen
        if window_resolution is not None:
            self.window_resolution = window_resolution
        if fullscreen_resolution is not None:
            self.fullscreen_resolution = fullscreen_resolution
        if commited_window_resolution is not None:
            self.commited_window_resolution = commited_window_resolution
        if commited_fullscreen_resolution is not None:
            self.commited_fullscreen_resolution = commited_fullscreen_resolution
        if needs_to_apply_resolution is not None:
            self.needs_to_apply_resolution = needs_to_apply_resolution

    @property
    def fullscreen(self) -> bool | None:
        """The Fullscreen field value."""
        member = self.get_member("Fullscreen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fullscreen.setter
    def fullscreen(self, value: bool) -> None:
        """Set the Fullscreen field value."""
        member = self.get_member("Fullscreen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Fullscreen", fields.FieldBool(value=value)
            )

    @property
    def window_resolution(self) -> primitives.Int2 | None:
        """The WindowResolution field value."""
        member = self.get_member("WindowResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @window_resolution.setter
    def window_resolution(self, value: primitives.Int2) -> None:
        """Set the WindowResolution field value."""
        member = self.get_member("WindowResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WindowResolution", fields.FieldInt2(value=value)
            )

    @property
    def fullscreen_resolution(self) -> primitives.Int2 | None:
        """The FullscreenResolution field value."""
        member = self.get_member("FullscreenResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fullscreen_resolution.setter
    def fullscreen_resolution(self, value: primitives.Int2) -> None:
        """Set the FullscreenResolution field value."""
        member = self.get_member("FullscreenResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullscreenResolution", fields.FieldInt2(value=value)
            )

    @property
    def commited_window_resolution(self) -> primitives.Int2 | None:
        """The CommitedWindowResolution field value."""
        member = self.get_member("CommitedWindowResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @commited_window_resolution.setter
    def commited_window_resolution(self, value: primitives.Int2) -> None:
        """Set the CommitedWindowResolution field value."""
        member = self.get_member("CommitedWindowResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CommitedWindowResolution", fields.FieldInt2(value=value)
            )

    @property
    def commited_fullscreen_resolution(self) -> primitives.Int2 | None:
        """The CommitedFullscreenResolution field value."""
        member = self.get_member("CommitedFullscreenResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @commited_fullscreen_resolution.setter
    def commited_fullscreen_resolution(self, value: primitives.Int2) -> None:
        """Set the CommitedFullscreenResolution field value."""
        member = self.get_member("CommitedFullscreenResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CommitedFullscreenResolution", fields.FieldInt2(value=value)
            )

    @property
    def needs_to_apply_resolution(self) -> bool | None:
        """The NeedsToApplyResolution field value."""
        member = self.get_member("NeedsToApplyResolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @needs_to_apply_resolution.setter
    def needs_to_apply_resolution(self, value: bool) -> None:
        """Set the NeedsToApplyResolution field value."""
        member = self.get_member("NeedsToApplyResolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NeedsToApplyResolution", fields.FieldBool(value=value)
            )

    async def apply_resolution(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ApplyResolution sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ApplyResolution", {}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

