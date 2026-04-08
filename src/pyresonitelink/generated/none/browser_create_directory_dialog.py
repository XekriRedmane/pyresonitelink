"""Generated component: BrowserCreateDirectoryDialog."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.browser_dialog import BrowserDialog
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BrowserCreateDirectoryDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BrowserCreateDirectoryDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BrowserCreateDirectoryDialog"

    def __init__(self, browser: str | BrowserDialog | None = None, text: str | Text | None = None, text_field: str | TextField | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            browser: Initial value for _browser.
            text: Initial value for _text.
            text_field: Initial value for _textField.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if browser is not None:
            self.browser = browser
        if text is not None:
            self.text = text
        if text_field is not None:
            self.text_field = text_field

    @property
    def browser(self) -> str | None:
        """Target ID of the _browser reference (targets BrowserDialog)."""
        member = self.get_member("_browser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @browser.setter
    def browser(self, target: str | BrowserDialog | None) -> None:
        """Set the _browser reference by target ID or BrowserDialog instance."""
        target_id: str | None = target.id if isinstance(target, BrowserDialog) else target  # type: ignore[assignment]
        member = self.get_member("_browser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_browser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BrowserDialog'),
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
    def text_field(self) -> str | None:
        """Target ID of the _textField reference (targets TextField)."""
        member = self.get_member("_textField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_field.setter
    def text_field(self, target: str | TextField | None) -> None:
        """Set the _textField reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_textField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

