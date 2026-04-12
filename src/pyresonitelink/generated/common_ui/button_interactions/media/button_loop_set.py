"""Generated component: ButtonLoopSet."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.loop_set_options import LoopSetOptions
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonLoopSet(GeneratedComponent, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """The ButtonLoopSet component takes in an IPlayable. When an IButton is pressed while this component is in the same slot, it will set the loop on this playable media depending on what is set up in this component.

}}

    Category: Common UI/Button Interactions/Media

    Basically a loop button that can be setup anywhere.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonLoopSet"

    def __init__(self, playback: str | IPlayable | None = None, on_press: LoopSetOptions | str | None = None, on_release: LoopSetOptions | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playback: Initial value for Playback.
            on_press: Initial value for OnPress.
            on_release: Initial value for OnRelease.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playback is not None:
            self.playback = playback
        if on_press is not None:
            self.on_press = on_press
        if on_release is not None:
            self.on_release = on_release

    @property
    def playback(self) -> str | None:
        """The referenced playable media."""
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
    def on_press(self) -> LoopSetOptions | None:
        """Sets the type of loop for this media when pressed."""
        member = self.get_member("OnPress")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LoopSetOptions(member.value)
        return None

    @on_press.setter
    def on_press(self, value: LoopSetOptions | str) -> None:
        """Set OnPress. Sets the type of loop for this media when pressed."""
        member = self.get_member("OnPress")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnPress",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_release(self) -> LoopSetOptions | None:
        """Sets the type of loop for this media when released."""
        member = self.get_member("OnRelease")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return LoopSetOptions(member.value)
        return None

    @on_release.setter
    def on_release(self, value: LoopSetOptions | str) -> None:
        """Set OnRelease. Sets the type of loop for this media when released."""
        member = self.get_member("OnRelease")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnRelease",
                members.FieldEnum(value=str(value)),
            )

