"""Generated component: ContextMenuItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.sprite import Sprite
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.context_menu import ContextMenu
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.ibutton_hover_receiver import IButtonHoverReceiver
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ContextMenuItem(GeneratedComponent, IButtonHoverReceiver, IButtonPressReceiver, IWorldEventReceiver):
    """A component that is used internally within context menus. If you want to create a custom context menu, you should look at ContextMenuItemSource.

    Category: Radiant UI/Context Menu
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ContextMenuItem"

    def __init__(self, highlight: primitives.Bool | None = None, icon: str | Image | None = None, sprite: str | IAssetProvider[Sprite] | None = None, label: str | IField[primitives.String] | None = None, color: primitives.ColorX | None = None, menu: str | ContextMenu | None = None, highlighted: primitives.Bool | None = None, arc: str | IField[primitives.Float] | None = None, outer_radius: str | IField[primitives.Float] | None = None, button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            highlight: Initial value for Highlight.
            icon: Initial value for Icon.
            sprite: Initial value for Sprite.
            label: Initial value for Label.
            color: Initial value for Color.
            menu: Initial value for _menu.
            highlighted: Initial value for _highlighted.
            arc: Initial value for _arc.
            outer_radius: Initial value for _outerRadius.
            button: Initial value for _button.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if highlight is not None:
            self.highlight = highlight
        if icon is not None:
            self.icon = icon
        if sprite is not None:
            self.sprite = sprite
        if label is not None:
            self.label = label
        if color is not None:
            self.color = color
        if menu is not None:
            self.menu = menu
        if highlighted is not None:
            self.highlighted = highlighted
        if arc is not None:
            self.arc = arc
        if outer_radius is not None:
            self.outer_radius = outer_radius
        if button is not None:
            self.button = button

    @property
    def highlight(self) -> primitives.Bool | None:
        """Set and unset whether the item is being hovered over and should be highlighted."""
        member = self.get_member("Highlight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlight.setter
    def highlight(self, value: primitives.Bool) -> None:
        """Set the Highlight field value."""
        member = self.get_member("Highlight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Highlight", fields.FieldBool(value=value)
            )

    @property
    def icon(self) -> str | None:
        """The icon of this item."""
        member = self.get_member("Icon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon.setter
    def icon(self, target: str | Image | None) -> None:
        """Set the Icon reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("Icon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Icon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def sprite(self) -> str | None:
        """The sprite of this item."""
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
    def label(self) -> str | None:
        """The label element of this item."""
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the Label reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Label")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Label",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The color of this item."""
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
    def menu(self) -> str | None:
        """This item's origin context menu."""
        member = self.get_member("_menu")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @menu.setter
    def menu(self, target: str | ContextMenu | None) -> None:
        """Set the _menu reference by target ID or ContextMenu instance."""
        target_id: str | None = target.id if isinstance(target, ContextMenu) else target  # type: ignore[assignment]
        member = self.get_member("_menu")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_menu",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ContextMenu'),
            )

    @property
    def highlighted(self) -> primitives.Bool | None:
        """The item is being hovered over."""
        member = self.get_member("_highlighted")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlighted.setter
    def highlighted(self, value: primitives.Bool) -> None:
        """Set the _highlighted field value."""
        member = self.get_member("_highlighted")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_highlighted", fields.FieldBool(value=value)
            )

    @property
    def arc(self) -> str | None:
        """The arc that makes up this item."""
        member = self.get_member("_arc")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arc.setter
    def arc(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _arc reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arc")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arc",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def outer_radius(self) -> str | None:
        """The field that specifies the outer radius of this item."""
        member = self.get_member("_outerRadius")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outer_radius.setter
    def outer_radius(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _outerRadius reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_outerRadius")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_outerRadius",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def button(self) -> str | None:
        """The button that makes up this item."""
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

