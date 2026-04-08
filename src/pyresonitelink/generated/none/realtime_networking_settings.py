"""Generated component: RealtimeNetworkingSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class RealtimeNetworkingSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.RealtimeNetworkingSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RealtimeNetworkingSettings"

    def __init__(self, disable_lan: primitives.Bool | None = None, prefer_steam_networking: primitives.Bool | None = None, prefer_tcp: primitives.Bool | None = None, lnl_window_size: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            disable_lan: Initial value for DisableLAN.
            prefer_steam_networking: Initial value for PreferSteamNetworking.
            prefer_tcp: Initial value for PreferTCP.
            lnl_window_size: Initial value for LNL_WindowSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if disable_lan is not None:
            self.disable_lan = disable_lan
        if prefer_steam_networking is not None:
            self.prefer_steam_networking = prefer_steam_networking
        if prefer_tcp is not None:
            self.prefer_tcp = prefer_tcp
        if lnl_window_size is not None:
            self.lnl_window_size = lnl_window_size

    @property
    def disable_lan(self) -> primitives.Bool | None:
        """The DisableLAN field value."""
        member = self.get_member("DisableLAN")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_lan.setter
    def disable_lan(self, value: primitives.Bool) -> None:
        """Set the DisableLAN field value."""
        member = self.get_member("DisableLAN")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableLAN", fields.FieldBool(value=value)
            )

    @property
    def prefer_steam_networking(self) -> primitives.Bool | None:
        """The PreferSteamNetworking field value."""
        member = self.get_member("PreferSteamNetworking")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @prefer_steam_networking.setter
    def prefer_steam_networking(self, value: primitives.Bool) -> None:
        """Set the PreferSteamNetworking field value."""
        member = self.get_member("PreferSteamNetworking")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreferSteamNetworking", fields.FieldBool(value=value)
            )

    @property
    def prefer_tcp(self) -> primitives.Bool | None:
        """The PreferTCP field value."""
        member = self.get_member("PreferTCP")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @prefer_tcp.setter
    def prefer_tcp(self, value: primitives.Bool) -> None:
        """Set the PreferTCP field value."""
        member = self.get_member("PreferTCP")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreferTCP", fields.FieldBool(value=value)
            )

    @property
    def lnl_window_size(self) -> primitives.Int | None:
        """The LNL_WindowSize field value."""
        member = self.get_member("LNL_WindowSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lnl_window_size.setter
    def lnl_window_size(self, value: primitives.Int) -> None:
        """Set the LNL_WindowSize field value."""
        member = self.get_member("LNL_WindowSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LNL_WindowSize", fields.FieldInt(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

