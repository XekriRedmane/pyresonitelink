"""Generated component: AudioInputDeviceSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioInputDeviceSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.AudioInputDeviceSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioInputDeviceSettings"

    def __init__(self, use_system_default: primitives.Bool | None = None, device_priorities_enabled: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_system_default: Initial value for UseSystemDefault.
            device_priorities_enabled: Initial value for DevicePrioritiesEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_system_default is not None:
            self.use_system_default = use_system_default
        if device_priorities_enabled is not None:
            self.device_priorities_enabled = device_priorities_enabled

    @property
    def use_system_default(self) -> primitives.Bool | None:
        """The UseSystemDefault field value."""
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
        """The DevicePriorities member."""
        member = self.get_member("DevicePriorities")
        if isinstance(member, members.SyncList):
            return member
        return None

    @device_priorities.setter
    def device_priorities(self, value: members.SyncList) -> None:
        """Set the DevicePriorities member."""
        self.set_member("DevicePriorities", value)

    @property
    def device_priorities_enabled(self) -> primitives.Bool | None:
        """The DevicePrioritiesEnabled field value."""
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

    async def get_device(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, debug: bool = False) -> dict:
        """Call the GetDevice sync method.

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

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

