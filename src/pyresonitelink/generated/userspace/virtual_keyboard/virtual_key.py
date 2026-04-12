"""Generated component: VirtualKey."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.key import Key
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_modifier_key import VirtualModifierKey
from pyresonitelink.generated._types.virtual_keyboard import VirtualKeyboard
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualKey(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Virtual key is a component that turns a button event into a button press on the keyboard in game as if it came from the physical keyboard.

    Category: Userspace/Virtual Keyboard

    **Behavior**: When paired with a UIX button or physical button on the same slot, it allows for simulation of key presses as if they came from the actual physical keyboard. This can be used for some funny effects where pressing a button forces the user that pressed it to jump (or, god forbid, make them switch to desktop or VR)

This cannot be used to send key presses outside of Resonite to control the external operating system unless the component is in Userspace.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualKey"

    def __init__(self, target_key: Key | str | None = None, append_string: primitives.String | None = None, shift_target_key: Key | str | None = None, shift_append_string: primitives.String | None = None, ignore_shift: primitives.Bool | None = None, modifier_key: str | VirtualModifierKey | None = None, modified_target_key: Key | str | None = None, modified_append_string: primitives.String | None = None, keyboard: str | VirtualKeyboard | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_key: Initial value for TargetKey.
            append_string: Initial value for AppendString.
            shift_target_key: Initial value for ShiftTargetKey.
            shift_append_string: Initial value for ShiftAppendString.
            ignore_shift: Initial value for IgnoreShift.
            modifier_key: Initial value for ModifierKey.
            modified_target_key: Initial value for ModifiedTargetKey.
            modified_append_string: Initial value for ModifiedAppendString.
            keyboard: Initial value for Keyboard.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_key is not None:
            self.target_key = target_key
        if append_string is not None:
            self.append_string = append_string
        if shift_target_key is not None:
            self.shift_target_key = shift_target_key
        if shift_append_string is not None:
            self.shift_append_string = shift_append_string
        if ignore_shift is not None:
            self.ignore_shift = ignore_shift
        if modifier_key is not None:
            self.modifier_key = modifier_key
        if modified_target_key is not None:
            self.modified_target_key = modified_target_key
        if modified_append_string is not None:
            self.modified_append_string = modified_append_string
        if keyboard is not None:
            self.keyboard = keyboard

    @property
    def target_key(self) -> Key | None:
        """The key to simulate."""
        member = self.get_member("TargetKey")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Key(member.value)
        return None

    @target_key.setter
    def target_key(self, value: Key | str) -> None:
        """Set TargetKey. The key to simulate."""
        member = self.get_member("TargetKey")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TargetKey",
                members.FieldEnum(value=str(value)),
            )

    @property
    def append_string(self) -> primitives.String | None:
        """What text to append if the user is focused into a text field"""
        member = self.get_member("AppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @append_string.setter
    def append_string(self, value: primitives.String) -> None:
        """Set the AppendString field value."""
        member = self.get_member("AppendString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppendString", fields.FieldString(value=value)
            )

    @property
    def shift_target_key(self) -> Key | None:
        """What key to use if the Virtual Shift component is taking effect, or shift is held on the physical keyboard."""
        member = self.get_member("ShiftTargetKey")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Key(member.value)
        return None

    @shift_target_key.setter
    def shift_target_key(self, value: Key | str) -> None:
        """Set ShiftTargetKey. What key to use if the Virtual Shift component is taking effect, or shift is held on the physical keyboard."""
        member = self.get_member("ShiftTargetKey")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ShiftTargetKey",
                members.FieldEnum(value=str(value)),
            )

    @property
    def shift_append_string(self) -> primitives.String | None:
        """What text to append if the user is focused into a text field and if the Virtual Shift component is taking effect, or shift is held on the physical keyboard."""
        member = self.get_member("ShiftAppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shift_append_string.setter
    def shift_append_string(self, value: primitives.String) -> None:
        """Set the ShiftAppendString field value."""
        member = self.get_member("ShiftAppendString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShiftAppendString", fields.FieldString(value=value)
            )

    @property
    def ignore_shift(self) -> primitives.Bool | None:
        """Whether to ignore shift and virtual shift keys entirely."""
        member = self.get_member("IgnoreShift")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_shift.setter
    def ignore_shift(self, value: primitives.Bool) -> None:
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
        """A key that can act as a special modifier (for example, if you wanted a key on your VR keyboard that appended "Cat!!" every time you type a letter)"""
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
    def modified_target_key(self) -> Key | None:
        """The key to use instead of ``TargetKey`` when ``ModifiedTargetKey`` is pressed down."""
        member = self.get_member("ModifiedTargetKey")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Key(member.value)
        return None

    @modified_target_key.setter
    def modified_target_key(self, value: Key | str) -> None:
        """Set ModifiedTargetKey. The key to use instead of ``TargetKey`` when ``ModifiedTargetKey`` is pressed down."""
        member = self.get_member("ModifiedTargetKey")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ModifiedTargetKey",
                members.FieldEnum(value=str(value)),
            )

    @property
    def modified_append_string(self) -> primitives.String | None:
        """hat text to append if the user is focused into a text field and the key specified by ``ModifiedTargetKey`` is pressed down."""
        member = self.get_member("ModifiedAppendString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @modified_append_string.setter
    def modified_append_string(self, value: primitives.String) -> None:
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
        """The keyboard object this key is a part of."""
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

