"""Generated component: TextGizmo."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent_gizmo import IComponentGizmo
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextGizmo(GeneratedComponent, IComponentGizmo, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TextGizmo.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextGizmo"

    def __init__(self, target: str | TextRenderer | None = None, editor: str | TextEditor | None = None, edit_icon_position: str | IField[primitives.Float3] | None = None, edit_icon_scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for _target.
            editor: Initial value for _editor.
            edit_icon_position: Initial value for _editIconPosition.
            edit_icon_scale: Initial value for _editIconScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if editor is not None:
            self.editor = editor
        if edit_icon_position is not None:
            self.edit_icon_position = edit_icon_position
        if edit_icon_scale is not None:
            self.edit_icon_scale = edit_icon_scale

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets TextRenderer)."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | TextRenderer | None) -> None:
        """Set the _target reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def editor(self) -> str | None:
        """Target ID of the _editor reference (targets TextEditor)."""
        member = self.get_member("_editor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @editor.setter
    def editor(self, target: str | TextEditor | None) -> None:
        """Set the _editor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("_editor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_editor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def edit_icon_position(self) -> str | None:
        """Target ID of the _editIconPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_editIconPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @edit_icon_position.setter
    def edit_icon_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _editIconPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_editIconPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_editIconPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def edit_icon_scale(self) -> str | None:
        """Target ID of the _editIconScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_editIconScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @edit_icon_scale.setter
    def edit_icon_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _editIconScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_editIconScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_editIconScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

