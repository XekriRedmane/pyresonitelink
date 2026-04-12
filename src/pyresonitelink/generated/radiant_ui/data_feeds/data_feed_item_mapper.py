"""Generated component: DataFeedItemMapper."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataFeedItemMapper(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The DataFeedItemMapper allows you to define which data feed items map to which UI templates. It does this via the list ``Mappings``, which take classes that extend DataFeedItem and If they match a mapping in the list it Duplicates that item's template and adds it into the list.

For more info on data feeds, see Data Feeds

    Category: Radiant UI/Data Feeds

    This component is to be put into a SingleFeedView or similar so that the
    component it is specified inside of can use this component to map
    incoming feed items from the data feed to UI or object templates.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataFeedItemMapper"

    @property
    def mappings(self) -> members.SyncList | None:
        """A list of item Mappings to map data feed item types to Feed Templates."""
        member = self.get_member("Mappings")
        if isinstance(member, members.SyncList):
            return member
        return None

    @mappings.setter
    def mappings(self, value: members.SyncList) -> None:
        """Set Mappings. A list of item Mappings to map data feed item types to Feed Templates."""
        self.set_member("Mappings", value)

    async def on_setup_template(self, resolink: protocols.ResoniteLinkClient, button: str, data: str, debug: bool = False) -> dict:
        """Set up a basic settup with this component with a bunch of example UIs.

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

