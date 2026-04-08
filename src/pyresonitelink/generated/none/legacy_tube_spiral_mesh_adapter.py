"""Generated component: LegacyTubeSpiralMeshAdapter."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyTubeSpiralMeshAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyTubeSpiralMeshAdapter.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyTubeSpiralMeshAdapter"

    def __init__(self, upward_trend: np.float32 | None = None, length: np.float32 | None = None, end_point: str | IField[primitives.Float3] | None = None, coil_count: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            upward_trend: Initial value for UpwardTrend.
            length: Initial value for Length.
            end_point: Initial value for EndPoint.
            coil_count: Initial value for CoilCount.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if upward_trend is not None:
            self.upward_trend = upward_trend
        if length is not None:
            self.length = length
        if end_point is not None:
            self.end_point = end_point
        if coil_count is not None:
            self.coil_count = coil_count

    @property
    def upward_trend(self) -> np.float32 | None:
        """The UpwardTrend field value."""
        member = self.get_member("UpwardTrend")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @upward_trend.setter
    def upward_trend(self, value: np.float32) -> None:
        """Set the UpwardTrend field value."""
        member = self.get_member("UpwardTrend")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpwardTrend", fields.FieldFloat(value=value)
            )

    @property
    def length(self) -> np.float32 | None:
        """The Length field value."""
        member = self.get_member("Length")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @length.setter
    def length(self, value: np.float32) -> None:
        """Set the Length field value."""
        member = self.get_member("Length")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Length", fields.FieldFloat(value=value)
            )

    @property
    def end_point(self) -> str | None:
        """Target ID of the EndPoint reference (targets IField[primitives.Float3])."""
        member = self.get_member("EndPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @end_point.setter
    def end_point(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the EndPoint reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("EndPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EndPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def coil_count(self) -> str | None:
        """Target ID of the CoilCount reference (targets IField[np.float32])."""
        member = self.get_member("CoilCount")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @coil_count.setter
    def coil_count(self, target: str | IField[np.float32] | None) -> None:
        """Set the CoilCount reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CoilCount")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CoilCount",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

