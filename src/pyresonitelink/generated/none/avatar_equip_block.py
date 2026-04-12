"""Generated component: AvatarEquipBlock."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarEquipBlock(GeneratedComponent, IComponent, IWorldEventReceiver):
    """AvatarEquipBlock prevents anyone from equipping an avatar. Place at the avatar's root.

This works to block both in-world equipping and equipping from inventory.

CAUTION: When attempting to equip from inventory results in user being in no avatar.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarEquipBlock"

    pass

