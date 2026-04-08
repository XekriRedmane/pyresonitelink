"""Generated component: RelaySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class RelaySettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.RelaySettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RelaySettings"

    def __init__(self, always_use_relay: primitives.Bool | None = None, use_closest_available_relay: primitives.Bool | None = None, relay_priorities_enabled: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            always_use_relay: Initial value for AlwaysUseRelay.
            use_closest_available_relay: Initial value for UseClosestAvailableRelay.
            relay_priorities_enabled: Initial value for RelayPrioritiesEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if always_use_relay is not None:
            self.always_use_relay = always_use_relay
        if use_closest_available_relay is not None:
            self.use_closest_available_relay = use_closest_available_relay
        if relay_priorities_enabled is not None:
            self.relay_priorities_enabled = relay_priorities_enabled

    @property
    def always_use_relay(self) -> primitives.Bool | None:
        """The AlwaysUseRelay field value."""
        member = self.get_member("AlwaysUseRelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @always_use_relay.setter
    def always_use_relay(self, value: primitives.Bool) -> None:
        """Set the AlwaysUseRelay field value."""
        member = self.get_member("AlwaysUseRelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlwaysUseRelay", fields.FieldBool(value=value)
            )

    @property
    def use_closest_available_relay(self) -> primitives.Bool | None:
        """The UseClosestAvailableRelay field value."""
        member = self.get_member("UseClosestAvailableRelay")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_closest_available_relay.setter
    def use_closest_available_relay(self, value: primitives.Bool) -> None:
        """Set the UseClosestAvailableRelay field value."""
        member = self.get_member("UseClosestAvailableRelay")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseClosestAvailableRelay", fields.FieldBool(value=value)
            )

    @property
    def relay_priorities(self) -> members.SyncList | None:
        """The RelayPriorities member."""
        member = self.get_member("RelayPriorities")
        if isinstance(member, members.SyncList):
            return member
        return None

    @relay_priorities.setter
    def relay_priorities(self, value: members.SyncList) -> None:
        """Set the RelayPriorities member."""
        self.set_member("RelayPriorities", value)

    @property
    def relay_priorities_enabled(self) -> primitives.Bool | None:
        """The RelayPrioritiesEnabled field value."""
        member = self.get_member("RelayPrioritiesEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @relay_priorities_enabled.setter
    def relay_priorities_enabled(self, value: primitives.Bool) -> None:
        """Set the RelayPrioritiesEnabled field value."""
        member = self.get_member("RelayPrioritiesEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RelayPrioritiesEnabled", fields.FieldBool(value=value)
            )

    async def get_entry(self, resolink: protocols.ResoniteLinkClient, key: primitives.String, debug: bool = False) -> dict:
        """Call the GetEntry sync method.

        Args:
            resolink: Connected ResoniteLink client.
            key: The key parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "GetEntry", {"key": key}, debug,
        )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

