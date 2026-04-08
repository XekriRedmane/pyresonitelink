"""Generated component: LocomotionSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class LocomotionSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionSettings"

    @property
    def locomotion_preferences(self) -> members.SyncList | None:
        """The LocomotionPreferences member."""
        member = self.get_member("LocomotionPreferences")
        if isinstance(member, members.SyncList):
            return member
        return None

    @locomotion_preferences.setter
    def locomotion_preferences(self, value: members.SyncList) -> None:
        """Set the LocomotionPreferences member."""
        self.set_member("LocomotionPreferences", value)

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

