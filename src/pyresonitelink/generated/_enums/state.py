"""Generated enum: State."""

from enum import StrEnum


class State(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.TOTP_Dialog+State."""

    initializing = "Initializing"
    setup_auth = "SetupAuth"
    save_recovery_codes = "SaveRecoveryCodes"
    activate = "Activate"
    deactivate = "Deactivate"
    message = "Message"

