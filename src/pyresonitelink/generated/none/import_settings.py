"""Generated component: ImportSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class ImportSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.ImportSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ImportSettings"

    @property
    def session_urls(self) -> members.FieldEnum | None:
        """The SessionUrls member."""
        member = self.get_member("SessionUrls")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @session_urls.setter
    def session_urls(self, value: members.FieldEnum) -> None:
        """Set the SessionUrls member."""
        self.set_member("SessionUrls", value)

    @property
    def world_urls(self) -> members.FieldEnum | None:
        """The WorldUrls member."""
        member = self.get_member("WorldUrls")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @world_urls.setter
    def world_urls(self, value: members.FieldEnum) -> None:
        """Set the WorldUrls member."""
        self.set_member("WorldUrls", value)

    @property
    def network_urls(self) -> members.FieldEnum | None:
        """The NetworkUrls member."""
        member = self.get_member("NetworkUrls")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @network_urls.setter
    def network_urls(self, value: members.FieldEnum) -> None:
        """Set the NetworkUrls member."""
        self.set_member("NetworkUrls", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

