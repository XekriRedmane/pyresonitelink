"""Generated component: HoverPlayback."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_playback import SyncPlayback
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HoverPlayback(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HoverPlayback.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HoverPlayback"

    def __init__(self, target: str | SyncPlayback | None = None, from_beginning: primitives.Bool | None = None, loop: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            from_beginning: Initial value for FromBeginning.
            loop: Initial value for Loop.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if from_beginning is not None:
            self.from_beginning = from_beginning
        if loop is not None:
            self.loop = loop

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
    def trigger(self) -> members.FieldEnum | None:
        """The Trigger member."""
        member = self.get_member("Trigger")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @trigger.setter
    def trigger(self, value: members.FieldEnum) -> None:
        """Set the Trigger member."""
        self.set_member("Trigger", value)

    @property
    def from_beginning(self) -> primitives.Bool | None:
        """The FromBeginning field value."""
        member = self.get_member("FromBeginning")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @from_beginning.setter
    def from_beginning(self, value: primitives.Bool) -> None:
        """Set the FromBeginning field value."""
        member = self.get_member("FromBeginning")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FromBeginning", fields.FieldBool(value=value)
            )

    @property
    def loop(self) -> primitives.Bool | None:
        """The Loop field value."""
        member = self.get_member("Loop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @loop.setter
    def loop(self, value: primitives.Bool) -> None:
        """Set the Loop field value."""
        member = self.get_member("Loop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Loop", fields.FieldBool(value=value)
            )

