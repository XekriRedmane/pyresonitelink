"""Generated component: AudioInputDeviceInfo."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioInputDeviceInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioInputDeviceInfo.

    Category: Audio/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioInputDeviceInfo"

    def __init__(self, device_index: np.int32 | None = None, device_name: str | None = None, is_app_default: bool | None = None, is_system_default: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            device_index: Initial value for DeviceIndex.
            device_name: Initial value for DeviceName.
            is_app_default: Initial value for IsAppDefault.
            is_system_default: Initial value for IsSystemDefault.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if device_index is not None:
            self.device_index = device_index
        if device_name is not None:
            self.device_name = device_name
        if is_app_default is not None:
            self.is_app_default = is_app_default
        if is_system_default is not None:
            self.is_system_default = is_system_default

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

    @property
    def device_name(self) -> str | None:
        """The DeviceName field value."""
        member = self.get_member("DeviceName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_name.setter
    def device_name(self, value: str) -> None:
        """Set the DeviceName field value."""
        member = self.get_member("DeviceName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceName", fields.FieldString(value=value)
            )

    @property
    def is_app_default(self) -> bool | None:
        """The IsAppDefault field value."""
        member = self.get_member("IsAppDefault")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_app_default.setter
    def is_app_default(self, value: bool) -> None:
        """Set the IsAppDefault field value."""
        member = self.get_member("IsAppDefault")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsAppDefault", fields.FieldBool(value=value)
            )

    @property
    def is_system_default(self) -> bool | None:
        """The IsSystemDefault field value."""
        member = self.get_member("IsSystemDefault")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_system_default.setter
    def is_system_default(self, value: bool) -> None:
        """Set the IsSystemDefault field value."""
        member = self.get_member("IsSystemDefault")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSystemDefault", fields.FieldBool(value=value)
            )

    @property
    def device_type(self) -> members.FieldEnum | None:
        """The DeviceType member."""
        member = self.get_member("DeviceType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @device_type.setter
    def device_type(self, value: members.FieldEnum) -> None:
        """Set the DeviceType member."""
        self.set_member("DeviceType", value)

