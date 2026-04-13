"""Generated component: SteamLinkSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.osc_port import OSC_Port
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class SteamLinkSettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SteamLinkSettings"

    def __init__(self, osc_data_port: OSC_Port | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            osc_data_port: Initial value for OSC_DataPort.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if osc_data_port is not None:
            self.osc_data_port = osc_data_port

    @property
    def osc_data_port(self) -> OSC_Port | None:
        """the port to use to communicate steam link info via OSC."""
        member = self.get_member("OSC_DataPort")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OSC_Port(member.value)
        return None

    @osc_data_port.setter
    def osc_data_port(self, value: OSC_Port | str) -> None:
        """Set OSC_DataPort. the port to use to communicate steam link info via OSC."""
        member = self.get_member("OSC_DataPort")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OSC_DataPort",
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

