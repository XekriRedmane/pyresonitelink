"""Generated component: FileSystemItem."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.entry_type import EntryType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.browser_dialog import BrowserDialog
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FileSystemItem(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The FileSystemItem component is a type of BrowserItem used for system files or inventory items being viewed on the dash menu.

    Used internally by the inventory and file system menus. Not used by the
    user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FileSystemItem"

    def __init__(self, browser: str | BrowserDialog | None = None, selected_color: primitives.ColorX | None = None, selected_text: primitives.ColorX | None = None, normal_color: primitives.ColorX | None = None, normal_text: primitives.ColorX | None = None, name: primitives.String | None = None, base_path: primitives.String | None = None, type_: EntryType | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            browser: Initial value for Browser.
            selected_color: Initial value for SelectedColor.
            selected_text: Initial value for SelectedText.
            normal_color: Initial value for NormalColor.
            normal_text: Initial value for NormalText.
            name: Initial value for Name.
            base_path: Initial value for BasePath.
            type_: Initial value for Type.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if browser is not None:
            self.browser = browser
        if selected_color is not None:
            self.selected_color = selected_color
        if selected_text is not None:
            self.selected_text = selected_text
        if normal_color is not None:
            self.normal_color = normal_color
        if normal_text is not None:
            self.normal_text = normal_text
        if name is not None:
            self.name = name
        if base_path is not None:
            self.base_path = base_path
        if type_ is not None:
            self.type_ = type_

    @property
    def browser(self) -> str | None:
        """The source browser this item came from."""
        member = self.get_member("Browser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @browser.setter
    def browser(self, target: str | BrowserDialog | None) -> None:
        """Set the Browser reference by target ID or BrowserDialog instance."""
        target_id: str | None = target.id if isinstance(target, BrowserDialog) else target  # type: ignore[assignment]
        member = self.get_member("Browser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Browser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BrowserDialog'),
            )

    @property
    def selected_color(self) -> primitives.ColorX | None:
        """The color this item's background should be when selected."""
        member = self.get_member("SelectedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_color.setter
    def selected_color(self, value: primitives.ColorX) -> None:
        """Set the SelectedColor field value."""
        member = self.get_member("SelectedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedColor", fields.FieldColorX(value=value)
            )

    @property
    def selected_text(self) -> primitives.ColorX | None:
        """The color this item's text should be when selected."""
        member = self.get_member("SelectedText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_text.setter
    def selected_text(self, value: primitives.ColorX) -> None:
        """Set the SelectedText field value."""
        member = self.get_member("SelectedText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedText", fields.FieldColorX(value=value)
            )

    @property
    def normal_color(self) -> primitives.ColorX | None:
        """The color this item's background should be at rest state"""
        member = self.get_member("NormalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_color.setter
    def normal_color(self, value: primitives.ColorX) -> None:
        """Set the NormalColor field value."""
        member = self.get_member("NormalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalColor", fields.FieldColorX(value=value)
            )

    @property
    def normal_text(self) -> primitives.ColorX | None:
        """The color this item's text would be at rest state."""
        member = self.get_member("NormalText")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_text.setter
    def normal_text(self, value: primitives.ColorX) -> None:
        """Set the NormalText field value."""
        member = self.get_member("NormalText")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalText", fields.FieldColorX(value=value)
            )

    @property
    def name(self) -> primitives.String | None:
        """The name of the"""
        member = self.get_member("Name")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name.setter
    def name(self, value: primitives.String) -> None:
        """Set the Name field value."""
        member = self.get_member("Name")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Name", fields.FieldString(value=value)
            )

    @property
    def base_path(self) -> primitives.String | None:
        """The base directory of the item."""
        member = self.get_member("BasePath")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_path.setter
    def base_path(self, value: primitives.String) -> None:
        """Set the BasePath field value."""
        member = self.get_member("BasePath")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BasePath", fields.FieldString(value=value)
            )

    @property
    def type_(self) -> EntryType | None:
        """Whether if this is a file or folder."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return EntryType(member.value)
        return None

    @type_.setter
    def type_(self, value: EntryType | str) -> None:
        """Set Type. Whether if this is a file or folder."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Type",
                members.FieldEnum(value=str(value)),
            )

