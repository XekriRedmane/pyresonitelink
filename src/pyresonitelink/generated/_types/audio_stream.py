"""Generated type: AudioStream."""

from typing import Generic, TypeVar

from pyresonitelink.generated._types.stream import Stream
from pyresonitelink.generated._types.iaudio_stream import IAudioStream
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iaudio_sample import IAudioSample

S = TypeVar('S')


class AudioStream(Stream, IAudioStream, ICustomInspector, Generic[S]):
    """Abstract class: [FrooxEngine]FrooxEngine.AudioStream<>."""

    RESONITE_TYPE: str = "[FrooxEngine]FrooxEngine.AudioStream<>"

