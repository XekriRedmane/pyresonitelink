"""Generated component: PlaybackStateDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaybackStateDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The PlaybackStateDriver is a component that drives a set of booleans to whether or not certain states are currently active or not for a particular IPlayable.

    Category: Media/Utility

    Attach to a slot and provide ``Source`` any Bool provided to the other
    fields will be driven to the status of that field's status check.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlaybackStateDriver"

    def __init__(self, source: str | IPlayable | None = None, is_playing: str | IField[primitives.Bool] | None = None, is_not_playing: str | IField[primitives.Bool] | None = None, is_paused: str | IField[primitives.Bool] | None = None, is_stopped: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            is_playing: Initial value for IsPlaying.
            is_not_playing: Initial value for IsNotPlaying.
            is_paused: Initial value for IsPaused.
            is_stopped: Initial value for IsStopped.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if is_playing is not None:
            self.is_playing = is_playing
        if is_not_playing is not None:
            self.is_not_playing = is_not_playing
        if is_paused is not None:
            self.is_paused = is_paused
        if is_stopped is not None:
            self.is_stopped = is_stopped

    @property
    def source(self) -> str | None:
        """Playback source - VideoTextureProvider or Playback"""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IPlayable | None) -> None:
        """Set the Source reference by target ID or IPlayable instance."""
        target_id: str | None = target.id if isinstance(target, IPlayable) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IPlayable'),
            )

    @property
    def is_playing(self) -> str | None:
        """Will drive IField to true if playing, false if not playing"""
        member = self.get_member("IsPlaying")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_playing.setter
    def is_playing(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsPlaying reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsPlaying")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsPlaying",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def is_not_playing(self) -> str | None:
        """Will drive IField to true is not playing, false if playing"""
        member = self.get_member("IsNotPlaying")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_not_playing.setter
    def is_not_playing(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsNotPlaying reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsNotPlaying")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsNotPlaying",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def is_paused(self) -> str | None:
        """Will drive IField to true if playable is paused"""
        member = self.get_member("IsPaused")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_paused.setter
    def is_paused(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsPaused reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsPaused")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsPaused",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def is_stopped(self) -> str | None:
        """Will drive IField to true if playable is stopped"""
        member = self.get_member("IsStopped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_stopped.setter
    def is_stopped(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the IsStopped reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsStopped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsStopped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

