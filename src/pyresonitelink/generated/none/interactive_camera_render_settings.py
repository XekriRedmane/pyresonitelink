"""Generated component: InteractiveCameraRenderSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraRenderSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraRenderSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraRenderSettings"

    def __init__(self, hide_all_badges: bool | None = None, hide_all_lasers: bool | None = None, force_eyes_on_camera: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            hide_all_badges: Initial value for HideAllBadges.
            hide_all_lasers: Initial value for HideAllLasers.
            force_eyes_on_camera: Initial value for ForceEyesOnCamera.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if hide_all_badges is not None:
            self.hide_all_badges = hide_all_badges
        if hide_all_lasers is not None:
            self.hide_all_lasers = hide_all_lasers
        if force_eyes_on_camera is not None:
            self.force_eyes_on_camera = force_eyes_on_camera

    @property
    def hide_all_badges(self) -> bool | None:
        """The HideAllBadges field value."""
        member = self.get_member("HideAllBadges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_all_badges.setter
    def hide_all_badges(self, value: bool) -> None:
        """Set the HideAllBadges field value."""
        member = self.get_member("HideAllBadges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideAllBadges", fields.FieldBool(value=value)
            )

    @property
    def hide_all_lasers(self) -> bool | None:
        """The HideAllLasers field value."""
        member = self.get_member("HideAllLasers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_all_lasers.setter
    def hide_all_lasers(self, value: bool) -> None:
        """Set the HideAllLasers field value."""
        member = self.get_member("HideAllLasers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideAllLasers", fields.FieldBool(value=value)
            )

    @property
    def force_eyes_on_camera(self) -> bool | None:
        """The ForceEyesOnCamera field value."""
        member = self.get_member("ForceEyesOnCamera")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_eyes_on_camera.setter
    def force_eyes_on_camera(self, value: bool) -> None:
        """Set the ForceEyesOnCamera field value."""
        member = self.get_member("ForceEyesOnCamera")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceEyesOnCamera", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

