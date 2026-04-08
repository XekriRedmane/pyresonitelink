"""Generated component: SteamIntegrationSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class SteamIntegrationSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.SteamIntegrationSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SteamIntegrationSettings"

    def __init__(self, save_screenshots: bool | None = None, force_steam_voice_on_remote_play: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            save_screenshots: Initial value for SaveScreenshots.
            force_steam_voice_on_remote_play: Initial value for ForceSteamVoiceOnRemotePlay.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if save_screenshots is not None:
            self.save_screenshots = save_screenshots
        if force_steam_voice_on_remote_play is not None:
            self.force_steam_voice_on_remote_play = force_steam_voice_on_remote_play

    @property
    def rich_presence(self) -> members.FieldEnum | None:
        """The RichPresence member."""
        member = self.get_member("RichPresence")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rich_presence.setter
    def rich_presence(self, value: members.FieldEnum) -> None:
        """Set the RichPresence member."""
        self.set_member("RichPresence", value)

    @property
    def save_screenshots(self) -> bool | None:
        """The SaveScreenshots field value."""
        member = self.get_member("SaveScreenshots")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @save_screenshots.setter
    def save_screenshots(self, value: bool) -> None:
        """Set the SaveScreenshots field value."""
        member = self.get_member("SaveScreenshots")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaveScreenshots", fields.FieldBool(value=value)
            )

    @property
    def force_steam_voice_on_remote_play(self) -> bool | None:
        """The ForceSteamVoiceOnRemotePlay field value."""
        member = self.get_member("ForceSteamVoiceOnRemotePlay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_steam_voice_on_remote_play.setter
    def force_steam_voice_on_remote_play(self, value: bool) -> None:
        """Set the ForceSteamVoiceOnRemotePlay field value."""
        member = self.get_member("ForceSteamVoiceOnRemotePlay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceSteamVoiceOnRemotePlay", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

