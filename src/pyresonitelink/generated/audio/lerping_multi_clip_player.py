"""Generated component: LerpingMultiClipPlayer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LerpingMultiClipPlayer(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """The LerpingMultiClipPlayer component is an IAudioSource type that transitions between different audio clips (tracks) by lerping the volume and speed from one audio to the other using ``Lerp``.

When an audio is lerped to, the audio will continue to loop till ``Lerp`` is moved to another clips range.

If ``Lerp`` is not within a clip range, this component will provide silent audio.

    Category: Audio

    Can be used to make looping noises that play over a video at different
    positions in the playtime.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LerpingMultiClipPlayer"

    def __init__(self, lerp: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            lerp: Initial value for Lerp.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if lerp is not None:
            self.lerp = lerp

    @property
    def lerp(self) -> primitives.Float | None:
        """The reference value to use to lerp between different tracks with different values. This does not have to be 0-1, and can be any value."""
        member = self.get_member("Lerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lerp.setter
    def lerp(self, value: primitives.Float) -> None:
        """Set the Lerp field value."""
        member = self.get_member("Lerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Lerp", fields.FieldFloat(value=value)
            )

    @property
    def tracks(self) -> members.SyncList | None:
        """A list of track's to lerp between using ``Lerp``."""
        member = self.get_member("Tracks")
        if isinstance(member, members.SyncList):
            return member
        return None

    @tracks.setter
    def tracks(self, value: members.SyncList) -> None:
        """Set Tracks. A list of track's to lerp between using ``Lerp``."""
        self.set_member("Tracks", value)

