"""Generated component: PlaybackSynchronizer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_playback import SyncPlayback
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaybackSynchronizer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PlaybackSynchronizer.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlaybackSynchronizer"

    def __init__(self, target: str | SyncPlayback | None = None, source: str | IPlayable | None = None, use_normalized_position: primitives.Bool | None = None, position_offset: primitives.Float | None = None, position_rate: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            source: Initial value for Source.
            use_normalized_position: Initial value for UseNormalizedPosition.
            position_offset: Initial value for PositionOffset.
            position_rate: Initial value for PositionRate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if source is not None:
            self.source = source
        if use_normalized_position is not None:
            self.use_normalized_position = use_normalized_position
        if position_offset is not None:
            self.position_offset = position_offset
        if position_rate is not None:
            self.position_rate = position_rate

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets SyncPlayback)."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncPlayback | None) -> None:
        """Set the Target reference by target ID or SyncPlayback instance."""
        target_id: str | None = target.id if isinstance(target, SyncPlayback) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncPlayback'),
            )

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
    def use_normalized_position(self) -> primitives.Bool | None:
        """The UseNormalizedPosition field value."""
        member = self.get_member("UseNormalizedPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_normalized_position.setter
    def use_normalized_position(self, value: primitives.Bool) -> None:
        """Set the UseNormalizedPosition field value."""
        member = self.get_member("UseNormalizedPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseNormalizedPosition", fields.FieldBool(value=value)
            )

    @property
    def position_offset(self) -> primitives.Float | None:
        """The PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_offset.setter
    def position_offset(self, value: primitives.Float) -> None:
        """Set the PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOffset", fields.FieldFloat(value=value)
            )

    @property
    def position_rate(self) -> primitives.Float | None:
        """The PositionRate field value."""
        member = self.get_member("PositionRate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_rate.setter
    def position_rate(self, value: primitives.Float) -> None:
        """Set the PositionRate field value."""
        member = self.get_member("PositionRate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionRate", fields.FieldFloat(value=value)
            )

