"""Generated component: ButtonLoopSet."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonLoopSet(GeneratedComponent, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonLoopSet.

    Category: Common UI/Button Interactions/Media
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonLoopSet"

    def __init__(self, playback: str | IPlayable | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playback: Initial value for Playback.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playback is not None:
            self.playback = playback

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
    def on_press(self) -> members.FieldEnum | None:
        """The OnPress member."""
        member = self.get_member("OnPress")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_press.setter
    def on_press(self, value: members.FieldEnum) -> None:
        """Set the OnPress member."""
        self.set_member("OnPress", value)

    @property
    def on_release(self) -> members.FieldEnum | None:
        """The OnRelease member."""
        member = self.get_member("OnRelease")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @on_release.setter
    def on_release(self, value: members.FieldEnum) -> None:
        """Set the OnRelease member."""
        self.set_member("OnRelease", value)

