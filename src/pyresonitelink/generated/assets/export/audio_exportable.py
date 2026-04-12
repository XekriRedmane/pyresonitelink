"""Generated component: AudioExportable."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.audio_clip import AudioClip
from pyresonitelink.generated._types.iexportable import IExportable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioExportable(GeneratedComponent, IExportable, IWorldEventReceiver):
    """The AudioExportable component is used to export an AudioClip as a file for your device.

To export using this component, look at the file browser export section.

    Category: Assets/Export

    Is used to make an item export an audio clip when a user tries to export
    the root object.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioExportable"

    def __init__(self, audio: str | IAssetProvider[AudioClip] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio: Initial value for Audio.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio is not None:
            self.audio = audio

    @property
    def audio(self) -> str | None:
        """The audio clip to be exported."""
        member = self.get_member("Audio")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio.setter
    def audio(self, target: str | IAssetProvider[AudioClip] | None) -> None:
        """Set the Audio reference by target ID or IAssetProvider[AudioClip] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Audio")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Audio",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.AudioClip>'),
            )

