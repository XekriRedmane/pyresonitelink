"""Generated component: VirtualMultiKey."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualMultiKey(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VirtualMultiKey.

    Category: Userspace/Virtual Keyboard
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualMultiKey"

    @property
    def keys(self) -> members.SyncList | None:
        """The Keys member."""
        member = self.get_member("Keys")
        if isinstance(member, members.SyncList):
            return member
        return None

    @keys.setter
    def keys(self, value: members.SyncList) -> None:
        """Set the Keys member."""
        self.set_member("Keys", value)

