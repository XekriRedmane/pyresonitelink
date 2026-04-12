"""Generated component: ButtonAudioClipPlayer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonAudioClipPlayer(GeneratedComponent, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """The ButtonAudioClipPlayer plays an AudioClip from a list on press, release, and hover.

}}

}}

    Category: Common UI/Button Interactions/Media

    This is a powerful component that allows for customizability for your
    many sounds in one slot, great for boopers and UIX buttons that need to
    have a variety of sounds.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonAudioClipPlayer"

    def __init__(self, parent_under: str | Slot | None = None, min_distance: primitives.Float | None = None, max_distance: primitives.Float | None = None, ignore_audio_effects: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parent_under: Initial value for ParentUnder.
            min_distance: Initial value for MinDistance.
            max_distance: Initial value for MaxDistance.
            ignore_audio_effects: Initial value for IgnoreAudioEffects.
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

    @property
    def parent_under(self) -> str | None:
        """Parents the one shot sound under the specified slot."""
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
        """The minimum distance for this sound."""
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
        """The maximum distance for this sound."""
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
        """The rolloff for this sound."""
        member = self.get_member("RolloffMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @rolloff_mode.setter
    def rolloff_mode(self, value: members.FieldEnum) -> None:
        """Set RolloffMode. The rolloff for this sound."""
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
    def pressed_clips(self) -> members.SyncList | None:
        """The list of pressed clip sounds."""
        member = self.get_member("PressedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @pressed_clips.setter
    def pressed_clips(self, value: members.SyncList) -> None:
        """Set PressedClips. The list of pressed clip sounds."""
        self.set_member("PressedClips", value)

    @property
    def released_clips(self) -> members.SyncList | None:
        """The list of released clip sounds."""
        member = self.get_member("ReleasedClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @released_clips.setter
    def released_clips(self, value: members.SyncList) -> None:
        """Set ReleasedClips. The list of released clip sounds."""
        self.set_member("ReleasedClips", value)

    @property
    def hover_enter_clips(self) -> members.SyncList | None:
        """The list of hover enter clip sounds."""
        member = self.get_member("HoverEnterClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @hover_enter_clips.setter
    def hover_enter_clips(self, value: members.SyncList) -> None:
        """Set HoverEnterClips. The list of hover enter clip sounds."""
        self.set_member("HoverEnterClips", value)

    @property
    def hover_leave_clips(self) -> members.SyncList | None:
        """The list of hover leave clip sounds."""
        member = self.get_member("HoverLeaveClips")
        if isinstance(member, members.SyncList):
            return member
        return None

    @hover_leave_clips.setter
    def hover_leave_clips(self, value: members.SyncList) -> None:
        """Set HoverLeaveClips. The list of hover leave clip sounds."""
        self.set_member("HoverLeaveClips", value)

