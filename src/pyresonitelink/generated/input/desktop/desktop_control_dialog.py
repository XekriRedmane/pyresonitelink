"""Generated component: DesktopControlDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.desktop_interaction_relay import DesktopInteractionRelay
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopControlDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DesktopControlDialog.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopControlDialog"

    def __init__(self, interaction_relay: str | DesktopInteractionRelay | None = None, index: primitives.Int | None = None, follow_cursor: primitives.Bool | None = None, brightness: primitives.Float | None = None, opacity: primitives.Float | None = None, legacy_input_mode: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            interaction_relay: Initial value for InteractionRelay.
            index: Initial value for Index.
            follow_cursor: Initial value for FollowCursor.
            brightness: Initial value for Brightness.
            opacity: Initial value for Opacity.
            legacy_input_mode: Initial value for LegacyInputMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if interaction_relay is not None:
            self.interaction_relay = interaction_relay
        if index is not None:
            self.index = index
        if follow_cursor is not None:
            self.follow_cursor = follow_cursor
        if brightness is not None:
            self.brightness = brightness
        if opacity is not None:
            self.opacity = opacity
        if legacy_input_mode is not None:
            self.legacy_input_mode = legacy_input_mode

    @property
    def interaction_relay(self) -> str | None:
        """Target ID of the InteractionRelay reference (targets DesktopInteractionRelay)."""
        member = self.get_member("InteractionRelay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interaction_relay.setter
    def interaction_relay(self, target: str | DesktopInteractionRelay | None) -> None:
        """Set the InteractionRelay reference by target ID or DesktopInteractionRelay instance."""
        target_id: str | None = target.id if isinstance(target, DesktopInteractionRelay) else target  # type: ignore[assignment]
        member = self.get_member("InteractionRelay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InteractionRelay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DesktopInteractionRelay'),
            )

    @property
    def index(self) -> primitives.Int | None:
        """The Index field value."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: primitives.Int) -> None:
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
        """The FollowCursor field value."""
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
        """The Brightness field value."""
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
        """The Opacity field value."""
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
        """The LegacyInputMode field value."""
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

