"""Generated component: ValueGraphRecorder."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sync_array import SyncArray
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ValueGraphRecorder(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ValueGraphRecorder.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ValueGraphRecorder"

    def __init__(self, source_value: str | IField[primitives.Float] | None = None, update_interval: primitives.Float | None = None, points: primitives.Int | None = None, target_array: str | SyncArray[primitives.Float] | None = None, target_array_offset: str | IField[primitives.Int] | None = None, min_range_adjust_threshold: primitives.Float | None = None, min_range_adjust_multiplier: primitives.Float | None = None, max_range_adjust_threshold: primitives.Float | None = None, max_range_adjust_multiplier: primitives.Float | None = None, range_min: str | IField[primitives.Float] | None = None, range_max: str | IField[primitives.Float] | None = None, drive: primitives.Bool | None = None, array_drive: str | SyncArray[primitives.Float] | None = None, array_offset_drive: str | IField[primitives.Int] | None = None, range_min_drive: str | IField[primitives.Float] | None = None, range_max_drive: str | IField[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source_value: Initial value for SourceValue.
            update_interval: Initial value for UpdateInterval.
            points: Initial value for Points.
            target_array: Initial value for TargetArray.
            target_array_offset: Initial value for TargetArrayOffset.
            min_range_adjust_threshold: Initial value for MinRangeAdjustThreshold.
            min_range_adjust_multiplier: Initial value for MinRangeAdjustMultiplier.
            max_range_adjust_threshold: Initial value for MaxRangeAdjustThreshold.
            max_range_adjust_multiplier: Initial value for MaxRangeAdjustMultiplier.
            range_min: Initial value for RangeMin.
            range_max: Initial value for RangeMax.
            drive: Initial value for Drive.
            array_drive: Initial value for _arrayDrive.
            array_offset_drive: Initial value for _arrayOffsetDrive.
            range_min_drive: Initial value for _rangeMinDrive.
            range_max_drive: Initial value for _rangeMaxDrive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source_value is not None:
            self.source_value = source_value
        if update_interval is not None:
            self.update_interval = update_interval
        if points is not None:
            self.points = points
        if target_array is not None:
            self.target_array = target_array
        if target_array_offset is not None:
            self.target_array_offset = target_array_offset
        if min_range_adjust_threshold is not None:
            self.min_range_adjust_threshold = min_range_adjust_threshold
        if min_range_adjust_multiplier is not None:
            self.min_range_adjust_multiplier = min_range_adjust_multiplier
        if max_range_adjust_threshold is not None:
            self.max_range_adjust_threshold = max_range_adjust_threshold
        if max_range_adjust_multiplier is not None:
            self.max_range_adjust_multiplier = max_range_adjust_multiplier
        if range_min is not None:
            self.range_min = range_min
        if range_max is not None:
            self.range_max = range_max
        if drive is not None:
            self.drive = drive
        if array_drive is not None:
            self.array_drive = array_drive
        if array_offset_drive is not None:
            self.array_offset_drive = array_offset_drive
        if range_min_drive is not None:
            self.range_min_drive = range_min_drive
        if range_max_drive is not None:
            self.range_max_drive = range_max_drive

    @property
    def recording_user(self) -> members.SyncObject | None:
        """The RecordingUser member."""
        member = self.get_member("RecordingUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @recording_user.setter
    def recording_user(self, value: members.SyncObject) -> None:
        """Set the RecordingUser member."""
        self.set_member("RecordingUser", value)

    @property
    def source_value(self) -> str | None:
        """Target ID of the SourceValue reference (targets IField[primitives.Float])."""
        member = self.get_member("SourceValue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_value.setter
    def source_value(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the SourceValue reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SourceValue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceValue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def update_interval(self) -> primitives.Float | None:
        """The UpdateInterval field value."""
        member = self.get_member("UpdateInterval")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_interval.setter
    def update_interval(self, value: primitives.Float) -> None:
        """Set the UpdateInterval field value."""
        member = self.get_member("UpdateInterval")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateInterval", fields.FieldFloat(value=value)
            )

    @property
    def points(self) -> primitives.Int | None:
        """The Points field value."""
        member = self.get_member("Points")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @points.setter
    def points(self, value: primitives.Int) -> None:
        """Set the Points field value."""
        member = self.get_member("Points")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Points", fields.FieldInt(value=value)
            )

    @property
    def target_array(self) -> str | None:
        """Target ID of the TargetArray reference (targets SyncArray[primitives.Float])."""
        member = self.get_member("TargetArray")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_array.setter
    def target_array(self, target: str | SyncArray[primitives.Float] | None) -> None:
        """Set the TargetArray reference by target ID or SyncArray[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, SyncArray) else target  # type: ignore[assignment]
        member = self.get_member("TargetArray")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetArray",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncArray<float>'),
            )

    @property
    def target_array_offset(self) -> str | None:
        """Target ID of the TargetArrayOffset reference (targets IField[primitives.Int])."""
        member = self.get_member("TargetArrayOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_array_offset.setter
    def target_array_offset(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the TargetArrayOffset reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TargetArrayOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetArrayOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def min_range_adjust_threshold(self) -> primitives.Float | None:
        """The MinRangeAdjustThreshold field value."""
        member = self.get_member("MinRangeAdjustThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_range_adjust_threshold.setter
    def min_range_adjust_threshold(self, value: primitives.Float) -> None:
        """Set the MinRangeAdjustThreshold field value."""
        member = self.get_member("MinRangeAdjustThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinRangeAdjustThreshold", fields.FieldFloat(value=value)
            )

    @property
    def min_range_adjust_multiplier(self) -> primitives.Float | None:
        """The MinRangeAdjustMultiplier field value."""
        member = self.get_member("MinRangeAdjustMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_range_adjust_multiplier.setter
    def min_range_adjust_multiplier(self, value: primitives.Float) -> None:
        """Set the MinRangeAdjustMultiplier field value."""
        member = self.get_member("MinRangeAdjustMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinRangeAdjustMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def max_range_adjust_threshold(self) -> primitives.Float | None:
        """The MaxRangeAdjustThreshold field value."""
        member = self.get_member("MaxRangeAdjustThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_range_adjust_threshold.setter
    def max_range_adjust_threshold(self, value: primitives.Float) -> None:
        """Set the MaxRangeAdjustThreshold field value."""
        member = self.get_member("MaxRangeAdjustThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRangeAdjustThreshold", fields.FieldFloat(value=value)
            )

    @property
    def max_range_adjust_multiplier(self) -> primitives.Float | None:
        """The MaxRangeAdjustMultiplier field value."""
        member = self.get_member("MaxRangeAdjustMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_range_adjust_multiplier.setter
    def max_range_adjust_multiplier(self, value: primitives.Float) -> None:
        """Set the MaxRangeAdjustMultiplier field value."""
        member = self.get_member("MaxRangeAdjustMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxRangeAdjustMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def range_min(self) -> str | None:
        """Target ID of the RangeMin reference (targets IField[primitives.Float])."""
        member = self.get_member("RangeMin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @range_min.setter
    def range_min(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the RangeMin reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RangeMin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RangeMin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def range_max(self) -> str | None:
        """Target ID of the RangeMax reference (targets IField[primitives.Float])."""
        member = self.get_member("RangeMax")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @range_max.setter
    def range_max(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the RangeMax reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RangeMax")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RangeMax",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def drive(self) -> primitives.Bool | None:
        """The Drive field value."""
        member = self.get_member("Drive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drive.setter
    def drive(self, value: primitives.Bool) -> None:
        """Set the Drive field value."""
        member = self.get_member("Drive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Drive", fields.FieldBool(value=value)
            )

    @property
    def array_drive(self) -> str | None:
        """Target ID of the _arrayDrive reference (targets SyncArray[primitives.Float])."""
        member = self.get_member("_arrayDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @array_drive.setter
    def array_drive(self, target: str | SyncArray[primitives.Float] | None) -> None:
        """Set the _arrayDrive reference by target ID or SyncArray[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, SyncArray) else target  # type: ignore[assignment]
        member = self.get_member("_arrayDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrayDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncArray<float>'),
            )

    @property
    def array_offset_drive(self) -> str | None:
        """Target ID of the _arrayOffsetDrive reference (targets IField[primitives.Int])."""
        member = self.get_member("_arrayOffsetDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @array_offset_drive.setter
    def array_offset_drive(self, target: str | IField[primitives.Int] | None) -> None:
        """Set the _arrayOffsetDrive reference by target ID or IField[primitives.Int] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arrayOffsetDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrayOffsetDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<int>'),
            )

    @property
    def range_min_drive(self) -> str | None:
        """Target ID of the _rangeMinDrive reference (targets IField[primitives.Float])."""
        member = self.get_member("_rangeMinDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @range_min_drive.setter
    def range_min_drive(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _rangeMinDrive reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rangeMinDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rangeMinDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def range_max_drive(self) -> str | None:
        """Target ID of the _rangeMaxDrive reference (targets IField[primitives.Float])."""
        member = self.get_member("_rangeMaxDrive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @range_max_drive.setter
    def range_max_drive(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _rangeMaxDrive reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_rangeMaxDrive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_rangeMaxDrive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    async def write_value(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the WriteValue sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "WriteValue", {}, debug,
        )

