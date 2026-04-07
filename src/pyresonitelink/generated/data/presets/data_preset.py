"""Generated component: DataPreset."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DataPreset(GeneratedComponent, ICustomInspector, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DataPreset.

    Category: Data/Presets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DataPreset"

    @property
    def is_active(self) -> members.EmptyElement | None:
        """The IsActive member."""
        member = self.get_member("IsActive")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @is_active.setter
    def is_active(self, value: members.EmptyElement) -> None:
        """Set the IsActive member."""
        self.set_member("IsActive", value)

    @property
    def entries(self) -> members.SyncList | None:
        """The Entries member."""
        member = self.get_member("Entries")
        if isinstance(member, members.SyncList):
            return member
        return None

    @entries.setter
    def entries(self, value: members.SyncList) -> None:
        """Set the Entries member."""
        self.set_member("Entries", value)

    async def set_active(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetActive sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetActive", {}, debug,
        )

    async def set_values(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetValues sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetValues", {}, debug,
        )

