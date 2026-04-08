"""Generated component: RecordSyncStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RecordSyncStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RecordSyncStatus.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RecordSyncStatus"

    def __init__(self, record_queue_count: primitives.Int | None = None, asset_variant_queue_count: primitives.Int | None = None, current_task_progress: primitives.Float | None = None, last_error: primitives.String | None = None, status_message: primitives.String | None = None, fully_synced_color: primitives.ColorX | None = None, error_color: primitives.ColorX | None = None, syncing_records_color: primitives.ColorX | None = None, uploading_asset_variants_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            record_queue_count: Initial value for RecordQueueCount.
            asset_variant_queue_count: Initial value for AssetVariantQueueCount.
            current_task_progress: Initial value for CurrentTaskProgress.
            last_error: Initial value for LastError.
            status_message: Initial value for StatusMessage.
            fully_synced_color: Initial value for FullySyncedColor.
            error_color: Initial value for ErrorColor.
            syncing_records_color: Initial value for SyncingRecordsColor.
            uploading_asset_variants_color: Initial value for UploadingAssetVariantsColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if record_queue_count is not None:
            self.record_queue_count = record_queue_count
        if asset_variant_queue_count is not None:
            self.asset_variant_queue_count = asset_variant_queue_count
        if current_task_progress is not None:
            self.current_task_progress = current_task_progress
        if last_error is not None:
            self.last_error = last_error
        if status_message is not None:
            self.status_message = status_message
        if fully_synced_color is not None:
            self.fully_synced_color = fully_synced_color
        if error_color is not None:
            self.error_color = error_color
        if syncing_records_color is not None:
            self.syncing_records_color = syncing_records_color
        if uploading_asset_variants_color is not None:
            self.uploading_asset_variants_color = uploading_asset_variants_color

    @property
    def record_queue_count(self) -> primitives.Int | None:
        """The RecordQueueCount field value."""
        member = self.get_member("RecordQueueCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @record_queue_count.setter
    def record_queue_count(self, value: primitives.Int) -> None:
        """Set the RecordQueueCount field value."""
        member = self.get_member("RecordQueueCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RecordQueueCount", fields.FieldInt(value=value)
            )

    @property
    def asset_variant_queue_count(self) -> primitives.Int | None:
        """The AssetVariantQueueCount field value."""
        member = self.get_member("AssetVariantQueueCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @asset_variant_queue_count.setter
    def asset_variant_queue_count(self, value: primitives.Int) -> None:
        """Set the AssetVariantQueueCount field value."""
        member = self.get_member("AssetVariantQueueCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AssetVariantQueueCount", fields.FieldInt(value=value)
            )

    @property
    def current_task_progress(self) -> primitives.Float | None:
        """The CurrentTaskProgress field value."""
        member = self.get_member("CurrentTaskProgress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @current_task_progress.setter
    def current_task_progress(self, value: primitives.Float) -> None:
        """Set the CurrentTaskProgress field value."""
        member = self.get_member("CurrentTaskProgress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CurrentTaskProgress", fields.FieldFloat(value=value)
            )

    @property
    def last_error(self) -> primitives.String | None:
        """The LastError field value."""
        member = self.get_member("LastError")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_error.setter
    def last_error(self, value: primitives.String) -> None:
        """Set the LastError field value."""
        member = self.get_member("LastError")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LastError", fields.FieldString(value=value)
            )

    @property
    def status_message(self) -> primitives.String | None:
        """The StatusMessage field value."""
        member = self.get_member("StatusMessage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @status_message.setter
    def status_message(self, value: primitives.String) -> None:
        """Set the StatusMessage field value."""
        member = self.get_member("StatusMessage")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StatusMessage", fields.FieldString(value=value)
            )

    @property
    def fully_synced_color(self) -> primitives.ColorX | None:
        """The FullySyncedColor field value."""
        member = self.get_member("FullySyncedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fully_synced_color.setter
    def fully_synced_color(self, value: primitives.ColorX) -> None:
        """Set the FullySyncedColor field value."""
        member = self.get_member("FullySyncedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullySyncedColor", fields.FieldColorX(value=value)
            )

    @property
    def error_color(self) -> primitives.ColorX | None:
        """The ErrorColor field value."""
        member = self.get_member("ErrorColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @error_color.setter
    def error_color(self, value: primitives.ColorX) -> None:
        """Set the ErrorColor field value."""
        member = self.get_member("ErrorColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ErrorColor", fields.FieldColorX(value=value)
            )

    @property
    def syncing_records_color(self) -> primitives.ColorX | None:
        """The SyncingRecordsColor field value."""
        member = self.get_member("SyncingRecordsColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @syncing_records_color.setter
    def syncing_records_color(self, value: primitives.ColorX) -> None:
        """Set the SyncingRecordsColor field value."""
        member = self.get_member("SyncingRecordsColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SyncingRecordsColor", fields.FieldColorX(value=value)
            )

    @property
    def uploading_asset_variants_color(self) -> primitives.ColorX | None:
        """The UploadingAssetVariantsColor field value."""
        member = self.get_member("UploadingAssetVariantsColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @uploading_asset_variants_color.setter
    def uploading_asset_variants_color(self, value: primitives.ColorX) -> None:
        """Set the UploadingAssetVariantsColor field value."""
        member = self.get_member("UploadingAssetVariantsColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UploadingAssetVariantsColor", fields.FieldColorX(value=value)
            )

