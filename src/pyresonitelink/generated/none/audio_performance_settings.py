"""Generated component: AudioPerformanceSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioPerformanceSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioPerformanceSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioPerformanceSettings"

    def __init__(self, max_voices: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            max_voices: Initial value for MaxVoices.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if max_voices is not None:
            self.max_voices = max_voices

    @property
    def max_voices(self) -> np.int32 | None:
        """The MaxVoices field value."""
        member = self.get_member("MaxVoices")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_voices.setter
    def max_voices(self, value: np.int32) -> None:
        """Set the MaxVoices field value."""
        member = self.get_member("MaxVoices")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxVoices", fields.FieldInt(value=value)
            )

    @property
    def output_buffer_size(self) -> members.FieldEnum | None:
        """The OutputBufferSize member."""
        member = self.get_member("OutputBufferSize")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @output_buffer_size.setter
    def output_buffer_size(self, value: members.FieldEnum) -> None:
        """Set the OutputBufferSize member."""
        self.set_member("OutputBufferSize", value)

    @property
    def simulation_frame_size(self) -> members.FieldEnum | None:
        """The SimulationFrameSize member."""
        member = self.get_member("SimulationFrameSize")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @simulation_frame_size.setter
    def simulation_frame_size(self, value: members.FieldEnum) -> None:
        """Set the SimulationFrameSize member."""
        self.set_member("SimulationFrameSize", value)

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

