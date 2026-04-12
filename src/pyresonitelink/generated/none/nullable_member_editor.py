"""Generated component: NullableMemberEditor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NullableMemberEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Nullable Member Editor component is commonly used in Ref Hacking and is used to modify nullable values.

Please look into Flux or component alternatives other than this component to edit nullables.

    Used in Ref Hacking. Don't use for your creations or they will break at
    any time.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NullableMemberEditor"

    def __init__(self, continuous: primitives.Bool | None = None, path: primitives.String | None = None, target: str | IField | None = None, nullable_base_type: Type | str | None = None, check_box: str | Checkbox | None = None, state_drive: str | IField[primitives.Bool] | None = None, button: str | Button | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            continuous: Initial value for Continuous.
            path: Initial value for _path.
            target: Initial value for _target.
            nullable_base_type: Initial value for NullableBaseType.
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
        if nullable_base_type is not None:
            self.nullable_base_type = nullable_base_type
        if check_box is not None:
            self.check_box = check_box
        if state_drive is not None:
            self.state_drive = state_drive
        if button is not None:
            self.button = button

    @property
    def continuous(self) -> primitives.Bool | None:
        """Whether changes should instantly update a target value."""
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
        """The sub element to edit via C# reflection."""
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
        """The value to be modifying."""
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
    def nullable_base_type(self) -> Type | None:
        """The type of the value stored within the nullable (for "Nullable" aka "Float?" This is "Float")"""
        member = self.get_member("NullableBaseType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @nullable_base_type.setter
    def nullable_base_type(self, value: Type | str) -> None:
        """Set NullableBaseType. The type of the value stored within the nullable (for "Nullable" aka "Float?" This is "Float")"""
        member = self.get_member("NullableBaseType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "NullableBaseType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def check_box(self) -> str | None:
        """Whether the nullable has a value."""
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
        """The field to drive with whether or not the nullable has a value."""
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
        """The button for editing the nullable."""
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

