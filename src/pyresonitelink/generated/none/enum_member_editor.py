"""Generated component: EnumMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class EnumMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.EnumMemberEditor.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.EnumMemberEditor"

    def __init__(self, continuous: bool | None = None, path: str | None = None, target: str | IField | None = None, text_drive: str | IField[str] | None = None, button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            text_drive: Initial value for _textDrive.
            button: Initial value for _button.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if continuous is not None:
            self.continuous = continuous
        if path is not None:
            self.path = path
        if target is not None:
            self.target = target
        if text_drive is not None:
            self.text_drive = text_drive
        if button is not None:
            self.button = button

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
    def text_drive(self) -> str | None:
        """Target ID of the _textDrive reference (targets IField[str])."""
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @text_drive.setter
    def text_drive(self, target: str | IField[str] | None) -> None:
        """Set the _textDrive reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_textDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_textDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def button(self) -> str | None:
        """Target ID of the _button reference (targets Button)."""
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button.setter
    def button(self, target: str | Button | None) -> None:
        """Set the _button reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

