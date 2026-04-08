"""Generated component: VirtualShift."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_keyboard import VirtualKeyboard
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualShift(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualShift.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualShift"

    def __init__(self, keyboard: str | VirtualKeyboard | None = None, hold_press_interval: primitives.Float | None = None, always_hold: primitives.Bool | None = None, last_press: primitives.Double | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            keyboard: Initial value for Keyboard.
            hold_press_interval: Initial value for HoldPressInterval.
            always_hold: Initial value for AlwaysHold.
            last_press: Initial value for _lastPress.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if keyboard is not None:
            self.keyboard = keyboard
        if hold_press_interval is not None:
            self.hold_press_interval = hold_press_interval
        if always_hold is not None:
            self.always_hold = always_hold
        if last_press is not None:
            self.last_press = last_press

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
    def hold_press_interval(self) -> primitives.Float | None:
        """The HoldPressInterval field value."""
        member = self.get_member("HoldPressInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hold_press_interval.setter
    def hold_press_interval(self, value: primitives.Float) -> None:
        """Set the HoldPressInterval field value."""
        member = self.get_member("HoldPressInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HoldPressInterval", fields.FieldFloat(value=value)
            )

    @property
    def always_hold(self) -> primitives.Bool | None:
        """The AlwaysHold field value."""
        member = self.get_member("AlwaysHold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @always_hold.setter
    def always_hold(self, value: primitives.Bool) -> None:
        """Set the AlwaysHold field value."""
        member = self.get_member("AlwaysHold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlwaysHold", fields.FieldBool(value=value)
            )

    @property
    def last_press(self) -> primitives.Double | None:
        """The _lastPress field value."""
        member = self.get_member("_lastPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_press.setter
    def last_press(self, value: primitives.Double) -> None:
        """Set the _lastPress field value."""
        member = self.get_member("_lastPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastPress", fields.FieldDouble(value=value)
            )

