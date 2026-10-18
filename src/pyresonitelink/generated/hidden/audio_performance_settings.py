"""Generated component: AudioPerformanceSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.audio_frame_size import AudioFrameSize
from pyresonitelink.generated._enums.audio_frame_count import AudioFrameCount
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioPerformanceSettings(GeneratedComponent, ICustomInspector):
    """The Audio Performance Settings component is part of the Settings that control audio buffers.

    Category: Hidden

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioPerformanceSettings"

    def __init__(self, max_voices: primitives.Int | None = None, output_buffer_size: AudioFrameSize | str | None = None, simulation_frames_per_buffer: AudioFrameCount | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_voices: Initial value for MaxVoices.
            output_buffer_size: Initial value for OutputBufferSize.
            simulation_frames_per_buffer: Initial value for SimulationFramesPerBuffer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_voices is not None:
            self.max_voices = max_voices
        if output_buffer_size is not None:
            self.output_buffer_size = output_buffer_size
        if simulation_frames_per_buffer is not None:
            self.simulation_frames_per_buffer = simulation_frames_per_buffer

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
    def simulation_frames_per_buffer(self) -> AudioFrameCount | None:
        """The SimulationFramesPerBuffer enum value."""
        member = self.get_member("SimulationFramesPerBuffer")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioFrameCount(member.value)
        return None

    @simulation_frames_per_buffer.setter
    def simulation_frames_per_buffer(self, value: AudioFrameCount | str) -> None:
        """Set the SimulationFramesPerBuffer enum value."""
        member = self.get_member("SimulationFramesPerBuffer")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SimulationFramesPerBuffer",
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

