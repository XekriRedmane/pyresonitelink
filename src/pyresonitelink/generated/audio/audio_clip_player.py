"""Generated component: AudioClipPlayer."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioClipPlayer(GeneratedComponent, IItemMetadataSource, IWorldAudioDataSource, IPlayable, IWorldEventReceiver):
    """Add an audio clip to the Clip field by holding a default audio clip player and clicking.

    Category: Audio

    Add an audio clip to the Clip field by holding a default audio clip
    player and clicking. then put the Audio Clip Player into an Audio Output
    and hit play to hear the audio.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioClipPlayer"

    def __init__(self, clip: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            clip: Initial value for Clip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if clip is not None:
            self.clip = clip

    @property
    def playback(self) -> members.SyncPlayback | None:
        """The playback object that includes data about playtime, duration, position, and playspeed of the audio."""
        member = self.get_member("playback")
        if isinstance(member, members.SyncPlayback):
            return member
        return None

    @playback.setter
    def playback(self, value: members.SyncPlayback) -> None:
        """Set playback. The playback object that includes data about playtime, duration, position, and playspeed of the audio."""
        self.set_member("playback", value)

    @property
    def clip(self) -> str | None:
        """The AudioClip to play. This can be a StaticAudioClip."""
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @clip.setter
    def clip(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the Clip reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Clip")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Clip",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

    async def play(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """When called, starts playback for this component.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Play", {}, debug,
        )

    async def stop(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """When called, stops playback for this component.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Stop", {}, debug,
        )

    async def pause(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """When called, pauses playback for this component.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Pause", {}, debug,
        )

    async def resume(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """When called, resumes playback for this component.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Resume", {}, debug,
        )

