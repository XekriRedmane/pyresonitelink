"""Generated component: PlaybackPositionDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PlaybackPositionDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PlaybackPositionDriver.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PlaybackPositionDriver"

    def __init__(self, target: str | IField[primitives.Float] | None = None, source: str | IPlayable | None = None, use_normalized_position: primitives.Bool | None = None, write_back: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            source: Initial value for Source.
            use_normalized_position: Initial value for UseNormalizedPosition.
            write_back: Initial value for WriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if source is not None:
            self.source = source
        if use_normalized_position is not None:
            self.use_normalized_position = use_normalized_position
        if write_back is not None:
            self.write_back = write_back

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.Float])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
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
    def write_back(self) -> primitives.Bool | None:
        """The WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

