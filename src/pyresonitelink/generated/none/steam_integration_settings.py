"""Generated component: SteamIntegrationSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.rich_presence_level import RichPresenceLevel
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class SteamIntegrationSettings(GeneratedComponent, ICustomInspector):
    """See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SteamIntegrationSettings"

    def __init__(self, rich_presence: RichPresenceLevel | str | None = None, save_screenshots: primitives.Bool | None = None, force_steam_voice_on_remote_play: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            rich_presence: Initial value for RichPresence.
            save_screenshots: Initial value for SaveScreenshots.
            force_steam_voice_on_remote_play: Initial value for ForceSteamVoiceOnRemotePlay.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if rich_presence is not None:
            self.rich_presence = rich_presence
        if save_screenshots is not None:
            self.save_screenshots = save_screenshots
        if force_steam_voice_on_remote_play is not None:
            self.force_steam_voice_on_remote_play = force_steam_voice_on_remote_play

    @property
    def rich_presence(self) -> RichPresenceLevel | None:
        """The setting to use when doing steam presence."""
        member = self.get_member("RichPresence")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RichPresenceLevel(member.value)
        return None

    @rich_presence.setter
    def rich_presence(self, value: RichPresenceLevel | str) -> None:
        """Set RichPresence. The setting to use when doing steam presence."""
        member = self.get_member("RichPresence")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RichPresence",
                members.FieldEnum(value=str(value)),
            )

    @property
    def save_screenshots(self) -> primitives.Bool | None:
        """Whether to save screenshots to steam."""
        member = self.get_member("SaveScreenshots")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @save_screenshots.setter
    def save_screenshots(self, value: primitives.Bool) -> None:
        """Set the SaveScreenshots field value."""
        member = self.get_member("SaveScreenshots")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SaveScreenshots", fields.FieldBool(value=value)
            )

    @property
    def force_steam_voice_on_remote_play(self) -> primitives.Bool | None:
        """Whether steam should force voice on remote playing via internet over connection to a pc remotely."""
        member = self.get_member("ForceSteamVoiceOnRemotePlay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_steam_voice_on_remote_play.setter
    def force_steam_voice_on_remote_play(self, value: primitives.Bool) -> None:
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

