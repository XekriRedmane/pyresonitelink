"""Generated component: AudioInputDeviceInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.audio_input_type import AudioInputType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioInputDeviceInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AudioDeviceIndexFinder component only works in user space, and is used to find an audio device by name and get info about it.

    Category: Audio/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioInputDeviceInfo"

    def __init__(self, device_index: primitives.Int | None = None, device_name: primitives.String | None = None, is_app_default: primitives.Bool | None = None, is_system_default: primitives.Bool | None = None, device_type: AudioInputType | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            device_index: Initial value for DeviceIndex.
            device_name: Initial value for DeviceName.
            is_app_default: Initial value for IsAppDefault.
            is_system_default: Initial value for IsSystemDefault.
            device_type: Initial value for DeviceType.
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
        if device_type is not None:
            self.device_type = device_type

    @property
    def device_index(self) -> primitives.Int | None:
        """The device index if found"""
        member = self.get_member("DeviceIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_index.setter
    def device_index(self, value: primitives.Int) -> None:
        """Set the DeviceIndex field value."""
        member = self.get_member("DeviceIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceIndex", fields.FieldInt(value=value)
            )

    @property
    def device_name(self) -> primitives.String | None:
        """the name to use when looking for a device"""
        member = self.get_member("DeviceName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_name.setter
    def device_name(self, value: primitives.String) -> None:
        """Set the DeviceName field value."""
        member = self.get_member("DeviceName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceName", fields.FieldString(value=value)
            )

    @property
    def is_app_default(self) -> primitives.Bool | None:
        """Whether this device is resonite's current default"""
        member = self.get_member("IsAppDefault")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_app_default.setter
    def is_app_default(self, value: primitives.Bool) -> None:
        """Set the IsAppDefault field value."""
        member = self.get_member("IsAppDefault")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsAppDefault", fields.FieldBool(value=value)
            )

    @property
    def is_system_default(self) -> primitives.Bool | None:
        """Whether this device is the user's OS current default"""
        member = self.get_member("IsSystemDefault")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_system_default.setter
    def is_system_default(self, value: primitives.Bool) -> None:
        """Set the IsSystemDefault field value."""
        member = self.get_member("IsSystemDefault")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSystemDefault", fields.FieldBool(value=value)
            )

    @property
    def device_type(self) -> AudioInputType | None:
        """The type of audio device this is."""
        member = self.get_member("DeviceType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AudioInputType(member.value)
        return None

    @device_type.setter
    def device_type(self, value: AudioInputType | str) -> None:
        """Set DeviceType. The type of audio device this is."""
        member = self.get_member("DeviceType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DeviceType",
                members.FieldEnum(value=str(value)),
            )

