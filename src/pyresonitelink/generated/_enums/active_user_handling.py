"""Generated enum: ActiveUserHandling."""

from enum import StrEnum


class ActiveUserHandling(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.ActiveUserHandling."""

    disabled = "Disabled"
    only_active_user = "OnlyActiveUser"
    active_user_when_present = "ActiveUserWhenPresent"
    exclude_active_user = "ExcludeActiveUser"

