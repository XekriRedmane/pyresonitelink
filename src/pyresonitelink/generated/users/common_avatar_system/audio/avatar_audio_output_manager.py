"""Generated component: AvatarAudioOutputManager."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.audio_output import AudioOutput
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.audio_rolloff_curve import AudioRolloffCurve
from pyresonitelink.generated._types.audio_distance_space import AudioDistanceSpace
from pyresonitelink.generated._types.avatar_audio_configuration import AvatarAudioConfiguration
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAudioOutputManager(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarAudioOutputManager.

    Category: Users/Common Avatar System/Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAudioOutputManager"

    def __init__(self, audio_output: str | AudioOutput | None = None, is_view_voice: bool | None = None, legacy_whisper_volume: np.float32 | None = None, legacy_normal_volume: np.float32 | None = None, legacy_shout_volume: np.float32 | None = None, legacy_broadcast_volume: np.float32 | None = None, legacy_normal_doppler_level: np.float32 | None = None, legacy_shout_doppler_level: np.float32 | None = None, legacy_whisper_range: np.float32 | None = None, active_user: str | User | None = None, enabled: str | IField[bool] | None = None, volume: str | IField[np.float32] | None = None, doppler: str | IField[np.float32] | None = None, spatialize: str | IField[bool] | None = None, spatial_blend: str | IField[np.float32] | None = None, ignore_audio_effects: str | IField[bool] | None = None, min_distance: str | IField[np.float32] | None = None, max_distance: str | IField[np.float32] | None = None, roll_off_mode: str | IField[AudioRolloffCurve] | None = None, distance_space: str | IField[AudioDistanceSpace] | None = None, min_scale: str | IField[np.float32] | None = None, max_scale: str | IField[np.float32] | None = None, scale_compensation: np.float32 | None = None, audio_configuration: str | AvatarAudioConfiguration | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            audio_output: Initial value for AudioOutput.
            is_view_voice: Initial value for IsViewVoice.
            legacy_whisper_volume: Initial value for __legacyWhisperVolume.
            legacy_normal_volume: Initial value for __legacyNormalVolume.
            legacy_shout_volume: Initial value for __legacyShoutVolume.
            legacy_broadcast_volume: Initial value for __legacyBroadcastVolume.
            legacy_normal_doppler_level: Initial value for __legacyNormalDopplerLevel.
            legacy_shout_doppler_level: Initial value for __legacyShoutDopplerLevel.
            legacy_whisper_range: Initial value for __legacyWhisperRange.
            active_user: Initial value for _activeUser.
            enabled: Initial value for _enabled.
            volume: Initial value for _volume.
            doppler: Initial value for _doppler.
            spatialize: Initial value for _spatialize.
            spatial_blend: Initial value for _spatialBlend.
            ignore_audio_effects: Initial value for _ignoreAudioEffects.
            min_distance: Initial value for _minDistance.
            max_distance: Initial value for _maxDistance.
            roll_off_mode: Initial value for _rollOffMode.
            distance_space: Initial value for _distanceSpace.
            min_scale: Initial value for _minScale.
            max_scale: Initial value for _maxScale.
            scale_compensation: Initial value for _scaleCompensation.
            audio_configuration: Initial value for _audioConfiguration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if audio_output is not None:
            self.audio_output = audio_output
        if is_view_voice is not None:
            self.is_view_voice = is_view_voice
        if legacy_whisper_volume is not None:
            self.legacy_whisper_volume = legacy_whisper_volume
        if legacy_normal_volume is not None:
            self.legacy_normal_volume = legacy_normal_volume
        if legacy_shout_volume is not None:
            self.legacy_shout_volume = legacy_shout_volume
        if legacy_broadcast_volume is not None:
            self.legacy_broadcast_volume = legacy_broadcast_volume
        if legacy_normal_doppler_level is not None:
            self.legacy_normal_doppler_level = legacy_normal_doppler_level
        if legacy_shout_doppler_level is not None:
            self.legacy_shout_doppler_level = legacy_shout_doppler_level
        if legacy_whisper_range is not None:
            self.legacy_whisper_range = legacy_whisper_range
        if active_user is not None:
            self.active_user = active_user
        if enabled is not None:
            self.enabled = enabled
        if volume is not None:
            self.volume = volume
        if doppler is not None:
            self.doppler = doppler
        if spatialize is not None:
            self.spatialize = spatialize
        if spatial_blend is not None:
            self.spatial_blend = spatial_blend
        if ignore_audio_effects is not None:
            self.ignore_audio_effects = ignore_audio_effects
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if roll_off_mode is not None:
            self.roll_off_mode = roll_off_mode
        if distance_space is not None:
            self.distance_space = distance_space
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if scale_compensation is not None:
            self.scale_compensation = scale_compensation
        if audio_configuration is not None:
            self.audio_configuration = audio_configuration

    @property
    def audio_output(self) -> str | None:
        """Target ID of the AudioOutput reference (targets AudioOutput)."""
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
    def is_view_voice(self) -> bool | None:
        """The IsViewVoice field value."""
        member = self.get_member("IsViewVoice")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_view_voice.setter
    def is_view_voice(self, value: bool) -> None:
        """Set the IsViewVoice field value."""
        member = self.get_member("IsViewVoice")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsViewVoice", fields.FieldBool(value=value)
            )

    @property
    def whisper_config(self) -> members.SyncObject | None:
        """The WhisperConfig member."""
        member = self.get_member("WhisperConfig")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @whisper_config.setter
    def whisper_config(self, value: members.SyncObject) -> None:
        """Set the WhisperConfig member."""
        self.set_member("WhisperConfig", value)

    @property
    def normal_config(self) -> members.SyncObject | None:
        """The NormalConfig member."""
        member = self.get_member("NormalConfig")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @normal_config.setter
    def normal_config(self, value: members.SyncObject) -> None:
        """Set the NormalConfig member."""
        self.set_member("NormalConfig", value)

    @property
    def shout_config(self) -> members.SyncObject | None:
        """The ShoutConfig member."""
        member = self.get_member("ShoutConfig")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @shout_config.setter
    def shout_config(self, value: members.SyncObject) -> None:
        """Set the ShoutConfig member."""
        self.set_member("ShoutConfig", value)

    @property
    def broadcast_config(self) -> members.SyncObject | None:
        """The BroadcastConfig member."""
        member = self.get_member("BroadcastConfig")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @broadcast_config.setter
    def broadcast_config(self, value: members.SyncObject) -> None:
        """Set the BroadcastConfig member."""
        self.set_member("BroadcastConfig", value)

    @property
    def legacy_whisper_volume(self) -> np.float32 | None:
        """The __legacyWhisperVolume field value."""
        member = self.get_member("__legacyWhisperVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_whisper_volume.setter
    def legacy_whisper_volume(self, value: np.float32) -> None:
        """Set the __legacyWhisperVolume field value."""
        member = self.get_member("__legacyWhisperVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyWhisperVolume", fields.FieldFloat(value=value)
            )

    @property
    def legacy_normal_volume(self) -> np.float32 | None:
        """The __legacyNormalVolume field value."""
        member = self.get_member("__legacyNormalVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_normal_volume.setter
    def legacy_normal_volume(self, value: np.float32) -> None:
        """Set the __legacyNormalVolume field value."""
        member = self.get_member("__legacyNormalVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyNormalVolume", fields.FieldFloat(value=value)
            )

    @property
    def legacy_shout_volume(self) -> np.float32 | None:
        """The __legacyShoutVolume field value."""
        member = self.get_member("__legacyShoutVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_shout_volume.setter
    def legacy_shout_volume(self, value: np.float32) -> None:
        """Set the __legacyShoutVolume field value."""
        member = self.get_member("__legacyShoutVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyShoutVolume", fields.FieldFloat(value=value)
            )

    @property
    def legacy_broadcast_volume(self) -> np.float32 | None:
        """The __legacyBroadcastVolume field value."""
        member = self.get_member("__legacyBroadcastVolume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_broadcast_volume.setter
    def legacy_broadcast_volume(self, value: np.float32) -> None:
        """Set the __legacyBroadcastVolume field value."""
        member = self.get_member("__legacyBroadcastVolume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyBroadcastVolume", fields.FieldFloat(value=value)
            )

    @property
    def legacy_normal_doppler_level(self) -> np.float32 | None:
        """The __legacyNormalDopplerLevel field value."""
        member = self.get_member("__legacyNormalDopplerLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_normal_doppler_level.setter
    def legacy_normal_doppler_level(self, value: np.float32) -> None:
        """Set the __legacyNormalDopplerLevel field value."""
        member = self.get_member("__legacyNormalDopplerLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyNormalDopplerLevel", fields.FieldFloat(value=value)
            )

    @property
    def legacy_shout_doppler_level(self) -> np.float32 | None:
        """The __legacyShoutDopplerLevel field value."""
        member = self.get_member("__legacyShoutDopplerLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_shout_doppler_level.setter
    def legacy_shout_doppler_level(self, value: np.float32) -> None:
        """Set the __legacyShoutDopplerLevel field value."""
        member = self.get_member("__legacyShoutDopplerLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyShoutDopplerLevel", fields.FieldFloat(value=value)
            )

    @property
    def legacy_whisper_range(self) -> np.float32 | None:
        """The __legacyWhisperRange field value."""
        member = self.get_member("__legacyWhisperRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_whisper_range.setter
    def legacy_whisper_range(self, value: np.float32) -> None:
        """Set the __legacyWhisperRange field value."""
        member = self.get_member("__legacyWhisperRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyWhisperRange", fields.FieldFloat(value=value)
            )

    @property
    def active_user(self) -> str | None:
        """Target ID of the _activeUser reference (targets User)."""
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
    def enabled(self) -> str | None:
        """Target ID of the _enabled reference (targets IField[bool])."""
        member = self.get_member("_enabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @enabled.setter
    def enabled(self, target: str | IField[bool] | None) -> None:
        """Set the _enabled reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_enabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_enabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def volume(self) -> str | None:
        """Target ID of the _volume reference (targets IField[np.float32])."""
        member = self.get_member("_volume")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume.setter
    def volume(self, target: str | IField[np.float32] | None) -> None:
        """Set the _volume reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_volume")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_volume",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def doppler(self) -> str | None:
        """Target ID of the _doppler reference (targets IField[np.float32])."""
        member = self.get_member("_doppler")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @doppler.setter
    def doppler(self, target: str | IField[np.float32] | None) -> None:
        """Set the _doppler reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_doppler")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_doppler",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def spatialize(self) -> str | None:
        """Target ID of the _spatialize reference (targets IField[bool])."""
        member = self.get_member("_spatialize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatialize.setter
    def spatialize(self, target: str | IField[bool] | None) -> None:
        """Set the _spatialize reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_spatialize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spatialize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def spatial_blend(self) -> str | None:
        """Target ID of the _spatialBlend reference (targets IField[np.float32])."""
        member = self.get_member("_spatialBlend")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spatial_blend.setter
    def spatial_blend(self, target: str | IField[np.float32] | None) -> None:
        """Set the _spatialBlend reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_spatialBlend")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spatialBlend",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def ignore_audio_effects(self) -> str | None:
        """Target ID of the _ignoreAudioEffects reference (targets IField[bool])."""
        member = self.get_member("_ignoreAudioEffects")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ignore_audio_effects.setter
    def ignore_audio_effects(self, target: str | IField[bool] | None) -> None:
        """Set the _ignoreAudioEffects reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_ignoreAudioEffects")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_ignoreAudioEffects",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def min_distance(self) -> str | None:
        """Target ID of the _minDistance reference (targets IField[np.float32])."""
        member = self.get_member("_minDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min_distance.setter
    def min_distance(self, target: str | IField[np.float32] | None) -> None:
        """Set the _minDistance reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_minDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_minDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def max_distance(self) -> str | None:
        """Target ID of the _maxDistance reference (targets IField[np.float32])."""
        member = self.get_member("_maxDistance")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_distance.setter
    def max_distance(self, target: str | IField[np.float32] | None) -> None:
        """Set the _maxDistance reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_maxDistance")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maxDistance",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def roll_off_mode(self) -> str | None:
        """Target ID of the _rollOffMode reference (targets IField[AudioRolloffCurve])."""
        member = self.get_member("_rollOffMode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @roll_off_mode.setter
    def roll_off_mode(self, target: str | IField[AudioRolloffCurve] | None) -> None:
        """Set the _rollOffMode reference by target ID or IField[AudioRolloffCurve] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rollOffMode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rollOffMode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[Awwdio]Awwdio.AudioRolloffCurve>'),
            )

    @property
    def distance_space(self) -> str | None:
        """Target ID of the _distanceSpace reference (targets IField[AudioDistanceSpace])."""
        member = self.get_member("_distanceSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @distance_space.setter
    def distance_space(self, target: str | IField[AudioDistanceSpace] | None) -> None:
        """Set the _distanceSpace reference by target ID or IField[AudioDistanceSpace] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_distanceSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_distanceSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.AudioDistanceSpace>'),
            )

    @property
    def min_scale(self) -> str | None:
        """Target ID of the _minScale reference (targets IField[np.float32])."""
        member = self.get_member("_minScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @min_scale.setter
    def min_scale(self, target: str | IField[np.float32] | None) -> None:
        """Set the _minScale reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_minScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_minScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def max_scale(self) -> str | None:
        """Target ID of the _maxScale reference (targets IField[np.float32])."""
        member = self.get_member("_maxScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @max_scale.setter
    def max_scale(self, target: str | IField[np.float32] | None) -> None:
        """Set the _maxScale reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_maxScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_maxScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def scale_compensation(self) -> np.float32 | None:
        """The _scaleCompensation field value."""
        member = self.get_member("_scaleCompensation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_compensation.setter
    def scale_compensation(self, value: np.float32) -> None:
        """Set the _scaleCompensation field value."""
        member = self.get_member("_scaleCompensation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_scaleCompensation", fields.FieldFloat(value=value)
            )

    @property
    def audio_configuration(self) -> str | None:
        """Target ID of the _audioConfiguration reference (targets AvatarAudioConfiguration)."""
        member = self.get_member("_audioConfiguration")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @audio_configuration.setter
    def audio_configuration(self, target: str | AvatarAudioConfiguration | None) -> None:
        """Set the _audioConfiguration reference by target ID or AvatarAudioConfiguration instance."""
        target_id: str | None = target.id if isinstance(target, AvatarAudioConfiguration) else target  # type: ignore[assignment]
        member = self.get_member("_audioConfiguration")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_audioConfiguration",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AvatarAudioConfiguration'),
            )

