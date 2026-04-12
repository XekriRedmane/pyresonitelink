"""Generated component: ButtonPlaybackSeeker."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonPlaybackSeeker(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonPlaybackSeeker component takes in an IPlayable. When a user uses thier laser on an IButton that also has connections to a slider or set of values that allow it to slide, this component will determine how to interpret that interaction to the seek bar of the IPlayable media.

    Category: Common UI/Button Interactions/Media

    This just gives extra functionality or options to control your media.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonPlaybackSeeker"

    def __init__(self, playback: str | IPlayable | None = None, vertical: primitives.Bool | None = None, continuous: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """The media to seek through."""
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
    def vertical(self) -> primitives.Bool | None:
        """If true, the button will interpret the seek bar as vertical instead of horizontal."""
        member = self.get_member("Vertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical.setter
    def vertical(self, value: primitives.Bool) -> None:
        """Set the Vertical field value."""
        member = self.get_member("Vertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertical", fields.FieldBool(value=value)
            )

    @property
    def continuous(self) -> primitives.Bool | None:
        """If true, allows the user to hold down the laser on the seek bar button and have it constantly change as the laser moves around."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: primitives.Bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

