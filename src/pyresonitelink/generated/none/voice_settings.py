"""Generated component: VoiceSettings."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.mute_persistence import MutePersistence
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class VoiceSettings(GeneratedComponent, ICustomInspector):
    """See Voice Settings
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VoiceSettings"

    def __init__(self, mute_persistence: MutePersistence | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            mute_persistence: Initial value for MutePersistence.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if mute_persistence is not None:
            self.mute_persistence = mute_persistence

    @property
    def mute_persistence(self) -> MutePersistence | None:
        """this component's setting"""
        member = self.get_member("MutePersistence")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return MutePersistence(member.value)
        return None

    @mute_persistence.setter
    def mute_persistence(self, value: MutePersistence | str) -> None:
        """Set MutePersistence. this component's setting"""
        member = self.get_member("MutePersistence")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "MutePersistence",
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

