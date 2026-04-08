"""Generated component: VoiceSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class VoiceSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.VoiceSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VoiceSettings"

    @property
    def mute_persistence(self) -> members.FieldEnum | None:
        """The MutePersistence member."""
        member = self.get_member("MutePersistence")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @mute_persistence.setter
    def mute_persistence(self, value: members.FieldEnum) -> None:
        """Set the MutePersistence member."""
        self.set_member("MutePersistence", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

