"""Generated component: VirtualModifierKey."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_keyboard import VirtualKeyboard
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualModifierKey(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualModifierKey.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualModifierKey"

    def __init__(self, keyboard: str | VirtualKeyboard | None = None, state: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            keyboard: Initial value for Keyboard.
            state: Initial value for State.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if keyboard is not None:
            self.keyboard = keyboard
        if state is not None:
            self.state = state

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
    def state(self) -> primitives.Bool | None:
        """The State field value."""
        member = self.get_member("State")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @state.setter
    def state(self, value: primitives.Bool) -> None:
        """Set the State field value."""
        member = self.get_member("State")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "State", fields.FieldBool(value=value)
            )

