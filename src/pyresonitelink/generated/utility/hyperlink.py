"""Generated component: Hyperlink."""

from pyresonitelink.data import fields
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Hyperlink(GeneratedComponent, ITouchable, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Hyperlink.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Hyperlink"

    def __init__(self, url: str | None = None, open_once: bool | None = None, reason: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            open_once: Initial value for OpenOnce.
            reason: Initial value for Reason.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if open_once is not None:
            self.open_once = open_once
        if reason is not None:
            self.reason = reason

    @property
    def url(self) -> str | None:
        """The URL field value."""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def open_once(self) -> bool | None:
        """The OpenOnce field value."""
        member = self.get_member("OpenOnce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open_once.setter
    def open_once(self, value: bool) -> None:
        """Set the OpenOnce field value."""
        member = self.get_member("OpenOnce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpenOnce", fields.FieldBool(value=value)
            )

    @property
    def reason(self) -> str | None:
        """The Reason field value."""
        member = self.get_member("Reason")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reason.setter
    def reason(self, value: str) -> None:
        """Set the Reason field value."""
        member = self.get_member("Reason")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Reason", fields.FieldString(value=value)
            )

    async def open(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Open sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Open", {}, debug,
        )

