"""Generated component: TestSineWaveSource."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TestSineWaveSource(GeneratedComponent, IWorldAudioDataSource, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TestSineWaveSource.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TestSineWaveSource"

    def __init__(self, frequency: np.float32 | None = None, amplitude: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
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
    def frequency(self) -> np.float32 | None:
        """The Frequency field value."""
        member = self.get_member("Frequency")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frequency.setter
    def frequency(self, value: np.float32) -> None:
        """Set the Frequency field value."""
        member = self.get_member("Frequency")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Frequency", fields.FieldFloat(value=value)
            )

    @property
    def amplitude(self) -> np.float32 | None:
        """The Amplitude field value."""
        member = self.get_member("Amplitude")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @amplitude.setter
    def amplitude(self, value: np.float32) -> None:
        """Set the Amplitude field value."""
        member = self.get_member("Amplitude")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Amplitude", fields.FieldFloat(value=value)
            )

