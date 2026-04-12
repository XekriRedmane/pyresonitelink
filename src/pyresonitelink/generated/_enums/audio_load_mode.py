"""Generated enum: AudioLoadMode."""

from enum import StrEnum


class AudioLoadMode(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.AudioLoadMode."""

    automatic = "Automatic"
    stream_from_file = "StreamFromFile"
    stream_from_memory = "StreamFromMemory"
    fully_decode = "FullyDecode"

