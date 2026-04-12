"""Generated enum: CloudVariableChangeMode."""

from enum import StrEnum


class CloudVariableChangeMode(StrEnum):
    """Enum: [FrooxEngine]FrooxEngine.CloudVariableChangeMode."""

    ignore = "Ignore"
    write_if_owner = "WriteIfOwner"
    always_write = "AlwaysWrite"

