"""Generated component: PlaybackStateDriver."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaybackStateDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PlaybackStateDriver.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlaybackStateDriver"

    def __init__(self, source: str | IPlayable | None = None, is_playing: str | IField[bool] | None = None, is_not_playing: str | IField[bool] | None = None, is_paused: str | IField[bool] | None = None, is_stopped: str | IField[bool] | None = None, *, component: workers.Component | None = None) -> None:
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
        """Target ID of the Source reference (targets IPlayable)."""
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
        """Target ID of the IsPlaying reference (targets IField[bool])."""
        member = self.get_member("IsPlaying")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_playing.setter
    def is_playing(self, target: str | IField[bool] | None) -> None:
        """Set the IsPlaying reference by target ID or IField[bool] instance."""
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
        """Target ID of the IsNotPlaying reference (targets IField[bool])."""
        member = self.get_member("IsNotPlaying")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_not_playing.setter
    def is_not_playing(self, target: str | IField[bool] | None) -> None:
        """Set the IsNotPlaying reference by target ID or IField[bool] instance."""
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
        """Target ID of the IsPaused reference (targets IField[bool])."""
        member = self.get_member("IsPaused")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_paused.setter
    def is_paused(self, target: str | IField[bool] | None) -> None:
        """Set the IsPaused reference by target ID or IField[bool] instance."""
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
        """Target ID of the IsStopped reference (targets IField[bool])."""
        member = self.get_member("IsStopped")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_stopped.setter
    def is_stopped(self, target: str | IField[bool] | None) -> None:
        """Set the IsStopped reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("IsStopped")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsStopped",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

