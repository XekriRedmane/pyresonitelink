"""Generated component: DesktopController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.desktop_texture_provider import DesktopTextureProvider
from pyresonitelink.generated._types.desktop_interaction_relay import DesktopInteractionRelay
from pyresonitelink.generated._types.desktop_control_dialog import DesktopControlDialog
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DesktopController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DesktopController.

    Category: Input/Desktop
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DesktopController"

    def __init__(self, follow_cursor: primitives.Bool | None = None, legacy_input_mode: primitives.Bool | None = None, brightness: primitives.Float | None = None, opacity: primitives.Float | None = None, display_color: str | IField[primitives.ColorX] | None = None, display_rect: str | RectTransform | None = None, desktop_texture: str | DesktopTextureProvider | None = None, interaction_relay: str | DesktopInteractionRelay | None = None, current_control: str | DesktopControlDialog | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            follow_cursor: Initial value for FollowCursor.
            legacy_input_mode: Initial value for LegacyInputMode.
            brightness: Initial value for Brightness.
            opacity: Initial value for Opacity.
            display_color: Initial value for _displayColor.
            display_rect: Initial value for _displayRect.
            desktop_texture: Initial value for _desktopTexture.
            interaction_relay: Initial value for _interactionRelay.
            current_control: Initial value for _currentControl.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if follow_cursor is not None:
            self.follow_cursor = follow_cursor
        if legacy_input_mode is not None:
            self.legacy_input_mode = legacy_input_mode
        if brightness is not None:
            self.brightness = brightness
        if opacity is not None:
            self.opacity = opacity
        if display_color is not None:
            self.display_color = display_color
        if display_rect is not None:
            self.display_rect = display_rect
        if desktop_texture is not None:
            self.desktop_texture = desktop_texture
        if interaction_relay is not None:
            self.interaction_relay = interaction_relay
        if current_control is not None:
            self.current_control = current_control

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
    def display_color(self) -> str | None:
        """Target ID of the _displayColor reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_displayColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_color.setter
    def display_color(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _displayColor reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_displayColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_displayColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def display_rect(self) -> str | None:
        """Target ID of the _displayRect reference (targets RectTransform)."""
        member = self.get_member("_displayRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @display_rect.setter
    def display_rect(self, target: str | RectTransform | None) -> None:
        """Set the _displayRect reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_displayRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_displayRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def desktop_texture(self) -> str | None:
        """Target ID of the _desktopTexture reference (targets DesktopTextureProvider)."""
        member = self.get_member("_desktopTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @desktop_texture.setter
    def desktop_texture(self, target: str | DesktopTextureProvider | None) -> None:
        """Set the _desktopTexture reference by target ID or DesktopTextureProvider instance."""
        target_id: str | None = target.id if isinstance(target, DesktopTextureProvider) else target  # type: ignore[assignment]
        member = self.get_member("_desktopTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_desktopTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DesktopTextureProvider'),
            )

    @property
    def interaction_relay(self) -> str | None:
        """Target ID of the _interactionRelay reference (targets DesktopInteractionRelay)."""
        member = self.get_member("_interactionRelay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interaction_relay.setter
    def interaction_relay(self, target: str | DesktopInteractionRelay | None) -> None:
        """Set the _interactionRelay reference by target ID or DesktopInteractionRelay instance."""
        target_id: str | None = target.id if isinstance(target, DesktopInteractionRelay) else target  # type: ignore[assignment]
        member = self.get_member("_interactionRelay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_interactionRelay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DesktopInteractionRelay'),
            )

    @property
    def current_control(self) -> str | None:
        """Target ID of the _currentControl reference (targets DesktopControlDialog)."""
        member = self.get_member("_currentControl")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_control.setter
    def current_control(self, target: str | DesktopControlDialog | None) -> None:
        """Set the _currentControl reference by target ID or DesktopControlDialog instance."""
        target_id: str | None = target.id if isinstance(target, DesktopControlDialog) else target  # type: ignore[assignment]
        member = self.get_member("_currentControl")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentControl",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DesktopControlDialog'),
            )

