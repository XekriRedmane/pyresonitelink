"""Generated component: DesktopControlDialog."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.corner import Corner
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent

if TYPE_CHECKING:
    from pyresonitelink.generated.input.desktop.desktop_interaction_relay import DesktopInteractionRelay
    from pyresonitelink.generated.uix.interaction.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopControlDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DesktopControlDialog is used to change the settings for what desktop to control and how to control it.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopControlDialog"

    def __init__(self, interaction_relay: str | DesktopInteractionRelay | None = None, index_: primitives.Int | None = None, follow_cursor: primitives.Bool | None = None, brightness: primitives.Float | None = None, opacity: primitives.Float | None = None, legacy_input_mode: primitives.Bool | None = None, button_corner: Corner | str | None = None, stream_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interaction_relay: Initial value for InteractionRelay.
            index_: Initial value for Index.
            follow_cursor: Initial value for FollowCursor.
            brightness: Initial value for Brightness.
            opacity: Initial value for Opacity.
            legacy_input_mode: Initial value for LegacyInputMode.
            button_corner: Initial value for ButtonCorner.
            stream_button: Initial value for _streamButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interaction_relay is not None:
            self.interaction_relay = interaction_relay
        if index_ is not None:
            self.index_ = index_
        if follow_cursor is not None:
            self.follow_cursor = follow_cursor
        if brightness is not None:
            self.brightness = brightness
        if opacity is not None:
            self.opacity = opacity
        if legacy_input_mode is not None:
            self.legacy_input_mode = legacy_input_mode
        if button_corner is not None:
            self.button_corner = button_corner
        if stream_button is not None:
            self.stream_button = stream_button

    @property
    def interaction_relay(self) -> str | None:
        """The relay allowing desktop interaction."""
        member = self.get_member("InteractionRelay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interaction_relay.setter
    def interaction_relay(self, target: str | DesktopInteractionRelay | None) -> None:
        """Set the InteractionRelay reference by target ID or DesktopInteractionRelay instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("InteractionRelay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InteractionRelay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DesktopInteractionRelay'),
            )

    @property
    def index_(self) -> primitives.Int | None:
        """The display to show in a multi monitor settup."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index_.setter
    def index_(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def follow_cursor(self) -> primitives.Bool | None:
        """whether the desktop cursor should follow the Resonite dash cursor when not clicking."""
        member = self.get_member("FollowCursor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @follow_cursor.setter
    def follow_cursor(self, value: primitives.Bool) -> None:
        """Set the FollowCursor field value."""
        member = self.get_member("FollowCursor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FollowCursor", fields.FieldBool(value=value)
            )

    @property
    def brightness(self) -> primitives.Float | None:
        """how bright the desktop display should be in the dash."""
        member = self.get_member("Brightness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @brightness.setter
    def brightness(self, value: primitives.Float) -> None:
        """Set the Brightness field value."""
        member = self.get_member("Brightness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Brightness", fields.FieldFloat(value=value)
            )

    @property
    def opacity(self) -> primitives.Float | None:
        """how transparent the desktop display should be in the dash."""
        member = self.get_member("Opacity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @opacity.setter
    def opacity(self, value: primitives.Float) -> None:
        """Set the Opacity field value."""
        member = self.get_member("Opacity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Opacity", fields.FieldFloat(value=value)
            )

    @property
    def legacy_input_mode(self) -> primitives.Bool | None:
        """Whether to use the legacy input system for desktop interaction."""
        member = self.get_member("LegacyInputMode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_input_mode.setter
    def legacy_input_mode(self, value: primitives.Bool) -> None:
        """Set the LegacyInputMode field value."""
        member = self.get_member("LegacyInputMode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LegacyInputMode", fields.FieldBool(value=value)
            )

    @property
    def button_corner(self) -> Corner | None:
        """The ButtonCorner enum value."""
        member = self.get_member("ButtonCorner")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Corner(member.value)
        return None

    @button_corner.setter
    def button_corner(self, value: Corner | str) -> None:
        """Set the ButtonCorner enum value."""
        member = self.get_member("ButtonCorner")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ButtonCorner",
                members.FieldEnum(value=str(value)),
            )

    @property
    def stream_button(self) -> str | None:
        """Target ID of the _streamButton reference (targets Button)."""
        member = self.get_member("_streamButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stream_button.setter
    def stream_button(self, target: str | Button | None) -> None:
        """Set the _streamButton reference by target ID or Button instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_streamButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_streamButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

