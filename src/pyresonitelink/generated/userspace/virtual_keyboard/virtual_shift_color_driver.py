"""Generated component: VirtualShiftColorDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_keyboard import VirtualKeyboard
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualShiftColorDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualShiftColorDriver.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualShiftColorDriver"

    def __init__(self, keyboard: str | VirtualKeyboard | None = None, color_target: str | IField[primitives.ColorX] | None = None, normal_color: primitives.ColorX | None = None, shift_color: primitives.ColorX | None = None, hold_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            keyboard: Initial value for Keyboard.
            color_target: Initial value for ColorTarget.
            normal_color: Initial value for NormalColor.
            shift_color: Initial value for ShiftColor.
            hold_color: Initial value for HoldColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if keyboard is not None:
            self.keyboard = keyboard
        if color_target is not None:
            self.color_target = color_target
        if normal_color is not None:
            self.normal_color = normal_color
        if shift_color is not None:
            self.shift_color = shift_color
        if hold_color is not None:
            self.hold_color = hold_color

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

    @property
    def color_target(self) -> str | None:
        """Target ID of the ColorTarget reference (targets IField[primitives.ColorX])."""
        member = self.get_member("ColorTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @color_target.setter
    def color_target(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the ColorTarget reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ColorTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ColorTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def normal_color(self) -> primitives.ColorX | None:
        """The NormalColor field value."""
        member = self.get_member("NormalColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @normal_color.setter
    def normal_color(self, value: primitives.ColorX) -> None:
        """Set the NormalColor field value."""
        member = self.get_member("NormalColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NormalColor", fields.FieldColorX(value=value)
            )

    @property
    def shift_color(self) -> primitives.ColorX | None:
        """The ShiftColor field value."""
        member = self.get_member("ShiftColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shift_color.setter
    def shift_color(self, value: primitives.ColorX) -> None:
        """Set the ShiftColor field value."""
        member = self.get_member("ShiftColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShiftColor", fields.FieldColorX(value=value)
            )

    @property
    def hold_color(self) -> primitives.ColorX | None:
        """The HoldColor field value."""
        member = self.get_member("HoldColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_color.setter
    def hold_color(self, value: primitives.ColorX) -> None:
        """Set the HoldColor field value."""
        member = self.get_member("HoldColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldColor", fields.FieldColorX(value=value)
            )

