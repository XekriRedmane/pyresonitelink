"""Generated component: DesktopViewSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DesktopViewSettings(GeneratedComponent, ICustomInspector):
    """The DesktopViewSettings component is used to adjust how viewing the local user's computer screen is done via the Dash Menu.

    Used in the dash desktop tab. Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopViewSettings"

    def __init__(self, follow_cursor: primitives.Bool | None = None, brightness: primitives.Float | None = None, opacity: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            follow_cursor: Initial value for FollowCursor.
            brightness: Initial value for Brightness.
            opacity: Initial value for Opacity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if follow_cursor is not None:
            self.follow_cursor = follow_cursor
        if brightness is not None:
            self.brightness = brightness
        if opacity is not None:
            self.opacity = opacity

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

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

