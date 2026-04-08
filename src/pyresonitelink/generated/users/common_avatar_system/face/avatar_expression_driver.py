"""Generated component: AvatarExpressionDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarExpressionDriver(GeneratedComponent, IAvatarObjectComponent, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CommonAvatar.AvatarExpressionDriver.

    Category: Users/Common Avatar System/Face
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarExpressionDriver"

    def __init__(self, data_source: str | IMouthTrackingSourceComponent | None = None, strength_multiplier: primitives.Float | None = None, volume_source: str | IField[primitives.Float] | None = None, silence_source: str | IField[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            data_source: Initial value for DataSource.
            strength_multiplier: Initial value for StrengthMultiplier.
            volume_source: Initial value for VolumeSource.
            silence_source: Initial value for SilenceSource.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if data_source is not None:
            self.data_source = data_source
        if strength_multiplier is not None:
            self.strength_multiplier = strength_multiplier
        if volume_source is not None:
            self.volume_source = volume_source
        if silence_source is not None:
            self.silence_source = silence_source

    @property
    def data_source(self) -> str | None:
        """Target ID of the DataSource reference (targets IMouthTrackingSourceComponent)."""
        member = self.get_member("DataSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @data_source.setter
    def data_source(self, target: str | IMouthTrackingSourceComponent | None) -> None:
        """Set the DataSource reference by target ID or IMouthTrackingSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IMouthTrackingSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("DataSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DataSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IMouthTrackingSourceComponent'),
            )

    @property
    def strength_multiplier(self) -> primitives.Float | None:
        """The StrengthMultiplier field value."""
        member = self.get_member("StrengthMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strength_multiplier.setter
    def strength_multiplier(self, value: primitives.Float) -> None:
        """Set the StrengthMultiplier field value."""
        member = self.get_member("StrengthMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrengthMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def volume_source(self) -> str | None:
        """Target ID of the VolumeSource reference (targets IField[primitives.Float])."""
        member = self.get_member("VolumeSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume_source.setter
    def volume_source(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the VolumeSource reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("VolumeSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "VolumeSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def silence_source(self) -> str | None:
        """Target ID of the SilenceSource reference (targets IField[primitives.Float])."""
        member = self.get_member("SilenceSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @silence_source.setter
    def silence_source(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the SilenceSource reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SilenceSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SilenceSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def expression_drivers(self) -> members.SyncList | None:
        """The ExpressionDrivers member."""
        member = self.get_member("ExpressionDrivers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @expression_drivers.setter
    def expression_drivers(self, value: members.SyncList) -> None:
        """Set the ExpressionDrivers member."""
        self.set_member("ExpressionDrivers", value)

