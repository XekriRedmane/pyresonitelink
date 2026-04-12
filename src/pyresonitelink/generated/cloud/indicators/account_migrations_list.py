"""Generated component: AccountMigrationsList."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AccountMigrationsList(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Account Migrations List is a component that only works in user space. It checks the current Migrations being ran by the cloud and gives a running count every game update. It shows how many there are total including counts of different statuses the different migrations have.

    Category: Cloud/Indicators

    **Behavior**: Only works in user space. Updates with migrations automatically.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AccountMigrationsList"

    def __init__(self, total_migrations: primitives.Int | None = None, waiting_migrations: primitives.Int | None = None, running_migrations: primitives.Int | None = None, completed_migrations: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
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
    def total_migrations(self) -> primitives.Int | None:
        """How many total migrations are currently happening on the cloud right now for the current user."""
        member = self.get_member("TotalMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_migrations.setter
    def total_migrations(self, value: primitives.Int) -> None:
        """Set the TotalMigrations field value."""
        member = self.get_member("TotalMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMigrations", fields.FieldInt(value=value)
            )

    @property
    def waiting_migrations(self) -> primitives.Int | None:
        """How many migrations are currently waiting to start on the cloud right now for the current user."""
        member = self.get_member("WaitingMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @waiting_migrations.setter
    def waiting_migrations(self, value: primitives.Int) -> None:
        """Set the WaitingMigrations field value."""
        member = self.get_member("WaitingMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WaitingMigrations", fields.FieldInt(value=value)
            )

    @property
    def running_migrations(self) -> primitives.Int | None:
        """How many migrations are currently happening on the cloud right now for the current user."""
        member = self.get_member("RunningMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @running_migrations.setter
    def running_migrations(self, value: primitives.Int) -> None:
        """Set the RunningMigrations field value."""
        member = self.get_member("RunningMigrations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RunningMigrations", fields.FieldInt(value=value)
            )

    @property
    def completed_migrations(self) -> primitives.Int | None:
        """How many completed migrations have happened on the cloud before for the current user."""
        member = self.get_member("CompletedMigrations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @completed_migrations.setter
    def completed_migrations(self, value: primitives.Int) -> None:
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
        """The task ID's of all the migrations for the current user."""
        member = self.get_member("MigrationTaskIds")
        if isinstance(member, members.SyncList):
            return member
        return None

    @migration_task_ids.setter
    def migration_task_ids(self, value: members.SyncList) -> None:
        """Set MigrationTaskIds. The task ID's of all the migrations for the current user."""
        self.set_member("MigrationTaskIds", value)

