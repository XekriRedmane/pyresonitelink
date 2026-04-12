"""Generated enum: MigrationState."""

from enum import StrEnum


class MigrationState(StrEnum):
    """Enum: [SkyFrost.Base]SkyFrost.Base.MigrationState."""

    waiting = "Waiting"
    migrating = "Migrating"
    completed = "Completed"
    failed = "Failed"

