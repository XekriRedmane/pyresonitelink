"""Generated component: Userspace."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iempty_avatar_slot_handler import IEmptyAvatarSlotHandler
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Userspace(GeneratedComponent, IEmptyAvatarSlotHandler, IWorldEventReceiver):
    """Userspace is a component that manages some of the tasks like exiting, saving, and emergency desktop shortcuts.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Userspace"

    pass

