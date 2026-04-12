"""Generated component: AvatarVoiceRangeVisualizer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarVoiceRangeVisualizer(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarVoiceRangeVisualizer component is used to generate and maintain the whisper bubble that appears when a user enables their whisper bubble mode.

    Category: Users/Common Avatar System/Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarVoiceRangeVisualizer"

    def __init__(self, volume_source: str | IField[primitives.Float] | None = None, audio_output: str | AudioOutput | None = None, whisper_color_min: primitives.ColorX | None = None, whisper_color_max: primitives.ColorX | None = None, whisper_color_recording_message: primitives.ColorX | None = None, visual_root: str | Slot | None = None, active_user: str | User | None = None, visual_size: str | IField[primitives.Float3] | None = None, visual_color: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            volume_source: Initial value for VolumeSource.
            audio_output: Initial value for AudioOutput.
            whisper_color_min: Initial value for WhisperColorMin.
            whisper_color_max: Initial value for WhisperColorMax.
            whisper_color_recording_message: Initial value for WhisperColorRecordingMessage.
            visual_root: Initial value for VisualRoot.
            active_user: Initial value for _activeUser.
            visual_size: Initial value for _visualSize.
            visual_color: Initial value for _visualColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if volume_source is not None:
            self.volume_source = volume_source
        if audio_output is not None:
            self.audio_output = audio_output
        if whisper_color_min is not None:
            self.whisper_color_min = whisper_color_min
        if whisper_color_max is not None:
            self.whisper_color_max = whisper_color_max
        if whisper_color_recording_message is not None:
            self.whisper_color_recording_message = whisper_color_recording_message
        if visual_root is not None:
            self.visual_root = visual_root
        if active_user is not None:
            self.active_user = active_user
        if visual_size is not None:
            self.visual_size = visual_size
        if visual_color is not None:
            self.visual_color = visual_color

    @property
    def volume_source(self) -> str | None:
        """A float representing audio change. Usually the ``Volume`` field from a Component:VolumeMeter"""
        member = self.get_member("VolumeSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_source.setter
    def volume_source(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the VolumeSource reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("VolumeSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VolumeSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def audio_output(self) -> str | None:
        """An audio output to read info from to make the bubble size"""
        member = self.get_member("AudioOutput")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_output.setter
    def audio_output(self, target: str | AudioOutput | None) -> None:
        """Set the AudioOutput reference by target ID or AudioOutput instance."""
        target_id: str | None = target.id if isinstance(target, AudioOutput) else target  # type: ignore[assignment]
        member = self.get_member("AudioOutput")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AudioOutput",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AudioOutput'),
            )

    @property
    def whisper_color_min(self) -> primitives.ColorX | None:
        """The color the bubble should glow at when the user is not speaking during whisper mode."""
        member = self.get_member("WhisperColorMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @whisper_color_min.setter
    def whisper_color_min(self, value: primitives.ColorX) -> None:
        """Set the WhisperColorMin field value."""
        member = self.get_member("WhisperColorMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WhisperColorMin", fields.FieldColorX(value=value)
            )

    @property
    def whisper_color_max(self) -> primitives.ColorX | None:
        """The color the bubble should glow at when the user is speaking at max volume during whisper mode."""
        member = self.get_member("WhisperColorMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @whisper_color_max.setter
    def whisper_color_max(self, value: primitives.ColorX) -> None:
        """Set the WhisperColorMax field value."""
        member = self.get_member("WhisperColorMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WhisperColorMax", fields.FieldColorX(value=value)
            )

    @property
    def whisper_color_recording_message(self) -> primitives.ColorX | None:
        """The color the bubble should be when the user is recording a message."""
        member = self.get_member("WhisperColorRecordingMessage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @whisper_color_recording_message.setter
    def whisper_color_recording_message(self, value: primitives.ColorX) -> None:
        """Set the WhisperColorRecordingMessage field value."""
        member = self.get_member("WhisperColorRecordingMessage")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WhisperColorRecordingMessage", fields.FieldColorX(value=value)
            )

    @property
    def visual_root(self) -> str | None:
        """The root slot of the visual generated for this component to function"""
        member = self.get_member("VisualRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_root.setter
    def visual_root(self, target: str | Slot | None) -> None:
        """Set the VisualRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("VisualRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VisualRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def active_user(self) -> str | None:
        """The user controlling and updating this component's logic."""
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_user.setter
    def active_user(self, target: str | User | None) -> None:
        """Set the _activeUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_activeUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activeUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def visual_size(self) -> str | None:
        """The field to use when driving the size of this visual to match the range of the user's whisper mode. Uses ``AudioOutput``'s range for the source of the data."""
        member = self.get_member("_visualSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_size.setter
    def visual_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _visualSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def visual_color(self) -> str | None:
        """The field to drive to a color in an inclusive range of ``WhisperColorMin`` and ``WhisperColorMax`` depending on volume output."""
        member = self.get_member("_visualColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_color.setter
    def visual_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _visualColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

