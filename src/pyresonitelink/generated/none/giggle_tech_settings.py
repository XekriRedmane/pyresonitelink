"""Generated component: GiggleTechSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class GiggleTechSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.GiggleTechSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GiggleTechSettings"

    def __init__(self, giggle_puck_ip: primitives.String | None = None, is_giggle_puck_valid: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            giggle_puck_ip: Initial value for GigglePuckIP.
            is_giggle_puck_valid: Initial value for IsGigglePuckValid.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if giggle_puck_ip is not None:
            self.giggle_puck_ip = giggle_puck_ip
        if is_giggle_puck_valid is not None:
            self.is_giggle_puck_valid = is_giggle_puck_valid

    @property
    def devices(self) -> members.SyncList | None:
        """The Devices member."""
        member = self.get_member("Devices")
        if isinstance(member, members.SyncList):
            return member
        return None

    @devices.setter
    def devices(self, value: members.SyncList) -> None:
        """Set the Devices member."""
        self.set_member("Devices", value)

    @property
    def giggle_puck_ip(self) -> primitives.String | None:
        """The GigglePuckIP field value."""
        member = self.get_member("GigglePuckIP")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @giggle_puck_ip.setter
    def giggle_puck_ip(self, value: primitives.String) -> None:
        """Set the GigglePuckIP field value."""
        member = self.get_member("GigglePuckIP")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GigglePuckIP", fields.FieldString(value=value)
            )

    @property
    def is_giggle_puck_valid(self) -> primitives.Bool | None:
        """The IsGigglePuckValid field value."""
        member = self.get_member("IsGigglePuckValid")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_giggle_puck_valid.setter
    def is_giggle_puck_valid(self, value: primitives.Bool) -> None:
        """Set the IsGigglePuckValid field value."""
        member = self.get_member("IsGigglePuckValid")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsGigglePuckValid", fields.FieldBool(value=value)
            )

    async def register_giggle_puck(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the RegisterGigglePuck sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RegisterGigglePuck", {}, debug,
        )

    async def get_device_for_subsetting(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, debug: bool = False) -> dict:
        """Call the GetDeviceForSubsetting sync method.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GetDeviceForSubsetting", {"key": key}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

