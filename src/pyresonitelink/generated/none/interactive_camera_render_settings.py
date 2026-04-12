"""Generated component: InteractiveCameraRenderSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraRenderSettings(GeneratedComponent, ICustomInspector):
    """See Camera.

    See Camera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraRenderSettings"

    def __init__(self, hide_all_badges: primitives.Bool | None = None, hide_all_lasers: primitives.Bool | None = None, force_eyes_on_camera: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
    def hide_all_badges(self) -> primitives.Bool | None:
        """This hides the user's badges (including the nameplate) from the camera preview and any pictures taken."""
        member = self.get_member("HideAllBadges")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_all_badges.setter
    def hide_all_badges(self, value: primitives.Bool) -> None:
        """Set the HideAllBadges field value."""
        member = self.get_member("HideAllBadges")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideAllBadges", fields.FieldBool(value=value)
            )

    @property
    def hide_all_lasers(self) -> primitives.Bool | None:
        """This hides the user's lasers from the camera preview and any pictures taken."""
        member = self.get_member("HideAllLasers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_all_lasers.setter
    def hide_all_lasers(self, value: primitives.Bool) -> None:
        """Set the HideAllLasers field value."""
        member = self.get_member("HideAllLasers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideAllLasers", fields.FieldBool(value=value)
            )

    @property
    def force_eyes_on_camera(self) -> primitives.Bool | None:
        """This makes the user's avatar's eyes lock on to the camera position."""
        member = self.get_member("ForceEyesOnCamera")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_eyes_on_camera.setter
    def force_eyes_on_camera(self, value: primitives.Bool) -> None:
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

