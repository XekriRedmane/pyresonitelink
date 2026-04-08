"""Generated component: AudioOutput."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.audio_rolloff_curve import AudioRolloffCurve
from pyresonitelink.generated._enums.audio_type_group import AudioTypeGroup
from pyresonitelink.generated._enums.audio_distance_space import AudioDistanceSpace
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioOutput(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Audio Output is a component that is used to output sound from any kind of IAudioSource. This includes but is not limited to: Audio streams, audio clip players, and voices.

    Category: Audio

    Audio Output is used to Output audio from a large variety of audio
    sources. From Audio Clips, Audio Streams, Opus Streams, etc. Be careful
    with how many Audio Outputs you have in a world at once or the Audio
    Buffer can be overfilled and you wont hear anymore Audio Sources until
    it's cleared. You can negate this by disabling the hierarchy of the
    Component or the Component itself when it's not in use.

    **Min and Max scale**: If ``AudioDistanceSpace`` is set to Local, then first the scale's XYZ values are averaged. then that number is clamped between ``MinScale`` and ``MaxScale``. Finally ``MinDistance`` and ``MaxDistance`` are multipled by the number, and set to the results. Basically scaling min and max distances up/down.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioOutput"

    def __init__(self, volume: primitives.Float | None = None, source: str | IWorldAudioDataSource | None = None, spatial_blend: primitives.Float | None = None, spatialize: primitives.Bool | None = None, spatialization_start_distance: primitives.Float | None = None, spatialization_transition_range: primitives.Float | None = None, doppler_level: primitives.Float | None = None, pitch: primitives.Float | None = None, global_: primitives.Bool | None = None, rolloff_mode: AudioRolloffCurve | str | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, priority: primitives.Int | None = None, audio_type_group: AudioTypeGroup | str | None = None, distance_space: AudioDistanceSpace | str | None = None, min_scale: primitives.Float | None = None, max_scale: primitives.Float | None = None, ignore_audio_effects: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            volume: Initial value for Volume.
            source: Initial value for Source.
            spatial_blend: Initial value for SpatialBlend.
            spatialize: Initial value for Spatialize.
            spatialization_start_distance: Initial value for SpatializationStartDistance.
            spatialization_transition_range: Initial value for SpatializationTransitionRange.
            doppler_level: Initial value for DopplerLevel.
            pitch: Initial value for Pitch.
            global_: Initial value for Global.
            rolloff_mode: Initial value for RolloffMode.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            priority: Initial value for Priority.
            audio_type_group: Initial value for AudioTypeGroup.
            distance_space: Initial value for DistanceSpace.
            min_scale: Initial value for MinScale.
            max_scale: Initial value for MaxScale.
            ignore_audio_effects: Initial value for IgnoreAudioEffects.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if volume is not None:
            self.volume = volume
        if source is not None:
            self.source = source
        if spatial_blend is not None:
            self.spatial_blend = spatial_blend
        if spatialize is not None:
            self.spatialize = spatialize
        if spatialization_start_distance is not None:
            self.spatialization_start_distance = spatialization_start_distance
        if spatialization_transition_range is not None:
            self.spatialization_transition_range = spatialization_transition_range
        if doppler_level is not None:
            self.doppler_level = doppler_level
        if pitch is not None:
            self.pitch = pitch
        if global_ is not None:
            self.global_ = global_
        if rolloff_mode is not None:
            self.rolloff_mode = rolloff_mode
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if priority is not None:
            self.priority = priority
        if audio_type_group is not None:
            self.audio_type_group = audio_type_group
        if distance_space is not None:
            self.distance_space = distance_space
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if ignore_audio_effects is not None:
            self.ignore_audio_effects = ignore_audio_effects

    @property
    def volume(self) -> primitives.Float | None:
        """The volume to play the clip at, from 0 to 1."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: primitives.Float) -> None:
        """Set the Volume field value."""
        member = self.get_member("Volume")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Volume", fields.FieldFloat(value=value)
            )

    @property
    def source(self) -> str | None:
        """The source of audio. Can be an AudioClipPlayer, LerpingMultiClipPlayer, or MultiAudioClipPlayer."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IWorldAudioDataSource | None) -> None:
        """Set the Source reference by target ID or IWorldAudioDataSource instance."""
        target_id: str | None = target.id if isinstance(target, IWorldAudioDataSource) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldAudioDataSource'),
            )

    @property
    def spatial_blend(self) -> primitives.Float | None:
        """Blends the the audio between 3D & 2D."""
        member = self.get_member("SpatialBlend")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatial_blend.setter
    def spatial_blend(self, value: primitives.Float) -> None:
        """Set the SpatialBlend field value."""
        member = self.get_member("SpatialBlend")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpatialBlend", fields.FieldFloat(value=value)
            )

    @property
    def spatialize(self) -> primitives.Bool | None:
        """Enables or disables rather it's 3D or 2D."""
        member = self.get_member("Spatialize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialize.setter
    def spatialize(self, value: primitives.Bool) -> None:
        """Set the Spatialize field value."""
        member = self.get_member("Spatialize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spatialize", fields.FieldBool(value=value)
            )

    @property
    def spatialization_start_distance(self) -> primitives.Float | None:
        """The SpatializationStartDistance field value."""
        member = self.get_member("SpatializationStartDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialization_start_distance.setter
    def spatialization_start_distance(self, value: primitives.Float) -> None:
        """Set the SpatializationStartDistance field value."""
        member = self.get_member("SpatializationStartDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpatializationStartDistance", fields.FieldFloat(value=value)
            )

    @property
    def spatialization_transition_range(self) -> primitives.Float | None:
        """The SpatializationTransitionRange field value."""
        member = self.get_member("SpatializationTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialization_transition_range.setter
    def spatialization_transition_range(self, value: primitives.Float) -> None:
        """Set the SpatializationTransitionRange field value."""
        member = self.get_member("SpatializationTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpatializationTransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def doppler_level(self) -> primitives.Float | None:
        """Simulates audio distortion when you or the object is moving."""
        member = self.get_member("DopplerLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @doppler_level.setter
    def doppler_level(self, value: primitives.Float) -> None:
        """Set the DopplerLevel field value."""
        member = self.get_member("DopplerLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DopplerLevel", fields.FieldFloat(value=value)
            )

    @property
    def pitch(self) -> primitives.Float | None:
        """The Pitch field value."""
        member = self.get_member("Pitch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pitch.setter
    def pitch(self, value: primitives.Float) -> None:
        """Set the Pitch field value."""
        member = self.get_member("Pitch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pitch", fields.FieldFloat(value=value)
            )

    @property
    def global_(self) -> primitives.Bool | None:
        """The Global field value."""
        member = self.get_member("Global")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_.setter
    def global_(self, value: primitives.Bool) -> None:
        """Set the Global field value."""
        member = self.get_member("Global")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Global", fields.FieldNullableBool(value=value)
            )

    @property
    def rolloff_mode(self) -> AudioRolloffCurve | None:
        """Switches between logarithmic and Linear audio falloff."""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioRolloffCurve(member.value)
        return None

    @rolloff_mode.setter
    def rolloff_mode(self, value: AudioRolloffCurve | str) -> None:
        """Set RolloffMode. Switches between logarithmic and Linear audio falloff."""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RolloffMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_distance(self) -> primitives.Float | None:
        """Minimum distance you need to be from the source to hear the audio."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: primitives.Float) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """Maximum distance from the source until you no longer hear the audio."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: primitives.Float) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def priority(self) -> primitives.Int | None:
        """see Unity audio source priority"""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def audio_type_group(self) -> AudioTypeGroup | None:
        """Changes what track of Audio the source should be. SoundEffects, Multimedia, Voice, User Interface."""
        member = self.get_member("AudioTypeGroup")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioTypeGroup(member.value)
        return None

    @audio_type_group.setter
    def audio_type_group(self, value: AudioTypeGroup | str) -> None:
        """Set AudioTypeGroup. Changes what track of Audio the source should be. SoundEffects, Multimedia, Voice, User Interface."""
        member = self.get_member("AudioTypeGroup")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "AudioTypeGroup",
                members.FieldEnum(value=str(value)),
            )

    @property
    def distance_space(self) -> AudioDistanceSpace | None:
        """Chooses rather the audio should use it's local scale or it's global scale."""
        member = self.get_member("DistanceSpace")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioDistanceSpace(member.value)
        return None

    @distance_space.setter
    def distance_space(self, value: AudioDistanceSpace | str) -> None:
        """Set DistanceSpace. Chooses rather the audio should use it's local scale or it's global scale."""
        member = self.get_member("DistanceSpace")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DistanceSpace",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_scale(self) -> primitives.Float | None:
        """See Min and Max Scale"""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: primitives.Float) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat(value=value)
            )

    @property
    def max_scale(self) -> primitives.Float | None:
        """See Min and Max Scale"""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: primitives.Float) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat(value=value)
            )

    @property
    def ignore_audio_effects(self) -> primitives.Bool | None:
        """The IgnoreAudioEffects field value."""
        member = self.get_member("IgnoreAudioEffects")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_audio_effects.setter
    def ignore_audio_effects(self, value: primitives.Bool) -> None:
        """Set the IgnoreAudioEffects field value."""
        member = self.get_member("IgnoreAudioEffects")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreAudioEffects", fields.FieldBool(value=value)
            )

    @property
    def excluded_listeners(self) -> members.SyncList | None:
        """The ExcludedListeners member."""
        member = self.get_member("ExcludedListeners")
        if isinstance(member, members.SyncList):
            return member
        return None

    @excluded_listeners.setter
    def excluded_listeners(self, value: members.SyncList) -> None:
        """Set the ExcludedListeners member."""
        self.set_member("ExcludedListeners", value)

    @property
    def excluded_users(self) -> members.SyncList | None:
        """User references placed in here will be excluded from hearing the audio."""
        member = self.get_member("excludedUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @excluded_users.setter
    def excluded_users(self, value: members.SyncList) -> None:
        """Set excludedUsers. User references placed in here will be excluded from hearing the audio."""
        self.set_member("excludedUsers", value)

    async def exlude_user(self, resolink: protocols.ResoniteLinkClient, user: str, debug: bool = False) -> dict:
        """Excludes the User provided to it, so that user cannot hear this audio output.

        Args:
            resolink: Connected ResoniteLink client.
            user: The user parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ExludeUser", {"user": user}, debug,
        )

    async def exlude_local_user(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Excludes the local user running this sync method, so they cannot hear this audio output.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ExludeLocalUser", {}, debug,
        )

    async def remove_local_excluded_user(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """if currently excluded, makes it to where the local user running this sync method is no longer excluded from hearing this audio output.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveLocalExcludedUser", {}, debug,
        )

    async def remove_exluded_user(self, resolink: protocols.ResoniteLinkClient, user: str, debug: bool = False) -> dict:
        """If provided user is currently excluded, makes it so that the provided user is no longer excluded from hearing this audio output.

        Args:
            resolink: Connected ResoniteLink client.
            user: The user parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveExludedUser", {"user": user}, debug,
        )

    async def clear_exluded_users(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Clears all excluded users from the list

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ClearExludedUsers", {}, debug,
        )

    async def is_user_exluded(self, resolink: protocols.ResoniteLinkClient, user: str, debug: bool = False) -> dict:
        """When provided a user, this function returns whether or not that user is excluded from hearing this audio clip.

        Args:
            resolink: Connected ResoniteLink client.
            user: The user parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "IsUserExluded", {"user": user}, debug,
        )

