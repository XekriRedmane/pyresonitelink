"""Generated component: RemoteConnectionPointDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RemoteConnectionPointDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RemoteConnectionPointDriver.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RemoteConnectionPointDriver"

    def __init__(self, filter_threshold: np.float32 | None = None, target_point: str | Slot | None = None, target_vector: primitives.Float3 | None = None, target_size: np.float32 | None = None, target_orientation: primitives.FloatQ | None = None, local_point: str | IField[primitives.Float3] | None = None, local_vector: str | IField[primitives.Float3] | None = None, local_orientation: str | IField[primitives.FloatQ] | None = None, local_size: str | IField[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            filter_threshold: Initial value for FilterThreshold.
            target_point: Initial value for TargetPoint.
            target_vector: Initial value for TargetVector.
            target_size: Initial value for TargetSize.
            target_orientation: Initial value for TargetOrientation.
            local_point: Initial value for LocalPoint.
            local_vector: Initial value for LocalVector.
            local_orientation: Initial value for LocalOrientation.
            local_size: Initial value for LocalSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if filter_threshold is not None:
            self.filter_threshold = filter_threshold
        if target_point is not None:
            self.target_point = target_point
        if target_vector is not None:
            self.target_vector = target_vector
        if target_size is not None:
            self.target_size = target_size
        if target_orientation is not None:
            self.target_orientation = target_orientation
        if local_point is not None:
            self.local_point = local_point
        if local_vector is not None:
            self.local_vector = local_vector
        if local_orientation is not None:
            self.local_orientation = local_orientation
        if local_size is not None:
            self.local_size = local_size

    @property
    def filter_threshold(self) -> np.float32 | None:
        """The FilterThreshold field value."""
        member = self.get_member("FilterThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @filter_threshold.setter
    def filter_threshold(self, value: np.float32) -> None:
        """Set the FilterThreshold field value."""
        member = self.get_member("FilterThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FilterThreshold", fields.FieldFloat(value=value)
            )

    @property
    def target_point(self) -> str | None:
        """Target ID of the TargetPoint reference (targets Slot)."""
        member = self.get_member("TargetPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_point.setter
    def target_point(self, target: str | Slot | None) -> None:
        """Set the TargetPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TargetPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_vector(self) -> primitives.Float3 | None:
        """The TargetVector field value."""
        member = self.get_member("TargetVector")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_vector.setter
    def target_vector(self, value: primitives.Float3) -> None:
        """Set the TargetVector field value."""
        member = self.get_member("TargetVector")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetVector", fields.FieldFloat3(value=value)
            )

    @property
    def target_size(self) -> np.float32 | None:
        """The TargetSize field value."""
        member = self.get_member("TargetSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_size.setter
    def target_size(self, value: np.float32) -> None:
        """Set the TargetSize field value."""
        member = self.get_member("TargetSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetSize", fields.FieldFloat(value=value)
            )

    @property
    def target_orientation(self) -> primitives.FloatQ | None:
        """The TargetOrientation field value."""
        member = self.get_member("TargetOrientation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_orientation.setter
    def target_orientation(self, value: primitives.FloatQ) -> None:
        """Set the TargetOrientation field value."""
        member = self.get_member("TargetOrientation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetOrientation", fields.FieldFloatQ(value=value)
            )

    @property
    def local_point(self) -> str | None:
        """Target ID of the LocalPoint reference (targets IField[primitives.Float3])."""
        member = self.get_member("LocalPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_point.setter
    def local_point(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the LocalPoint reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LocalPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def local_vector(self) -> str | None:
        """Target ID of the LocalVector reference (targets IField[primitives.Float3])."""
        member = self.get_member("LocalVector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_vector.setter
    def local_vector(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the LocalVector reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LocalVector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalVector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def local_orientation(self) -> str | None:
        """Target ID of the LocalOrientation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("LocalOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_orientation.setter
    def local_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the LocalOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LocalOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def local_size(self) -> str | None:
        """Target ID of the LocalSize reference (targets IField[np.float32])."""
        member = self.get_member("LocalSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @local_size.setter
    def local_size(self, target: str | IField[np.float32] | None) -> None:
        """Set the LocalSize reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("LocalSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LocalSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

