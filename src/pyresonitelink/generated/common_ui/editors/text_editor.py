"""Generated component: TextEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itext import IText
from pyresonitelink.generated._types.ifocusable import IFocusable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextEditor(GeneratedComponent, IFocusable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextEditor.

    Category: Common UI/Editors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextEditor"

    def __init__(self, text: str | IText | None = None, undo: primitives.Bool | None = None, undo_description: primitives.String | None = None, auto_caret_color_field: primitives.Bool | None = None, caret_color_field: primitives.ColorX | None = None, selection_color_field: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text: Initial value for Text.
            undo: Initial value for Undo.
            undo_description: Initial value for UndoDescription.
            auto_caret_color_field: Initial value for AutoCaretColorField.
            caret_color_field: Initial value for CaretColorField.
            selection_color_field: Initial value for SelectionColorField.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text is not None:
            self.text = text
        if undo is not None:
            self.undo = undo
        if undo_description is not None:
            self.undo_description = undo_description
        if auto_caret_color_field is not None:
            self.auto_caret_color_field = auto_caret_color_field
        if caret_color_field is not None:
            self.caret_color_field = caret_color_field
        if selection_color_field is not None:
            self.selection_color_field = selection_color_field

    @property
    def text(self) -> str | None:
        """Target ID of the Text reference (targets IText)."""
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text.setter
    def text(self, target: str | IText | None) -> None:
        """Set the Text reference by target ID or IText instance."""
        target_id: str | None = target.id if isinstance(target, IText) else target  # type: ignore[assignment]
        member = self.get_member("Text")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Text",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IText'),
            )

    @property
    def undo(self) -> primitives.Bool | None:
        """The Undo field value."""
        member = self.get_member("Undo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undo.setter
    def undo(self, value: primitives.Bool) -> None:
        """Set the Undo field value."""
        member = self.get_member("Undo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Undo", fields.FieldBool(value=value)
            )

    @property
    def undo_description(self) -> primitives.String | None:
        """The UndoDescription field value."""
        member = self.get_member("UndoDescription")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undo_description.setter
    def undo_description(self, value: primitives.String) -> None:
        """Set the UndoDescription field value."""
        member = self.get_member("UndoDescription")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UndoDescription", fields.FieldString(value=value)
            )

    @property
    def finish_handling(self) -> members.FieldEnum | None:
        """The FinishHandling member."""
        member = self.get_member("FinishHandling")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @finish_handling.setter
    def finish_handling(self, value: members.FieldEnum) -> None:
        """Set the FinishHandling member."""
        self.set_member("FinishHandling", value)

    @property
    def auto_caret_color_field(self) -> primitives.Bool | None:
        """The AutoCaretColorField field value."""
        member = self.get_member("AutoCaretColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_caret_color_field.setter
    def auto_caret_color_field(self, value: primitives.Bool) -> None:
        """Set the AutoCaretColorField field value."""
        member = self.get_member("AutoCaretColorField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoCaretColorField", fields.FieldBool(value=value)
            )

    @property
    def caret_color_field(self) -> primitives.ColorX | None:
        """The CaretColorField field value."""
        member = self.get_member("CaretColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @caret_color_field.setter
    def caret_color_field(self, value: primitives.ColorX) -> None:
        """Set the CaretColorField field value."""
        member = self.get_member("CaretColorField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CaretColorField", fields.FieldColorX(value=value)
            )

    @property
    def selection_color_field(self) -> primitives.ColorX | None:
        """The SelectionColorField field value."""
        member = self.get_member("SelectionColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selection_color_field.setter
    def selection_color_field(self, value: primitives.ColorX) -> None:
        """Set the SelectionColorField field value."""
        member = self.get_member("SelectionColorField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectionColorField", fields.FieldColorX(value=value)
            )

