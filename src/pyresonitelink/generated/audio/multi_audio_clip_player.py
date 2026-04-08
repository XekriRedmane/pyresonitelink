"""Generated component: MultiAudioClipPlayer."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiAudioClipPlayer(GeneratedComponent, IWorldAudioDataSource, IPlayable, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MultiAudioClipPlayer.

    Category: Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiAudioClipPlayer"

    @property
    def playback(self) -> members.SyncPlayback | None:
        """The playback member."""
        member = self.get_member("playback")
        if isinstance(member, members.SyncPlayback):
            return member
        return None

    @playback.setter
    def playback(self, value: members.SyncPlayback) -> None:
        """Set the playback member."""
        self.set_member("playback", value)

    @property
    def tracks(self) -> members.SyncList | None:
        """The Tracks member."""
        member = self.get_member("Tracks")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tracks.setter
    def tracks(self, value: members.SyncList) -> None:
        """Set the Tracks member."""
        self.set_member("Tracks", value)

    async def play(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Play sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Play", {}, debug,
        )

    async def stop(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Stop sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Stop", {}, debug,
        )

    async def pause(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Pause sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Pause", {}, debug,
        )

    async def resume(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Resume sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Resume", {}, debug,
        )

