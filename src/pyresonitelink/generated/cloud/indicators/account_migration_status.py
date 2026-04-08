"""Generated component: AccountMigrationStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AccountMigrationStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AccountMigrationStatus.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AccountMigrationStatus"

    def __init__(self, task_id: primitives.String | None = None, exists: primitives.Bool | None = None, name: primitives.String | None = None, description: primitives.String | None = None, estimated_queue_position: primitives.Int | None = None, start_count: primitives.Int | None = None, created_on: str | None = None, started_on: str | None = None, completed_on: str | None = None, records_per_minute: primitives.Double | None = None, currently_migrating: primitives.String | None = None, current_item: primitives.String | None = None, total_record_count: primitives.Int | None = None, total_migrated_record_count: primitives.Int | None = None, total_failed_record_count: primitives.Int | None = None, total_migrated_variable_count: primitives.Int | None = None, total_migrated_variable_definition_count: primitives.Int | None = None, total_contact_count: primitives.Int | None = None, migrated_contact_count: primitives.Int | None = None, migrated_message_count: primitives.Int | None = None, total_group_count: primitives.Int | None = None, migrated_group_count: primitives.Int | None = None, total_migrated_member_count: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            task_id: Initial value for TaskId.
            exists: Initial value for Exists.
            name: Initial value for Name.
            description: Initial value for Description.
            estimated_queue_position: Initial value for EstimatedQueuePosition.
            start_count: Initial value for StartCount.
            created_on: Initial value for CreatedOn.
            started_on: Initial value for StartedOn.
            completed_on: Initial value for CompletedOn.
            records_per_minute: Initial value for RecordsPerMinute.
            currently_migrating: Initial value for CurrentlyMigrating.
            current_item: Initial value for CurrentItem.
            total_record_count: Initial value for TotalRecordCount.
            total_migrated_record_count: Initial value for TotalMigratedRecordCount.
            total_failed_record_count: Initial value for TotalFailedRecordCount.
            total_migrated_variable_count: Initial value for TotalMigratedVariableCount.
            total_migrated_variable_definition_count: Initial value for TotalMigratedVariableDefinitionCount.
            total_contact_count: Initial value for TotalContactCount.
            migrated_contact_count: Initial value for MigratedContactCount.
            migrated_message_count: Initial value for MigratedMessageCount.
            total_group_count: Initial value for TotalGroupCount.
            migrated_group_count: Initial value for MigratedGroupCount.
            total_migrated_member_count: Initial value for TotalMigratedMemberCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if task_id is not None:
            self.task_id = task_id
        if exists is not None:
            self.exists = exists
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if estimated_queue_position is not None:
            self.estimated_queue_position = estimated_queue_position
        if start_count is not None:
            self.start_count = start_count
        if created_on is not None:
            self.created_on = created_on
        if started_on is not None:
            self.started_on = started_on
        if completed_on is not None:
            self.completed_on = completed_on
        if records_per_minute is not None:
            self.records_per_minute = records_per_minute
        if currently_migrating is not None:
            self.currently_migrating = currently_migrating
        if current_item is not None:
            self.current_item = current_item
        if total_record_count is not None:
            self.total_record_count = total_record_count
        if total_migrated_record_count is not None:
            self.total_migrated_record_count = total_migrated_record_count
        if total_failed_record_count is not None:
            self.total_failed_record_count = total_failed_record_count
        if total_migrated_variable_count is not None:
            self.total_migrated_variable_count = total_migrated_variable_count
        if total_migrated_variable_definition_count is not None:
            self.total_migrated_variable_definition_count = total_migrated_variable_definition_count
        if total_contact_count is not None:
            self.total_contact_count = total_contact_count
        if migrated_contact_count is not None:
            self.migrated_contact_count = migrated_contact_count
        if migrated_message_count is not None:
            self.migrated_message_count = migrated_message_count
        if total_group_count is not None:
            self.total_group_count = total_group_count
        if migrated_group_count is not None:
            self.migrated_group_count = migrated_group_count
        if total_migrated_member_count is not None:
            self.total_migrated_member_count = total_migrated_member_count

    @property
    def task_id(self) -> primitives.String | None:
        """The TaskId field value."""
        member = self.get_member("TaskId")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @task_id.setter
    def task_id(self, value: primitives.String) -> None:
        """Set the TaskId field value."""
        member = self.get_member("TaskId")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TaskId", fields.FieldString(value=value)
            )

    @property
    def exists(self) -> primitives.Bool | None:
        """The Exists field value."""
        member = self.get_member("Exists")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exists.setter
    def exists(self, value: primitives.Bool) -> None:
        """Set the Exists field value."""
        member = self.get_member("Exists")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exists", fields.FieldBool(value=value)
            )

    @property
    def name(self) -> primitives.String | None:
        """The Name field value."""
        member = self.get_member("Name")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @name.setter
    def name(self, value: primitives.String) -> None:
        """Set the Name field value."""
        member = self.get_member("Name")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Name", fields.FieldString(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The Description field value."""
        member = self.get_member("Description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the Description field value."""
        member = self.get_member("Description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Description", fields.FieldString(value=value)
            )

    @property
    def state(self) -> members.FieldEnum | None:
        """The State member."""
        member = self.get_member("State")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @state.setter
    def state(self, value: members.FieldEnum) -> None:
        """Set the State member."""
        self.set_member("State", value)

    @property
    def estimated_queue_position(self) -> primitives.Int | None:
        """The EstimatedQueuePosition field value."""
        member = self.get_member("EstimatedQueuePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @estimated_queue_position.setter
    def estimated_queue_position(self, value: primitives.Int) -> None:
        """Set the EstimatedQueuePosition field value."""
        member = self.get_member("EstimatedQueuePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EstimatedQueuePosition", fields.FieldNullableInt(value=value)
            )

    @property
    def start_count(self) -> primitives.Int | None:
        """The StartCount field value."""
        member = self.get_member("StartCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_count.setter
    def start_count(self, value: primitives.Int) -> None:
        """Set the StartCount field value."""
        member = self.get_member("StartCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartCount", fields.FieldInt(value=value)
            )

    @property
    def created_on(self) -> str | None:
        """The CreatedOn field value."""
        member = self.get_member("CreatedOn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @created_on.setter
    def created_on(self, value: str) -> None:
        """Set the CreatedOn field value."""
        member = self.get_member("CreatedOn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreatedOn", fields.FieldDateTime(value=value)
            )

    @property
    def started_on(self) -> str | None:
        """The StartedOn field value."""
        member = self.get_member("StartedOn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @started_on.setter
    def started_on(self, value: str) -> None:
        """Set the StartedOn field value."""
        member = self.get_member("StartedOn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartedOn", fields.FieldNullableDateTime(value=value)
            )

    @property
    def completed_on(self) -> str | None:
        """The CompletedOn field value."""
        member = self.get_member("CompletedOn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @completed_on.setter
    def completed_on(self, value: str) -> None:
        """Set the CompletedOn field value."""
        member = self.get_member("CompletedOn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CompletedOn", fields.FieldNullableDateTime(value=value)
            )

    @property
    def records_per_minute(self) -> primitives.Double | None:
        """The RecordsPerMinute field value."""
        member = self.get_member("RecordsPerMinute")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @records_per_minute.setter
    def records_per_minute(self, value: primitives.Double) -> None:
        """Set the RecordsPerMinute field value."""
        member = self.get_member("RecordsPerMinute")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RecordsPerMinute", fields.FieldDouble(value=value)
            )

    @property
    def currently_migrating(self) -> primitives.String | None:
        """The CurrentlyMigrating field value."""
        member = self.get_member("CurrentlyMigrating")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @currently_migrating.setter
    def currently_migrating(self, value: primitives.String) -> None:
        """Set the CurrentlyMigrating field value."""
        member = self.get_member("CurrentlyMigrating")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentlyMigrating", fields.FieldString(value=value)
            )

    @property
    def current_item(self) -> primitives.String | None:
        """The CurrentItem field value."""
        member = self.get_member("CurrentItem")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_item.setter
    def current_item(self, value: primitives.String) -> None:
        """Set the CurrentItem field value."""
        member = self.get_member("CurrentItem")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentItem", fields.FieldString(value=value)
            )

    @property
    def total_record_count(self) -> primitives.Int | None:
        """The TotalRecordCount field value."""
        member = self.get_member("TotalRecordCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_record_count.setter
    def total_record_count(self, value: primitives.Int) -> None:
        """Set the TotalRecordCount field value."""
        member = self.get_member("TotalRecordCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalRecordCount", fields.FieldInt(value=value)
            )

    @property
    def total_migrated_record_count(self) -> primitives.Int | None:
        """The TotalMigratedRecordCount field value."""
        member = self.get_member("TotalMigratedRecordCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_migrated_record_count.setter
    def total_migrated_record_count(self, value: primitives.Int) -> None:
        """Set the TotalMigratedRecordCount field value."""
        member = self.get_member("TotalMigratedRecordCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMigratedRecordCount", fields.FieldInt(value=value)
            )

    @property
    def total_failed_record_count(self) -> primitives.Int | None:
        """The TotalFailedRecordCount field value."""
        member = self.get_member("TotalFailedRecordCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_failed_record_count.setter
    def total_failed_record_count(self, value: primitives.Int) -> None:
        """Set the TotalFailedRecordCount field value."""
        member = self.get_member("TotalFailedRecordCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalFailedRecordCount", fields.FieldInt(value=value)
            )

    @property
    def total_migrated_variable_count(self) -> primitives.Int | None:
        """The TotalMigratedVariableCount field value."""
        member = self.get_member("TotalMigratedVariableCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_migrated_variable_count.setter
    def total_migrated_variable_count(self, value: primitives.Int) -> None:
        """Set the TotalMigratedVariableCount field value."""
        member = self.get_member("TotalMigratedVariableCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMigratedVariableCount", fields.FieldInt(value=value)
            )

    @property
    def total_migrated_variable_definition_count(self) -> primitives.Int | None:
        """The TotalMigratedVariableDefinitionCount field value."""
        member = self.get_member("TotalMigratedVariableDefinitionCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_migrated_variable_definition_count.setter
    def total_migrated_variable_definition_count(self, value: primitives.Int) -> None:
        """Set the TotalMigratedVariableDefinitionCount field value."""
        member = self.get_member("TotalMigratedVariableDefinitionCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMigratedVariableDefinitionCount", fields.FieldInt(value=value)
            )

    @property
    def total_contact_count(self) -> primitives.Int | None:
        """The TotalContactCount field value."""
        member = self.get_member("TotalContactCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_contact_count.setter
    def total_contact_count(self, value: primitives.Int) -> None:
        """Set the TotalContactCount field value."""
        member = self.get_member("TotalContactCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalContactCount", fields.FieldInt(value=value)
            )

    @property
    def migrated_contact_count(self) -> primitives.Int | None:
        """The MigratedContactCount field value."""
        member = self.get_member("MigratedContactCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrated_contact_count.setter
    def migrated_contact_count(self, value: primitives.Int) -> None:
        """Set the MigratedContactCount field value."""
        member = self.get_member("MigratedContactCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MigratedContactCount", fields.FieldInt(value=value)
            )

    @property
    def migrated_message_count(self) -> primitives.Int | None:
        """The MigratedMessageCount field value."""
        member = self.get_member("MigratedMessageCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrated_message_count.setter
    def migrated_message_count(self, value: primitives.Int) -> None:
        """Set the MigratedMessageCount field value."""
        member = self.get_member("MigratedMessageCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MigratedMessageCount", fields.FieldInt(value=value)
            )

    @property
    def total_group_count(self) -> primitives.Int | None:
        """The TotalGroupCount field value."""
        member = self.get_member("TotalGroupCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_group_count.setter
    def total_group_count(self, value: primitives.Int) -> None:
        """Set the TotalGroupCount field value."""
        member = self.get_member("TotalGroupCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalGroupCount", fields.FieldInt(value=value)
            )

    @property
    def migrated_group_count(self) -> primitives.Int | None:
        """The MigratedGroupCount field value."""
        member = self.get_member("MigratedGroupCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @migrated_group_count.setter
    def migrated_group_count(self, value: primitives.Int) -> None:
        """Set the MigratedGroupCount field value."""
        member = self.get_member("MigratedGroupCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MigratedGroupCount", fields.FieldInt(value=value)
            )

    @property
    def total_migrated_member_count(self) -> primitives.Int | None:
        """The TotalMigratedMemberCount field value."""
        member = self.get_member("TotalMigratedMemberCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_migrated_member_count.setter
    def total_migrated_member_count(self, value: primitives.Int) -> None:
        """Set the TotalMigratedMemberCount field value."""
        member = self.get_member("TotalMigratedMemberCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalMigratedMemberCount", fields.FieldInt(value=value)
            )

