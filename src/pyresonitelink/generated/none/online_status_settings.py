"""Generated component: OnlineStatusSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.online_status import OnlineStatus
from pyresonitelink.generated._enums.status_remember_mode import StatusRememberMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class OnlineStatusSettings(GeneratedComponent, ICustomInspector):
    """The OnlineStatusSettings component is used to define how online status for the user should be handled.

See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OnlineStatusSettings"

    def __init__(self, default_status: OnlineStatus | str | None = None, remember_mode: StatusRememberMode | str | None = None, remember_timespan: primitives.Double | None = None, invisible_remember_mode: StatusRememberMode | str | None = None, invisible_remember_timespan: primitives.Double | None = None, auto_away_timespan: primitives.Double | None = None, enable_default_status: primitives.Bool | None = None, show_remember_timespan: primitives.Bool | None = None, show_invisible_remember_timespan: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            default_status: Initial value for DefaultStatus.
            remember_mode: Initial value for RememberMode.
            remember_timespan: Initial value for RememberTimespan.
            invisible_remember_mode: Initial value for InvisibleRememberMode.
            invisible_remember_timespan: Initial value for InvisibleRememberTimespan.
            auto_away_timespan: Initial value for AutoAwayTimespan.
            enable_default_status: Initial value for EnableDefaultStatus.
            show_remember_timespan: Initial value for ShowRememberTimespan.
            show_invisible_remember_timespan: Initial value for ShowInvisibleRememberTimespan.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if default_status is not None:
            self.default_status = default_status
        if remember_mode is not None:
            self.remember_mode = remember_mode
        if remember_timespan is not None:
            self.remember_timespan = remember_timespan
        if invisible_remember_mode is not None:
            self.invisible_remember_mode = invisible_remember_mode
        if invisible_remember_timespan is not None:
            self.invisible_remember_timespan = invisible_remember_timespan
        if auto_away_timespan is not None:
            self.auto_away_timespan = auto_away_timespan
        if enable_default_status is not None:
            self.enable_default_status = enable_default_status
        if show_remember_timespan is not None:
            self.show_remember_timespan = show_remember_timespan
        if show_invisible_remember_timespan is not None:
            self.show_invisible_remember_timespan = show_invisible_remember_timespan

    @property
    def default_status(self) -> OnlineStatus | None:
        """The default status for the user when they log in."""
        member = self.get_member("DefaultStatus")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return OnlineStatus(member.value)
        return None

    @default_status.setter
    def default_status(self, value: OnlineStatus | str) -> None:
        """Set DefaultStatus. The default status for the user when they log in."""
        member = self.get_member("DefaultStatus")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DefaultStatus",
                members.FieldEnum(value=str(value)),
            )

    @property
    def remember_mode(self) -> StatusRememberMode | None:
        """Whether the status the user had when they were last on should be remembered."""
        member = self.get_member("RememberMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StatusRememberMode(member.value)
        return None

    @remember_mode.setter
    def remember_mode(self, value: StatusRememberMode | str) -> None:
        """Set RememberMode. Whether the status the user had when they were last on should be remembered."""
        member = self.get_member("RememberMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "RememberMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def remember_timespan(self) -> primitives.Double | None:
        """How long to remember the last status from the previous login before setting back to default again."""
        member = self.get_member("RememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @remember_timespan.setter
    def remember_timespan(self, value: primitives.Double) -> None:
        """Set the RememberTimespan field value."""
        member = self.get_member("RememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RememberTimespan", fields.FieldDouble(value=value)
            )

    @property
    def invisible_remember_mode(self) -> StatusRememberMode | None:
        """How to remember the previous status from the last login."""
        member = self.get_member("InvisibleRememberMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StatusRememberMode(member.value)
        return None

    @invisible_remember_mode.setter
    def invisible_remember_mode(self, value: StatusRememberMode | str) -> None:
        """Set InvisibleRememberMode. How to remember the previous status from the last login."""
        member = self.get_member("InvisibleRememberMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "InvisibleRememberMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def invisible_remember_timespan(self) -> primitives.Double | None:
        """How long to remember a status if it's set to invisible."""
        member = self.get_member("InvisibleRememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @invisible_remember_timespan.setter
    def invisible_remember_timespan(self, value: primitives.Double) -> None:
        """Set the InvisibleRememberTimespan field value."""
        member = self.get_member("InvisibleRememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InvisibleRememberTimespan", fields.FieldDouble(value=value)
            )

    @property
    def auto_away_timespan(self) -> primitives.Double | None:
        """How long to wait when the user is AFK before enabling Away."""
        member = self.get_member("AutoAwayTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_away_timespan.setter
    def auto_away_timespan(self, value: primitives.Double) -> None:
        """Set the AutoAwayTimespan field value."""
        member = self.get_member("AutoAwayTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAwayTimespan", fields.FieldDouble(value=value)
            )

    @property
    def enable_default_status(self) -> primitives.Bool | None:
        """Whether to enable the default status behavior."""
        member = self.get_member("EnableDefaultStatus")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enable_default_status.setter
    def enable_default_status(self, value: primitives.Bool) -> None:
        """Set the EnableDefaultStatus field value."""
        member = self.get_member("EnableDefaultStatus")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnableDefaultStatus", fields.FieldBool(value=value)
            )

    @property
    def show_remember_timespan(self) -> primitives.Bool | None:
        """Whether to show the remember timespan control UI."""
        member = self.get_member("ShowRememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_remember_timespan.setter
    def show_remember_timespan(self, value: primitives.Bool) -> None:
        """Set the ShowRememberTimespan field value."""
        member = self.get_member("ShowRememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowRememberTimespan", fields.FieldBool(value=value)
            )

    @property
    def show_invisible_remember_timespan(self) -> primitives.Bool | None:
        """Whether to show the remember invisible timespan control UI."""
        member = self.get_member("ShowInvisibleRememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_invisible_remember_timespan.setter
    def show_invisible_remember_timespan(self, value: primitives.Bool) -> None:
        """Set the ShowInvisibleRememberTimespan field value."""
        member = self.get_member("ShowInvisibleRememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowInvisibleRememberTimespan", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

