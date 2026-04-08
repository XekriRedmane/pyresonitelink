"""Generated component: ChildParentAudioClipPlayer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ChildParentAudioClipPlayer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ChildParentAudioClipPlayer.

    Category: Media
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ChildParentAudioClipPlayer"

    def __init__(self, parent_under: str | Slot | None = None, min_distance: np.float32 | None = None, max_distance: np.float32 | None = None, ignore_audio_effects: bool | None = None, child_limit: np.int32 | None = None, filter_tag: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_under: Initial value for ParentUnder.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            ignore_audio_effects: Initial value for IgnoreAudioEffects.
            child_limit: Initial value for ChildLimit.
            filter_tag: Initial value for FilterTag.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parent_under is not None:
            self.parent_under = parent_under
        if min_distance is not None:
            self.min_distance = min_distance
        if max_distance is not None:
            self.max_distance = max_distance
        if ignore_audio_effects is not None:
            self.ignore_audio_effects = ignore_audio_effects
        if child_limit is not None:
            self.child_limit = child_limit
        if filter_tag is not None:
            self.filter_tag = filter_tag

    @property
    def parent_under(self) -> str | None:
        """Target ID of the ParentUnder reference (targets Slot)."""
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @parent_under.setter
    def parent_under(self, target: str | Slot | None) -> None:
        """Set the ParentUnder reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ParentUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ParentUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

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
                "MinDistance", fields.FieldNullableFloat(value=value)
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
                "MaxDistance", fields.FieldNullableFloat(value=value)
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
    def play_point_mode(self) -> members.FieldEnum | None:
        """The PlayPointMode member."""
        member = self.get_member("PlayPointMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @play_point_mode.setter
    def play_point_mode(self, value: members.FieldEnum) -> None:
        """Set the PlayPointMode member."""
        self.set_member("PlayPointMode", value)

    @property
    def child_limit(self) -> np.int32 | None:
        """The ChildLimit field value."""
        member = self.get_member("ChildLimit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @child_limit.setter
    def child_limit(self, value: np.int32) -> None:
        """Set the ChildLimit field value."""
        member = self.get_member("ChildLimit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChildLimit", fields.FieldInt(value=value)
            )

    @property
    def filter_tag(self) -> str | None:
        """The FilterTag field value."""
        member = self.get_member("FilterTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @filter_tag.setter
    def filter_tag(self, value: str) -> None:
        """Set the FilterTag field value."""
        member = self.get_member("FilterTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FilterTag", fields.FieldString(value=value)
            )

    @property
    def parented_clips(self) -> members.SyncList | None:
        """The ParentedClips member."""
        member = self.get_member("ParentedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @parented_clips.setter
    def parented_clips(self, value: members.SyncList) -> None:
        """Set the ParentedClips member."""
        self.set_member("ParentedClips", value)

    @property
    def unparented_clips(self) -> members.SyncList | None:
        """The UnparentedClips member."""
        member = self.get_member("UnparentedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @unparented_clips.setter
    def unparented_clips(self, value: members.SyncList) -> None:
        """Set the UnparentedClips member."""
        self.set_member("UnparentedClips", value)

