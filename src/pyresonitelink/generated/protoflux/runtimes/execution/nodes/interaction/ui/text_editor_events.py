"""Generated component: TextEditorEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextEditorEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Text Editor Events`` node takes in a global TextEditor reference and will listen for events from that global reference. This node fires events that relate to the TextEditor, and can be useful when you want certain things to happen when things get edited or submitted by the user.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction/UI
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.TextEditorEvents"

    def __init__(self, editor: str | IGlobalValueProxy[TextEditor] | None = None, editing_started: str | ISyncNodeOperation | None = None, editing_changed: str | ISyncNodeOperation | None = None, editing_finished: str | ISyncNodeOperation | None = None, submit_pressed: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            editor: Initial value for Editor.
            editing_started: Initial value for EditingStarted.
            editing_changed: Initial value for EditingChanged.
            editing_finished: Initial value for EditingFinished.
            submit_pressed: Initial value for SubmitPressed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if editor is not None:
            self.editor = editor
        if editing_started is not None:
            self.editing_started = editing_started
        if editing_changed is not None:
            self.editing_changed = editing_changed
        if editing_finished is not None:
            self.editing_finished = editing_finished
        if submit_pressed is not None:
            self.submit_pressed = submit_pressed

    @property
    def editor(self) -> str | None:
        """Target ID of the Editor reference (targets IGlobalValueProxy[TextEditor])."""
        member = self.get_member("Editor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editor.setter
    def editor(self, target: str | IGlobalValueProxy[TextEditor] | None) -> None:
        """Set the Editor reference by target ID or IGlobalValueProxy[TextEditor] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Editor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Editor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.TextEditor>'),
            )

    @property
    def editing_started(self) -> str | None:
        """Fires when the editing has started (After the editor is focused)."""
        member = self.get_member("EditingStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editing_started.setter
    def editing_started(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the EditingStarted reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("EditingStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EditingStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def editing_changed(self) -> str | None:
        """Fires after every change during the editing."""
        member = self.get_member("EditingChanged")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editing_changed.setter
    def editing_changed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the EditingChanged reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("EditingChanged")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EditingChanged",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def editing_finished(self) -> str | None:
        """Fires when the editing finishes (before the editor loses focus)."""
        member = self.get_member("EditingFinished")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editing_finished.setter
    def editing_finished(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the EditingFinished reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("EditingFinished")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EditingFinished",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def submit_pressed(self) -> str | None:
        """Fires When the user submits the changes for the editor (called before ``EditingFinished`` gets fired)."""
        member = self.get_member("SubmitPressed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @submit_pressed.setter
    def submit_pressed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the SubmitPressed reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("SubmitPressed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SubmitPressed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

