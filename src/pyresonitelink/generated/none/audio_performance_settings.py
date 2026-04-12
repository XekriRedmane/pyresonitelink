"""Generated component: AudioPerformanceSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.audio_frame_size import AudioFrameSize
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioPerformanceSettings(GeneratedComponent, ICustomInspector):
    """The Audio Performance Settings component is part of the Settings that control audio buffers.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioPerformanceSettings"

    def __init__(self, max_voices: primitives.Int | None = None, output_buffer_size: AudioFrameSize | str | None = None, simulation_frame_size: AudioFrameSize | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_voices: Initial value for MaxVoices.
            output_buffer_size: Initial value for OutputBufferSize.
            simulation_frame_size: Initial value for SimulationFrameSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_voices is not None:
            self.max_voices = max_voices
        if output_buffer_size is not None:
            self.output_buffer_size = output_buffer_size
        if simulation_frame_size is not None:
            self.simulation_frame_size = simulation_frame_size

    @property
    def max_voices(self) -> primitives.Int | None:
        """The maximum voices the user is allowed to hear."""
        member = self.get_member("MaxVoices")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_voices.setter
    def max_voices(self, value: primitives.Int) -> None:
        """Set the MaxVoices field value."""
        member = self.get_member("MaxVoices")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxVoices", fields.FieldInt(value=value)
            )

    @property
    def output_buffer_size(self) -> AudioFrameSize | None:
        """The output buffer size in samples."""
        member = self.get_member("OutputBufferSize")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioFrameSize(member.value)
        return None

    @output_buffer_size.setter
    def output_buffer_size(self, value: AudioFrameSize | str) -> None:
        """Set OutputBufferSize. The output buffer size in samples."""
        member = self.get_member("OutputBufferSize")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OutputBufferSize",
                members.FieldEnum(value=str(value)),
            )

    @property
    def simulation_frame_size(self) -> AudioFrameSize | None:
        """The simulation buffer size in samples."""
        member = self.get_member("SimulationFrameSize")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioFrameSize(member.value)
        return None

    @simulation_frame_size.setter
    def simulation_frame_size(self, value: AudioFrameSize | str) -> None:
        """Set SimulationFrameSize. The simulation buffer size in samples."""
        member = self.get_member("SimulationFrameSize")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SimulationFrameSize",
                members.FieldEnum(value=str(value)),
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

