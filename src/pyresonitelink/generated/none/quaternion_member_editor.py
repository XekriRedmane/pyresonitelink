"""Generated component: QuaternionMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.text_editor import TextEditor
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class QuaternionMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.QuaternionMemberEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.QuaternionMemberEditor"

    def __init__(self, continuous: bool | None = None, path: str | None = None, target: str | IField | None = None, vertical: bool | None = None, x_editor: str | TextEditor | None = None, y_editor: str | TextEditor | None = None, z_editor: str | TextEditor | None = None, x_drive: str | IField[str] | None = None, y_drive: str | IField[str] | None = None, z_drive: str | IField[str] | None = None, x_button: str | Button | None = None, y_button: str | Button | None = None, z_button: str | Button | None = None, editing_value: primitives.Double3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            vertical: Initial value for Vertical.
            x_editor: Initial value for _xEditor.
            y_editor: Initial value for _yEditor.
            z_editor: Initial value for _zEditor.
            x_drive: Initial value for _xDrive.
            y_drive: Initial value for _yDrive.
            z_drive: Initial value for _zDrive.
            x_button: Initial value for _xButton.
            y_button: Initial value for _yButton.
            z_button: Initial value for _zButton.
            editing_value: Initial value for _editingValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if continuous is not None:
            self.continuous = continuous
        if path is not None:
            self.path = path
        if target is not None:
            self.target = target
        if vertical is not None:
            self.vertical = vertical
        if x_editor is not None:
            self.x_editor = x_editor
        if y_editor is not None:
            self.y_editor = y_editor
        if z_editor is not None:
            self.z_editor = z_editor
        if x_drive is not None:
            self.x_drive = x_drive
        if y_drive is not None:
            self.y_drive = y_drive
        if z_drive is not None:
            self.z_drive = z_drive
        if x_button is not None:
            self.x_button = x_button
        if y_button is not None:
            self.y_button = y_button
        if z_button is not None:
            self.z_button = z_button
        if editing_value is not None:
            self.editing_value = editing_value

    @property
    def continuous(self) -> bool | None:
        """The Continuous field value."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

    @property
    def path(self) -> str | None:
        """The _path field value."""
        member = self.get_member("_path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: str) -> None:
        """Set the _path field value."""
        member = self.get_member("_path")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_path", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the _target reference (targets IField)."""
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField | None) -> None:
        """Set the _target reference by target ID or IField instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField'),
            )

    @property
    def vertical(self) -> bool | None:
        """The Vertical field value."""
        member = self.get_member("Vertical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vertical.setter
    def vertical(self, value: bool) -> None:
        """Set the Vertical field value."""
        member = self.get_member("Vertical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vertical", fields.FieldBool(value=value)
            )

    @property
    def x_editor(self) -> str | None:
        """Target ID of the _xEditor reference (targets TextEditor)."""
        member = self.get_member("_xEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x_editor.setter
    def x_editor(self, target: str | TextEditor | None) -> None:
        """Set the _xEditor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("_xEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def y_editor(self) -> str | None:
        """Target ID of the _yEditor reference (targets TextEditor)."""
        member = self.get_member("_yEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y_editor.setter
    def y_editor(self, target: str | TextEditor | None) -> None:
        """Set the _yEditor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("_yEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def z_editor(self) -> str | None:
        """Target ID of the _zEditor reference (targets TextEditor)."""
        member = self.get_member("_zEditor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z_editor.setter
    def z_editor(self, target: str | TextEditor | None) -> None:
        """Set the _zEditor reference by target ID or TextEditor instance."""
        target_id: str | None = target.id if isinstance(target, TextEditor) else target  # type: ignore[assignment]
        member = self.get_member("_zEditor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zEditor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextEditor'),
            )

    @property
    def x_drive(self) -> str | None:
        """Target ID of the _xDrive reference (targets IField[str])."""
        member = self.get_member("_xDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x_drive.setter
    def x_drive(self, target: str | IField[str] | None) -> None:
        """Set the _xDrive reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_xDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def y_drive(self) -> str | None:
        """Target ID of the _yDrive reference (targets IField[str])."""
        member = self.get_member("_yDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y_drive.setter
    def y_drive(self, target: str | IField[str] | None) -> None:
        """Set the _yDrive reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_yDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def z_drive(self) -> str | None:
        """Target ID of the _zDrive reference (targets IField[str])."""
        member = self.get_member("_zDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z_drive.setter
    def z_drive(self, target: str | IField[str] | None) -> None:
        """Set the _zDrive reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_zDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def x_button(self) -> str | None:
        """Target ID of the _xButton reference (targets Button)."""
        member = self.get_member("_xButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @x_button.setter
    def x_button(self, target: str | Button | None) -> None:
        """Set the _xButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_xButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_xButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def y_button(self) -> str | None:
        """Target ID of the _yButton reference (targets Button)."""
        member = self.get_member("_yButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @y_button.setter
    def y_button(self, target: str | Button | None) -> None:
        """Set the _yButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_yButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_yButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def z_button(self) -> str | None:
        """Target ID of the _zButton reference (targets Button)."""
        member = self.get_member("_zButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @z_button.setter
    def z_button(self, target: str | Button | None) -> None:
        """Set the _zButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_zButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_zButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def editing_value(self) -> primitives.Double3 | None:
        """The _editingValue field value."""
        member = self.get_member("_editingValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @editing_value.setter
    def editing_value(self, value: primitives.Double3) -> None:
        """Set the _editingValue field value."""
        member = self.get_member("_editingValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_editingValue", fields.FieldNullableDouble3(value=value)
            )

