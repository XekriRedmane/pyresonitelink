"""Generated component: OnlineStatusSettings."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class OnlineStatusSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.OnlineStatusSettings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OnlineStatusSettings"

    def __init__(self, remember_timespan: np.float64 | None = None, invisible_remember_timespan: np.float64 | None = None, auto_away_timespan: np.float64 | None = None, enable_default_status: bool | None = None, show_remember_timespan: bool | None = None, show_invisible_remember_timespan: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            remember_timespan: Initial value for RememberTimespan.
            invisible_remember_timespan: Initial value for InvisibleRememberTimespan.
            auto_away_timespan: Initial value for AutoAwayTimespan.
            enable_default_status: Initial value for EnableDefaultStatus.
            show_remember_timespan: Initial value for ShowRememberTimespan.
            show_invisible_remember_timespan: Initial value for ShowInvisibleRememberTimespan.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if remember_timespan is not None:
            self.remember_timespan = remember_timespan
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
    def default_status(self) -> members.FieldEnum | None:
        """The DefaultStatus member."""
        member = self.get_member("DefaultStatus")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @default_status.setter
    def default_status(self, value: members.FieldEnum) -> None:
        """Set the DefaultStatus member."""
        self.set_member("DefaultStatus", value)

    @property
    def remember_mode(self) -> members.FieldEnum | None:
        """The RememberMode member."""
        member = self.get_member("RememberMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @remember_mode.setter
    def remember_mode(self, value: members.FieldEnum) -> None:
        """Set the RememberMode member."""
        self.set_member("RememberMode", value)

    @property
    def remember_timespan(self) -> np.float64 | None:
        """The RememberTimespan field value."""
        member = self.get_member("RememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @remember_timespan.setter
    def remember_timespan(self, value: np.float64) -> None:
        """Set the RememberTimespan field value."""
        member = self.get_member("RememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RememberTimespan", fields.FieldDouble(value=value)
            )

    @property
    def invisible_remember_mode(self) -> members.FieldEnum | None:
        """The InvisibleRememberMode member."""
        member = self.get_member("InvisibleRememberMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @invisible_remember_mode.setter
    def invisible_remember_mode(self, value: members.FieldEnum) -> None:
        """Set the InvisibleRememberMode member."""
        self.set_member("InvisibleRememberMode", value)

    @property
    def invisible_remember_timespan(self) -> np.float64 | None:
        """The InvisibleRememberTimespan field value."""
        member = self.get_member("InvisibleRememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @invisible_remember_timespan.setter
    def invisible_remember_timespan(self, value: np.float64) -> None:
        """Set the InvisibleRememberTimespan field value."""
        member = self.get_member("InvisibleRememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InvisibleRememberTimespan", fields.FieldDouble(value=value)
            )

    @property
    def auto_away_timespan(self) -> np.float64 | None:
        """The AutoAwayTimespan field value."""
        member = self.get_member("AutoAwayTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_away_timespan.setter
    def auto_away_timespan(self, value: np.float64) -> None:
        """Set the AutoAwayTimespan field value."""
        member = self.get_member("AutoAwayTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAwayTimespan", fields.FieldDouble(value=value)
            )

    @property
    def enable_default_status(self) -> bool | None:
        """The EnableDefaultStatus field value."""
        member = self.get_member("EnableDefaultStatus")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enable_default_status.setter
    def enable_default_status(self, value: bool) -> None:
        """Set the EnableDefaultStatus field value."""
        member = self.get_member("EnableDefaultStatus")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnableDefaultStatus", fields.FieldBool(value=value)
            )

    @property
    def show_remember_timespan(self) -> bool | None:
        """The ShowRememberTimespan field value."""
        member = self.get_member("ShowRememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_remember_timespan.setter
    def show_remember_timespan(self, value: bool) -> None:
        """Set the ShowRememberTimespan field value."""
        member = self.get_member("ShowRememberTimespan")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowRememberTimespan", fields.FieldBool(value=value)
            )

    @property
    def show_invisible_remember_timespan(self) -> bool | None:
        """The ShowInvisibleRememberTimespan field value."""
        member = self.get_member("ShowInvisibleRememberTimespan")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_invisible_remember_timespan.setter
    def show_invisible_remember_timespan(self, value: bool) -> None:
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

