"""Generated component: AudioOutputDeviceSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioOutputDeviceSettings(GeneratedComponent, ICustomInspector):
    """The AudioOutputDeviceSettings Component is used to set the priority order of output devices for the local user. It also can be used to disable priority and use the system default instead.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioOutputDeviceSettings"

    def __init__(self, use_system_default: primitives.Bool | None = None, device_priorities_enabled: primitives.Bool | None = None, separate_streaming_camera_output: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_system_default: Initial value for UseSystemDefault.
            device_priorities_enabled: Initial value for DevicePrioritiesEnabled.
            separate_streaming_camera_output: Initial value for SeparateStreamingCameraOutput.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_system_default is not None:
            self.use_system_default = use_system_default
        if device_priorities_enabled is not None:
            self.device_priorities_enabled = device_priorities_enabled
        if separate_streaming_camera_output is not None:
            self.separate_streaming_camera_output = separate_streaming_camera_output

    @property
    def use_system_default(self) -> primitives.Bool | None:
        """Whether or not to use the user's default device on their OS or not."""
        member = self.get_member("UseSystemDefault")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_system_default.setter
    def use_system_default(self, value: primitives.Bool) -> None:
        """Set the UseSystemDefault field value."""
        member = self.get_member("UseSystemDefault")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseSystemDefault", fields.FieldBool(value=value)
            )

    @property
    def device_priorities(self) -> members.SyncList | None:
        """A list of devices and their priority which is the order to use them in."""
        member = self.get_member("DevicePriorities")
        if isinstance(member, members.SyncList):
            return member
        return None

    @device_priorities.setter
    def device_priorities(self, value: members.SyncList) -> None:
        """Set DevicePriorities. A list of devices and their priority which is the order to use them in."""
        self.set_member("DevicePriorities", value)

    @property
    def device_priorities_enabled(self) -> primitives.Bool | None:
        """Whether the "Use Default Device" setting is turned on or off"""
        member = self.get_member("DevicePrioritiesEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_priorities_enabled.setter
    def device_priorities_enabled(self, value: primitives.Bool) -> None:
        """Set the DevicePrioritiesEnabled field value."""
        member = self.get_member("DevicePrioritiesEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DevicePrioritiesEnabled", fields.FieldBool(value=value)
            )

    @property
    def separate_streaming_camera_output(self) -> primitives.Bool | None:
        """The SeparateStreamingCameraOutput field value."""
        member = self.get_member("SeparateStreamingCameraOutput")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separate_streaming_camera_output.setter
    def separate_streaming_camera_output(self, value: primitives.Bool) -> None:
        """Set the SeparateStreamingCameraOutput field value."""
        member = self.get_member("SeparateStreamingCameraOutput")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SeparateStreamingCameraOutput", fields.FieldBool(value=value)
            )

    @property
    def streaming_camera_priorities(self) -> members.SyncList | None:
        """The StreamingCameraPriorities member."""
        member = self.get_member("StreamingCameraPriorities")
        if isinstance(member, members.SyncList):
            return member
        return None

    @streaming_camera_priorities.setter
    def streaming_camera_priorities(self, value: members.SyncList) -> None:
        """Set the StreamingCameraPriorities member."""
        self.set_member("StreamingCameraPriorities", value)

    async def get_device(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, debug: bool = False) -> dict:
        """This returns a setting with the name specified by the methods ``key`` input.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GetDevice", {"key": key}, debug,
        )

    async def force_refresh_devices(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ForceRefreshDevices sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ForceRefreshDevices", {}, debug,
        )

    async def get_streaming_device(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, debug: bool = False) -> dict:
        """Call the GetStreamingDevice sync method.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GetStreamingDevice", {"key": key}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

