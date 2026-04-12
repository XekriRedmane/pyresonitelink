"""Generated component: MultiAudioClipPlayer."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiAudioClipPlayer(GeneratedComponent, IWorldAudioDataSource, IPlayable, IComponent, IWorldEventReceiver):
    """TODO: instead of being written by me with 2 brain cells of math this should be rewritten with actual math terms.

The MultiAudioClipPlayer is a component able to make a group of audios play at the exact same time with a timeline. How the math is determined is made by taking each track and checking their play length in seconds. Next a math equation is done to find how much to repeat each Audio Clip by, so they end at the same time. Then it makes this component's playback length where all the audio clips would end. This could be used as a way of doing said math equation.

    Category: Audio

    Add a group of tracks to the tracks list to make them part of the
    player. The player can be referenced by IPlayable capable nodes such as
    Media ProtoFlux Nodes and Components that take such. This component can
    also be put into an Audio Output Component to be heard by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiAudioClipPlayer"

    @property
    def playback(self) -> members.SyncPlayback | None:
        """the position of the multi audio clip player"""
        member = self.get_member("playback")
        if isinstance(member, members.SyncPlayback):
            return member
        return None

    @playback.setter
    def playback(self, value: members.SyncPlayback) -> None:
        """Set playback. the position of the multi audio clip player"""
        self.set_member("playback", value)

    @property
    def tracks(self) -> members.SyncList | None:
        """the different tracks this Multi Audio Clip is playing."""
        member = self.get_member("Tracks")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tracks.setter
    def tracks(self, value: members.SyncList) -> None:
        """Set Tracks. the different tracks this Multi Audio Clip is playing."""
        self.set_member("Tracks", value)

    async def play(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Starts playback of the audio clips

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Play", {}, debug,
        )

    async def stop(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Stops playback of the audio clips and sets playhead back to beginning.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Stop", {}, debug,
        )

    async def pause(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Pauses playback of the audio clips.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Pause", {}, debug,
        )

    async def resume(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Resumes playback of the audio clips at current position.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Resume", {}, debug,
        )

