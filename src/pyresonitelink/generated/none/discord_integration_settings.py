"""Generated component: DiscordIntegrationSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DiscordIntegrationSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.DiscordIntegrationSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DiscordIntegrationSettings"

    @property
    def rich_presence(self) -> members.FieldEnum | None:
        """The RichPresence member."""
        member = self.get_member("RichPresence")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rich_presence.setter
    def rich_presence(self, value: members.FieldEnum) -> None:
        """Set the RichPresence member."""
        self.set_member("RichPresence", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

