"""Generated component: ButtonAudioDeviceSet."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonAudioDeviceSet(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonAudioDeviceSet.

    Category: Common UI/Button Interactions/Specialized
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonAudioDeviceSet"

    def __init__(self, device_index: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            device_index: Initial value for DeviceIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if device_index is not None:
            self.device_index = device_index

    @property
    def device_index(self) -> np.int32 | None:
        """The DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_index.setter
    def device_index(self, value: np.int32) -> None:
        """Set the DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceIndex", fields.FieldInt(value=value)
            )

