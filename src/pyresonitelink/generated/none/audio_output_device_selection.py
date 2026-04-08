"""Generated component: AudioOutputDeviceSelection."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioOutputDeviceSelection(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioOutputDeviceSelection.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioOutputDeviceSelection"

    def __init__(self, selected_device_index: np.int32 | None = None, selected_device_name: str | None = None, device_button_root: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selected_device_index: Initial value for SelectedDeviceIndex.
            selected_device_name: Initial value for SelectedDeviceName.
            device_button_root: Initial value for _deviceButtonRoot.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selected_device_index is not None:
            self.selected_device_index = selected_device_index
        if selected_device_name is not None:
            self.selected_device_name = selected_device_name
        if device_button_root is not None:
            self.device_button_root = device_button_root

    @property
    def selected_device_index(self) -> np.int32 | None:
        """The SelectedDeviceIndex field value."""
        member = self.get_member("SelectedDeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_device_index.setter
    def selected_device_index(self, value: np.int32) -> None:
        """Set the SelectedDeviceIndex field value."""
        member = self.get_member("SelectedDeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedDeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def selected_device_name(self) -> str | None:
        """The SelectedDeviceName field value."""
        member = self.get_member("SelectedDeviceName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_device_name.setter
    def selected_device_name(self, value: str) -> None:
        """Set the SelectedDeviceName field value."""
        member = self.get_member("SelectedDeviceName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedDeviceName", fields.FieldString(value=value)
            )

    @property
    def device_button_root(self) -> str | None:
        """Target ID of the _deviceButtonRoot reference (targets Slot)."""
        member = self.get_member("_deviceButtonRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @device_button_root.setter
    def device_button_root(self, target: str | Slot | None) -> None:
        """Set the _deviceButtonRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_deviceButtonRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_deviceButtonRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

