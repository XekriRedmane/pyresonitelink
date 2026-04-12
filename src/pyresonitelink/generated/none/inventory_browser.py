"""Generated component: InventoryBrowser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.special_item_type import SpecialItemType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.browser_item import BrowserItem
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.grid_layout import GridLayout
from pyresonitelink.generated._types.sprite_provider import SpriteProvider
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InventoryBrowser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The InventoryBrowser Component is the component that handles the Inventory screen.

    Not used directly by the user.

    **SpecialItemType**: Every one of these map to their corrosponding favorite item. To see what components map to these enums when saved to inventory, refer to the favorites page.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InventoryBrowser"

    def __init__(self, selected_item: str | BrowserItem | None = None, previous_selected_item: str | BrowserItem | None = None, allow_select: primitives.Bool | None = None, item_size: primitives.Float | None = None, selected_text: str | Text | None = None, path_root: str | Slot | None = None, buttons_root: str | Slot | None = None, folder_grid: str | GridLayout | None = None, item_grid: str | GridLayout | None = None, tab_sprite: str | SpriteProvider | None = None, loading_indicator: str | Slot | None = None, swapper: str | SlideSwapRegion | None = None, auto_reinitialize: primitives.Bool | None = None, current_path: primitives.String | None = None, current_owner_id: primitives.String | None = None, add_new_button: str | Button | None = None, delete_button: str | Button | None = None, inventories_button: str | Button | None = None, share_button: str | Button | None = None, unshare_button: str | Button | None = None, copy_link: str | Button | None = None, add_current_avatar: str | Button | None = None, last_special_item_type: SpecialItemType | str | None = None, *, component: workers.Component | None = None) -> None:
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
            auto_reinitialize: Initial value for _autoReinitialize.
            current_path: Initial value for _currentPath.
            current_owner_id: Initial value for _currentOwnerId.
            add_new_button: Initial value for _addNewButton.
            delete_button: Initial value for _deleteButton.
            inventories_button: Initial value for _inventoriesButton.
            share_button: Initial value for _shareButton.
            unshare_button: Initial value for _unshareButton.
            copy_link: Initial value for _copyLink.
            add_current_avatar: Initial value for _addCurrentAvatar.
            last_special_item_type: Initial value for _lastSpecialItemType.
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
        if auto_reinitialize is not None:
            self.auto_reinitialize = auto_reinitialize
        if current_path is not None:
            self.current_path = current_path
        if current_owner_id is not None:
            self.current_owner_id = current_owner_id
        if add_new_button is not None:
            self.add_new_button = add_new_button
        if delete_button is not None:
            self.delete_button = delete_button
        if inventories_button is not None:
            self.inventories_button = inventories_button
        if share_button is not None:
            self.share_button = share_button
        if unshare_button is not None:
            self.unshare_button = unshare_button
        if copy_link is not None:
            self.copy_link = copy_link
        if add_current_avatar is not None:
            self.add_current_avatar = add_current_avatar
        if last_special_item_type is not None:
            self.last_special_item_type = last_special_item_type

    @property
    def selected_item(self) -> str | None:
        """The currently selected item being highlighted."""
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
        """The item previously highlighted."""
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
    def allow_select(self) -> primitives.Bool | None:
        """Whether this file browser allows selecting item elements."""
        member = self.get_member("AllowSelect")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_select.setter
    def allow_select(self, value: primitives.Bool) -> None:
        """Set the AllowSelect field value."""
        member = self.get_member("AllowSelect")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSelect", fields.FieldBool(value=value)
            )

    @property
    def item_size(self) -> primitives.Float | None:
        """How big the items are on the view."""
        member = self.get_member("ItemSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @item_size.setter
    def item_size(self, value: primitives.Float) -> None:
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
        """The text to fill with the name of the selected item."""
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
        """The root of the area being used to display the current path."""
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
        """The root of the area being used to show the different button actions."""
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
        """The grid layout Component being used to align the folders in the directory."""
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
        """The grid layout Component being used to align the files in the directory."""
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
        """The sprite being used to show the tab sprite."""
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
        """The slot that stores the loading indicator for a newly opened directory."""
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
        """The component to handle the slide animation when opening a different directory."""
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

    @property
    def user(self) -> members.SyncObject | None:
        """The user this belongs to."""
        member = self.get_member("_user")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set _user. The user this belongs to."""
        self.set_member("_user", value)

    @property
    def auto_reinitialize(self) -> primitives.Bool | None:
        """Whether to fix issues by auto reinitializing."""
        member = self.get_member("_autoReinitialize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_reinitialize.setter
    def auto_reinitialize(self, value: primitives.Bool) -> None:
        """Set the _autoReinitialize field value."""
        member = self.get_member("_autoReinitialize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_autoReinitialize", fields.FieldBool(value=value)
            )

    @property
    def current_path(self) -> primitives.String | None:
        """The current inventory path this is navigated to."""
        member = self.get_member("_currentPath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_path.setter
    def current_path(self, value: primitives.String) -> None:
        """Set the _currentPath field value."""
        member = self.get_member("_currentPath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_currentPath", fields.FieldString(value=value)
            )

    @property
    def current_owner_id(self) -> primitives.String | None:
        """The owner of this inventory screen."""
        member = self.get_member("_currentOwnerId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_owner_id.setter
    def current_owner_id(self, value: primitives.String) -> None:
        """Set the _currentOwnerId field value."""
        member = self.get_member("_currentOwnerId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_currentOwnerId", fields.FieldString(value=value)
            )

    @property
    def add_new_button(self) -> str | None:
        """The button for adding new directories."""
        member = self.get_member("_addNewButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @add_new_button.setter
    def add_new_button(self, target: str | Button | None) -> None:
        """Set the _addNewButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_addNewButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_addNewButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def delete_button(self) -> str | None:
        """The button for deleting items and directories."""
        member = self.get_member("_deleteButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delete_button.setter
    def delete_button(self, target: str | Button | None) -> None:
        """Set the _deleteButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_deleteButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_deleteButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def inventories_button(self) -> str | None:
        """The button to go to the main inventories screen in order to go to the personal inventory or group shared inventories."""
        member = self.get_member("_inventoriesButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inventories_button.setter
    def inventories_button(self, target: str | Button | None) -> None:
        """Set the _inventoriesButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_inventoriesButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inventoriesButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def share_button(self) -> str | None:
        """The button to share folders to the public."""
        member = self.get_member("_shareButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @share_button.setter
    def share_button(self, target: str | Button | None) -> None:
        """Set the _shareButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_shareButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shareButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def unshare_button(self) -> str | None:
        """The button to unshare folders to the public."""
        member = self.get_member("_unshareButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @unshare_button.setter
    def unshare_button(self, target: str | Button | None) -> None:
        """Set the _unshareButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_unshareButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_unshareButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def copy_link(self) -> str | None:
        """The button to copy the link for an item or folder."""
        member = self.get_member("_copyLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @copy_link.setter
    def copy_link(self, target: str | Button | None) -> None:
        """Set the _copyLink reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_copyLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_copyLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def add_current_avatar(self) -> str | None:
        """The button to favorite the currently selected avatar"""
        member = self.get_member("_addCurrentAvatar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @add_current_avatar.setter
    def add_current_avatar(self, target: str | Button | None) -> None:
        """Set the _addCurrentAvatar reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_addCurrentAvatar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_addCurrentAvatar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def last_special_item_type(self) -> SpecialItemType | None:
        """The last special item type that was selected in this inventory."""
        member = self.get_member("_lastSpecialItemType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SpecialItemType(member.value)
        return None

    @last_special_item_type.setter
    def last_special_item_type(self, value: SpecialItemType | str) -> None:
        """Set _lastSpecialItemType. The last special item type that was selected in this inventory."""
        member = self.get_member("_lastSpecialItemType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_lastSpecialItemType",
                members.FieldEnum(value=str(value)),
            )

