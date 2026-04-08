"""Generated component: SteamLinkSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class SteamLinkSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.SteamLinkSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SteamLinkSettings"

    @property
    def osc_data_port(self) -> members.FieldEnum | None:
        """The OSC_DataPort member."""
        member = self.get_member("OSC_DataPort")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @osc_data_port.setter
    def osc_data_port(self, value: members.FieldEnum) -> None:
        """Set the OSC_DataPort member."""
        self.set_member("OSC_DataPort", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

