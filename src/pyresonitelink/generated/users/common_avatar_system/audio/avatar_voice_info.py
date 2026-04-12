"""Generated component: AvatarVoiceInfo."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarVoiceInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AvatarVoiceInfo is used to override the assigning behavior from a AvatarVoiceSourceAssigner component on the avatar when it assigns a target.

    Category: Users/Common Avatar System/Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarVoiceInfo"

    def __init__(self, audio_source: str | IWorldAudioDataSource | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_source: Initial value for AudioSource.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_source is not None:
            self.audio_source = audio_source

    @property
    def audio_source(self) -> str | None:
        """The audio source to override the assigning behavior of a Component:AvatarVoiceSourceAssigner on the avatar with."""
        member = self.get_member("AudioSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_source.setter
    def audio_source(self, target: str | IWorldAudioDataSource | None) -> None:
        """Set the AudioSource reference by target ID or IWorldAudioDataSource instance."""
        target_id: str | None = target.id if isinstance(target, IWorldAudioDataSource) else target  # type: ignore[assignment]
        member = self.get_member("AudioSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AudioSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldAudioDataSource'),
            )

