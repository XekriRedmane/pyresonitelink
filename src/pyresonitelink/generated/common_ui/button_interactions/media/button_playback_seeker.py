"""Generated component: ButtonPlaybackSeeker."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonPlaybackSeeker(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonPlaybackSeeker.

    Category: Common UI/Button Interactions/Media
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonPlaybackSeeker"

    def __init__(self, playback: str | IPlayable | None = None, vertical: bool | None = None, continuous: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playback: Initial value for Playback.
            vertical: Initial value for Vertical.
            continuous: Initial value for Continuous.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playback is not None:
            self.playback = playback
        if vertical is not None:
            self.vertical = vertical
        if continuous is not None:
            self.continuous = continuous

    @property
    def playback(self) -> str | None:
        """Target ID of the Playback reference (targets IPlayable)."""
        member = self.get_member("Playback")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @playback.setter
    def playback(self, target: str | IPlayable | None) -> None:
        """Set the Playback reference by target ID or IPlayable instance."""
        target_id: str | None = target.id if isinstance(target, IPlayable) else target  # type: ignore[assignment]
        member = self.get_member("Playback")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Playback",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IPlayable'),
            )

    @property
    def vertical(self) -> bool | None:
        """The Vertical field value."""
        member = self.get_member("Vertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical.setter
    def vertical(self, value: bool) -> None:
        """Set the Vertical field value."""
        member = self.get_member("Vertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertical", fields.FieldBool(value=value)
            )

    @property
    def continuous(self) -> bool | None:
        """The Continuous field value."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

