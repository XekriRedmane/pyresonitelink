"""Generated component: ButtonPlaybackAction."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.playback_action import PlaybackAction
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iplayable import IPlayable
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonPlaybackAction(GeneratedComponent, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """The ButtonPlaybackAction component takes in an IPlayable. When an IButton is pressed while this component is in the same slot, it will set the action on this playable media depending on what is set up in this component.

    Category: Common UI/Button Interactions/Media

    Basically your media buttons (``Play``, ``Pause``, ``Resume``, and
    ``Stop``) that can be setup anywhere.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonPlaybackAction"

    def __init__(self, playback: str | IPlayable | None = None, on_hover: PlaybackAction | str | None = None, on_leave: PlaybackAction | str | None = None, on_press: PlaybackAction | str | None = None, on_release: PlaybackAction | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            playback: Initial value for Playback.
            on_hover: Initial value for OnHover.
            on_leave: Initial value for OnLeave.
            on_press: Initial value for OnPress.
            on_release: Initial value for OnRelease.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if playback is not None:
            self.playback = playback
        if on_hover is not None:
            self.on_hover = on_hover
        if on_leave is not None:
            self.on_leave = on_leave
        if on_press is not None:
            self.on_press = on_press
        if on_release is not None:
            self.on_release = on_release

    @property
    def playback(self) -> str | None:
        """The playable media itself."""
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
    def on_hover(self) -> PlaybackAction | None:
        """The action to take when the button is hovered over."""
        member = self.get_member("OnHover")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PlaybackAction(member.value)
        return None

    @on_hover.setter
    def on_hover(self, value: PlaybackAction | str) -> None:
        """Set OnHover. The action to take when the button is hovered over."""
        member = self.get_member("OnHover")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnHover",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_leave(self) -> PlaybackAction | None:
        """The action to take when the button is left."""
        member = self.get_member("OnLeave")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PlaybackAction(member.value)
        return None

    @on_leave.setter
    def on_leave(self, value: PlaybackAction | str) -> None:
        """Set OnLeave. The action to take when the button is left."""
        member = self.get_member("OnLeave")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnLeave",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_press(self) -> PlaybackAction | None:
        """The action to take when the button is pressed."""
        member = self.get_member("OnPress")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PlaybackAction(member.value)
        return None

    @on_press.setter
    def on_press(self, value: PlaybackAction | str) -> None:
        """Set OnPress. The action to take when the button is pressed."""
        member = self.get_member("OnPress")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnPress",
                members.FieldEnum(value=str(value)),
            )

    @property
    def on_release(self) -> PlaybackAction | None:
        """The action to take when the button is released."""
        member = self.get_member("OnRelease")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PlaybackAction(member.value)
        return None

    @on_release.setter
    def on_release(self, value: PlaybackAction | str) -> None:
        """Set OnRelease. The action to take when the button is released."""
        member = self.get_member("OnRelease")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OnRelease",
                members.FieldEnum(value=str(value)),
            )

