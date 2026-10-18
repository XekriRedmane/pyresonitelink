"""Generated component: DesktopViewSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.corner import Corner
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DesktopViewSettings(GeneratedComponent, ICustomInspector):
    """The DesktopViewSettings component is used to adjust how viewing the local user's computer screen is done via the Dash Menu.

    Category: Hidden

    Used in the dash desktop tab. Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopViewSettings"

    def __init__(self, follow_cursor: primitives.Bool | None = None, brightness: primitives.Float | None = None, opacity: primitives.Float | None = None, button_corner: Corner | str | None = None, hide_menu_button_in_vr: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            follow_cursor: Initial value for FollowCursor.
            brightness: Initial value for Brightness.
            opacity: Initial value for Opacity.
            button_corner: Initial value for ButtonCorner.
            hide_menu_button_in_vr: Initial value for HideMenuButtonInVR.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if follow_cursor is not None:
            self.follow_cursor = follow_cursor
        if brightness is not None:
            self.brightness = brightness
        if opacity is not None:
            self.opacity = opacity
        if button_corner is not None:
            self.button_corner = button_corner
        if hide_menu_button_in_vr is not None:
            self.hide_menu_button_in_vr = hide_menu_button_in_vr

    @property
    def follow_cursor(self) -> primitives.Bool | None:
        """Whether the Desktop cursor should follow where the user's in game cursor is on the dash in real time."""
        member = self.get_member("FollowCursor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @follow_cursor.setter
    def follow_cursor(self, value: primitives.Bool) -> None:
        """Set the FollowCursor field value."""
        member = self.get_member("FollowCursor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FollowCursor", fields.FieldBool(value=value)
            )

    @property
    def brightness(self) -> primitives.Float | None:
        """How bright the display of the desktop is on the in game dash menu."""
        member = self.get_member("Brightness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @brightness.setter
    def brightness(self, value: primitives.Float) -> None:
        """Set the Brightness field value."""
        member = self.get_member("Brightness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Brightness", fields.FieldFloat(value=value)
            )

    @property
    def opacity(self) -> primitives.Float | None:
        """How transparent the in game view of the desktop is on the dash menu."""
        member = self.get_member("Opacity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @opacity.setter
    def opacity(self, value: primitives.Float) -> None:
        """Set the Opacity field value."""
        member = self.get_member("Opacity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Opacity", fields.FieldFloat(value=value)
            )

    @property
    def button_corner(self) -> Corner | None:
        """The ButtonCorner enum value."""
        member = self.get_member("ButtonCorner")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Corner(member.value)
        return None

    @button_corner.setter
    def button_corner(self, value: Corner | str) -> None:
        """Set the ButtonCorner enum value."""
        member = self.get_member("ButtonCorner")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ButtonCorner",
                members.FieldEnum(value=str(value)),
            )

    @property
    def hide_menu_button_in_vr(self) -> primitives.Bool | None:
        """The HideMenuButtonInVR field value."""
        member = self.get_member("HideMenuButtonInVR")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_menu_button_in_vr.setter
    def hide_menu_button_in_vr(self, value: primitives.Bool) -> None:
        """Set the HideMenuButtonInVR field value."""
        member = self.get_member("HideMenuButtonInVR")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideMenuButtonInVR", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

