"""Generated component: TextEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itext import IText
from pyresonitelink.generated._types.action import Action
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.ifocusable import IFocusable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextEditor(GeneratedComponent, IFocusable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextEditor.

    Category: Common UI/Editors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextEditor"

    def __init__(self, text: str | IText | None = None, editing_started: str | Action[TextEditor] | None = None, editing_changed: str | Action[TextEditor] | None = None, editing_finished: str | Action[TextEditor] | None = None, submit_pressed: str | Action[TextEditor] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            text: Initial value for Text.
            editing_started: Initial value for EditingStarted.
            editing_changed: Initial value for EditingChanged.
            editing_finished: Initial value for EditingFinished.
            submit_pressed: Initial value for SubmitPressed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if text is not None:
            self.text = text
        if editing_started is not None:
            self.editing_started = editing_started
        if editing_changed is not None:
            self.editing_changed = editing_changed
        if editing_finished is not None:
            self.editing_finished = editing_finished
        if submit_pressed is not None:
            self.submit_pressed = submit_pressed

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
    def undo(self) -> bool | None:
        """The Undo field value."""
        member = self.get_member("Undo")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undo.setter
    def undo(self, value: bool) -> None:
        """Set the Undo field value."""
        member = self.get_member("Undo")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Undo", fields.FieldBool(value=value)
            )

    @property
    def undo_description(self) -> str | None:
        """The UndoDescription field value."""
        member = self.get_member("UndoDescription")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undo_description.setter
    def undo_description(self, value: str) -> None:
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
    def auto_caret_color_field(self) -> bool | None:
        """The AutoCaretColorField field value."""
        member = self.get_member("AutoCaretColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_caret_color_field.setter
    def auto_caret_color_field(self, value: bool) -> None:
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

    @property
    def editing_started(self) -> str | None:
        """Target ID of the EditingStarted reference (targets Action[TextEditor])."""
        member = self.get_member("EditingStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editing_started.setter
    def editing_started(self, target: str | Action[TextEditor] | None) -> None:
        """Set the EditingStarted reference by target ID or Action[TextEditor] instance."""
        target_id: str | None = target.id if isinstance(target, Action) else target  # type: ignore[assignment]
        member = self.get_member("EditingStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EditingStarted",
                members.Reference(targetId=target_id, targetType='Action<[FrooxEngine]FrooxEngine.TextEditor>'),
            )

    @property
    def editing_changed(self) -> str | None:
        """Target ID of the EditingChanged reference (targets Action[TextEditor])."""
        member = self.get_member("EditingChanged")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editing_changed.setter
    def editing_changed(self, target: str | Action[TextEditor] | None) -> None:
        """Set the EditingChanged reference by target ID or Action[TextEditor] instance."""
        target_id: str | None = target.id if isinstance(target, Action) else target  # type: ignore[assignment]
        member = self.get_member("EditingChanged")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EditingChanged",
                members.Reference(targetId=target_id, targetType='Action<[FrooxEngine]FrooxEngine.TextEditor>'),
            )

    @property
    def editing_finished(self) -> str | None:
        """Target ID of the EditingFinished reference (targets Action[TextEditor])."""
        member = self.get_member("EditingFinished")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editing_finished.setter
    def editing_finished(self, target: str | Action[TextEditor] | None) -> None:
        """Set the EditingFinished reference by target ID or Action[TextEditor] instance."""
        target_id: str | None = target.id if isinstance(target, Action) else target  # type: ignore[assignment]
        member = self.get_member("EditingFinished")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EditingFinished",
                members.Reference(targetId=target_id, targetType='Action<[FrooxEngine]FrooxEngine.TextEditor>'),
            )

    @property
    def submit_pressed(self) -> str | None:
        """Target ID of the SubmitPressed reference (targets Action[TextEditor])."""
        member = self.get_member("SubmitPressed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @submit_pressed.setter
    def submit_pressed(self, target: str | Action[TextEditor] | None) -> None:
        """Set the SubmitPressed reference by target ID or Action[TextEditor] instance."""
        target_id: str | None = target.id if isinstance(target, Action) else target  # type: ignore[assignment]
        member = self.get_member("SubmitPressed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SubmitPressed",
                members.Reference(targetId=target_id, targetType='Action<[FrooxEngine]FrooxEngine.TextEditor>'),
            )

