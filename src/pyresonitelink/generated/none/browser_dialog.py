"""Generated component: BrowserDialog."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.browser_item import BrowserItem
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.grid_layout import GridLayout
from pyresonitelink.generated._types.sprite_provider import SpriteProvider
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BrowserDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BrowserDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BrowserDialog"

    def __init__(self, selected_item: str | BrowserItem | None = None, previous_selected_item: str | BrowserItem | None = None, allow_select: bool | None = None, item_size: np.float32 | None = None, selected_text: str | Text | None = None, path_root: str | Slot | None = None, buttons_root: str | Slot | None = None, folder_grid: str | GridLayout | None = None, item_grid: str | GridLayout | None = None, tab_sprite: str | SpriteProvider | None = None, loading_indicator: str | Slot | None = None, swapper: str | SlideSwapRegion | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selected_item: Initial value for SelectedItem.
            previous_selected_item: Initial value for _previousSelectedItem.
            allow_select: Initial value for AllowSelect.
            item_size: Initial value for ItemSize.
            selected_text: Initial value for _selectedText.
            path_root: Initial value for _pathRoot.
            buttons_root: Initial value for _buttonsRoot.
            folder_grid: Initial value for _folderGrid.
            item_grid: Initial value for _itemGrid.
            tab_sprite: Initial value for _tabSprite.
            loading_indicator: Initial value for _loadingIndicator.
            swapper: Initial value for _swapper.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selected_item is not None:
            self.selected_item = selected_item
        if previous_selected_item is not None:
            self.previous_selected_item = previous_selected_item
        if allow_select is not None:
            self.allow_select = allow_select
        if item_size is not None:
            self.item_size = item_size
        if selected_text is not None:
            self.selected_text = selected_text
        if path_root is not None:
            self.path_root = path_root
        if buttons_root is not None:
            self.buttons_root = buttons_root
        if folder_grid is not None:
            self.folder_grid = folder_grid
        if item_grid is not None:
            self.item_grid = item_grid
        if tab_sprite is not None:
            self.tab_sprite = tab_sprite
        if loading_indicator is not None:
            self.loading_indicator = loading_indicator
        if swapper is not None:
            self.swapper = swapper

    @property
    def selected_item(self) -> str | None:
        """Target ID of the SelectedItem reference (targets BrowserItem)."""
        member = self.get_member("SelectedItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_item.setter
    def selected_item(self, target: str | BrowserItem | None) -> None:
        """Set the SelectedItem reference by target ID or BrowserItem instance."""
        target_id: str | None = target.id if isinstance(target, BrowserItem) else target  # type: ignore[assignment]
        member = self.get_member("SelectedItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SelectedItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BrowserItem'),
            )

    @property
    def previous_selected_item(self) -> str | None:
        """Target ID of the _previousSelectedItem reference (targets BrowserItem)."""
        member = self.get_member("_previousSelectedItem")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @previous_selected_item.setter
    def previous_selected_item(self, target: str | BrowserItem | None) -> None:
        """Set the _previousSelectedItem reference by target ID or BrowserItem instance."""
        target_id: str | None = target.id if isinstance(target, BrowserItem) else target  # type: ignore[assignment]
        member = self.get_member("_previousSelectedItem")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previousSelectedItem",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BrowserItem'),
            )

    @property
    def allow_select(self) -> bool | None:
        """The AllowSelect field value."""
        member = self.get_member("AllowSelect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_select.setter
    def allow_select(self, value: bool) -> None:
        """Set the AllowSelect field value."""
        member = self.get_member("AllowSelect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSelect", fields.FieldBool(value=value)
            )

    @property
    def item_size(self) -> np.float32 | None:
        """The ItemSize field value."""
        member = self.get_member("ItemSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @item_size.setter
    def item_size(self, value: np.float32) -> None:
        """Set the ItemSize field value."""
        member = self.get_member("ItemSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ItemSize", fields.FieldFloat(value=value)
            )

    @property
    def selected_text(self) -> str | None:
        """Target ID of the _selectedText reference (targets Text)."""
        member = self.get_member("_selectedText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_text.setter
    def selected_text(self, target: str | Text | None) -> None:
        """Set the _selectedText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_selectedText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selectedText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def path_root(self) -> str | None:
        """Target ID of the _pathRoot reference (targets Slot)."""
        member = self.get_member("_pathRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path_root.setter
    def path_root(self, target: str | Slot | None) -> None:
        """Set the _pathRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_pathRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pathRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def buttons_root(self) -> str | None:
        """Target ID of the _buttonsRoot reference (targets Slot)."""
        member = self.get_member("_buttonsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_root.setter
    def buttons_root(self, target: str | Slot | None) -> None:
        """Set the _buttonsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def folder_grid(self) -> str | None:
        """Target ID of the _folderGrid reference (targets GridLayout)."""
        member = self.get_member("_folderGrid")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @folder_grid.setter
    def folder_grid(self, target: str | GridLayout | None) -> None:
        """Set the _folderGrid reference by target ID or GridLayout instance."""
        target_id: str | None = target.id if isinstance(target, GridLayout) else target  # type: ignore[assignment]
        member = self.get_member("_folderGrid")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_folderGrid",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.GridLayout'),
            )

    @property
    def item_grid(self) -> str | None:
        """Target ID of the _itemGrid reference (targets GridLayout)."""
        member = self.get_member("_itemGrid")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_grid.setter
    def item_grid(self, target: str | GridLayout | None) -> None:
        """Set the _itemGrid reference by target ID or GridLayout instance."""
        target_id: str | None = target.id if isinstance(target, GridLayout) else target  # type: ignore[assignment]
        member = self.get_member("_itemGrid")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_itemGrid",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.GridLayout'),
            )

    @property
    def tab_sprite(self) -> str | None:
        """Target ID of the _tabSprite reference (targets SpriteProvider)."""
        member = self.get_member("_tabSprite")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tab_sprite.setter
    def tab_sprite(self, target: str | SpriteProvider | None) -> None:
        """Set the _tabSprite reference by target ID or SpriteProvider instance."""
        target_id: str | None = target.id if isinstance(target, SpriteProvider) else target  # type: ignore[assignment]
        member = self.get_member("_tabSprite")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tabSprite",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SpriteProvider'),
            )

    @property
    def loading_indicator(self) -> str | None:
        """Target ID of the _loadingIndicator reference (targets Slot)."""
        member = self.get_member("_loadingIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loading_indicator.setter
    def loading_indicator(self, target: str | Slot | None) -> None:
        """Set the _loadingIndicator reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_loadingIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_loadingIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def swapper(self) -> str | None:
        """Target ID of the _swapper reference (targets SlideSwapRegion)."""
        member = self.get_member("_swapper")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @swapper.setter
    def swapper(self, target: str | SlideSwapRegion | None) -> None:
        """Set the _swapper reference by target ID or SlideSwapRegion instance."""
        target_id: str | None = target.id if isinstance(target, SlideSwapRegion) else target  # type: ignore[assignment]
        member = self.get_member("_swapper")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_swapper",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion'),
            )

