"""Generated component: TwitchChatDialog."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.legacy_panel import LegacyPanel
from pyresonitelink.generated._types.twitch_interface import TwitchInterface
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.scroll_rect import ScrollRect
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.dynamic_sprite_font import DynamicSpriteFont
from pyresonitelink.generated._types.font_collection import FontCollection
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TwitchChatDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TwitchChatDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TwitchChatDialog"

    def __init__(self, canvas: str | Canvas | None = None, panel: str | LegacyPanel | None = None, max_messages: np.int32 | None = None, interface: str | TwitchInterface | None = None, channel_name: str | TextField | None = None, viewer_count: str | Text | None = None, messages_root: str | Slot | None = None, messages_scroll_rect: str | ScrollRect | None = None, highlight_panel: str | Image | None = None, highlight_text: str | Text | None = None, sprite_sheet: str | DynamicSpriteFont | None = None, font_collection: str | FontCollection | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            canvas: Initial value for _canvas.
            panel: Initial value for _panel.
            max_messages: Initial value for MaxMessages.
            interface: Initial value for Interface.
            channel_name: Initial value for _channelName.
            viewer_count: Initial value for _viewerCount.
            messages_root: Initial value for _messagesRoot.
            messages_scroll_rect: Initial value for _messagesScrollRect.
            highlight_panel: Initial value for _highlightPanel.
            highlight_text: Initial value for _highlightText.
            sprite_sheet: Initial value for _spriteSheet.
            font_collection: Initial value for _fontCollection.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if canvas is not None:
            self.canvas = canvas
        if panel is not None:
            self.panel = panel
        if max_messages is not None:
            self.max_messages = max_messages
        if interface is not None:
            self.interface = interface
        if channel_name is not None:
            self.channel_name = channel_name
        if viewer_count is not None:
            self.viewer_count = viewer_count
        if messages_root is not None:
            self.messages_root = messages_root
        if messages_scroll_rect is not None:
            self.messages_scroll_rect = messages_scroll_rect
        if highlight_panel is not None:
            self.highlight_panel = highlight_panel
        if highlight_text is not None:
            self.highlight_text = highlight_text
        if sprite_sheet is not None:
            self.sprite_sheet = sprite_sheet
        if font_collection is not None:
            self.font_collection = font_collection

    @property
    def canvas(self) -> str | None:
        """Target ID of the _canvas reference (targets Canvas)."""
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @canvas.setter
    def canvas(self, target: str | Canvas | None) -> None:
        """Set the _canvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_canvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_canvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def panel(self) -> str | None:
        """Target ID of the _panel reference (targets LegacyPanel)."""
        member = self.get_member("_panel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panel.setter
    def panel(self, target: str | LegacyPanel | None) -> None:
        """Set the _panel reference by target ID or LegacyPanel instance."""
        target_id: str | None = target.id if isinstance(target, LegacyPanel) else target  # type: ignore[assignment]
        member = self.get_member("_panel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_panel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyPanel'),
            )

    @property
    def max_messages(self) -> np.int32 | None:
        """The MaxMessages field value."""
        member = self.get_member("MaxMessages")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_messages.setter
    def max_messages(self, value: np.int32) -> None:
        """Set the MaxMessages field value."""
        member = self.get_member("MaxMessages")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxMessages", fields.FieldInt(value=value)
            )

    @property
    def interface(self) -> str | None:
        """Target ID of the Interface reference (targets TwitchInterface)."""
        member = self.get_member("Interface")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @interface.setter
    def interface(self, target: str | TwitchInterface | None) -> None:
        """Set the Interface reference by target ID or TwitchInterface instance."""
        target_id: str | None = target.id if isinstance(target, TwitchInterface) else target  # type: ignore[assignment]
        member = self.get_member("Interface")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Interface",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TwitchInterface'),
            )

    @property
    def channel_name(self) -> str | None:
        """Target ID of the _channelName reference (targets TextField)."""
        member = self.get_member("_channelName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @channel_name.setter
    def channel_name(self, target: str | TextField | None) -> None:
        """Set the _channelName reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_channelName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_channelName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def viewer_count(self) -> str | None:
        """Target ID of the _viewerCount reference (targets Text)."""
        member = self.get_member("_viewerCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @viewer_count.setter
    def viewer_count(self, target: str | Text | None) -> None:
        """Set the _viewerCount reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_viewerCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_viewerCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def messages_root(self) -> str | None:
        """Target ID of the _messagesRoot reference (targets Slot)."""
        member = self.get_member("_messagesRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @messages_root.setter
    def messages_root(self, target: str | Slot | None) -> None:
        """Set the _messagesRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_messagesRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_messagesRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def messages_scroll_rect(self) -> str | None:
        """Target ID of the _messagesScrollRect reference (targets ScrollRect)."""
        member = self.get_member("_messagesScrollRect")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @messages_scroll_rect.setter
    def messages_scroll_rect(self, target: str | ScrollRect | None) -> None:
        """Set the _messagesScrollRect reference by target ID or ScrollRect instance."""
        target_id: str | None = target.id if isinstance(target, ScrollRect) else target  # type: ignore[assignment]
        member = self.get_member("_messagesScrollRect")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_messagesScrollRect",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.ScrollRect'),
            )

    @property
    def highlight_panel(self) -> str | None:
        """Target ID of the _highlightPanel reference (targets Image)."""
        member = self.get_member("_highlightPanel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @highlight_panel.setter
    def highlight_panel(self, target: str | Image | None) -> None:
        """Set the _highlightPanel reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_highlightPanel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_highlightPanel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def highlight_text(self) -> str | None:
        """Target ID of the _highlightText reference (targets Text)."""
        member = self.get_member("_highlightText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @highlight_text.setter
    def highlight_text(self, target: str | Text | None) -> None:
        """Set the _highlightText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_highlightText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_highlightText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def sprite_sheet(self) -> str | None:
        """Target ID of the _spriteSheet reference (targets DynamicSpriteFont)."""
        member = self.get_member("_spriteSheet")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite_sheet.setter
    def sprite_sheet(self, target: str | DynamicSpriteFont | None) -> None:
        """Set the _spriteSheet reference by target ID or DynamicSpriteFont instance."""
        target_id: str | None = target.id if isinstance(target, DynamicSpriteFont) else target  # type: ignore[assignment]
        member = self.get_member("_spriteSheet")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_spriteSheet",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.DynamicSpriteFont'),
            )

    @property
    def font_collection(self) -> str | None:
        """Target ID of the _fontCollection reference (targets FontCollection)."""
        member = self.get_member("_fontCollection")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font_collection.setter
    def font_collection(self, target: str | FontCollection | None) -> None:
        """Set the _fontCollection reference by target ID or FontCollection instance."""
        target_id: str | None = target.id if isinstance(target, FontCollection) else target  # type: ignore[assignment]
        member = self.get_member("_fontCollection")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_fontCollection",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FontCollection'),
            )

