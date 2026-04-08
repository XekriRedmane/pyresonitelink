"""Generated component: AxisPanner."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisPanner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AxisPanner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisPanner"

    def __init__(self, time_base: str | IValue[np.float64] | None = None, speed: np.float32 | None = None, range_: np.float32 | None = None, offset: primitives.Float3 | None = None, axis: primitives.Float3 | None = None, reference_scale: primitives.Float3 | None = None, full_scale_range_ratio: np.float32 | None = None, position: str | IField[primitives.Float3] | None = None, scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            time_base: Initial value for TimeBase.
            speed: Initial value for Speed.
            range_: Initial value for Range.
            offset: Initial value for Offset.
            axis: Initial value for Axis.
            reference_scale: Initial value for ReferenceScale.
            full_scale_range_ratio: Initial value for FullScaleRangeRatio.
            position: Initial value for _position.
            scale: Initial value for _scale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if time_base is not None:
            self.time_base = time_base
        if speed is not None:
            self.speed = speed
        if range_ is not None:
            self.range_ = range_
        if offset is not None:
            self.offset = offset
        if axis is not None:
            self.axis = axis
        if reference_scale is not None:
            self.reference_scale = reference_scale
        if full_scale_range_ratio is not None:
            self.full_scale_range_ratio = full_scale_range_ratio
        if position is not None:
            self.position = position
        if scale is not None:
            self.scale = scale

    @property
    def time_base(self) -> str | None:
        """Target ID of the TimeBase reference (targets IValue[np.float64])."""
        member = self.get_member("TimeBase")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @time_base.setter
    def time_base(self, target: str | IValue[np.float64] | None) -> None:
        """Set the TimeBase reference by target ID or IValue[np.float64] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("TimeBase")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TimeBase",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<double>'),
            )

    @property
    def speed(self) -> np.float32 | None:
        """The Speed field value."""
        member = self.get_member("Speed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @speed.setter
    def speed(self, value: np.float32) -> None:
        """Set the Speed field value."""
        member = self.get_member("Speed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Speed", fields.FieldFloat(value=value)
            )

    @property
    def range_(self) -> np.float32 | None:
        """The Range field value."""
        member = self.get_member("Range")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_.setter
    def range_(self, value: np.float32) -> None:
        """Set the Range field value."""
        member = self.get_member("Range")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Range", fields.FieldFloat(value=value)
            )

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def axis(self) -> primitives.Float3 | None:
        """The Axis field value."""
        member = self.get_member("Axis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis.setter
    def axis(self, value: primitives.Float3) -> None:
        """Set the Axis field value."""
        member = self.get_member("Axis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Axis", fields.FieldFloat3(value=value)
            )

    @property
    def reference_scale(self) -> primitives.Float3 | None:
        """The ReferenceScale field value."""
        member = self.get_member("ReferenceScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_scale.setter
    def reference_scale(self, value: primitives.Float3) -> None:
        """Set the ReferenceScale field value."""
        member = self.get_member("ReferenceScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReferenceScale", fields.FieldFloat3(value=value)
            )

    @property
    def full_scale_range_ratio(self) -> np.float32 | None:
        """The FullScaleRangeRatio field value."""
        member = self.get_member("FullScaleRangeRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @full_scale_range_ratio.setter
    def full_scale_range_ratio(self, value: np.float32) -> None:
        """Set the FullScaleRangeRatio field value."""
        member = self.get_member("FullScaleRangeRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FullScaleRangeRatio", fields.FieldFloat(value=value)
            )

    @property
    def position(self) -> str | None:
        """Target ID of the _position reference (targets IField[primitives.Float3])."""
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def scale(self) -> str | None:
        """Target ID of the _scale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

