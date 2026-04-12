"""Generated component: MessagingPrivacySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class MessagingPrivacySettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MessagingPrivacySettings"

    def __init__(self, do_not_send_read_status: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            do_not_send_read_status: Initial value for DoNotSendReadStatus.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if do_not_send_read_status is not None:
            self.do_not_send_read_status = do_not_send_read_status

    @property
    def do_not_send_read_status(self) -> primitives.Bool | None:
        """Doesn't tell the cloud whether or not the user has read a message when enabled. Can prevent users from knowing you are online from the act of you reading a message even when appearing as offline."""
        member = self.get_member("DoNotSendReadStatus")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @do_not_send_read_status.setter
    def do_not_send_read_status(self, value: primitives.Bool) -> None:
        """Set the DoNotSendReadStatus field value."""
        member = self.get_member("DoNotSendReadStatus")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoNotSendReadStatus", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

