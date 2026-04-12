"""Generated component: BooleanMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BooleanMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The BooleanMemberEditor component is commonly used in Scene Inspectors to allow toggling of booleans even if they are a sub property of a type like a Bool3 Using ``_path``. This can be utilized in Ref Hacking.

    Used in Scene Inspectors
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BooleanMemberEditor"

    def __init__(self, continuous: primitives.Bool | None = None, path: primitives.String | None = None, target: str | IField | None = None, check_box: str | Checkbox | None = None, state_drive: str | IField[primitives.Bool] | None = None, button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            check_box: Initial value for _checkBox.
            state_drive: Initial value for _stateDrive.
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
        if check_box is not None:
            self.check_box = check_box
        if state_drive is not None:
            self.state_drive = state_drive
        if button is not None:
            self.button = button

    @property
    def continuous(self) -> primitives.Bool | None:
        """Whether editing of this field instantly updates the ``_target``."""
        member = self.get_member("Continuous")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @continuous.setter
    def continuous(self, value: primitives.Bool) -> None:
        """Set the Continuous field value."""
        member = self.get_member("Continuous")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Continuous", fields.FieldBool(value=value)
            )

    @property
    def path(self) -> primitives.String | None:
        """The sub path under ``_target``. This can be something like "x" to represent the first value of a Bool3 field."""
        member = self.get_member("_path")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @path.setter
    def path(self, value: primitives.String) -> None:
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
        """The bool field or a field with a toggleable bool subfield."""
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
    def check_box(self) -> str | None:
        """The Checkbox to toggle ``_target``->``_path`` with."""
        member = self.get_member("_checkBox")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_box.setter
    def check_box(self, target: str | Checkbox | None) -> None:
        """Set the _checkBox reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_checkBox")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_checkBox",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def state_drive(self) -> str | None:
        """The field to drive with the state of ``_target``->``_path``"""
        member = self.get_member("_stateDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @state_drive.setter
    def state_drive(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _stateDrive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_stateDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_stateDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def button(self) -> str | None:
        """The button to toggle ``_target``->``_path`` with."""
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

