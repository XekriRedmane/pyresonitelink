"""Generated component: DiscordIntegrationSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.rich_presence_level import RichPresenceLevel
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class DiscordIntegrationSettings(GeneratedComponent, ICustomInspector):
    """The DiscordIntegrationSettings component handles discord rich presence info communicated from Resonite. This is interacted with via the Settings system.

    Interacted with via the settings system. Isn't directly interacted with
    by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DiscordIntegrationSettings"

    def __init__(self, rich_presence: RichPresenceLevel | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rich_presence: Initial value for RichPresence.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rich_presence is not None:
            self.rich_presence = rich_presence

    @property
    def rich_presence(self) -> RichPresenceLevel | None:
        """The level of information to communicate via discord rich presence."""
        member = self.get_member("RichPresence")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RichPresenceLevel(member.value)
        return None

    @rich_presence.setter
    def rich_presence(self, value: RichPresenceLevel | str) -> None:
        """Set RichPresence. The level of information to communicate via discord rich presence."""
        member = self.get_member("RichPresence")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RichPresence",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

