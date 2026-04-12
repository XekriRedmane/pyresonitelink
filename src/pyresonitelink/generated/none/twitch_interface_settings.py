"""Generated component: TwitchInterfaceSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class TwitchInterfaceSettings(GeneratedComponent, ICustomInspector):
    """This component is used with the settings for the InteractiveCamera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TwitchInterfaceSettings"

    def __init__(self, channel_name: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            channel_name: Initial value for ChannelName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if channel_name is not None:
            self.channel_name = channel_name

    @property
    def channel_name(self) -> primitives.String | None:
        """The twitch channel name to use."""
        member = self.get_member("ChannelName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @channel_name.setter
    def channel_name(self, value: primitives.String) -> None:
        """Set the ChannelName field value."""
        member = self.get_member("ChannelName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChannelName", fields.FieldString(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

