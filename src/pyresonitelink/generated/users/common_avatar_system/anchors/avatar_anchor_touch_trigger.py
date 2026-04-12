"""Generated component: AvatarAnchorTouchTrigger."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.vibrate_preset import VibratePreset
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.avatar_anchor import AvatarAnchor
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarAnchorTouchTrigger(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Used often for a way of entering and exiting an Avatar Anchor when the user wants to.

    Category: Users/Common Avatar System/Anchors

    **Behavior**: This needs a collider on the same slot to allow for clicking and bringing up the prompt. The ``EnterText`` and ``ExitText`` fields are usually driven by a component. The component automatically translates the dialogues for them in their context menu to their selected locale language.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchorTouchTrigger"

    def __init__(self, anchor: str | AvatarAnchor | None = None, enter_text: primitives.String | None = None, exit_text: primitives.String | None = None, enter: primitives.Bool | None = None, exit: primitives.Bool | None = None, accept_out_of_sight_touch: primitives.Bool | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, vibrate: VibratePreset | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor: Initial value for Anchor.
            enter_text: Initial value for EnterText.
            exit_text: Initial value for ExitText.
            enter: Initial value for Enter.
            exit: Initial value for Exit.
            accept_out_of_sight_touch: Initial value for AcceptOutOfSightTouch.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            vibrate: Initial value for Vibrate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor is not None:
            self.anchor = anchor
        if enter_text is not None:
            self.enter_text = enter_text
        if exit_text is not None:
            self.exit_text = exit_text
        if enter is not None:
            self.enter = enter
        if exit is not None:
            self.exit = exit
        if accept_out_of_sight_touch is not None:
            self.accept_out_of_sight_touch = accept_out_of_sight_touch
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if vibrate is not None:
            self.vibrate = vibrate

    @property
    def anchor(self) -> str | None:
        """The anchor to enter after confirming the enter anchor."""
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor.setter
    def anchor(self, target: str | AvatarAnchor | None) -> None:
        """Set the Anchor reference by target ID or AvatarAnchor instance."""
        target_id: str | None = target.id if isinstance(target, AvatarAnchor) else target  # type: ignore[assignment]
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor'),
            )

    @property
    def enter_text(self) -> primitives.String | None:
        """The text for when the user is being prompted to enter the anchor."""
        member = self.get_member("EnterText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enter_text.setter
    def enter_text(self, value: primitives.String) -> None:
        """Set the EnterText field value."""
        member = self.get_member("EnterText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnterText", fields.FieldString(value=value)
            )

    @property
    def exit_text(self) -> primitives.String | None:
        """The text for when the user is being prompted to exit the anchor."""
        member = self.get_member("ExitText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exit_text.setter
    def exit_text(self, value: primitives.String) -> None:
        """Set the ExitText field value."""
        member = self.get_member("ExitText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExitText", fields.FieldString(value=value)
            )

    @property
    def enter(self) -> primitives.Bool | None:
        """Whether to allow this component to be used for entering the anchor."""
        member = self.get_member("Enter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enter.setter
    def enter(self, value: primitives.Bool) -> None:
        """Set the Enter field value."""
        member = self.get_member("Enter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Enter", fields.FieldBool(value=value)
            )

    @property
    def exit(self) -> primitives.Bool | None:
        """Whether to allow this component to be used for exiting the anchor."""
        member = self.get_member("Exit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exit.setter
    def exit(self, value: primitives.Bool) -> None:
        """Set the Exit field value."""
        member = self.get_member("Exit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exit", fields.FieldBool(value=value)
            )

    @property
    def accept_out_of_sight_touch(self) -> primitives.Bool | None:
        """The AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_out_of_sight_touch.setter
    def accept_out_of_sight_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptOutOfSightTouch field value."""
        member = self.get_member("AcceptOutOfSightTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptOutOfSightTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def vibrate(self) -> VibratePreset | None:
        """What kind of haptics vibration feedback to send to the user's controller when bringing up the enter or exiting prompt."""
        member = self.get_member("Vibrate")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return VibratePreset(member.value)
        return None

    @vibrate.setter
    def vibrate(self, value: VibratePreset | str) -> None:
        """Set Vibrate. What kind of haptics vibration feedback to send to the user's controller when bringing up the enter or exiting prompt."""
        member = self.get_member("Vibrate")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Vibrate",
                members.FieldEnum(value=str(value)),
            )

