"""Generated component: Hyperlink."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Hyperlink(GeneratedComponent, ITouchable, IButtonPressReceiver, IWorldEventReceiver):
    """The Hyperlink component allows you to turn an object with a collider into a clickable link that will prompt the user in Userspace to open the provided link in their default web browser.

Example for connecting to the local host of the device: ``http://localhost:5000``|warning}}

    Category: Utility

    It can be triggered or activated in the following ways: * Using a
    collider and physically touching the object to prompt for a connection.
    * Attaching a UIX button component along with this component on the same
    slot, then clicking on the UIX button will prompt for a connection.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Hyperlink"

    def __init__(self, url: str | None = None, open_once: primitives.Bool | None = None, reason: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
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
        """The hyperlink to open."""
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
    def open_once(self) -> primitives.Bool | None:
        """Prevents the user from clicking on the URL more than once and bringing up multiple confirmation dialouges"""
        member = self.get_member("OpenOnce")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open_once.setter
    def open_once(self, value: primitives.Bool) -> None:
        """Set the OpenOnce field value."""
        member = self.get_member("OpenOnce")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpenOnce", fields.FieldBool(value=value)
            )

    @property
    def reason(self) -> primitives.String | None:
        """The reason that the hyperlink is being opened. Displayed to the user when they click it in the security dialog."""
        member = self.get_member("Reason")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reason.setter
    def reason(self, value: primitives.String) -> None:
        """Set the Reason field value."""
        member = self.get_member("Reason")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Reason", fields.FieldString(value=value)
            )

    async def open(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """When called, this function will bring up the confirmation dialogue for the user that is executing the function (local user).

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Open", {}, debug,
        )

