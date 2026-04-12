"""Generated component: TestSineWaveSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TestSineWaveSource(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """The TestSineWaveSource component acts the same as a SineWaveClip if it were continuously playing as an AudioClipPlayer. The main difference though is it allows constant and quick changes in ``Frequency`` and ``Amplitude`` without needing time to recalculate.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TestSineWaveSource"

    def __init__(self, frequency: primitives.Float | None = None, amplitude: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            frequency: Initial value for Frequency.
            amplitude: Initial value for Amplitude.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if frequency is not None:
            self.frequency = frequency
        if amplitude is not None:
            self.amplitude = amplitude

    @property
    def frequency(self) -> primitives.Float | None:
        """The pitch of the audio streamed whistle tone."""
        member = self.get_member("Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frequency.setter
    def frequency(self, value: primitives.Float) -> None:
        """Set the Frequency field value."""
        member = self.get_member("Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Frequency", fields.FieldFloat(value=value)
            )

    @property
    def amplitude(self) -> primitives.Float | None:
        """The loudness of the streamed whistle tone."""
        member = self.get_member("Amplitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @amplitude.setter
    def amplitude(self, value: primitives.Float) -> None:
        """Set the Amplitude field value."""
        member = self.get_member("Amplitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Amplitude", fields.FieldFloat(value=value)
            )

