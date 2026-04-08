"""Generated component: VirtualKey."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_modifier_key import VirtualModifierKey
from pyresonitelink.generated._types.virtual_keyboard import VirtualKeyboard
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualKey(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualKey.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualKey"

    def __init__(self, append_string: str | None = None, shift_append_string: str | None = None, ignore_shift: bool | None = None, modifier_key: str | VirtualModifierKey | None = None, modified_append_string: str | None = None, keyboard: str | VirtualKeyboard | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            append_string: Initial value for AppendString.
            shift_append_string: Initial value for ShiftAppendString.
            ignore_shift: Initial value for IgnoreShift.
            modifier_key: Initial value for ModifierKey.
            modified_append_string: Initial value for ModifiedAppendString.
            keyboard: Initial value for Keyboard.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if append_string is not None:
            self.append_string = append_string
        if shift_append_string is not None:
            self.shift_append_string = shift_append_string
        if ignore_shift is not None:
            self.ignore_shift = ignore_shift
        if modifier_key is not None:
            self.modifier_key = modifier_key
        if modified_append_string is not None:
            self.modified_append_string = modified_append_string
        if keyboard is not None:
            self.keyboard = keyboard

    @property
    def target_key(self) -> members.FieldEnum | None:
        """The TargetKey member."""
        member = self.get_member("TargetKey")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @target_key.setter
    def target_key(self, value: members.FieldEnum) -> None:
        """Set the TargetKey member."""
        self.set_member("TargetKey", value)

    @property
    def append_string(self) -> str | None:
        """The AppendString field value."""
        member = self.get_member("AppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @append_string.setter
    def append_string(self, value: str) -> None:
        """Set the AppendString field value."""
        member = self.get_member("AppendString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppendString", fields.FieldString(value=value)
            )

    @property
    def shift_target_key(self) -> members.FieldEnum | None:
        """The ShiftTargetKey member."""
        member = self.get_member("ShiftTargetKey")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @shift_target_key.setter
    def shift_target_key(self, value: members.FieldEnum) -> None:
        """Set the ShiftTargetKey member."""
        self.set_member("ShiftTargetKey", value)

    @property
    def shift_append_string(self) -> str | None:
        """The ShiftAppendString field value."""
        member = self.get_member("ShiftAppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shift_append_string.setter
    def shift_append_string(self, value: str) -> None:
        """Set the ShiftAppendString field value."""
        member = self.get_member("ShiftAppendString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShiftAppendString", fields.FieldString(value=value)
            )

    @property
    def ignore_shift(self) -> bool | None:
        """The IgnoreShift field value."""
        member = self.get_member("IgnoreShift")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_shift.setter
    def ignore_shift(self, value: bool) -> None:
        """Set the IgnoreShift field value."""
        member = self.get_member("IgnoreShift")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreShift", fields.FieldBool(value=value)
            )

    @property
    def modifier_key(self) -> str | None:
        """Target ID of the ModifierKey reference (targets VirtualModifierKey)."""
        member = self.get_member("ModifierKey")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @modifier_key.setter
    def modifier_key(self, target: str | VirtualModifierKey | None) -> None:
        """Set the ModifierKey reference by target ID or VirtualModifierKey instance."""
        target_id: str | None = target.id if isinstance(target, VirtualModifierKey) else target  # type: ignore[assignment]
        member = self.get_member("ModifierKey")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ModifierKey",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VirtualModifierKey'),
            )

    @property
    def modified_target_key(self) -> members.FieldEnum | None:
        """The ModifiedTargetKey member."""
        member = self.get_member("ModifiedTargetKey")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @modified_target_key.setter
    def modified_target_key(self, value: members.FieldEnum) -> None:
        """Set the ModifiedTargetKey member."""
        self.set_member("ModifiedTargetKey", value)

    @property
    def modified_append_string(self) -> str | None:
        """The ModifiedAppendString field value."""
        member = self.get_member("ModifiedAppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modified_append_string.setter
    def modified_append_string(self, value: str) -> None:
        """Set the ModifiedAppendString field value."""
        member = self.get_member("ModifiedAppendString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ModifiedAppendString", fields.FieldString(value=value)
            )

    @property
    def keyboard(self) -> str | None:
        """Target ID of the Keyboard reference (targets VirtualKeyboard)."""
        member = self.get_member("Keyboard")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @keyboard.setter
    def keyboard(self, target: str | VirtualKeyboard | None) -> None:
        """Set the Keyboard reference by target ID or VirtualKeyboard instance."""
        target_id: str | None = target.id if isinstance(target, VirtualKeyboard) else target  # type: ignore[assignment]
        member = self.get_member("Keyboard")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Keyboard",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VirtualKeyboard'),
            )

