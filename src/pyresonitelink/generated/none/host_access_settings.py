"""Generated component: HostAccessSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class HostAccessSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.HostAccessSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HostAccessSettings"

    @property
    def entries(self) -> members.SyncDictionary | None:
        """The Entries member."""
        member = self.get_member("Entries")
        if isinstance(member, members.SyncDictionary):
            return member
        return None

    @entries.setter
    def entries(self, value: members.SyncDictionary) -> None:
        """Set the Entries member."""
        self.set_member("Entries", value)

    async def get_entry(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, debug: bool = False) -> dict:
        """Call the GetEntry sync method.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GetEntry", {"key": key}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

