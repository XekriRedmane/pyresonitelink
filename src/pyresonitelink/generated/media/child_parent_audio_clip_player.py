"""Generated component: ChildParentAudioClipPlayer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.point_mode import PointMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ChildParentAudioClipPlayer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ChildParentAudioClipPlayer component plays specified audio clips when it's immediate children are added to or removed from.

    Category: Media
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ChildParentAudioClipPlayer"

    def __init__(self, parent_under: str | Slot | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, ignore_audio_effects: primitives.Bool | None = None, play_point_mode: PointMode | str | None = None, child_limit: primitives.Int | None = None, filter_tag: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_under: Initial value for ParentUnder.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            ignore_audio_effects: Initial value for IgnoreAudioEffects.
            play_point_mode: Initial value for PlayPointMode.
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
        if play_point_mode is not None:
            self.play_point_mode = play_point_mode
        if child_limit is not None:
            self.child_limit = child_limit
        if filter_tag is not None:
            self.filter_tag = filter_tag

    @property
    def parent_under(self) -> str | None:
        """Where to parent the slots to when playing sounds. (DON'T SET THIS TO THE SLOT THIS COMPONENT IS ON. else it will spam audio every game tick)"""
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
    def min_distance(self) -> primitives.Float | None:
        """The override for all ClipDatas Min Distance when they are played."""
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
                "MinDistance", fields.FieldNullableFloat(value=value)
            )

    @property
    def max_distance(self) -> primitives.Float | None:
        """The override for all ClipDatas Max Distance when they are played."""
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
                "MaxDistance", fields.FieldNullableFloat(value=value)
            )

    @property
    def rolloff_mode(self) -> members.FieldEnum | None:
        """The override for all ClipDatas Rolloff Mode when they are played."""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rolloff_mode.setter
    def rolloff_mode(self, value: members.FieldEnum) -> None:
        """Set RolloffMode. The override for all ClipDatas Rolloff Mode when they are played."""
        self.set_member("RolloffMode", value)

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
    def play_point_mode(self) -> PointMode | None:
        """Where to position audio clips when they are played."""
        member = self.get_member("PlayPointMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PointMode(member.value)
        return None

    @play_point_mode.setter
    def play_point_mode(self, value: PointMode | str) -> None:
        """Set PlayPointMode. Where to position audio clips when they are played."""
        member = self.get_member("PlayPointMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "PlayPointMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def child_limit(self) -> primitives.Int | None:
        """If the immediate children count of this component's slot is above this amount, it will not play sounds."""
        member = self.get_member("ChildLimit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @child_limit.setter
    def child_limit(self, value: primitives.Int) -> None:
        """Set the ChildLimit field value."""
        member = self.get_member("ChildLimit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChildLimit", fields.FieldInt(value=value)
            )

    @property
    def filter_tag(self) -> primitives.String | None:
        """If an added or removed immediate child has a tag that matches this value, a sound will not be played."""
        member = self.get_member("FilterTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @filter_tag.setter
    def filter_tag(self, value: primitives.String) -> None:
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
        """A list of audio clips to play when a slot is added to the immediate children of this component's slot."""
        member = self.get_member("ParentedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @parented_clips.setter
    def parented_clips(self, value: members.SyncList) -> None:
        """Set ParentedClips. A list of audio clips to play when a slot is added to the immediate children of this component's slot."""
        self.set_member("ParentedClips", value)

    @property
    def unparented_clips(self) -> members.SyncList | None:
        """A list of audio clips to play when a slot is removed from the immediate children of this component's slot."""
        member = self.get_member("UnparentedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @unparented_clips.setter
    def unparented_clips(self, value: members.SyncList) -> None:
        """Set UnparentedClips. A list of audio clips to play when a slot is removed from the immediate children of this component's slot."""
        self.set_member("UnparentedClips", value)

