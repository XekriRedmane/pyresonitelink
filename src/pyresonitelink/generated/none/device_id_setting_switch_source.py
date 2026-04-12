"""Generated component: DeviceIDSettingSwitchSource."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DeviceIDSettingSwitchSource(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DeviceIDSettingSwitchSource component is used to switch setting sets when a different device is used in conjunction with a DeviceIDSettingSwitch

    Used as part of the settings system. Not usually used directly by the
    user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DeviceIDSettingSwitchSource"

    pass

