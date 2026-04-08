"""Generated component: DeviceIDSettingSwitch."""

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent


class DeviceIDSettingSwitch(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.DeviceIDSettingSwitch.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DeviceIDSettingSwitch"

    def __init__(self, device_id: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            device_id: Initial value for DeviceID.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if device_id is not None:
            self.device_id = device_id

    @property
    def device_id(self) -> str | None:
        """The DeviceID field value."""
        member = self.get_member("DeviceID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_id.setter
    def device_id(self, value: str) -> None:
        """Set the DeviceID field value."""
        member = self.get_member("DeviceID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceID", fields.FieldString(value=value)
            )

