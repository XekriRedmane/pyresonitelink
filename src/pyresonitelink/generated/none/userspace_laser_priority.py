"""Generated component: UserspaceLaserPriority."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iuserspace_laser_priority import IUserspaceLaserPriority
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceLaserPriority(GeneratedComponent, IUserspaceLaserPriority, IWorldEventReceiver):
    """The UserspaceLaserPriority component is used in dash space only.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceLaserPriority"

    pass

