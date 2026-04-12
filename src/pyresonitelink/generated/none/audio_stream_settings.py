"""Generated component: AudioStreamSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class AudioStreamSettings(GeneratedComponent, ICustomInspector):
    """The AudioStreamSettings component is a Legacy component used for the old settings menu.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioStreamSettings"

    def __init__(self, default_bitrate: primitives.Float | None = None, default_device_id: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default_bitrate: Initial value for DefaultBitrate.
            default_device_id: Initial value for DefaultDeviceID.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default_bitrate is not None:
            self.default_bitrate = default_bitrate
        if default_device_id is not None:
            self.default_device_id = default_device_id

    @property
    def default_bitrate(self) -> primitives.Float | None:
        """The default bit rate for this Audio stream when spawned by the user."""
        member = self.get_member("DefaultBitrate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_bitrate.setter
    def default_bitrate(self, value: primitives.Float) -> None:
        """Set the DefaultBitrate field value."""
        member = self.get_member("DefaultBitrate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultBitrate", fields.FieldFloat(value=value)
            )

    @property
    def default_device_id(self) -> primitives.String | None:
        """The default device ID."""
        member = self.get_member("DefaultDeviceID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_device_id.setter
    def default_device_id(self, value: primitives.String) -> None:
        """Set the DefaultDeviceID field value."""
        member = self.get_member("DefaultDeviceID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DefaultDeviceID", fields.FieldString(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

