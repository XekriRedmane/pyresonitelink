"""Generated component: AudioStreamMetadata."""

from typing import Any
import numpy as np

S = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.audio_stream import AudioStream
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioStreamMetadata(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioStreamMetadata<>.

    Category: Assets/Utility

    Parameterize with a value type::

        AudioStreamMetadata[np.float32]
        AudioStreamMetadata[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioStreamMetadata<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.AudioStreamMetadata<>"

    def __init__(self, stream: str | AudioStream[S] | None = None, unread_samples: np.int32 | None = None, total_missed_samples: np.int32 | None = None, last_missed_samples: np.int32 | None = None, buffer_length: np.int32 | None = None, average_read_samples_per_second: np.float64 | None = None, average_write_samples_per_second: np.float64 | None = None, global_index: np.int64 | None = None, samples_available_for_encode: np.int32 | None = None, frame_size: np.int32 | None = None, max_frame_size: np.int32 | None = None, encoded_sample_rate: np.int32 | None = None, total_packet_count: np.int32 | None = None, total_lost_packets: np.int32 | None = None, last_lost_packets: np.int32 | None = None, packet_loss_ratio: np.float32 | None = None, average_codec_samples_per_second: np.float64 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            stream: Initial value for Stream.
            unread_samples: Initial value for UnreadSamples.
            total_missed_samples: Initial value for TotalMissedSamples.
            last_missed_samples: Initial value for LastMissedSamples.
            buffer_length: Initial value for BufferLength.
            average_read_samples_per_second: Initial value for AverageReadSamplesPerSecond.
            average_write_samples_per_second: Initial value for AverageWriteSamplesPerSecond.
            global_index: Initial value for GlobalIndex.
            samples_available_for_encode: Initial value for SamplesAvailableForEncode.
            frame_size: Initial value for FrameSize.
            max_frame_size: Initial value for MaxFrameSize.
            encoded_sample_rate: Initial value for EncodedSampleRate.
            total_packet_count: Initial value for TotalPacketCount.
            total_lost_packets: Initial value for TotalLostPackets.
            last_lost_packets: Initial value for LastLostPackets.
            packet_loss_ratio: Initial value for PacketLossRatio.
            average_codec_samples_per_second: Initial value for AverageCodecSamplesPerSecond.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if stream is not None:
            self.stream = stream
        if unread_samples is not None:
            self.unread_samples = unread_samples
        if total_missed_samples is not None:
            self.total_missed_samples = total_missed_samples
        if last_missed_samples is not None:
            self.last_missed_samples = last_missed_samples
        if buffer_length is not None:
            self.buffer_length = buffer_length
        if average_read_samples_per_second is not None:
            self.average_read_samples_per_second = average_read_samples_per_second
        if average_write_samples_per_second is not None:
            self.average_write_samples_per_second = average_write_samples_per_second
        if global_index is not None:
            self.global_index = global_index
        if samples_available_for_encode is not None:
            self.samples_available_for_encode = samples_available_for_encode
        if frame_size is not None:
            self.frame_size = frame_size
        if max_frame_size is not None:
            self.max_frame_size = max_frame_size
        if encoded_sample_rate is not None:
            self.encoded_sample_rate = encoded_sample_rate
        if total_packet_count is not None:
            self.total_packet_count = total_packet_count
        if total_lost_packets is not None:
            self.total_lost_packets = total_lost_packets
        if last_lost_packets is not None:
            self.last_lost_packets = last_lost_packets
        if packet_loss_ratio is not None:
            self.packet_loss_ratio = packet_loss_ratio
        if average_codec_samples_per_second is not None:
            self.average_codec_samples_per_second = average_codec_samples_per_second

    @property
    def stream(self) -> str | None:
        """Target ID of the Stream reference (targets AudioStream[S])."""
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream.setter
    def stream(self, target: str | AudioStream[S] | None) -> None:
        """Set the Stream reference by target ID or AudioStream[S] instance."""
        target_id: str | None = target.id if isinstance(target, AudioStream) else target  # type: ignore[assignment]
        member = self.get_member("Stream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioStream<S>'),
            )

    @property
    def unread_samples(self) -> np.int32 | None:
        """The UnreadSamples field value."""
        member = self.get_member("UnreadSamples")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unread_samples.setter
    def unread_samples(self, value: np.int32) -> None:
        """Set the UnreadSamples field value."""
        member = self.get_member("UnreadSamples")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnreadSamples", fields.FieldInt(value=value)
            )

    @property
    def total_missed_samples(self) -> np.int32 | None:
        """The TotalMissedSamples field value."""
        member = self.get_member("TotalMissedSamples")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_missed_samples.setter
    def total_missed_samples(self, value: np.int32) -> None:
        """Set the TotalMissedSamples field value."""
        member = self.get_member("TotalMissedSamples")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMissedSamples", fields.FieldInt(value=value)
            )

    @property
    def last_missed_samples(self) -> np.int32 | None:
        """The LastMissedSamples field value."""
        member = self.get_member("LastMissedSamples")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_missed_samples.setter
    def last_missed_samples(self, value: np.int32) -> None:
        """Set the LastMissedSamples field value."""
        member = self.get_member("LastMissedSamples")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastMissedSamples", fields.FieldInt(value=value)
            )

    @property
    def buffer_length(self) -> np.int32 | None:
        """The BufferLength field value."""
        member = self.get_member("BufferLength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @buffer_length.setter
    def buffer_length(self, value: np.int32) -> None:
        """Set the BufferLength field value."""
        member = self.get_member("BufferLength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BufferLength", fields.FieldInt(value=value)
            )

    @property
    def average_read_samples_per_second(self) -> np.float64 | None:
        """The AverageReadSamplesPerSecond field value."""
        member = self.get_member("AverageReadSamplesPerSecond")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_read_samples_per_second.setter
    def average_read_samples_per_second(self, value: np.float64) -> None:
        """Set the AverageReadSamplesPerSecond field value."""
        member = self.get_member("AverageReadSamplesPerSecond")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageReadSamplesPerSecond", fields.FieldDouble(value=value)
            )

    @property
    def average_write_samples_per_second(self) -> np.float64 | None:
        """The AverageWriteSamplesPerSecond field value."""
        member = self.get_member("AverageWriteSamplesPerSecond")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_write_samples_per_second.setter
    def average_write_samples_per_second(self, value: np.float64) -> None:
        """Set the AverageWriteSamplesPerSecond field value."""
        member = self.get_member("AverageWriteSamplesPerSecond")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageWriteSamplesPerSecond", fields.FieldDouble(value=value)
            )

    @property
    def global_index(self) -> np.int64 | None:
        """The GlobalIndex field value."""
        member = self.get_member("GlobalIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_index.setter
    def global_index(self, value: np.int64) -> None:
        """Set the GlobalIndex field value."""
        member = self.get_member("GlobalIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GlobalIndex", fields.FieldLong(value=value)
            )

    @property
    def samples_available_for_encode(self) -> np.int32 | None:
        """The SamplesAvailableForEncode field value."""
        member = self.get_member("SamplesAvailableForEncode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @samples_available_for_encode.setter
    def samples_available_for_encode(self, value: np.int32) -> None:
        """Set the SamplesAvailableForEncode field value."""
        member = self.get_member("SamplesAvailableForEncode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SamplesAvailableForEncode", fields.FieldInt(value=value)
            )

    @property
    def frame_size(self) -> np.int32 | None:
        """The FrameSize field value."""
        member = self.get_member("FrameSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @frame_size.setter
    def frame_size(self, value: np.int32) -> None:
        """Set the FrameSize field value."""
        member = self.get_member("FrameSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FrameSize", fields.FieldInt(value=value)
            )

    @property
    def max_frame_size(self) -> np.int32 | None:
        """The MaxFrameSize field value."""
        member = self.get_member("MaxFrameSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_frame_size.setter
    def max_frame_size(self, value: np.int32) -> None:
        """Set the MaxFrameSize field value."""
        member = self.get_member("MaxFrameSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxFrameSize", fields.FieldInt(value=value)
            )

    @property
    def encoded_sample_rate(self) -> np.int32 | None:
        """The EncodedSampleRate field value."""
        member = self.get_member("EncodedSampleRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @encoded_sample_rate.setter
    def encoded_sample_rate(self, value: np.int32) -> None:
        """Set the EncodedSampleRate field value."""
        member = self.get_member("EncodedSampleRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EncodedSampleRate", fields.FieldInt(value=value)
            )

    @property
    def total_packet_count(self) -> np.int32 | None:
        """The TotalPacketCount field value."""
        member = self.get_member("TotalPacketCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_packet_count.setter
    def total_packet_count(self, value: np.int32) -> None:
        """Set the TotalPacketCount field value."""
        member = self.get_member("TotalPacketCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalPacketCount", fields.FieldInt(value=value)
            )

    @property
    def total_lost_packets(self) -> np.int32 | None:
        """The TotalLostPackets field value."""
        member = self.get_member("TotalLostPackets")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_lost_packets.setter
    def total_lost_packets(self, value: np.int32) -> None:
        """Set the TotalLostPackets field value."""
        member = self.get_member("TotalLostPackets")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalLostPackets", fields.FieldInt(value=value)
            )

    @property
    def last_lost_packets(self) -> np.int32 | None:
        """The LastLostPackets field value."""
        member = self.get_member("LastLostPackets")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_lost_packets.setter
    def last_lost_packets(self, value: np.int32) -> None:
        """Set the LastLostPackets field value."""
        member = self.get_member("LastLostPackets")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastLostPackets", fields.FieldInt(value=value)
            )

    @property
    def packet_loss_ratio(self) -> np.float32 | None:
        """The PacketLossRatio field value."""
        member = self.get_member("PacketLossRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @packet_loss_ratio.setter
    def packet_loss_ratio(self, value: np.float32) -> None:
        """Set the PacketLossRatio field value."""
        member = self.get_member("PacketLossRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PacketLossRatio", fields.FieldFloat(value=value)
            )

    @property
    def average_codec_samples_per_second(self) -> np.float64 | None:
        """The AverageCodecSamplesPerSecond field value."""
        member = self.get_member("AverageCodecSamplesPerSecond")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @average_codec_samples_per_second.setter
    def average_codec_samples_per_second(self, value: np.float64) -> None:
        """Set the AverageCodecSamplesPerSecond field value."""
        member = self.get_member("AverageCodecSamplesPerSecond")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AverageCodecSamplesPerSecond", fields.FieldDouble(value=value)
            )

