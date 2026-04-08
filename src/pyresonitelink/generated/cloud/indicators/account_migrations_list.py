"""Generated component: AccountMigrationsList."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AccountMigrationsList(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AccountMigrationsList.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AccountMigrationsList"

    def __init__(self, total_migrations: np.int32 | None = None, waiting_migrations: np.int32 | None = None, running_migrations: np.int32 | None = None, completed_migrations: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            total_migrations: Initial value for TotalMigrations.
            waiting_migrations: Initial value for WaitingMigrations.
            running_migrations: Initial value for RunningMigrations.
            completed_migrations: Initial value for CompletedMigrations.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if total_migrations is not None:
            self.total_migrations = total_migrations
        if waiting_migrations is not None:
            self.waiting_migrations = waiting_migrations
        if running_migrations is not None:
            self.running_migrations = running_migrations
        if completed_migrations is not None:
            self.completed_migrations = completed_migrations

    @property
    def total_migrations(self) -> np.int32 | None:
        """The TotalMigrations field value."""
        member = self.get_member("TotalMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_migrations.setter
    def total_migrations(self, value: np.int32) -> None:
        """Set the TotalMigrations field value."""
        member = self.get_member("TotalMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMigrations", fields.FieldInt(value=value)
            )

    @property
    def waiting_migrations(self) -> np.int32 | None:
        """The WaitingMigrations field value."""
        member = self.get_member("WaitingMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @waiting_migrations.setter
    def waiting_migrations(self, value: np.int32) -> None:
        """Set the WaitingMigrations field value."""
        member = self.get_member("WaitingMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WaitingMigrations", fields.FieldInt(value=value)
            )

    @property
    def running_migrations(self) -> np.int32 | None:
        """The RunningMigrations field value."""
        member = self.get_member("RunningMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @running_migrations.setter
    def running_migrations(self, value: np.int32) -> None:
        """Set the RunningMigrations field value."""
        member = self.get_member("RunningMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RunningMigrations", fields.FieldInt(value=value)
            )

    @property
    def completed_migrations(self) -> np.int32 | None:
        """The CompletedMigrations field value."""
        member = self.get_member("CompletedMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @completed_migrations.setter
    def completed_migrations(self, value: np.int32) -> None:
        """Set the CompletedMigrations field value."""
        member = self.get_member("CompletedMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompletedMigrations", fields.FieldInt(value=value)
            )

    @property
    def migration_task_ids(self) -> members.SyncList | None:
        """The MigrationTaskIds member."""
        member = self.get_member("MigrationTaskIds")
        if isinstance(member, members.SyncList):
            return member
        return None

    @migration_task_ids.setter
    def migration_task_ids(self, value: members.SyncList) -> None:
        """Set the MigrationTaskIds member."""
        self.set_member("MigrationTaskIds", value)

