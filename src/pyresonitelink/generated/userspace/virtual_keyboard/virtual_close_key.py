"""Generated component: VirtualCloseKey."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.virtual_keyboard import VirtualKeyboard
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualCloseKey(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualCloseKey.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualCloseKey"

    def __init__(self, keyboard: str | VirtualKeyboard | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            keyboard: Initial value for Keyboard.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if keyboard is not None:
            self.keyboard = keyboard

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

