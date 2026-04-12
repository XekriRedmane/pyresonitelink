"""Generated component: AudioStreamSpawner."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AudioStreamSpawner(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The AudioStreamSpawner component is used as part of the dash to spawn a selected audio stream.

    Category: Utility/Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AudioStreamSpawner"

    def __init__(self, bitrate_kbps: primitives.Float | None = None, device_id: primitives.String | None = None, bitrate_string: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bitrate_kbps: Initial value for BitrateKbps.
            device_id: Initial value for DeviceID.
            bitrate_string: Initial value for _bitrateString.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bitrate_kbps is not None:
            self.bitrate_kbps = bitrate_kbps
        if device_id is not None:
            self.device_id = device_id
        if bitrate_string is not None:
            self.bitrate_string = bitrate_string

    @property
    def bitrate_kbps(self) -> primitives.Float | None:
        """The bitrate the audio stream should be"""
        member = self.get_member("BitrateKbps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bitrate_kbps.setter
    def bitrate_kbps(self, value: primitives.Float) -> None:
        """Set the BitrateKbps field value."""
        member = self.get_member("BitrateKbps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BitrateKbps", fields.FieldFloat(value=value)
            )

    @property
    def device_id(self) -> primitives.String | None:
        """the device name of the stream we are spawning"""
        member = self.get_member("DeviceID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @device_id.setter
    def device_id(self, value: primitives.String) -> None:
        """Set the DeviceID field value."""
        member = self.get_member("DeviceID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeviceID", fields.FieldString(value=value)
            )

    @property
    def bitrate_string(self) -> primitives.String | None:
        """The bitrate as a string."""
        member = self.get_member("_bitrateString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bitrate_string.setter
    def bitrate_string(self, value: primitives.String) -> None:
        """Set the _bitrateString field value."""
        member = self.get_member("_bitrateString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_bitrateString", fields.FieldString(value=value)
            )

    async def on_start_streaming(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Triggered by a button in order to spawn the stream in the world.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OnStartStreaming", {"button": button, "eventData": event_data}, debug,
        )

