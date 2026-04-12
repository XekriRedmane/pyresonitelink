"""Generated component: FileBrowser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
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


class FileBrowser(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The FileBrowser component is used to show file lists of files on the user's PC in the userspace dash menu.

    Not used directly by the user.

    **CreateHandler**: Handles creation of directories. Is a sync delegate type.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FileBrowser"

    def __init__(self, selected_item: str | BrowserItem | None = None, previous_selected_item: str | BrowserItem | None = None, allow_select: primitives.Bool | None = None, item_size: primitives.Float | None = None, selected_text: str | Text | None = None, path_root: str | Slot | None = None, buttons_root: str | Slot | None = None, folder_grid: str | GridLayout | None = None, item_grid: str | GridLayout | None = None, tab_sprite: str | SpriteProvider | None = None, loading_indicator: str | Slot | None = None, swapper: str | SlideSwapRegion | None = None, current_path: primitives.String | None = None, last_path: primitives.String | None = None, import_button: str | Button | None = None, raw_import_button: str | Button | None = None, create_new_button: str | Button | None = None, reload_button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
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
            current_path: Initial value for CurrentPath.
            last_path: Initial value for _lastPath.
            import_button: Initial value for _importButton.
            raw_import_button: Initial value for _rawImportButton.
            create_new_button: Initial value for _createNewButton.
            reload_button: Initial value for _reloadButton.
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
        if current_path is not None:
            self.current_path = current_path
        if last_path is not None:
            self.last_path = last_path
        if import_button is not None:
            self.import_button = import_button
        if raw_import_button is not None:
            self.raw_import_button = raw_import_button
        if create_new_button is not None:
            self.create_new_button = create_new_button
        if reload_button is not None:
            self.reload_button = reload_button

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
    def current_path(self) -> primitives.String | None:
        """The current folder path."""
        member = self.get_member("CurrentPath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_path.setter
    def current_path(self, value: primitives.String) -> None:
        """Set the CurrentPath field value."""
        member = self.get_member("CurrentPath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentPath", fields.FieldString(value=value)
            )

    @property
    def last_path(self) -> primitives.String | None:
        """The last folder path."""
        member = self.get_member("_lastPath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_path.setter
    def last_path(self, value: primitives.String) -> None:
        """Set the _lastPath field value."""
        member = self.get_member("_lastPath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastPath", fields.FieldString(value=value)
            )

    @property
    def user(self) -> members.SyncObject | None:
        """The user using this file browser."""
        member = self.get_member("_user")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set _user. The user using this file browser."""
        self.set_member("_user", value)

    @property
    def import_button(self) -> str | None:
        """The button to import a selected folder or file."""
        member = self.get_member("_importButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @import_button.setter
    def import_button(self, target: str | Button | None) -> None:
        """Set the _importButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_importButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_importButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def raw_import_button(self) -> str | None:
        """The button to import a selected file as a raw file object."""
        member = self.get_member("_rawImportButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @raw_import_button.setter
    def raw_import_button(self, target: str | Button | None) -> None:
        """Set the _rawImportButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_rawImportButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rawImportButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def create_new_button(self) -> str | None:
        """The button to create a new file directory."""
        member = self.get_member("_createNewButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @create_new_button.setter
    def create_new_button(self, target: str | Button | None) -> None:
        """Set the _createNewButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_createNewButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_createNewButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def reload_button(self) -> str | None:
        """The button used to refresh the folder and file list."""
        member = self.get_member("_reloadButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reload_button.setter
    def reload_button(self, target: str | Button | None) -> None:
        """Set the _reloadButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_reloadButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_reloadButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

