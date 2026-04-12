"""Generated component: TextField."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextField(GeneratedComponent, IButtonPressReceiver, IUIGrabbable, IUIGrabReceiver, IWorldEventReceiver):
    """The TextField component is used in conjunction with a TextEditor, Text, and Button component to provide an editable text field. The Text component stores the text, the TextEditor is the editor for the text, and the Button allows the text editor to appear when then text field is selected.

You must drag a reference to the Text component into the Text property of the TextEditor in order for the editor to know what text it is editing.

}}

    Category: UIX/Interaction

    This component is useful for forms, user input, and other text based
    projects.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.TextField"

    def __init__(self, editor: str | TextEditor | None = None, text: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            editor: Initial value for Editor.
            text: Initial value for __text.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if editor is not None:
            self.editor = editor
        if text is not None:
            self.text = text

    @property
    def editor(self) -> str | None:
        """A reference to the text editor component."""
        member = self.get_member("Editor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editor.setter
    def editor(self, target: str | TextEditor | None) -> None:
        """Set the Editor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("Editor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Editor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def text(self) -> str | None:
        """Internal - The text for this field."""
        member = self.get_member("__text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | Text | None) -> None:
        """Set the __text reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("__text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "__text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

