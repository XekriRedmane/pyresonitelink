"""Generated component: ContextMenuItemSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContextMenuItemSource(GeneratedComponent, IButton, IButtonPressReceiver, IButtonHoverReceiver, IWorldEventReceiver):
    """The ContextMenuItemSource component is used to add additional items to a context menu.

    Category: Radiant UI/Context Menu

    Attach to a slot, and provide a name and color. The name and color can
    also be dynamically driven using a Value Option Description Driver to
    display what the button does/did. To show up, it needs to be either
    within a Context Menu Submenu or assigned to a Root Context Menu Item as
    its Item.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContextMenuItemSource"

    def __init__(self, label: primitives.String | None = None, color: primitives.ColorX | None = None, sprite: str | IAssetProvider[Sprite] | None = None, button_enabled: primitives.Bool | None = None, allow_drag: primitives.Bool | None = None, close_menu_on_press: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            label: Initial value for Label.
            color: Initial value for Color.
            sprite: Initial value for Sprite.
            button_enabled: Initial value for ButtonEnabled.
            allow_drag: Initial value for AllowDrag.
            close_menu_on_press: Initial value for CloseMenuOnPress.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if label is not None:
            self.label = label
        if color is not None:
            self.color = color
        if sprite is not None:
            self.sprite = sprite
        if button_enabled is not None:
            self.button_enabled = button_enabled
        if allow_drag is not None:
            self.allow_drag = allow_drag
        if close_menu_on_press is not None:
            self.close_menu_on_press = close_menu_on_press

    @property
    def label(self) -> primitives.String | None:
        """The text label next to the item."""
        member = self.get_member("Label")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label.setter
    def label(self, value: primitives.String) -> None:
        """Set the Label field value."""
        member = self.get_member("Label")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Label", fields.FieldString(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The background/border color of the item."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def sprite(self) -> str | None:
        """The icon that is displayed on the item."""
        member = self.get_member("Sprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sprite.setter
    def sprite(self, target: str | IAssetProvider[Sprite] | None) -> None:
        """Set the Sprite reference by target ID or IAssetProvider[Sprite] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Sprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Sprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Sprite>'),
            )

    @property
    def button_enabled(self) -> primitives.Bool | None:
        """Whether or not the button is active. If false, it will be greyed out and unclickable."""
        member = self.get_member("ButtonEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @button_enabled.setter
    def button_enabled(self, value: primitives.Bool) -> None:
        """Set the ButtonEnabled field value."""
        member = self.get_member("ButtonEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ButtonEnabled", fields.FieldBool(value=value)
            )

    @property
    def allow_drag(self) -> primitives.Bool | None:
        """Whether or not the user can drag onto the button from the center of the context menu to click it."""
        member = self.get_member("AllowDrag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_drag.setter
    def allow_drag(self, value: primitives.Bool) -> None:
        """Set the AllowDrag field value."""
        member = self.get_member("AllowDrag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowDrag", fields.FieldBool(value=value)
            )

    @property
    def close_menu_on_press(self) -> primitives.Bool | None:
        """Whether or not the context menu should be closed after the item is pressed."""
        member = self.get_member("CloseMenuOnPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @close_menu_on_press.setter
    def close_menu_on_press(self, value: primitives.Bool) -> None:
        """Set the CloseMenuOnPress field value."""
        member = self.get_member("CloseMenuOnPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CloseMenuOnPress", fields.FieldBool(value=value)
            )

