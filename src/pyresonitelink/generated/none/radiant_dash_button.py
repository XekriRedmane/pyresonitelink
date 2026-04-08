"""Generated component: RadiantDashButton."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.radiant_dash import RadiantDash
from pyresonitelink.generated._types.radiant_dash_screen import RadiantDashScreen
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.layout_element import LayoutElement
from pyresonitelink.generated._types.rect_transform import RectTransform
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadiantDashButton(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RadiantDashButton.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadiantDashButton"

    def __init__(self, dash: str | RadiantDash | None = None, screen: str | RadiantDashScreen | None = None, switching_enabled: str | IField[primitives.Bool] | None = None, screen_enabled: str | IField[primitives.Bool] | None = None, current_screen: str | SyncRef[RadiantDashScreen] | None = None, button: str | Button | None = None, text: str | Text | None = None, text_bg: str | Image | None = None, icon: str | Image | None = None, layout: str | LayoutElement | None = None, root_rect: str | RectTransform | None = None, icon_rect: str | RectTransform | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            dash: Initial value for Dash.
            screen: Initial value for Screen.
            switching_enabled: Initial value for _switchingEnabled.
            screen_enabled: Initial value for _screenEnabled.
            current_screen: Initial value for _currentScreen.
            button: Initial value for _button.
            text: Initial value for _text.
            text_bg: Initial value for _textBg.
            icon: Initial value for _icon.
            layout: Initial value for _layout.
            root_rect: Initial value for _rootRect.
            icon_rect: Initial value for _iconRect.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if dash is not None:
            self.dash = dash
        if screen is not None:
            self.screen = screen
        if switching_enabled is not None:
            self.switching_enabled = switching_enabled
        if screen_enabled is not None:
            self.screen_enabled = screen_enabled
        if current_screen is not None:
            self.current_screen = current_screen
        if button is not None:
            self.button = button
        if text is not None:
            self.text = text
        if text_bg is not None:
            self.text_bg = text_bg
        if icon is not None:
            self.icon = icon
        if layout is not None:
            self.layout = layout
        if root_rect is not None:
            self.root_rect = root_rect
        if icon_rect is not None:
            self.icon_rect = icon_rect

    @property
    def dash(self) -> str | None:
        """Target ID of the Dash reference (targets RadiantDash)."""
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash.setter
    def dash(self, target: str | RadiantDash | None) -> None:
        """Set the Dash reference by target ID or RadiantDash instance."""
        target_id: str | None = target.id if isinstance(target, RadiantDash) else target  # type: ignore[assignment]
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dash",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantDash'),
            )

    @property
    def screen(self) -> str | None:
        """Target ID of the Screen reference (targets RadiantDashScreen)."""
        member = self.get_member("Screen")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen.setter
    def screen(self, target: str | RadiantDashScreen | None) -> None:
        """Set the Screen reference by target ID or RadiantDashScreen instance."""
        target_id: str | None = target.id if isinstance(target, RadiantDashScreen) else target  # type: ignore[assignment]
        member = self.get_member("Screen")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Screen",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantDashScreen'),
            )

    @property
    def switching_enabled(self) -> str | None:
        """Target ID of the _switchingEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_switchingEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @switching_enabled.setter
    def switching_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _switchingEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_switchingEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_switchingEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def screen_enabled(self) -> str | None:
        """Target ID of the _screenEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_screenEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_enabled.setter
    def screen_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _screenEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_screenEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def current_screen(self) -> str | None:
        """Target ID of the _currentScreen reference (targets SyncRef[RadiantDashScreen])."""
        member = self.get_member("_currentScreen")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_screen.setter
    def current_screen(self, target: str | SyncRef[RadiantDashScreen] | None) -> None:
        """Set the _currentScreen reference by target ID or SyncRef[RadiantDashScreen] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("_currentScreen")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentScreen",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<[FrooxEngine]FrooxEngine.RadiantDashScreen>'),
            )

    @property
    def button(self) -> str | None:
        """Target ID of the _button reference (targets Button)."""
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button.setter
    def button(self, target: str | Button | None) -> None:
        """Set the _button reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def text(self) -> str | None:
        """Target ID of the _text reference (targets Text)."""
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | Text | None) -> None:
        """Set the _text reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def text_bg(self) -> str | None:
        """Target ID of the _textBg reference (targets Image)."""
        member = self.get_member("_textBg")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_bg.setter
    def text_bg(self, target: str | Image | None) -> None:
        """Set the _textBg reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_textBg")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textBg",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def icon(self) -> str | None:
        """Target ID of the _icon reference (targets Image)."""
        member = self.get_member("_icon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon.setter
    def icon(self, target: str | Image | None) -> None:
        """Set the _icon reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_icon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_icon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def layout(self) -> str | None:
        """Target ID of the _layout reference (targets LayoutElement)."""
        member = self.get_member("_layout")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @layout.setter
    def layout(self, target: str | LayoutElement | None) -> None:
        """Set the _layout reference by target ID or LayoutElement instance."""
        target_id: str | None = target.id if isinstance(target, LayoutElement) else target  # type: ignore[assignment]
        member = self.get_member("_layout")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_layout",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.LayoutElement'),
            )

    @property
    def root_rect(self) -> str | None:
        """Target ID of the _rootRect reference (targets RectTransform)."""
        member = self.get_member("_rootRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_rect.setter
    def root_rect(self, target: str | RectTransform | None) -> None:
        """Set the _rootRect reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_rootRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rootRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

    @property
    def icon_rect(self) -> str | None:
        """Target ID of the _iconRect reference (targets RectTransform)."""
        member = self.get_member("_iconRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon_rect.setter
    def icon_rect(self, target: str | RectTransform | None) -> None:
        """Set the _iconRect reference by target ID or RectTransform instance."""
        target_id: str | None = target.id if isinstance(target, RectTransform) else target  # type: ignore[assignment]
        member = self.get_member("_iconRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_iconRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.RectTransform'),
            )

