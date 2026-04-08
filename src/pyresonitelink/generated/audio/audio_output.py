"""Generated component: AudioOutput."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioOutput(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioOutput.

    Category: Audio
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioOutput"

    def __init__(self, volume: np.float32 | None = None, source: str | IWorldAudioDataSource | None = None, spatial_blend: np.float32 | None = None, spatialize: bool | None = None, spatialization_start_distance: np.float32 | None = None, spatialization_transition_range: np.float32 | None = None, doppler_level: np.float32 | None = None, pitch: np.float32 | None = None, global_: bool | None = None, min_distance: np.float32 | None = None, max_distance: np.float32 | None = None, priority: np.int32 | None = None, min_scale: np.float32 | None = None, max_scale: np.float32 | None = None, ignore_audio_effects: bool | None = None, *, component: workers.Component | None = None) -> None:
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
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            priority: Initial value for Priority.
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
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if priority is not None:
            self.priority = priority
        if min_scale is not None:
            self.min_scale = min_scale
        if max_scale is not None:
            self.max_scale = max_scale
        if ignore_audio_effects is not None:
            self.ignore_audio_effects = ignore_audio_effects

    @property
    def volume(self) -> np.float32 | None:
        """The Volume field value."""
        member = self.get_member("Volume")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @volume.setter
    def volume(self, value: np.float32) -> None:
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
        """Target ID of the Source reference (targets IWorldAudioDataSource)."""
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
    def spatial_blend(self) -> np.float32 | None:
        """The SpatialBlend field value."""
        member = self.get_member("SpatialBlend")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatial_blend.setter
    def spatial_blend(self, value: np.float32) -> None:
        """Set the SpatialBlend field value."""
        member = self.get_member("SpatialBlend")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpatialBlend", fields.FieldFloat(value=value)
            )

    @property
    def spatialize(self) -> bool | None:
        """The Spatialize field value."""
        member = self.get_member("Spatialize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialize.setter
    def spatialize(self, value: bool) -> None:
        """Set the Spatialize field value."""
        member = self.get_member("Spatialize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Spatialize", fields.FieldBool(value=value)
            )

    @property
    def spatialization_start_distance(self) -> np.float32 | None:
        """The SpatializationStartDistance field value."""
        member = self.get_member("SpatializationStartDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialization_start_distance.setter
    def spatialization_start_distance(self, value: np.float32) -> None:
        """Set the SpatializationStartDistance field value."""
        member = self.get_member("SpatializationStartDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpatializationStartDistance", fields.FieldFloat(value=value)
            )

    @property
    def spatialization_transition_range(self) -> np.float32 | None:
        """The SpatializationTransitionRange field value."""
        member = self.get_member("SpatializationTransitionRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spatialization_transition_range.setter
    def spatialization_transition_range(self, value: np.float32) -> None:
        """Set the SpatializationTransitionRange field value."""
        member = self.get_member("SpatializationTransitionRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpatializationTransitionRange", fields.FieldFloat(value=value)
            )

    @property
    def doppler_level(self) -> np.float32 | None:
        """The DopplerLevel field value."""
        member = self.get_member("DopplerLevel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @doppler_level.setter
    def doppler_level(self, value: np.float32) -> None:
        """Set the DopplerLevel field value."""
        member = self.get_member("DopplerLevel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DopplerLevel", fields.FieldFloat(value=value)
            )

    @property
    def pitch(self) -> np.float32 | None:
        """The Pitch field value."""
        member = self.get_member("Pitch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pitch.setter
    def pitch(self, value: np.float32) -> None:
        """Set the Pitch field value."""
        member = self.get_member("Pitch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Pitch", fields.FieldFloat(value=value)
            )

    @property
    def global_(self) -> bool | None:
        """The Global field value."""
        member = self.get_member("Global")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @global_.setter
    def global_(self, value: bool) -> None:
        """Set the Global field value."""
        member = self.get_member("Global")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Global", fields.FieldNullableBool(value=value)
            )

    @property
    def rolloff_mode(self) -> members.FieldEnum | None:
        """The RolloffMode member."""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rolloff_mode.setter
    def rolloff_mode(self, value: members.FieldEnum) -> None:
        """Set the RolloffMode member."""
        self.set_member("RolloffMode", value)

    @property
    def min_distance(self) -> np.float32 | None:
        """The MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_distance.setter
    def min_distance(self, value: np.float32) -> None:
        """Set the MinDistance field value."""
        member = self.get_member("MinDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinDistance", fields.FieldFloat(value=value)
            )

    @property
    def max_distance(self) -> np.float32 | None:
        """The MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_distance.setter
    def max_distance(self, value: np.float32) -> None:
        """Set the MaxDistance field value."""
        member = self.get_member("MaxDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxDistance", fields.FieldFloat(value=value)
            )

    @property
    def priority(self) -> np.int32 | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: np.int32) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def audio_type_group(self) -> members.FieldEnum | None:
        """The AudioTypeGroup member."""
        member = self.get_member("AudioTypeGroup")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @audio_type_group.setter
    def audio_type_group(self, value: members.FieldEnum) -> None:
        """Set the AudioTypeGroup member."""
        self.set_member("AudioTypeGroup", value)

    @property
    def distance_space(self) -> members.FieldEnum | None:
        """The DistanceSpace member."""
        member = self.get_member("DistanceSpace")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @distance_space.setter
    def distance_space(self, value: members.FieldEnum) -> None:
        """Set the DistanceSpace member."""
        self.set_member("DistanceSpace", value)

    @property
    def min_scale(self) -> np.float32 | None:
        """The MinScale field value."""
        member = self.get_member("MinScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_scale.setter
    def min_scale(self, value: np.float32) -> None:
        """Set the MinScale field value."""
        member = self.get_member("MinScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinScale", fields.FieldFloat(value=value)
            )

    @property
    def max_scale(self) -> np.float32 | None:
        """The MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_scale.setter
    def max_scale(self, value: np.float32) -> None:
        """Set the MaxScale field value."""
        member = self.get_member("MaxScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxScale", fields.FieldFloat(value=value)
            )

    @property
    def ignore_audio_effects(self) -> bool | None:
        """The IgnoreAudioEffects field value."""
        member = self.get_member("IgnoreAudioEffects")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_audio_effects.setter
    def ignore_audio_effects(self, value: bool) -> None:
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
        """The excludedUsers member."""
        member = self.get_member("excludedUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @excluded_users.setter
    def excluded_users(self, value: members.SyncList) -> None:
        """Set the excludedUsers member."""
        self.set_member("excludedUsers", value)

    async def exlude_user(self, resolink: protocols.ResoniteLinkClient, user: str, debug: bool = False) -> dict:
        """Call the ExludeUser sync method.

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
        """Call the ExludeLocalUser sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ExludeLocalUser", {}, debug,
        )

    async def remove_local_excluded_user(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the RemoveLocalExcludedUser sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveLocalExcludedUser", {}, debug,
        )

    async def remove_exluded_user(self, resolink: protocols.ResoniteLinkClient, user: str, debug: bool = False) -> dict:
        """Call the RemoveExludedUser sync method.

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
        """Call the ClearExludedUsers sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ClearExludedUsers", {}, debug,
        )

    async def is_user_exluded(self, resolink: protocols.ResoniteLinkClient, user: str, debug: bool = False) -> dict:
        """Call the IsUserExluded sync method.

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

