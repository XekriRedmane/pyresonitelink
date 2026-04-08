"""Generated component: ProgressBarInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.progress_stage import ProgressStage
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProgressBarInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProgressBarInterface.

    Category: Utility/Entity Interfaces
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProgressBarInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, progress_known: str | IField[primitives.Bool] | None = None, progress: str | IField[primitives.Float] | None = None, processed_count_known: str | IField[primitives.Bool] | None = None, processed_item_count: str | IField[primitives.Int] | None = None, total_item_count_known: str | IField[primitives.Bool] | None = None, total_item_count: str | IField[primitives.Int] | None = None, phase_name: str | IField[primitives.String] | None = None, sub_phase_name: str | IField[primitives.String] | None = None, stage: str | IField[ProgressStage] | None = None, has_completed: str | IField[primitives.Bool] | None = None, has_failed: str | IField[primitives.Bool] | None = None, completion_message: str | IField[primitives.String] | None = None, failure_reason: str | IField[primitives.String] | None = None, can_be_hidden: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            progress_known: Initial value for ProgressKnown.
            progress: Initial value for Progress.
            processed_count_known: Initial value for ProcessedCountKnown.
            processed_item_count: Initial value for ProcessedItemCount.
            total_item_count_known: Initial value for TotalItemCountKnown.
            total_item_count: Initial value for TotalItemCount.
            phase_name: Initial value for PhaseName.
            sub_phase_name: Initial value for SubPhaseName.
            stage: Initial value for Stage.
            has_completed: Initial value for HasCompleted.
            has_failed: Initial value for HasFailed.
            completion_message: Initial value for CompletionMessage.
            failure_reason: Initial value for FailureReason.
            can_be_hidden: Initial value for CanBeHidden.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if item_name is not None:
            self.item_name = item_name
        if spawning_user is not None:
            self.spawning_user = spawning_user
        if spawning_user_id is not None:
            self.spawning_user_id = spawning_user_id
        if is_instance is not None:
            self.is_instance = is_instance
        if progress_known is not None:
            self.progress_known = progress_known
        if progress is not None:
            self.progress = progress
        if processed_count_known is not None:
            self.processed_count_known = processed_count_known
        if processed_item_count is not None:
            self.processed_item_count = processed_item_count
        if total_item_count_known is not None:
            self.total_item_count_known = total_item_count_known
        if total_item_count is not None:
            self.total_item_count = total_item_count
        if phase_name is not None:
            self.phase_name = phase_name
        if sub_phase_name is not None:
            self.sub_phase_name = sub_phase_name
        if stage is not None:
            self.stage = stage
        if has_completed is not None:
            self.has_completed = has_completed
        if has_failed is not None:
            self.has_failed = has_failed
        if completion_message is not None:
            self.completion_message = completion_message
        if failure_reason is not None:
            self.failure_reason = failure_reason
        if can_be_hidden is not None:
            self.can_be_hidden = can_be_hidden

    @property
    def item_name(self) -> str | None:
        """Target ID of the ItemName reference (targets IField[primitives.String])."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def spawning_user(self) -> str | None:
        """Target ID of the SpawningUser reference (targets UserRef)."""
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user.setter
    def spawning_user(self, target: str | UserRef | None) -> None:
        """Set the SpawningUser reference by target ID or UserRef instance."""
        target_id: str | None = target.id if isinstance(target, UserRef) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserRef'),
            )

    @property
    def spawning_user_id(self) -> str | None:
        """Target ID of the SpawningUserID reference (targets IField[primitives.String])."""
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user_id.setter
    def spawning_user_id(self, target: str | IField[primitives.String] | None) -> None:
        """Set the SpawningUserID reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUserID",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def is_instance(self) -> primitives.Bool | None:
        """The IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_instance.setter
    def is_instance(self, value: primitives.Bool) -> None:
        """Set the IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsInstance", fields.FieldBool(value=value)
            )

    @property
    def progress_known(self) -> str | None:
        """Target ID of the ProgressKnown reference (targets IField[primitives.Bool])."""
        member = self.get_member("ProgressKnown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress_known.setter
    def progress_known(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the ProgressKnown reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ProgressKnown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProgressKnown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def progress(self) -> str | None:
        """Target ID of the Progress reference (targets IField[primitives.Float])."""
        member = self.get_member("Progress")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress.setter
    def progress(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Progress reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Progress")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Progress",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def processed_count_known(self) -> str | None:
        """Target ID of the ProcessedCountKnown reference (targets IField[primitives.Bool])."""
        member = self.get_member("ProcessedCountKnown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @processed_count_known.setter
    def processed_count_known(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the ProcessedCountKnown reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ProcessedCountKnown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProcessedCountKnown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def processed_item_count(self) -> str | None:
        """Target ID of the ProcessedItemCount reference (targets IField[primitives.Int])."""
        member = self.get_member("ProcessedItemCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @processed_item_count.setter
    def processed_item_count(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the ProcessedItemCount reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ProcessedItemCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ProcessedItemCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def total_item_count_known(self) -> str | None:
        """Target ID of the TotalItemCountKnown reference (targets IField[primitives.Bool])."""
        member = self.get_member("TotalItemCountKnown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_item_count_known.setter
    def total_item_count_known(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the TotalItemCountKnown reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalItemCountKnown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalItemCountKnown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def total_item_count(self) -> str | None:
        """Target ID of the TotalItemCount reference (targets IField[primitives.Int])."""
        member = self.get_member("TotalItemCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @total_item_count.setter
    def total_item_count(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TotalItemCount reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TotalItemCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TotalItemCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def phase_name(self) -> str | None:
        """Target ID of the PhaseName reference (targets IField[primitives.String])."""
        member = self.get_member("PhaseName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @phase_name.setter
    def phase_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the PhaseName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PhaseName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PhaseName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def sub_phase_name(self) -> str | None:
        """Target ID of the SubPhaseName reference (targets IField[primitives.String])."""
        member = self.get_member("SubPhaseName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @sub_phase_name.setter
    def sub_phase_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the SubPhaseName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SubPhaseName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SubPhaseName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def stage(self) -> str | None:
        """Target ID of the Stage reference (targets IField[ProgressStage])."""
        member = self.get_member("Stage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @stage.setter
    def stage(self, target: str | IField[ProgressStage] | None) -> None:
        """Set the Stage reference by target ID or IField[ProgressStage] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Stage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Stage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[FrooxEngine]FrooxEngine.ProgressStage>'),
            )

    @property
    def has_completed(self) -> str | None:
        """Target ID of the HasCompleted reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasCompleted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_completed.setter
    def has_completed(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasCompleted reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasCompleted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasCompleted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def has_failed(self) -> str | None:
        """Target ID of the HasFailed reference (targets IField[primitives.Bool])."""
        member = self.get_member("HasFailed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @has_failed.setter
    def has_failed(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the HasFailed reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("HasFailed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HasFailed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def completion_message(self) -> str | None:
        """Target ID of the CompletionMessage reference (targets IField[primitives.String])."""
        member = self.get_member("CompletionMessage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @completion_message.setter
    def completion_message(self, target: str | IField[primitives.String] | None) -> None:
        """Set the CompletionMessage reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CompletionMessage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CompletionMessage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def failure_reason(self) -> str | None:
        """Target ID of the FailureReason reference (targets IField[primitives.String])."""
        member = self.get_member("FailureReason")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @failure_reason.setter
    def failure_reason(self, target: str | IField[primitives.String] | None) -> None:
        """Set the FailureReason reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FailureReason")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FailureReason",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def can_be_hidden(self) -> str | None:
        """Target ID of the CanBeHidden reference (targets IField[primitives.Bool])."""
        member = self.get_member("CanBeHidden")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @can_be_hidden.setter
    def can_be_hidden(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the CanBeHidden reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CanBeHidden")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CanBeHidden",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

