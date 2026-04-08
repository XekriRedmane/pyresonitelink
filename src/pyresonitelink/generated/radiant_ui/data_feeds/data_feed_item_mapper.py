"""Generated component: DataFeedItemMapper."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataFeedItemMapper(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DataFeedItemMapper.

    Category: Radiant UI/Data Feeds
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataFeedItemMapper"

    @property
    def mappings(self) -> members.SyncList | None:
        """The Mappings member."""
        member = self.get_member("Mappings")
        if isinstance(member, members.SyncList):
            return member
        return None

    @mappings.setter
    def mappings(self, value: members.SyncList) -> None:
        """Set the Mappings member."""
        self.set_member("Mappings", value)

    async def on_setup_template(self, resolink: protocols.ResoniteLinkClient, button: str, data: str, debug: bool = False) -> dict:
        """Call the OnSetupTemplate sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            data: The data parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OnSetupTemplate", {"button": button, "data": data}, debug,
        )

