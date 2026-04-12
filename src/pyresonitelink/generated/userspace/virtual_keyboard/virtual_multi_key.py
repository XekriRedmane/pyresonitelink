"""Generated component: VirtualMultiKey."""

from pyresonitelink.data import members
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VirtualMultiKey(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """This component when triggered by a button event will make the user press all the keys in the multikey at the same time.

    Category: Userspace/Virtual Keyboard

    **Behavior**: The keys do not press in order, and keys will not be pressed more than once if listed more than once.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VirtualMultiKey"

    @property
    def keys(self) -> members.SyncList | None:
        """A list of keys that should be simulated being pressed when receiving a button event and they will be simulated by the source user of the button event."""
        member = self.get_member("Keys")
        if isinstance(member, members.SyncList):
            return member
        return None

    @keys.setter
    def keys(self, value: members.SyncList) -> None:
        """Set Keys. A list of keys that should be simulated being pressed when receiving a button event and they will be simulated by the source user of the button event."""
        self.set_member("Keys", value)

